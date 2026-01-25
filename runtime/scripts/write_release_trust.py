#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

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


def git_head_sha() -> Optional[str]:
    try:
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(RUNTIME_ROOT), text=True).strip()
        return out or None
    except Exception:
        return None


def parse_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Write release_trust.json for latest release.")
    ap.add_argument("--book-id", default="BOOK-DEFAULT")
    ap.add_argument("--conclusion", default=None, choices=["success", "failure", "cancelled", "skipped", None])
    ap.add_argument("--trust-level", required=True, choices=["ci_passed", "ci_failed", "unverified"])
    ap.add_argument("--source", required=True, choices=["ci", "local"])
    ap.add_argument("--run-id", default=None)
    ap.add_argument("--commit-sha", default=None)
    ap.add_argument("--workflow", default=None)
    return ap.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    book_id = args.book_id

    latest_path = RUNTIME_ROOT / "exports" / "books" / book_id / "releases" / "latest.json"
    if not latest_path.exists():
        print(f"ERROR: missing latest.json at {latest_path}")
        return 1

    latest = read_json(latest_path)
    release_id = latest.get("release_id")
    if not isinstance(release_id, str) or not release_id:
        print("ERROR: latest.json missing release_id")
        return 1
    if release_id == "latest":
        print("ERROR: release_id is literal 'latest'")
        return 1

    release_dir = RUNTIME_ROOT / "exports" / "books" / book_id / "releases" / release_id
    if not release_dir.exists():
        print(f"ERROR: release dir missing: {release_dir}")
        return 1

    trust_path = release_dir / "release_trust.json"

    commit_sha = args.commit_sha or os.environ.get("GITHUB_SHA") or git_head_sha()

    ci_block = {
        "workflow": args.workflow or os.environ.get("GITHUB_WORKFLOW"),
        "run_id": args.run_id or os.environ.get("GITHUB_RUN_ID"),
        "commit_sha": commit_sha,
    }

    data = {
        "book_id": book_id,
        "release_id": release_id,
        "trust_level": args.trust_level,
        "conclusion": args.conclusion,
        "source": args.source,
        "created_at": utc_now(),
        "ci": ci_block,
    }

    write_json_atomic(trust_path, data)
    print(f"OK: wrote {trust_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(os.sys.argv[1:]))
