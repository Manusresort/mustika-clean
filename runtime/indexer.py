"""
Indexer for Mustika Rasa UI
Scans filesystem and generates JSON indices for inbox, runs, proposals, closures, promotions.
Idempotent: can be run multiple times safely.
"""

import json
from collections import defaultdict
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
            # Guard: do not emit closure_needed for closed proposals (MASTERPLAN Phase 3 rule).
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

    def load_chapter_manifest(self) -> Dict[str, Any]:
        manifest_path = self.base_path / "manifests" / "chapter_manifest.json"
        if not manifest_path.exists():
            return {}

        try:
            return json.loads(manifest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, IOError):
            return {}

    def load_closure_index(self) -> List[str]:
        closures = []
        closure_index_path = self.indices_path / "closure_index.json"
        if not closure_index_path.exists():
            return closures
        try:
            data = json.loads(closure_index_path.read_text(encoding="utf-8"))
            for closure in data.get("closures", []):
                closure_id = closure.get("closure_id")
                if isinstance(closure_id, str):
                    closures.append(closure_id)
        except (json.JSONDecodeError, IOError):
            pass
        return closures

    def _relative_path(self, path: Path) -> Optional[str]:
        try:
            rel = path.relative_to(self.base_path).as_posix()
            if rel.startswith("../") or ".." in rel.split("/"):
                return None
            return rel
        except ValueError:
            return None

    def build_chapter_registry_payload(self, manifest: Dict[str, Any]) -> Dict[str, Any]:
        chapters_raw = manifest.get("chapters", [])
        unassigned_raw = manifest.get("unassigned", {})

        def _unique_sorted(entries: List[str]) -> List[str]:
            return sorted(dict.fromkeys(entries))

        chapters = []
        for chapter in sorted(chapters_raw, key=lambda c: c.get("chapter_id", "")):
            chapter_id = chapter.get("chapter_id")
            if not chapter_id:
                continue
            run_ids = _unique_sorted(chapter.get("run_ids", []))
            proposal_ids = _unique_sorted(chapter.get("proposal_ids", []))
            closure_ids = _unique_sorted(chapter.get("closure_ids", []))
            chapters.append({
                "chapter_id": chapter_id,
                "title": chapter.get("title") if chapter.get("title") else None,
                "counts": {
                    "runs": len(run_ids),
                    "proposals": len(proposal_ids),
                    "closures": len(closure_ids),
                },
                "run_ids": run_ids,
                "proposal_ids": proposal_ids,
                "closure_ids": closure_ids,
            })

        unassigned = {
            "run_ids": _unique_sorted(unassigned_raw.get("run_ids", [])),
            "proposal_ids": _unique_sorted(unassigned_raw.get("proposal_ids", [])),
            "closure_ids": _unique_sorted(unassigned_raw.get("closure_ids", [])),
        }

        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "chapters": chapters,
            "unassigned": unassigned,
            "source_manifest": "manifests/chapter_manifest.json",
        }

    def build_glossary_evidence_index(self, manifest: Dict[str, Any], closures: List[Dict[str, Any]]) -> Dict[str, Any]:
        def _unique_sorted(entries: List[str]) -> List[str]:
            return sorted(dict.fromkeys(entries))

        chapter_map = {}
        for chapter in manifest.get("chapters", []):
            chapter_id = chapter.get("chapter_id")
            if chapter_id:
                for closure_id in chapter.get("closure_ids", []):
                    if isinstance(closure_id, str):
                        chapter_map[closure_id] = chapter_id

        def _extract_paths(entry: Dict[str, Any]) -> List[str]:
            paths = entry.get("evidence_paths") or []
            return [p for p in paths if isinstance(p, str)]

        chapters = {}
        unassigned_paths = []
        unassigned_sources = []

        for closure in closures:
            closure_id = closure.get("closure_id")
            evidence_paths = [_ for _ in _extract_paths(closure) if "glossary" in _ or "woordenlijst" in _]
            if not evidence_paths:
                continue
            target = chapter_map.get(closure_id)
            if target:
                chapters.setdefault(target, {"glossary_evidence_paths": [], "source_closure_ids": []})
                chapters[target]["glossary_evidence_paths"].extend(evidence_paths)
                chapters[target]["source_closure_ids"].append(closure_id)
            else:
                unassigned_paths.extend(evidence_paths)
                unassigned_sources.append(closure_id)

        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "chapters": [
                {
                    "chapter_id": cid,
                    "glossary_evidence_paths": _unique_sorted(details["glossary_evidence_paths"]),
                    "source_closure_ids": _unique_sorted(details["source_closure_ids"]),
                }
                for cid, details in sorted(chapters.items())
            ],
            "unassigned": {
                "glossary_evidence_paths": _unique_sorted(unassigned_paths),
                "source_closure_ids": _unique_sorted(unassigned_sources),
            },
            "heuristic": {
                "match_rules": ["path_contains:glossary", "path_contains:woordenlijst"],
            },
            "sources": {
                "chapter_manifest": "manifests/chapter_manifest.json",
                "closure_index": "indices/closure_index.json",
            },
        }

    def _glossary_lifecycle(self, evidence_paths: List[str], source_closure_ids: List[str]) -> str:
        if source_closure_ids:
            return "approved"
        if evidence_paths:
            return "approved"
        return "draft"

    def build_chapter_manifest_with_glossary(
        self, chapter_manifest: Dict[str, Any], glossary_entries: Dict[str, Any]
    ) -> Dict[str, Any]:
        chapters = chapter_manifest.get("chapters", []) if isinstance(chapter_manifest, dict) else []
        glossary_by_chapter = {
            entry.get("chapter_id"): entry
            for entry in glossary_entries.get("chapters", [])
            if isinstance(entry, dict)
        }

        def _unique_sorted(entries: List[str]) -> List[str]:
            return sorted(dict.fromkeys([e for e in entries if isinstance(e, str) and e]))

        updated = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "chapters": [],
            "unassigned": chapter_manifest.get("unassigned", {}),
            "sources": chapter_manifest.get("sources", {}),
        }

        for chapter in chapters:
            if not isinstance(chapter, dict):
                continue
            chapter_id = chapter.get("chapter_id")
            glossary_entry = glossary_by_chapter.get(chapter_id, {})
            evidence_paths = _unique_sorted(glossary_entry.get("glossary_evidence_paths", []))
            source_closure_ids = _unique_sorted(glossary_entry.get("source_closure_ids", []))
            glossary = {
                "lifecycle": self._glossary_lifecycle(evidence_paths, source_closure_ids),
                "evidence_paths": evidence_paths,
                "source_closure_ids": source_closure_ids,
            }
            enriched = dict(chapter)
            enriched["glossary"] = glossary
            updated["chapters"].append(enriched)

        return updated

    def _collect_glossary_summary(self, glossary_entries: Dict[str, Any]) -> Dict[str, Any]:
        def _unique_sorted(entries: List[str]) -> List[str]:
            return sorted(dict.fromkeys([e for e in entries if isinstance(e, str) and e]))

        evidence_paths = []
        source_closure_ids = []
        for entry in glossary_entries.get("chapters", []):
            if not isinstance(entry, dict):
                continue
            evidence_paths.extend(entry.get("glossary_evidence_paths", []))
            source_closure_ids.extend(entry.get("source_closure_ids", []))
        unassigned = glossary_entries.get("unassigned", {})
        if isinstance(unassigned, dict):
            evidence_paths.extend(unassigned.get("glossary_evidence_paths", []))
            source_closure_ids.extend(unassigned.get("source_closure_ids", []))

        evidence_paths = _unique_sorted(evidence_paths)
        source_closure_ids = _unique_sorted(source_closure_ids)
        return {
            "lifecycle": self._glossary_lifecycle(evidence_paths, source_closure_ids),
            "evidence_paths": evidence_paths,
            "source_closure_ids": source_closure_ids,
        }

    def build_review_pack_index(self, proposals: List[Dict[str, Any]], closures: List[Dict[str, Any]]) -> Dict[str, Any]:
        closure_map = {}
        for closure in closures:
            proposal_id = closure.get("proposal_id")
            if not proposal_id:
                continue
            for path in closure.get("evidence_paths", []) or []:
                if not isinstance(path, str):
                    continue
                norm = path
                if norm.startswith("/") or ".." in norm.split("/"):
                    continue
                closure_map.setdefault(proposal_id, []).append(norm)

        entries = []
        for proposal in sorted(proposals, key=lambda p: p.get("proposal_id", "")):
            proposal_id = proposal.get("proposal_id")
            if not proposal_id:
                continue
            files = []
            proposal_dir = self.proposals_path / proposal_id
            for candidate in [proposal_dir / "proposal.md", proposal_dir / "status.json"]:
                if candidate.exists():
                    rel = self._relative_path(candidate)
                    if rel:
                        files.append(rel)
            review_pack_dir = proposal_dir / "review_pack"
            has_pack = False
            if review_pack_dir.exists():
                for child in sorted(review_pack_dir.rglob("*")):
                    if child.is_file():
                        rel = self._relative_path(child)
                        if rel:
                            files.append(rel)
                has_pack = True
            for closure_path in sorted(set(closure_map.get(proposal_id, []))):
                files.append(closure_path)
            entries.append({
                "proposal_id": proposal_id,
                "review_pack_files": sorted(dict.fromkeys(files)),
                "source": {
                    "has_review_pack_dir": has_pack,
                    "derived_from": ["proposal_index", "closure_index", "run_index"],
                },
            })

        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "proposals": entries,
        }

    def load_closure_index_objects(self) -> List[Dict[str, Any]]:
        closure_index_path = self.indices_path / "closure_index.json"
        if not closure_index_path.exists():
            return []
        try:
            data = json.loads(closure_index_path.read_text(encoding="utf-8"))
            return data.get("closures", []) if isinstance(data, dict) else []
        except (json.JSONDecodeError, IOError):
            return []

    def build_chapter_closure_rollup(self, manifest: Dict[str, Any], closure_index_ids: List[str]) -> Dict[str, Any]:
        chapters_raw = manifest.get("chapters", [])
        rollup_chapters = []

        def _unique_sorted(entries: List[str]) -> List[str]:
            return sorted(dict.fromkeys(entries))

        assigned_ids = set()
        for chapter in sorted(chapters_raw, key=lambda c: c.get("chapter_id", "")):
            chapter_id = chapter.get("chapter_id")
            if not chapter_id:
                continue
            closure_ids = _unique_sorted(chapter.get("closure_ids", []))
            assigned_ids.update(closure_ids)
            rollup_chapters.append({
                "chapter_id": chapter_id,
                "closure_ids": closure_ids,
                "counts": {"total": len(closure_ids)},
                "status": "closed" if closure_ids else "none",
            })

        unassigned_ids = [cid for cid in closure_index_ids if cid not in assigned_ids]
        unassigned = {"closure_ids": _unique_sorted(unassigned_ids)}

        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "chapters": rollup_chapters,
            "unassigned": unassigned,
            "sources": {
                "chapter_manifest": "manifests/chapter_manifest.json",
                "closure_index": "indices/closure_index.json",
            },
        }

    def load_build_manifest_entries(self) -> List[Dict[str, Any]]:
        exports_root = self.base_path / "exports" / "books"
        entries: List[Dict[str, Any]] = []
        if not exports_root.exists():
            return entries
        for path in sorted(exports_root.glob("*/builds/latest/build_manifest.json")):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, IOError):
                continue
            book_id = data.get("book_id")
            if not isinstance(book_id, str) or not book_id.strip():
                book_id = path.parents[2].name
            rel = self._relative_path(path) or path.as_posix()
            entries.append({
                "book_id": book_id,
                "path": rel,
                "data": data,
            })
        return entries

    def build_book_manifest_payload(
        self,
        chapter_manifest: Dict[str, Any],
        book_rollup_payload: Dict[str, Any],
        build_manifest_entries: List[Dict[str, Any]],
        closure_index_ids: List[str],
        glossary_entries: Dict[str, Any],
    ) -> Dict[str, Any]:
        def _unique_sorted(entries: List[str]) -> List[str]:
            return sorted(dict.fromkeys([e for e in entries if isinstance(e, str) and e]))

        chapters_raw = chapter_manifest.get("chapters", [])
        chapters_by_id = {c.get("chapter_id"): c for c in chapters_raw if isinstance(c, dict)}
        closure_index_set = set(closure_index_ids)

        build_by_book: Dict[str, List[Dict[str, Any]]] = {}
        for entry in build_manifest_entries:
            book_id = entry.get("book_id")
            if not isinstance(book_id, str) or not book_id:
                continue
            build_by_book.setdefault(book_id, []).append(entry)

        rollup_books = book_rollup_payload.get("books", [])
        book_entries: List[Dict[str, Any]] = []
        for book in sorted(rollup_books, key=lambda b: b.get("book_id", "")):
            book_id = book.get("book_id")
            if not isinstance(book_id, str) or not book_id:
                continue
            chapter_ids = _unique_sorted(book.get("chapter_ids", []))
            closure_ids = _unique_sorted(book.get("closure_ids", []))

            chapters = []
            for chapter_id in chapter_ids:
                if chapter_id not in chapters_by_id:
                    continue
                chapters.append({
                    "chapter_id": chapter_id,
                    "plan": "manifests/chapter_manifest.json",
                })

            exports = []
            for entry in sorted(build_by_book.get(book_id, []), key=lambda e: e.get("path", "")):
                data = entry.get("data", {})
                exports_block = data.get("exports", {}) if isinstance(data, dict) else {}
                files = exports_block.get("files", []) if isinstance(exports_block, dict) else []
                exports.append({
                    "build_manifest": entry.get("path"),
                    "built_at": data.get("generated_at"),
                    "files": _unique_sorted(files),
                    "sha256": data.get("sha256", {}) if isinstance(data.get("sha256"), dict) else {},
                    "tool_versions": data.get("tool_versions", {}) if isinstance(data.get("tool_versions"), dict) else {},
                    "input_closure_ids": _unique_sorted(data.get("closure_ids", [])),
                })

            provenance_paths = [
                "manifests/chapter_manifest.json",
                "indices/book_closure_rollup.json",
                "indices/chapter_closure_rollup.json",
            ]
            for entry in exports:
                bm = entry.get("build_manifest")
                if isinstance(bm, str) and bm:
                    provenance_paths.append(bm)
            for closure_id in closure_ids:
                closure_path = self.base_path / "closures" / closure_id / "closure.json"
                rel = self._relative_path(closure_path)
                if rel:
                    provenance_paths.append(rel)

            status = "draft"
            if closure_ids:
                if all(cid in closure_index_set for cid in closure_ids):
                    status = "reviewable"

            glossary_summary = self._collect_glossary_summary(glossary_entries)
            book_entries.append({
                "book_id": book_id,
                "chapters": chapters,
                "required_closures": closure_ids,
                "status": status,
                "exports": exports,
                "provenance": {
                    "paths": _unique_sorted(provenance_paths),
                    "glossary": glossary_summary,
                },
                "mapping_mode": (book_rollup_payload.get("mapping") or {}).get("mode"),
            })

        generated_at = datetime.now(timezone.utc).isoformat()
        if len(book_entries) == 1:
            manifest = {
                "generated_at": generated_at,
                **book_entries[0],
            }
        else:
            manifest = {
                "generated_at": generated_at,
                "books": book_entries,
            }

        manifest["sources"] = {
            "chapter_manifest": "manifests/chapter_manifest.json",
            "book_closure_rollup": "indices/book_closure_rollup.json",
            "chapter_closure_rollup": "indices/chapter_closure_rollup.json",
            "build_manifest_root": "exports/books",
        }
        return manifest

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

        chapter_manifest = self.load_chapter_manifest()
        chapter_registry_payload = self.build_chapter_registry_payload(chapter_manifest)
        closure_index_ids = self.load_closure_index()
        chapter_rollup_payload = self.build_chapter_closure_rollup(chapter_manifest, closure_index_ids)
        glossary_entries = self.build_glossary_evidence_index(chapter_manifest, self.load_closure_index_objects())
        chapter_manifest_glossary = self.build_chapter_manifest_with_glossary(chapter_manifest, glossary_entries)

        _write_index_json_if_changed(self.indices_path / "run_index.json", run_payload)
        _write_index_json_if_changed(self.indices_path / "proposal_index.json", proposal_payload)
        _write_index_json_if_changed(self.indices_path / "closure_index.json", closure_payload)
        _write_index_json_if_changed(self.indices_path / "inbox_index.json", inbox_index)
        _write_index_json_if_changed(self.indices_path / "chapter_registry.json", chapter_registry_payload)
        _write_index_json_if_changed(self.indices_path / "chapter_closure_rollup.json", chapter_rollup_payload)

        # B8a: book closure rollup (derived)
        book_rollup_payload = build_book_closure_rollup(
            chapter_registry=chapter_registry_payload,
            chapter_closure_rollup=chapter_rollup_payload,
            generated_at=chapter_rollup_payload.get("generated_at", datetime.now(timezone.utc).isoformat()),
        )
        _write_index_json_if_changed(self.indices_path / "book_closure_rollup.json", book_rollup_payload)
        _write_index_json_if_changed(self.indices_path / "glossary_evidence_index.json", glossary_entries)

        # B9: book manifest (derived)
        build_manifest_entries = self.load_build_manifest_entries()
        book_manifest_payload = self.build_book_manifest_payload(
            chapter_manifest=chapter_manifest_glossary,
            book_rollup_payload=book_rollup_payload,
            build_manifest_entries=build_manifest_entries,
            closure_index_ids=closure_index_ids,
            glossary_entries=glossary_entries,
        )
        (self.base_path / "manifests").mkdir(parents=True, exist_ok=True)
        _write_index_json_if_changed(self.base_path / "manifests" / "book_manifest.json", book_manifest_payload)
        _write_index_json_if_changed(self.base_path / "manifests" / "chapter_manifest.json", chapter_manifest_glossary)
        
        return {
            "runs": len(runs),
            "proposals": len(proposals),
            "closures": len(closures),
            "inbox_items": len(inbox_index.get("items", [])),
        }



