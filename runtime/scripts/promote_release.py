#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

RUNTIME_ROOT = Path(__file__).resolve().parents[1]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json_atomic(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def parse_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Promote a release (manual-only).")
    ap.add_argument("--book-id", required=True)
    ap.add_argument("--release-id", required=True)
    ap.add_argument("--actor", required=True)
    return ap.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    if os.environ.get("CI") == "true":
        print("ERROR: promotion is manual-only; CI is not allowed")
        return 1

    book_id = args.book_id
    release_id = args.release_id

    release_dir = RUNTIME_ROOT / "exports" / "books" / book_id / "releases" / release_id
    trust_path = release_dir / "release_trust.json"
    if not trust_path.exists():
        print(f"ERROR: missing release_trust.json at {trust_path}")
        return 1

    trust = read_json(trust_path)
    if trust.get("trust_level") != "ci_passed":
        print("ERROR: trust_level is not ci_passed")
        return 1

    promotion_path = release_dir / "promotion.json"
    if promotion_path.exists():
        print(f"ERROR: promotion already exists at {promotion_path}")
        return 1
    payload = {
        "release_id": release_id,
        "promoted_at": utc_now(),
        "actor": args.actor,
        "basis": "ci_passed",
        "source": "manual",
    }
    write_json_atomic(promotion_path, payload)
    print(f"OK: wrote {promotion_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(os.sys.argv[1:]))
