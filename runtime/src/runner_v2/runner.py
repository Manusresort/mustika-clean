"""
Runner V2 - Phase-6 Excerpt-Aware Runner
Clean implementation with explicit excerpt metadata and standardized outputs.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
import os
import shutil


class RunnerV2:
    """Phase-6 excerpt-aware runner."""
    
    def __init__(self, base_path: Path):
        self.base_path = Path(base_path).resolve()
        self.runs_path = self.base_path / "runs"
        self.sandbox_tools = self.base_path / "sandbox" / "tools"
    
    def validate_preflight(
        self,
        excerpt_id: Optional[str],
        excerpt_source: Optional[str],
        excerpt_version: Optional[str],
        run_id: Optional[str],
    ) -> tuple[bool, Optional[str], Dict[str, Any]]:
        """
        Pre-flight validation: check required metadata.
        
        Returns: (is_valid, error_message, metadata_dict)
        """
        errors = []
        metadata = {}
        
        if not excerpt_id:
            errors.append("excerpt_id is required")
        else:
            metadata["excerpt_id"] = excerpt_id
        
        if not excerpt_source:
            errors.append("excerpt_source is required")
        else:
            metadata["excerpt_source"] = excerpt_source
        
        if not excerpt_version:
            errors.append("excerpt_version is required")
        else:
            metadata["excerpt_version"] = excerpt_version
        
        if not run_id:
            # Generate run_id if not provided
            timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
            safe_excerpt = excerpt_id.replace("/", "_").replace(" ", "_") if excerpt_id else "unknown"
            run_id = f"RUN_{safe_excerpt}_{timestamp}"
            metadata["run_id"] = run_id
        else:
            # Validate run_id format (basic check)
            if "/" in run_id or " " in run_id:
                errors.append(f"run_id contains invalid characters: {run_id}")
            else:
                metadata["run_id"] = run_id
        
        if errors:
            return False, "; ".join(errors), metadata
        
        return True, None, metadata
    
    def create_run_directory(self, excerpt_id: str, run_id: str) -> Path:
        """Create run directory structure."""
        run_dir = self.runs_path / excerpt_id / run_id
        run_dir.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories
        (run_dir / "logs").mkdir(exist_ok=True)
        (run_dir / "outputs").mkdir(exist_ok=True)
        (run_dir / "eval").mkdir(exist_ok=True)
        (run_dir / "inputs").mkdir(exist_ok=True)
        
        return run_dir
    
    def write_log_header(
        self,
        log_path: Path,
        metadata: Dict[str, Any],
        status: str = "PENDING",
        stop_reason: Optional[str] = None,
    ) -> None:
        """Write log header with excerpt metadata."""
        lines = [
            "mode: excerpt-aware",
            f"excerpt_id: {metadata['excerpt_id']}",
            f"excerpt_source: {metadata['excerpt_source']}",
            f"excerpt_version: {metadata['excerpt_version']}",
            f"run_id: {metadata['run_id']}",
            f"started_at: {datetime.utcnow().isoformat()}",
            f"status: {status}",
        ]
        if stop_reason:
            lines.append(f"stop_reason: {stop_reason}")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        log_path.write_text("\n".join(lines), encoding="utf-8")
    
    def append_log(self, log_path: Path, message: str) -> None:
        """Append message to log file."""
        with log_path.open("a", encoding="utf-8") as f:
            f.write(message)
            if not message.endswith("\n"):
                f.write("\n")
    
    def write_command_file(self, run_dir: Path, command: List[str]) -> None:
        """Write command.txt for reproducibility."""
        command_path = run_dir / "command.txt"
        command_path.write_text(" ".join(command) + "\n", encoding="utf-8")
    
    def write_env_allowlist(self, run_dir: Path) -> None:
        """Write redacted environment variables."""
        env_path = run_dir / "env_allowlist.txt"
        # Redact sensitive vars, keep safe ones
        safe_vars = ["PATH", "HOME", "USER", "SHELL", "LANG", "TERM"]
        env_lines = []
        for var in safe_vars:
            if var in os.environ:
                env_lines.append(f"{var}={os.environ[var]}")
        env_lines.append("OPENAI_API_KEY=[REDACTED]")
        env_path.write_text("\n".join(env_lines) + "\n", encoding="utf-8")
    
    def run_pipeline(
        self,
        run_dir: Path,
        english_text: str,
        rough_nl_text: str,
        log_path: Path,
    ) -> tuple[bool, str]:
        """
        Run the 3-phase pipeline (Translation → Readability → Fidelity).
        
        Returns: (success, output_text)
        """
        try:
            # Import pipeline function
            sys.path.insert(0, str(self.base_path))
            from test_multi_agent_fidelity import run_pipeline
            
            self.append_log(log_path, f"[{datetime.utcnow().isoformat()}] Starting pipeline...")
            
            result = run_pipeline(english_text, rough_nl_text)
            
            # Handle both string and dict results
            if isinstance(result, dict):
                output_text = result.get("text", "")
                remarks = result.get("remarks", "")
                if remarks:
                    output_text = f"{output_text}\n\nOpmerkingen:\n{remarks}\n"
            else:
                output_text = str(result)
            
            self.append_log(log_path, f"[{datetime.utcnow().isoformat()}] Pipeline completed")
            
            return True, output_text
            
        except Exception as e:
            error_msg = f"Pipeline failed: {str(e)}"
            self.append_log(log_path, f"[{datetime.utcnow().isoformat()}] ERROR: {error_msg}")
            return False, error_msg
    
    def create_output_files(
        self,
        run_dir: Path,
        metadata: Dict[str, Any],
        pipeline_output: str,
        log_path: Path,
    ) -> None:
        """Create required output files (JSON + text)."""
        outputs_dir = run_dir / "outputs"
        
        # Extract main text and remarks
        remarks_start = pipeline_output.find("\n\nOpmerkingen:")
        if remarks_start >= 0:
            main_text = pipeline_output[:remarks_start].strip()
            remarks_section = pipeline_output[remarks_start + 2:].strip()
        else:
            main_text = pipeline_output.strip()
            remarks_section = ""
        
        # annotator_primary.json (main structured output)
        annotator_output = {
            "excerpt_id": metadata["excerpt_id"],
            "excerpt_source": metadata["excerpt_source"],
            "excerpt_version": metadata["excerpt_version"],
            "run_id": metadata["run_id"],
            "output_type": "annotator_primary",
            "main_text": main_text,
            "remarks": remarks_section,
            "created_at": datetime.utcnow().isoformat(),
        }
        (outputs_dir / "annotator_primary.json").write_text(
            json.dumps(annotator_output, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        
        # challenger_primary.json (placeholder - no challenger in current pipeline)
        challenger_output = {
            "excerpt_id": metadata["excerpt_id"],
            "excerpt_source": metadata["excerpt_source"],
            "excerpt_version": metadata["excerpt_version"],
            "run_id": metadata["run_id"],
            "output_type": "challenger_primary",
            "issues": [],
            "created_at": datetime.utcnow().isoformat(),
        }
        (outputs_dir / "challenger_primary.json").write_text(
            json.dumps(challenger_output, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        
        # crew_provisional.json (consolidated output)
        crew_output = {
            "excerpt_id": metadata["excerpt_id"],
            "excerpt_source": metadata["excerpt_source"],
            "excerpt_version": metadata["excerpt_version"],
            "run_id": metadata["run_id"],
            "output_type": "crew_provisional",
            "main_text": main_text,
            "remarks": remarks_section,
            "annotator_output": annotator_output,
            "challenger_output": challenger_output,
            "created_at": datetime.utcnow().isoformat(),
        }
        (outputs_dir / "crew_provisional.json").write_text(
            json.dumps(crew_output, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        
        # final.txt (for validator compatibility)
        (outputs_dir / "final.txt").write_text(pipeline_output, encoding="utf-8")
        
        # review_notes.md (template)
        review_template = f"""# Review Notes

