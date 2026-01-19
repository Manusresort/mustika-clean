"""
Run Layout Adapter - Normalizes different run layouts into a single schema
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List


class RunSummary:
    """Normalized run summary schema."""
    
    def __init__(
        self,
        run_id: str,
        excerpt_id: Optional[str] = None,
        status: str = "completed",
        created_at: str = "",
        validator_status: Optional[str] = None,
        blocking_gates: bool = False,
        gate_count: int = 0,
        signal_count: int = 0,
        has_incident: bool = False,
        manifest: Optional[Dict[str, Any]] = None,
        layout_type: str = "unknown",
    ):
        self.run_id = run_id
        self.excerpt_id = excerpt_id
        self.status = status
        self.created_at = created_at
        self.validator_status = validator_status
        self.blocking_gates = blocking_gates
        self.gate_count = gate_count
        self.signal_count = signal_count
        self.has_incident = has_incident
        self.manifest = manifest or {}
        self.layout_type = layout_type
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "run_id": self.run_id,
            "excerpt_id": self.excerpt_id,
            "status": self.status,
            "created_at": self.created_at,
            "validator_status": self.validator_status,
            "blocking_gates": self.blocking_gates,
            "gate_count": self.gate_count,
            "signal_count": self.signal_count,
            "has_incident": self.has_incident,
            "manifest": self.manifest,
            "layout_type": self.layout_type,
        }


class RunLayoutAdapter:
    """Adapter that normalizes different run layouts."""
    
    @staticmethod
    def scan_runner_v2_layout(runs_path: Path) -> List[RunSummary]:
        """
        Scan Runner V2 layout: runs/<excerpt_id>/<run_id>/
        """
        summaries = []
        
        if not runs_path.exists():
            return summaries
        
        for excerpt_dir in runs_path.iterdir():
            if not excerpt_dir.is_dir():
                continue
            
            excerpt_id = excerpt_dir.name
            
            for run_dir in excerpt_dir.iterdir():
                if not run_dir.is_dir():
                    continue
                
                run_id = run_dir.name
                summary = RunLayoutAdapter._read_runner_v2_run(run_dir, excerpt_id, run_id)
                if summary:
                    summaries.append(summary)
        
        return summaries
    
    @staticmethod
    def _read_runner_v2_run(run_dir: Path, excerpt_id: str, run_id: str) -> Optional[RunSummary]:
        """Read Runner V2 run directory."""
        # Read manifest
        manifest_path = run_dir / "manifest.json"
        manifest = {}
        if manifest_path.exists():
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, IOError):
                pass
        
        # Check validator report
        validator_path = run_dir / "eval" / "output_contract_checks.txt"
        validator_status = None
        if validator_path.exists():
            try:
                content = validator_path.read_text(encoding="utf-8")
                # Parse validator report (simple format)
                if "overall_status: PASS" in content:
                    validator_status = "PASS"
                elif "overall_status: FAIL" in content:
                    validator_status = "FAIL"
            except IOError:
                pass
        
        # Check for gates (from validator report)
        gates = []
        blocking_gates = False
        if validator_status == "FAIL":
            blocking_gates = True
            gates = [{"type": "output_contract", "blocking": True}]
        
        # Check for signals (not in V2 yet, placeholder)
        signals = []
        
        # Check for incident
        log_path = run_dir / "logs" / "run.log"
        has_incident = False
        if log_path.exists():
            try:
                log_content = log_path.read_text(encoding="utf-8")
                if "status: FAILED" in log_content or "ERROR:" in log_content:
                    has_incident = True
            except IOError:
                pass
        
        # Determine status
        status = "completed"
        if has_incident:
            status = "failed"
        elif validator_status == "FAIL":
            status = "gated"
        elif blocking_gates:
            status = "gated"
        
        # Get creation time
        stat = run_dir.stat()
        created_at = datetime.fromtimestamp(stat.st_mtime).isoformat()
        
        return RunSummary(
            run_id=run_id,
            excerpt_id=excerpt_id,
            status=status,
            created_at=created_at,
            validator_status=validator_status,
            blocking_gates=blocking_gates,
            gate_count=len(gates),
            signal_count=len(signals),
            has_incident=has_incident,
            manifest=manifest,
            layout_type="runner_v2",
        )
    
    @staticmethod
    def scan_phase8_layout(phase8_path: Path) -> List[RunSummary]:
        """
        Scan Phase-8 layout: sandbox/phase8_runs/P8_RUN_<timestamp>/
        """
        summaries = []
        
        if not phase8_path.exists():
            return summaries
        
        for run_dir in sorted(phase8_path.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
            if not run_dir.is_dir() or not run_dir.name.startswith("P8_RUN_"):
                continue
            
            run_id = run_dir.name
            summary = RunLayoutAdapter._read_phase8_run(run_dir, run_id)
            if summary:
                summaries.append(summary)
        
        return summaries
    
    @staticmethod
    def _read_phase8_run(run_dir: Path, run_id: str) -> Optional[RunSummary]:
        """Read Phase-8 run directory."""
        # Check validator report
        validator_path = run_dir / "eval" / "output_contract_checks.txt"
        validator_status = None
        if validator_path.exists():
            try:
                content = validator_path.read_text(encoding="utf-8")
                if "overall_status: PASS" in content:
                    validator_status = "PASS"
                elif "overall_status: FAIL" in content:
                    validator_status = "FAIL"
            except IOError:
                pass
        
        # Check for gates
        gates = []
        blocking_gates = False
        if validator_status == "FAIL":
            blocking_gates = True
            gates = [{"type": "output_contract", "blocking": True}]
        
        # Check for incident
        log_path = run_dir / "logs" / "run.log"
        has_incident = False
        if log_path.exists():
            try:
                log_content = log_path.read_text(encoding="utf-8")
                if "ERROR" in log_content.upper():
                    has_incident = True
            except IOError:
                pass
        
        # Determine status
        status = "completed"
        if has_incident:
            status = "failed"
        elif validator_status == "FAIL":
            status = "gated"
        
        # Get creation time
        stat = run_dir.stat()
        created_at = datetime.fromtimestamp(stat.st_mtime).isoformat()
        
        # Try to read command.txt for metadata
        manifest = {}
        command_path = run_dir / "command.txt"
        if command_path.exists():
            try:
                command = command_path.read_text(encoding="utf-8").strip()
                manifest["command"] = command
            except IOError:
                pass
        
        return RunSummary(
            run_id=run_id,
            excerpt_id=None,  # Phase-8 doesn't have excerpt_id
            status=status,
            created_at=created_at,
            validator_status=validator_status,
            blocking_gates=blocking_gates,
            gate_count=len(gates),
            signal_count=0,
            has_incident=has_incident,
            manifest=manifest,
            layout_type="phase8",
        )
    
    @staticmethod
    def scan_all(base_path: Path) -> List[RunSummary]:
        """Scan all run layouts and return normalized summaries."""
        summaries = []
        
        # Scan Runner V2 layout
        runs_path = base_path / "runs"
        summaries.extend(RunLayoutAdapter.scan_runner_v2_layout(runs_path))
        
        # Scan Phase-8 layout
        phase8_path = base_path / "sandbox" / "phase8_runs"
        summaries.extend(RunLayoutAdapter.scan_phase8_layout(phase8_path))
        
        # Scan Phase-9 layout (similar to Phase-8)
        phase9_path = base_path / "sandbox" / "phase9_runs"
        if phase9_path.exists():
            for run_dir in sorted(phase9_path.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
                if not run_dir.is_dir() or not run_dir.name.startswith("P9_RUN_"):
                    continue
                
                run_id = run_dir.name
                # Phase-9 similar to Phase-8, reuse logic
                summary = RunLayoutAdapter._read_phase8_run(run_dir, run_id)
                if summary:
                    summary.layout_type = "phase9"
                    summaries.append(summary)
        
        return summaries
