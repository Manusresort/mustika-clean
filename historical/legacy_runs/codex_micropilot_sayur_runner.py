from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "sandbox" / "crew" / "run_logs"


def make_log_path() -> Path:
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    return LOG_DIR / f"MICROPILOT_SAYUR_{ts}.log"


def main() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = make_log_path()

    result = subprocess.run(
        ["python3", "sandbox/crew/micropilot_sayur_multi_runner.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )

    output = result.stdout
    if result.stderr:
        output = f"{output}\n{result.stderr}" if output else result.stderr

    # Preserve output; if markers are present, keep them as-is.
    log_path.write_text(output, encoding="utf-8")

    print(f"[INFO] Log written to: {log_path}")


if __name__ == "__main__":
    main()