## Excerpt: {metadata['excerpt_id']}
## Run: {metadata['run_id']}
## Created: {datetime.utcnow().isoformat()}

## Review Decision

[ ] Approve
[ ] Request Changes
[ ] Reject

## Notes

[Add review notes here]

## Changes Requested

[If requesting changes, list them here]
"""
        (outputs_dir / "review_notes.md").write_text(review_template, encoding="utf-8")
        
        self.append_log(log_path, f"[{datetime.utcnow().isoformat()}] Output files created")
    
    def run_validator(self, run_dir: Path, log_path: Path) -> tuple[bool, Optional[str]]:
        """
        Run output contract validator.
        
        Returns: (success, validator_report_path)
        """
        validator_script = self.sandbox_tools / "phase8_output_contract_validator.sh"
        
        if not validator_script.exists():
            self.append_log(log_path, f"[{datetime.utcnow().isoformat()}] WARNING: Validator script not found: {validator_script}")
            return False, None
        
        try:
            self.append_log(log_path, f"[{datetime.utcnow().isoformat()}] Running validator...")
            
            result = subprocess.run(
                [str(validator_script), str(run_dir)],
                capture_output=True,
                text=True,
                cwd=str(self.base_path),
            )
            
            report_path = run_dir / "eval" / "output_contract_checks.txt"
            
            if result.returncode == 0:
                self.append_log(log_path, f"[{datetime.utcnow().isoformat()}] Validator PASSED")
                return True, str(report_path)
            else:
                self.append_log(log_path, f"[{datetime.utcnow().isoformat()}] Validator FAILED: {result.stderr}")
                return False, str(report_path) if report_path.exists() else None
                
        except Exception as e:
            error_msg = f"Validator execution failed: {str(e)}"
            self.append_log(log_path, f"[{datetime.utcnow().isoformat()}] ERROR: {error_msg}")
            return False, None
    
    def create_manifest(self, run_dir: Path, metadata: Dict[str, Any], inputs: Dict[str, str]) -> None:
        """Create manifest.json for indexer compatibility."""
        manifest = {
            "excerpt_id": metadata["excerpt_id"],
            "excerpt_source": metadata["excerpt_source"],
            "excerpt_version": metadata["excerpt_version"],
            "run_id": metadata["run_id"],
            "created_at": datetime.utcnow().isoformat(),
            "inputs": inputs,
            "output_files": [
                "outputs/annotator_primary.json",
                "outputs/challenger_primary.json",
                "outputs/crew_provisional.json",
                "outputs/final.txt",
            ],
        }
        
        manifest_path = run_dir / "manifest.json"
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
    
    def run(
        self,
        excerpt_id: str,
        excerpt_source: str,
        excerpt_version: str,
        english_text: str,
        rough_nl_text: str,
        run_id: Optional[str] = None,
    ) -> tuple[bool, Path, Optional[str]]:
        """
        Execute complete run workflow.
        
        Returns: (success, run_dir, error_message)
        """
        # Pre-flight validation
        is_valid, error_msg, metadata = self.validate_preflight(
            excerpt_id, excerpt_source, excerpt_version, run_id
        )
        
        if not is_valid:
            return False, Path(), error_msg
        
        # Create run directory
        run_dir = self.create_run_directory(metadata["excerpt_id"], metadata["run_id"])
        log_path = run_dir / "logs" / "run.log"
        
        # Write log header
        self.write_log_header(log_path, metadata, status="RUNNING")
        
        try:
            # Write command and env files
            command = [
                "mustika_run_excerpt",
                "--excerpt-id", metadata["excerpt_id"],
                "--excerpt-source", metadata["excerpt_source"],
                "--excerpt-version", metadata["excerpt_version"],
                "--run-id", metadata["run_id"],
            ]
            self.write_command_file(run_dir, command)
            self.write_env_allowlist(run_dir)
            
            # Save inputs
            (run_dir / "inputs" / "english.txt").write_text(english_text, encoding="utf-8")
            (run_dir / "inputs" / "rough_nl.txt").write_text(rough_nl_text, encoding="utf-8")
            
            # Run pipeline
            pipeline_success, pipeline_output = self.run_pipeline(
                run_dir, english_text, rough_nl_text, log_path
            )
            
            if not pipeline_success:
                self.write_log_header(log_path, metadata, status="FAILED", stop_reason=pipeline_output)
                return False, run_dir, pipeline_output
            
            # Create output files
            self.create_output_files(run_dir, metadata, pipeline_output, log_path)
            
            # Run validator
            validator_success, validator_report = self.run_validator(run_dir, log_path)
            
            # Create manifest
            self.create_manifest(
                run_dir,
                metadata,
                inputs={
                    "english": "inputs/english.txt",
                    "rough_nl": "inputs/rough_nl.txt",
                }
            )
            
            # Update log status
            if validator_success:
                self.write_log_header(log_path, metadata, status="COMPLETED")
            else:
                self.write_log_header(log_path, metadata, status="GATED", stop_reason="Validator failed")
            
            return True, run_dir, None
            
        except Exception as e:
            error_msg = f"Run failed: {str(e)}"
            self.write_log_header(log_path, metadata, status="FAILED", stop_reason=error_msg)
            return False, run_dir, error_msg
