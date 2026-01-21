"""
Indexer for Mustika Rasa UI
Scans filesystem and generates JSON indices for inbox, runs, proposals, closures, promotions.
Idempotent: can be run multiple times safely.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional
import os
import sys

# Ensure runtime/src is importable (filesystem-first runtime)
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / "src"))

try:
    from runner_v2.run_layout_adapter import RunLayoutAdapter, RunSummary
    ADAPTER_AVAILABLE = True
except ImportError:
    ADAPTER_AVAILABLE = False

def _strip_generated_at(obj: Any) -> Any:
    """Return a deep copy-like structure with generated_at removed for stable comparisons."""
    if isinstance(obj, dict):
        return {k: _strip_generated_at(v) for k, v in obj.items() if k != "generated_at"}
    if isinstance(obj, list):
        return [_strip_generated_at(v) for v in obj]
    return obj


def _write_index_json_if_changed(path: Path, payload: Dict[str, Any]) -> bool:
    """Idempotent write: ignore generated_at-only diffs."""
    new_core = _strip_generated_at(payload)

    if path.exists():
        try:
            old = json.loads(path.read_text(encoding="utf-8"))
            old_core = _strip_generated_at(old)
            if old_core == new_core:
                return False
        except json.JSONDecodeError:
            # If file is unreadable/corrupt, rewrite it
            pass
        except Exception:
            pass

    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return True

class Indexer:
    """Scans filesystem and generates indices for UI consumption."""
    
    def __init__(self, base_path: Path):
        self.base_path = Path(base_path)
        self.runs_path = self.base_path / "runs"
        self.proposals_path = self.base_path / "proposals"
        self.closures_path = self.base_path / "closures"
        self.promotion_path = self.base_path / "promotion"
        self.indices_path = self.base_path / "indices"
        self.audit_path = self.base_path / "audit"
        self.canonical_path = self.base_path / "canonical"
        
        # Ensure indices directory exists
        self.indices_path.mkdir(parents=True, exist_ok=True)
    
    def generate_run_id_from_path(self, run_dir: Path) -> str:
        """Extract or generate run_id from directory path."""
        return run_dir.name
    
    def scan_runs(self) -> List[Dict[str, Any]]:
        """Scan runs/ directory and return list of run metadata."""
        runs = []
        
        # Use adapter if available (supports multiple layouts)
        if ADAPTER_AVAILABLE:
            summaries = RunLayoutAdapter.scan_all(self.base_path)
            for summary in summaries:
                run_dict = summary.to_dict()
                # Ensure path is included (adapter may not set it)
                if "path" not in run_dict and hasattr(summary, "run_id"):
                    # Try to reconstruct path from layout type
                    if summary.layout_type == "runner_v2" and summary.excerpt_id:
                        run_dict["path"] = str(self.runs_path / summary.excerpt_id / summary.run_id)
                    elif summary.layout_type in ["phase8", "phase9"]:
                        if summary.layout_type == "phase8":
                            run_dict["path"] = str(self.base_path / "sandbox" / "phase8_runs" / summary.run_id)
                        else:
                            run_dict["path"] = str(self.base_path / "sandbox" / "phase9_runs" / summary.run_id)
                runs.append(run_dict)
            # Filter invalid records: must have path and run_id starting with "RUN_"
            runs = [
                run for run in runs
                if run.get("path") and run.get("run_id", "").startswith("RUN_")
            ]
            return runs
        
        # Fallback: original scanning logic (for backward compatibility)
        if not self.runs_path.exists():
            return runs
        
        # Layout detection: legacy flat (runs/<RUN_...>/) vs nested v2 (runs/<excerpt_id>/<RUN_...>/)
        direct_children = list(self.runs_path.iterdir())
        has_legacy_runs = any(
            child.is_dir() and child.name.startswith("RUN_")
            for child in direct_children
        )
        
        run_dirs_to_scan = []
        
        if has_legacy_runs:
            # Legacy flat layout: runs/<RUN_...>/
            for run_dir in sorted(self.runs_path.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
                if run_dir.is_dir() and run_dir.name.startswith("RUN_"):
                    run_dirs_to_scan.append((run_dir, None))  # (run_dir, excerpt_id)
        else:
            # Nested layout: runs/<excerpt_id>/<RUN_...>/
            for excerpt_dir in sorted(self.runs_path.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
                if not excerpt_dir.is_dir():
                    continue
                excerpt_id = excerpt_dir.name
                for run_dir in sorted(excerpt_dir.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
                    if run_dir.is_dir() and run_dir.name.startswith("RUN_"):
                        run_dirs_to_scan.append((run_dir, excerpt_id))
        
        # Process each run directory
        for run_dir, excerpt_id in run_dirs_to_scan:
            run_id = run_dir.name
            
            # Try to read manifest.json if it exists
            manifest_path = run_dir / "manifest.json"
            manifest = {}
            if manifest_path.exists():
                try:
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, IOError):
                    pass
            
            # Check for validator report (try both locations)
            validator_path = run_dir / "validator" / "report.json"
            validator_status = None
            if validator_path.exists():
                try:
                    validator_data = json.loads(validator_path.read_text(encoding="utf-8"))
                    validator_status = validator_data.get("overall_status", "UNKNOWN")
                except (json.JSONDecodeError, IOError):
                    pass
            else:
                # Try eval/output_contract_checks.txt (Runner V2 / Phase-8 format)
                eval_path = run_dir / "eval" / "output_contract_checks.txt"
                if eval_path.exists():
                    try:
                        content = eval_path.read_text(encoding="utf-8")
                        if "overall_status: PASS" in content:
                            validator_status = "PASS"
                        elif "overall_status: FAIL" in content:
                            validator_status = "FAIL"
                    except IOError:
                        pass
            
            # Check for gates
            gates_path = run_dir / "validator" / "gates.json"
            gates = []
            blocking_gates = False
            if gates_path.exists():
                try:
                    gates_data = json.loads(gates_path.read_text(encoding="utf-8"))
                    gates = gates_data.get("gates", [])
                    blocking_gates = any(g.get("blocking", False) for g in gates)
                except (json.JSONDecodeError, IOError):
                    pass
            elif validator_status == "FAIL":
                # If validator failed, treat as blocking gate
                blocking_gates = True
                gates = [{"type": "output_contract", "blocking": True}]
            
            # Check for signals
            signals_path = run_dir / "signals.json"
            signals = []
            if signals_path.exists():
                try:
                    signals = json.loads(signals_path.read_text(encoding="utf-8"))
                    if isinstance(signals, dict) and "signals" in signals:
                        signals = signals["signals"]
                except (json.JSONDecodeError, IOError):
                    pass
            
            # Check for incident
            incident_path = run_dir / "incident.json"
            has_incident = incident_path.exists()
            
            # Determine status
            status = "completed"
            if has_incident:
                status = "failed"
            elif validator_status == "FAIL":
                status = "failed"
            elif blocking_gates:
                status = "gated"
            
            stat = run_dir.stat()
            runs.append({
                "run_id": run_id,
                "excerpt_id": excerpt_id,
                "path": str(run_dir),
                "status": status,
                "created_at": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "validator_status": validator_status,
                "blocking_gates": blocking_gates,
                "gate_count": len(gates),
                "signal_count": len(signals),
                "has_incident": has_incident,
                "manifest": manifest,
            })
        
        # Filter invalid records
        runs = [
            run for run in runs
            if run.get("path") and run.get("run_id", "").startswith("RUN_")
        ]
        
        return runs
    
    def scan_proposals(self) -> List[Dict[str, Any]]:
        """Scan proposals/ directory and return list of proposal metadata."""
        proposals = []
        
        if not self.proposals_path.exists():
            return proposals
        
        for proposal_dir in sorted(self.proposals_path.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
            if not proposal_dir.is_dir():
                continue
            
            proposal_id = proposal_dir.name
            
            # Read status.json if it exists
            status_path = proposal_dir / "status.json"
            status_data = {"status": "open", "severity": "info"}
            if status_path.exists():
                try:
                    status_data = json.loads(status_path.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, IOError):
                    pass
            
            # Check for required closure
            required_closure_path = proposal_dir / "required_closure.json"
            requires_closure = required_closure_path.exists()
            
            # Check for gates
            gates_path = proposal_dir / "gates.json"
            gates = []
            if gates_path.exists():
                try:
                    gates_data = json.loads(gates_path.read_text(encoding="utf-8"))
                    gates = gates_data.get("gates", [])
                except (json.JSONDecodeError, IOError):
                    pass
            
            # Read proposal.md if it exists for title
            proposal_md_path = proposal_dir / "proposal.md"
            title = proposal_id
            if proposal_md_path.exists():
                try:
                    content = proposal_md_path.read_text(encoding="utf-8")
                    # Extract first line or heading as title
                    lines = content.split("\n")
                    for line in lines:
                        if line.strip() and not line.strip().startswith("#"):
                            title = line.strip()[:100]  # Limit length
                            break
                        elif line.strip().startswith("#"):
                            title = line.strip().lstrip("#").strip()[:100]
                            break
                except IOError:
                    pass
            
            stat = proposal_dir.stat()
            proposals.append({
                "proposal_id": proposal_id,
                "title": title,
                "status": status_data.get("status", "open"),
                "severity": status_data.get("severity", "info"),
                "requires_closure": requires_closure,
                "gate_count": len(gates),
                "created_at": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            })
        
        return proposals
    
    def scan_closures(self) -> List[Dict[str, Any]]:
        """Scan closures/ directory and return list of closure metadata."""
        closures = []
        
        if not self.closures_path.exists():
            return closures
        
        for closure_dir in sorted(self.closures_path.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
            if not closure_dir.is_dir():
                continue
            
            closure_id = closure_dir.name
            
            # Try to read closure.json or closure.md
            closure_json_path = closure_dir / "closure.json"
            closure_md_path = closure_dir / "closure.md"
            closure_data = {}
            
            if closure_json_path.exists():
                try:
                    closure_data = json.loads(closure_json_path.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, IOError):
                    pass
            elif closure_md_path.exists():
                # Parse basic info from markdown if JSON not available
                try:
                    content = closure_md_path.read_text(encoding="utf-8")
                    closure_data = {"format": "markdown", "content_preview": content[:200]}
                except IOError:
                    pass
            
            stat = closure_dir.stat()
            closures.append({
                "closure_id": closure_id,
                "decision_type": closure_data.get("decision_type", "unknown"),
                "created_at": closure_data.get("created_at", datetime.fromtimestamp(stat.st_mtime).isoformat()),
                "created_by": closure_data.get("created_by", "unknown"),
                "proposal_id": closure_data.get("proposal_id"),
                "run_id": closure_data.get("source_run_id"),
            })
        
        return closures

    def build_closure_lookup(self) -> set:
        """Build a lookup of proposal_ids that already have closures."""
        proposal_ids = set()
        if not self.closures_path.exists():
            return proposal_ids

        for closure_dir in self.closures_path.iterdir():
            if not closure_dir.is_dir():
                continue

            closure_json_path = closure_dir / "closure.json"
            closure_data = {}
            if closure_json_path.exists():
                try:
                    closure_data = json.loads(closure_json_path.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, IOError):
                    closure_data = {}
            else:
                status_json_path = closure_dir / "status.json"
                if status_json_path.exists():
                    try:
                        closure_data = json.loads(status_json_path.read_text(encoding="utf-8"))
                    except (json.JSONDecodeError, IOError):
                        closure_data = {}

            proposal_id = None
            if isinstance(closure_data, dict):
                proposal_id = closure_data.get("proposal_id")

            if proposal_id:
                proposal_ids.add(proposal_id)

        return proposal_ids
    
    def check_challenger_issues(self, run_path: str) -> bool:
        """Check if challenger_primary.json indicates issues."""
        try:
            run_dir = Path(run_path)
            challenger_path = run_dir / "outputs" / "challenger_primary.json"
            
            if not challenger_path.exists():
                return False
            
            challenger_data = json.loads(challenger_path.read_text(encoding="utf-8"))
            
            # Check for non-empty "issues" list
            if "issues" in challenger_data:
                issues = challenger_data["issues"]
                if isinstance(issues, list) and len(issues) > 0:
                    return True
            
            # Check for numeric "issue_count" > 0
            if "issue_count" in challenger_data:
                count = challenger_data["issue_count"]
                if isinstance(count, (int, float)) and count > 0:
                    return True
            
            return False
        except (IOError, json.JSONDecodeError, KeyError, TypeError):
            return False
    
    def build_inbox_index(self) -> Dict[str, Any]:
        """Build inbox index from runs, proposals, and closures with explicit deterministic rules."""
        runs = self.scan_runs()
        proposals = self.scan_proposals()
        closures = self.scan_closures()
        closure_lookup = self.build_closure_lookup()
        
        # Build inbox items with explicit deterministic rules
        inbox_items = []
        item_keys_seen = set()  # Track (source_type, source_id, kind) to avoid duplicates
        
        # RUN-based inbox items
        for run in runs:
            run_id = run.get("run_id", "")
            run_path = run.get("path")
            if not run_path or not run_id:
                continue
            
            # Rule 1: Validator FAIL → kind="incident", severity="high"
            if run.get("validator_status") == "FAIL":
                item_key = ("run", run_id, "incident")
                if item_key not in item_keys_seen:
                    inbox_items.append({
                        "id": f"run_{run_id}_incident",
                        "kind": "incident",
                        "severity": "high",
                        "source_type": "run",
                        "source_id": run_id,
                        "reasons": ["validator_fail"],
                        "path": str(Path(run_path).resolve()),
                    })
                    item_keys_seen.add(item_key)
            
            # Rule 2: Blocking gates present → kind="gate", severity="high"
            if run.get("blocking_gates") is True:
                item_key = ("run", run_id, "gate")
                if item_key not in item_keys_seen:
                    inbox_items.append({
                        "id": f"run_{run_id}_gate",
                        "kind": "gate",
                        "severity": "high",
                        "source_type": "run",
                        "source_id": run_id,
                        "reasons": ["blocking_gate"],
                        "path": str(Path(run_path).resolve()),
                    })
                    item_keys_seen.add(item_key)
            
            # Rule 3: Challenger issues present → kind="review_required", severity="medium"
            if self.check_challenger_issues(run_path):
                item_key = ("run", run_id, "review_required")
                if item_key not in item_keys_seen:
                    inbox_items.append({
                        "id": f"run_{run_id}_review",
                        "kind": "review_required",
                        "severity": "medium",
                        "source_type": "run",
                        "source_id": run_id,
                        "reasons": ["challenger_issues"],
                        "path": str(Path(run_path).resolve()),
                    })
                    item_keys_seen.add(item_key)
        
        # PROPOSAL-based inbox items
        for proposal in proposals:
            proposal_id = proposal.get("proposal_id", "")
            proposal_path = self.proposals_path / proposal_id
            if not proposal_id:
                continue
            
            status = proposal.get("status", "").lower()
            is_closed = status == "closed"
            requires_closure = proposal.get("requires_closure", False)
            
            # Rule 4: Proposal status == "open" → kind="review_required", severity="low"
            if status == "open":
                item_key = ("proposal", proposal_id, "review_required")
                if item_key not in item_keys_seen:
                    inbox_items.append({
                        "id": f"proposal_{proposal_id}_review",
                        "kind": "review_required",
                        "severity": "low",
                        "source_type": "proposal",
                        "source_id": proposal_id,
                        "reasons": ["proposal_open"],
                        "path": str(proposal_path.resolve()),
                    })
                    item_keys_seen.add(item_key)
            
            # Rule 5: required_closure.json present → kind="closure_needed", severity="medium"
            if requires_closure and not is_closed and proposal_id not in closure_lookup:
                item_key = ("proposal", proposal_id, "closure_needed")
                if item_key not in item_keys_seen:
                    inbox_items.append({
                        "id": f"proposal_{proposal_id}_closure",
                        "kind": "closure_needed",
                        "severity": "medium",
                        "source_type": "proposal",
                        "source_id": proposal_id,
                        "reasons": ["required_closure"],
                        "path": str(proposal_path.resolve()),
                    })
                    item_keys_seen.add(item_key)
        
        # Sort by severity (high > medium > low) then by source_id (for stability)
        severity_order = {"high": 3, "medium": 2, "low": 1}
        inbox_items.sort(
            key=lambda x: (severity_order.get(x.get("severity", ""), 0), x.get("source_id", "")),
            reverse=True
        )
        
        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "items": inbox_items,
        }
    
    def reindex(self) -> Dict[str, Any]:
        """Generate all indices and return summary."""
        print("Scanning runs...")
        runs = self.scan_runs()
        
        print("Scanning proposals...")
        proposals = self.scan_proposals()
        
        print("Scanning closures...")
        closures = self.scan_closures()
        
        print("Building inbox index...")
        inbox_index = self.build_inbox_index()
        
        # Write indices
        run_payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "runs": runs,
        }
        proposal_payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "proposals": proposals,
        }
        closure_payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "closures": closures,
        }

        _write_index_json_if_changed(self.indices_path / "run_index.json", run_payload)
        _write_index_json_if_changed(self.indices_path / "proposal_index.json", proposal_payload)
        _write_index_json_if_changed(self.indices_path / "closure_index.json", closure_payload)
        _write_index_json_if_changed(self.indices_path / "inbox_index.json", inbox_index)
        
        return {
            "runs": len(runs),
            "proposals": len(proposals),
            "closures": len(closures),
            "inbox_items": len(inbox_index.get("items", [])),
        }


def main():
    """CLI entry point for indexer."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Index Mustika Rasa filesystem artefacts")
    parser.add_argument(
        "--base-path",
        type=str,
        default=".",
        help="Base path to scan (default: current directory)",
    )
    
    args = parser.parse_args()
    
    indexer = Indexer(Path(args.base_path).resolve())
    result = indexer.reindex()
    
    print(f"\nIndexing complete:")
    print(f"  Runs: {result['runs']}")
    print(f"  Proposals: {result['proposals']}")
    print(f"  Closures: {result['closures']}")
    print(f"  Inbox items: {result['inbox_items']}")
    print(f"\nIndices written to: {indexer.indices_path}")


if __name__ == "__main__":
    main()