def _get_chapter_book_key(ch: dict) -> tuple[str, str] | None:
    """
    Returns (mode, book_id) if chapter has a book mapping.
    mode in {"book_id","book"}.
    """
    if not isinstance(ch, dict):
        return None
    if isinstance(ch.get("book_id"), str) and ch["book_id"].strip():
        return ("book_id", ch["book_id"].strip())
    if isinstance(ch.get("book"), str) and ch["book"].strip():
        return ("book", ch["book"].strip())
    return None


def build_book_closure_rollup(
    chapter_registry: dict[str, Any],
    chapter_closure_rollup: dict[str, Any],
    generated_at: str,
) -> dict[str, Any]:
    chapters = chapter_registry.get("chapters", [])
    chapter_ids: list[str] = []
    chapters_by_id: dict[str, dict[str, Any]] = {}
    if isinstance(chapters, list):
        for ch in chapters:
            if isinstance(ch, dict):
                cid = ch.get("chapter_id")
                if isinstance(cid, str) and cid.strip():
                    cid = cid.strip()
                    chapter_ids.append(cid)
                    chapters_by_id[cid] = ch
    chapter_ids = sorted(set(chapter_ids))

    roll_chapters = chapter_closure_rollup.get("chapters", [])
    closure_ids_by_chapter: dict[str, list[str]] = {cid: [] for cid in chapter_ids}
    if isinstance(roll_chapters, list):
        for item in roll_chapters:
            if not isinstance(item, dict):
                continue
            cid = item.get("chapter_id")
            if not (isinstance(cid, str) and cid.strip()):
                continue
            cid = cid.strip()
            if cid not in closure_ids_by_chapter:
                continue
            cids = item.get("closure_ids", [])
            if isinstance(cids, list):
                closure_ids_by_chapter[cid] = sorted({c for c in cids if isinstance(c, str) and c})

    books: dict[str, dict[str, Any]] = defaultdict(lambda: {"chapter_ids": [], "closure_ids": set()})
    mapping_mode: str = "single_default"

    for cid in chapter_ids:
        ch = chapters_by_id.get(cid, {})
        bk = _get_chapter_book_key(ch)
        if bk is None:
            book_id = "BOOK-DEFAULT"
        else:
            mapping_mode = bk[0]
            book_id = bk[1]

        books[book_id]["chapter_ids"].append(cid)
        for cl in closure_ids_by_chapter.get(cid, []):
            books[book_id]["closure_ids"].add(cl)

    out_books: list[dict[str, Any]] = []
    for book_id in sorted(books.keys()):
        chs = sorted(set(books[book_id]["chapter_ids"]))
        cls = sorted(set(books[book_id]["closure_ids"]))
        status = "none" if len(cls) == 0 else "closed"
        out_books.append(
            {
                "book_id": book_id,
                "chapter_ids": chs,
                "closure_ids": cls,
                "counts": {"chapters": len(chs), "closures": len(cls)},
                "status": status,
            }
        )

    return {
        "generated_at": generated_at,
        "books": out_books,
        "sources": {
            "chapter_registry": "indices/chapter_registry.json",
            "chapter_closure_rollup": "indices/chapter_closure_rollup.json",
        },
        "mapping": {"mode": mapping_mode},
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
