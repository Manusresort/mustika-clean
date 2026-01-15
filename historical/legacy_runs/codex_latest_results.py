from __future__ import annotations

import json
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "sandbox" / "crew" / "run_logs"


def find_latest_json_log() -> Optional[Path]:
    if not LOG_DIR.exists():
        return None
    candidates = sorted(LOG_DIR.glob("*.json"))
    if not candidates:
        return None
    return candidates[-1]


def main() -> None:
    latest = find_latest_json_log()
    if latest is None:
        print("[INFO] No JSON logs found in sandbox/crew/run_logs/")
        return

    try:
        text = latest.read_text(encoding="utf-8").strip()
    except Exception as e:
        print(f"[WARN] Could not read {latest}: {e}")
        return

    # Probeer te pretty-printen als JSON, val anders terug op raw text
    try:
        data = json.loads(text)
        pretty = json.dumps(data, indent=2, ensure_ascii=False)
        print(pretty)
    except Exception:
        print(text)


if __name__ == "__main__":
    main()
