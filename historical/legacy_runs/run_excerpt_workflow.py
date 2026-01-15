"""
run_excerpt_workflow.py

Initial excerpt-aware runner for Phase-6 sandbox runs.

- Reads excerpt metadata from CLI.
- Writes a structured log header.
- Optionally runs an existing pipeline if a Python config is provided.
- Creates the run_outputs directory if the pipeline succeeds.

This is a minimal implementation aligned with Phase-6 design docs.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple


BASE_DIR = Path(__file__).resolve().parents[2]
LOG_ROOT = BASE_DIR / "sandbox" / "crew" / "run_logs"
OUTPUT_ROOT = BASE_DIR / "sandbox" / "crew" / "run_outputs"


@dataclass
class RunContext:
    excerpt_id: str
    excerpt_source: str
    excerpt_version: str
    config_path: Optional[Path]
    run_id: str
    started_at: str
    log_path: Path
    cli_config_mismatch: bool


def utc_timestamp_compact() -> str:
    return datetime.utcnow().strftime("%Y%m%dT%H%M%S")


def utc_timestamp_iso() -> str:
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def safe_id(value: str) -> str:
    return value.replace("/", "_").replace(" ", "_") if value else "unknown_excerpt"


def generate_run_id(excerpt_id: str) -> str:
    ts = utc_timestamp_compact()
    return f"RUN_{safe_id(excerpt_id)}_{ts}"


def make_log_path(excerpt_id: str, run_id: str) -> Path:
    log_dir = LOG_ROOT / safe_id(excerpt_id)
    log_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{run_id}_{utc_timestamp_compact()}.log"
    return log_dir / filename


def write_log_header(ctx: RunContext, status: str, stop_reason: Optional[str] = None) -> None:
    lines = [
        "mode: excerpt-aware",
        f"excerpt_id: {ctx.excerpt_id}",
        f"excerpt_source: {ctx.excerpt_source}",
        f"excerpt_version: {ctx.excerpt_version}",
        f"run_id: {ctx.run_id}",
        f"started_at: {ctx.started_at}",
        f"status: {status}",
        f"config_path: {ctx.config_path or ''}",
        f"cli_config_mismatch: {str(ctx.cli_config_mismatch).lower()}",
    ]
    if stop_reason:
        lines.append(f"stop_reason: {stop_reason}")
    lines.append("")
    ctx.log_path.write_text("\n".join(lines), encoding="utf-8")


def append_log(ctx: RunContext, message: str) -> None:
    with ctx.log_path.open("a", encoding="utf-8") as f:
        f.write(message)
        if not message.endswith("\n"):
            f.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase-6 excerpt-aware runner")
    parser.add_argument("--excerpt-id", dest="excerpt_id", required=False)
    parser.add_argument("--excerpt-source", dest="excerpt_source", required=False)
    parser.add_argument("--excerpt-version", dest="excerpt_version", required=False)
    parser.add_argument("--config", dest="config", required=False)
    parser.add_argument("--run-id", dest="run_id", required=False)
    return parser.parse_args()


def preflight_missing_fields(excerpt_id: str, excerpt_source: str, excerpt_version: str) -> list[str]:
    missing = []
    if not excerpt_id:
        missing.append("excerpt_id")
    if not excerpt_source:
        missing.append("excerpt_source")
    if not excerpt_version:
        missing.append("excerpt_version")
    return missing


def resolve_runner_script(config_path: Path) -> Tuple[Optional[Path], str]:
    if not config_path.exists():
        return None, f"Config path not found: {config_path}"

    if config_path.suffix == ".py":
        return config_path, ""

    if config_path.suffix in {".yaml", ".yml"}:
        candidate = config_path.with_name(f"{config_path.stem}_runner.py")
        if candidate.exists():
            return candidate, ""
        fallback = (BASE_DIR / "sandbox" / "crew" / f"{config_path.stem}_runner.py")
        if fallback.exists():
            return fallback, ""
        return None, f"No runner script found for YAML config: {config_path}"

    return None, f"Unsupported config type: {config_path.suffix}"


def extract_block(text: str, start_marker: str, end_marker: str) -> Optional[str]:
    if start_marker not in text or end_marker not in text:
        return None
    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker, start)
    return text[start:end].strip()


def parse_json_payload(text: Optional[str]) -> Tuple[Optional[object], Optional[str]]:
    if text is None:
        return None, None
    try:
        return json.loads(text), None
    except Exception as e:
        return None, f"JSON parse failed: {e}"


def run_pipeline(config_path: Optional[Path]) -> Tuple[int, str, Optional[object], Optional[object], Optional[str]]:
    if not config_path:
        return 1, "Config path is required to run the pipeline.", None, None, None

    runner_path, err = resolve_runner_script(config_path)
    if not runner_path:
        return 1, err, None, None, None

    result = subprocess.run(
        ["python3", str(runner_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )

    output = result.stdout
    if result.stderr:
        output = f"{output}\n{result.stderr}" if output else result.stderr

    annot_block = extract_block(output, "---ANNOTATIONS---", "---CHALLENGE_REPORT---")
    chall_block = extract_block(output, "---CHALLENGE_REPORT---", "---OPTIONAL_AGENT_STEPS---")

    annot_payload, annot_err = parse_json_payload(annot_block) if annot_block else parse_json_payload(output.strip() or None)
    chall_payload, chall_err = parse_json_payload(chall_block) if chall_block else (None, None)

    parse_note = annot_err or chall_err
    return result.returncode, output, annot_payload, chall_payload, parse_note


def write_json_payload(path: Path, ctx: RunContext, raw_output: str, payload: Optional[object]) -> None:
    data = {
        "excerpt": {
            "id": ctx.excerpt_id,
            "source": ctx.excerpt_source,
            "version": ctx.excerpt_version,
        },
        "run": {
            "id": ctx.run_id,
            "timestamp": ctx.started_at,
        },
        "raw_output": raw_output,
        "payload": payload,
    }
    path.write_text(json.dumps(data, ensure_ascii=True, indent=2), encoding="utf-8")


def main() -> int:
    args = parse_args()

    excerpt_id = (args.excerpt_id or "").strip()
    excerpt_source = (args.excerpt_source or "").strip()
    excerpt_version = (args.excerpt_version or "").strip()
    config_path = Path(args.config) if args.config else None

    # TODO: reconcile CLI vs config values (config should be source of truth).
    cli_config_mismatch = False

    run_id = (args.run_id or "").strip() or generate_run_id(excerpt_id)

    log_path = make_log_path(excerpt_id, run_id)
    ctx = RunContext(
        excerpt_id=excerpt_id,
        excerpt_source=excerpt_source,
        excerpt_version=excerpt_version,
        config_path=config_path,
        run_id=run_id,
        started_at=utc_timestamp_iso(),
        log_path=log_path,
        cli_config_mismatch=cli_config_mismatch,
    )

    missing = preflight_missing_fields(excerpt_id, excerpt_source, excerpt_version)
    if missing:
        stop_reason = f"missing required metadata: {', '.join(missing)}"
        write_log_header(ctx, status="SOFT-STOP", stop_reason=stop_reason)
        append_log(ctx, "Pre-flight failed; exiting before pipeline execution.")
        return 2

    write_log_header(ctx, status="PENDING")
    append_log(ctx, "Pre-flight OK. Starting pipeline.")

    try:
        returncode, output, annot_payload, chall_payload, parse_note = run_pipeline(config_path)
        if output:
            append_log(ctx, "--- PIPELINE OUTPUT ---")
            append_log(ctx, output)
        if parse_note:
            append_log(ctx, f"[WARN] {parse_note}")

        if returncode != 0:
            append_log(ctx, "Pipeline failed or not implemented.")
            append_log(ctx, "status: ERROR")
            return 3

        output_dir = OUTPUT_ROOT / safe_id(excerpt_id) / run_id
        output_dir.mkdir(parents=True, exist_ok=True)

        annot_path = output_dir / "annotator_primary.json"
        chall_path = output_dir / "challenger_primary.json"

        write_json_payload(annot_path, ctx, output, annot_payload)
        write_json_payload(chall_path, ctx, output, chall_payload)

        append_log(ctx, f"Run outputs directory created: {output_dir}")
        append_log(ctx, "Wrote annotator_primary.json and challenger_primary.json.")
        append_log(ctx, "status: COMPLETED")
        return 0

    except Exception as e:
        append_log(ctx, f"Exception during pipeline execution: {e}")
        append_log(ctx, "status: ERROR")
        return 4


if __name__ == "__main__":
    sys.exit(main())
