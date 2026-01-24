#!/usr/bin/env python3
"""
B9 — Book manifest generation.

Writes runtime/manifests/book_manifest.json as a derived artifact.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RUNTIME_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RUNTIME_ROOT))

from indexer import Indexer, _write_index_json_if_changed


def _load_json_if_exists(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def main() -> int:
    indexer = Indexer(RUNTIME_ROOT)

    book_rollup_path = RUNTIME_ROOT / "indices" / "book_closure_rollup.json"
    if not book_rollup_path.exists():
        print(f"ERROR: missing required {book_rollup_path}", file=sys.stderr)
        return 2

    book_rollup = _load_json_if_exists(book_rollup_path)
    chapter_manifest = indexer.load_chapter_manifest()
    build_manifest_entries = indexer.load_build_manifest_entries()
    closure_index_ids = indexer.load_closure_index()

    payload = indexer.build_book_manifest_payload(
        chapter_manifest=chapter_manifest,
        book_rollup_payload=book_rollup,
        build_manifest_entries=build_manifest_entries,
        closure_index_ids=closure_index_ids,
    )

    out_path = RUNTIME_ROOT / "manifests" / "book_manifest.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_index_json_if_changed(out_path, payload)
    print(f"OK  book_manifest={out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
