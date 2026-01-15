"""
codex_crew_runner.py

Generic, Codex-configurable runner for CrewAI/Mistral sandbox runs.

- Config is defined at the top in CONFIG.
- A human starts this script manually from the terminal.
- The script:
  * executes the configured command (e.g. a crew shakedown runner),
  * captures stdout/stderr,
  * prints stdout to the terminal,
  * writes a combined log to sandbox/crew/run_logs/.

This script MUST NOT be imported or executed automatically
by agents or CI; it is intended for manual, sandbox-only runs.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List


# === CONFIG BLOCK (Codex may edit this, the rest of the file is stable) ===

CONFIG = {
    # Human-readable label for this runner context
    "runner_name": "P4_SAYUR_MISTRAL_CREW",

    # Command to execute (list of args).
    # Example: Python shakedown-runner in this repo.
    "command": [
        "python3",
        "sandbox/crew/shakedown_sayur_mistral_runner.py",
    ],

    # Base directory for logs (relative to project root)
    "log_dir": "sandbox/crew/run_logs",

    # Optional prefix for log filenames
    "log_prefix": "P4_SAYUR_MISTRAL_CREW_RUN",
}

# === END OF CONFIG BLOCK ===


@dataclass
class RunnerConfig:
    runner_name: str
    command: List[str]
    log_dir: Path
    log_prefix: str


def load_config() -> RunnerConfig:
    base_dir = Path(__file__).resolve().parents[2]
    cfg = CONFIG.copy()

    runner_name = str(cfg.get("runner_name") or "P4_CODEx_CREW_RUNNER")
    command = cfg.get("command") or []
    if not isinstance(command, list) or not command:
        raise ValueError("CONFIG['command'] must be a non-empty list of strings.")

    log_dir_str = cfg.get("log_dir") or "sandbox/crew/run_logs"
    log_dir = base_dir / log_dir_str

    log_prefix = str(cfg.get("log_prefix") or runner_name)

    return RunnerConfig(
        runner_name=runner_name,
        command=[str(arg) for arg in command],
        log_dir=log_dir,
        log_prefix=log_prefix,
    )


def ensure_log_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def make_log_path(cfg: RunnerConfig) -> Path:
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    filename = f"{cfg.log_prefix}_{ts}.log"
    return cfg.log_dir / filename


def run_command(cfg: RunnerConfig) -> tuple[int, str, str]:
    """
    Run the configured command as a subprocess.

    Returns:
        (returncode, stdout_text, stderr_text)
    """
    result = subprocess.run(
        cfg.command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    return result.returncode, result.stdout, result.stderr


def write_log(log_path: Path, cfg: RunnerConfig, returncode: int, stdout: str, stderr: str) -> None:
    header = [
        f"runner_name: {cfg.runner_name}",
        f"command: {' '.join(cfg.command)}",
        f"returncode: {returncode}",
        "",
        "=== STDOUT ===",
        stdout,
        "",
        "=== STDERR ===",
        stderr,
        "",
    ]
    log_text = "\n".join(header)
    log_path.write_text(log_text, encoding="utf-8")


def main() -> None:
    cfg = load_config()
    ensure_log_dir(cfg.log_dir)
    log_path = make_log_path(cfg)

    print(f"[INFO] Runner: {cfg.runner_name}")
    print(f"[INFO] Command: {' '.join(cfg.command)}")
    print(f"[INFO] Log file will be written to: {log_path}")

    returncode, stdout, stderr = run_command(cfg)

    # Print stdout directly to the terminal so humans can see agent output.
    if stdout:
        print(stdout, end="")

    # Write combined log for later inspection via Codex.
    try:
        write_log(log_path, cfg, returncode, stdout, stderr)
        print(f"\n[INFO] Log written to: {log_path}")
    except Exception as e:
        print(f"\n[WARN] Failed to write log file {log_path}: {e}")

    if returncode != 0:
        print(f"[WARN] Command exited with non-zero return code: {returncode}")


if __name__ == "__main__":
    main()
