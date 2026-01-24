#!/usr/bin/env python3
"""
B9 — Exporter skeleton (non-deterministic, derived-only).

Consumes:
- runtime/manifests/book_manifest.json
- referenced build_manifest.json

Produces:
- runtime/exports/books/<book_id>/releases/<release_id>/
  - build_manifest.json (copied)
  - build_manifest_<n>.json (if multiple build manifests)
  - files/<relative paths> (copied as-is)
  - EXPORTER_README.txt
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

RUNTIME_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = RUNTIME_ROOT / "manifests" / "book_manifest.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def is_safe_rel_path(rel: str) -> bool:
    if not rel:
        return False
    rel = rel.replace("\\", "/")
    if rel.startswith("/"):
        return False
    parts = rel.split("/")
    return all(p not in ("..", "") for p in parts)


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_book_entries(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    books = payload.get("books")
    if isinstance(books, list):
        return [b for b in books if isinstance(b, dict)]
    if isinstance(payload, dict):
        return [payload]
    return []


def parse_args(argv: List[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="B9 exporter skeleton (derived-only).")
    ap.add_argument("--book-id", default=None, help="Export a single book_id")
    ap.add_argument("--release-id", default="latest", help="Release id (default: latest)")
    ap.add_argument("--manifest", default=str(DEFAULT_MANIFEST), help="Path to book_manifest.json")
    ap.add_argument("--out-dir", default="exports/books", help="Output base dir relative to runtime root")
    ap.add_argument("--dry-run", action="store_true", help="Print actions without writing files")
    return ap.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = (RUNTIME_ROOT / manifest_path).resolve()

    if not manifest_path.exists():
        print(f"Missing book_manifest.json: {manifest_path}", file=sys.stderr)
        return 1

    payload = load_json(manifest_path)
    book_entries = iter_book_entries(payload)
    if not book_entries:
        print("No books found in book_manifest.json")
        return 0

    book_ids = sorted({b.get("book_id") for b in book_entries if isinstance(b.get("book_id"), str) and b.get("book_id")})
    if args.book_id:
        if args.book_id not in book_ids:
            print(f"book_id not found in manifest: {args.book_id}", file=sys.stderr)
            return 2
        book_entries = [b for b in book_entries if b.get("book_id") == args.book_id]
    elif len(book_entries) > 1:
        # Predictable default: first by sorted book_id
        first_id = book_ids[0] if book_ids else None
        if first_id:
            book_entries = [b for b in book_entries if b.get("book_id") == first_id]

    out_dir = args.out_dir.strip("/")
    out_base = (RUNTIME_ROOT / out_dir).resolve()

    for entry in book_entries:
        book_id = entry.get("book_id") or "BOOK-DEFAULT"
        exports = entry.get("exports", [])
        if not isinstance(exports, list) or not exports:
            print(f"No exports found for book_id={book_id}")
            continue

        release_dir = out_base / book_id / "releases" / args.release_id
        files_dir = release_dir / "files"

        build_manifest_paths: List[Path] = []
        for exp in exports:
            if not isinstance(exp, dict):
                continue
            bm_ref = exp.get("build_manifest")
            if not isinstance(bm_ref, str) or not bm_ref:
                continue
            bm_path = (RUNTIME_ROOT / bm_ref).resolve()
            if not bm_path.exists():
                print(f"Referenced build_manifest not found: {bm_ref}", file=sys.stderr)
                return 3
            if bm_path not in build_manifest_paths:
                build_manifest_paths.append(bm_path)

        if not build_manifest_paths:
            print(f"No build_manifest references found for book_id={book_id}")
            continue

        if not args.dry_run:
            release_dir.mkdir(parents=True, exist_ok=True)
            files_dir.mkdir(parents=True, exist_ok=True)

        copied_files: List[str] = []
        for idx, bm_path in enumerate(build_manifest_paths, start=1):
            dst_name = "build_manifest.json" if idx == 1 else f"build_manifest_{idx}.json"
            if not args.dry_run:
                shutil.copy2(bm_path, release_dir / dst_name)

            data = load_json(bm_path)
            exports_block = data.get("exports", {}) if isinstance(data, dict) else {}
            file_list = exports_block.get("files", []) if isinstance(exports_block, dict) else []
            for rel in file_list:
                if not isinstance(rel, str) or not is_safe_rel_path(rel):
                    continue
                src = (RUNTIME_ROOT / rel).resolve()
                if not src.exists() or not src.is_file():
                    continue
                dst = files_dir / rel
                if not args.dry_run:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                copied_files.append(rel)

        readme_lines = [
            "Exporter: B9 skeleton",
            f"Generated at: {utc_now()}",
            f"Input book_manifest: {manifest_path}",
            f"Book id: {book_id}",
            f"Release id: {args.release_id}",
            "Notes: non-deterministic, no checksums, no packaging.",
            f"Build manifests: {len(build_manifest_paths)}",
            f"Files copied: {len(copied_files)}",
        ]
        if not args.dry_run:
            (release_dir / "EXPORTER_README.txt").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")

        print(f"Export written to {release_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
