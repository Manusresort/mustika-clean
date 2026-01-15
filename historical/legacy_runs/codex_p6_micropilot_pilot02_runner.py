from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


# Project root (Crew-AI/)
BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "sandbox" / "crew" / "run_logs"


def make_log_path() -> Path:
    """
    Create a timestamped log path for the P6 SAYUR mini Pilot 02 run.
    The log prefix distinguishes Pilot 02 from P5 micropilot logs.
    """
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    return LOG_DIR / f"P6_PILOT02_SAYUR_MINI_{ts}.log"


def main() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    log_path = make_log_path()

    runner_path = BASE_DIR / "sandbox" / "crew" / "micropilot_sayur_pilot02_runner.py"

    # Run the Pilot 02 SAYUR mini workflow runner.
    # This P6 wrapper does not alter behavior; it only captures stdout/stderr
    # into a clearly tagged log file for documentary analysis.
    result = subprocess.run(
        ["python3", str(runner_path)],
        capture_output=True,
        text=True,
    )

    output = result.stdout
    if result.stderr:
        output = f"{output}\n{result.stderr}" if output else result.stderr

    log_path.write_text(output, encoding="utf-8")

    print(f"[INFO] P6 Pilot 02 log written to: {log_path}")
    if result.returncode != 0:
        print(f"[WARN] Subprocess exited with code {result.returncode}")


if __name__ == "__main__":
    main()
