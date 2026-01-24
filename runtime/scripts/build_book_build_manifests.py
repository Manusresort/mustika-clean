#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


def utc_now_iso_z() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def norm_rel_path(rel: str) -> str:
    rel = rel.replace("\\", "/")
    while rel.startswith("./"):
        rel = rel[2:]
    return rel.strip("/")


def is_safe_rel_path(rel: str) -> bool:
    if not rel:
        return False
    if rel.startswith("/") or rel.startswith("\\"):
        return False
    parts = rel.replace("\\", "/").split("/")
    return not any(p == ".." for p in parts)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_text_if_changed(path: Path, text: str) -> None:
    if path.exists():
        existing = path.read_text(encoding="utf-8", errors="replace")
        if existing == text:
            return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def try_cmd(cmd: List[str]) -> Optional[str]:
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True).strip()
        return out
    except Exception:
        return None


def tool_versions() -> dict:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "node": try_cmd(["node", "--version"]),
        "npm": try_cmd(["npm", "--version"]),
    }


def collect_export_files(runtime_root: Path, roots: List[Tuple[str, Path]]) -> Tuple[List[str], Dict[str, str]]:
    """
    Collect repo-relative file paths under each root. Return (sorted_paths, sha256_map).
    Roots are labeled; label is included in manifest separately.
    """
    all_files: List[str] = []
    sha_map: Dict[str, str] = {}

    for _, root in roots:
        if not root.exists():
            continue
        if root.is_file():
            rel = str(root.relative_to(runtime_root)).replace("\\", "/")
            if is_safe_rel_path(rel):
                all_files.append(rel)
                sha_map[rel] = sha256_file(root)
            continue

        for p in sorted(root.rglob("*")):
            if not p.is_file():
                continue
            rel = str(p.relative_to(runtime_root)).replace("\\", "/")
            if not is_safe_rel_path(rel):
                continue
            all_files.append(rel)
            sha_map[rel] = sha256_file(p)

    all_files = sorted(set(all_files))
    sha_map = {k: sha_map[k] for k in sorted(sha_map.keys())}
    return all_files, sha_map


def parse_args(argv: List[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book-id", default=None, help="Build manifest for a single book_id from indices/book_closure_rollup.json")
    ap.add_argument("--first", action="store_true", help="Build manifest for first book_id in rollup")
    ap.add_argument("--all", action="store_true", help="Build manifest for all book_ids in rollup")
    ap.add_argument("--out-dir", default="exports/books", help="Output base dir relative to runtime root")
    ap.add_argument("--strict", action="store_true", help="Fail if required inputs missing")
    return ap.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    runtime_root = Path(__file__).resolve().parents[1]

    roll_path = runtime_root / "indices" / "book_closure_rollup.json"
    if not roll_path.exists():
        print(f"ERROR: missing required {roll_path}", file=sys.stderr)
        return 2

    roll = read_json(roll_path)
    books = roll.get("books", [])
    if not isinstance(books, list) or not books:
        print("WARN: no books found in book_closure_rollup.json", file=sys.stderr)
        return 0

    book_ids: List[str] = []
    book_by_id: Dict[str, dict] = {}
    for b in books:
        if isinstance(b, dict) and isinstance(b.get("book_id"), str) and b["book_id"].strip():
            bid = b["book_id"].strip()
            book_ids.append(bid)
            book_by_id[bid] = b
    book_ids = sorted(set(book_ids))
    if not book_ids:
        print("WARN: no valid book_id entries", file=sys.stderr)
        return 0

    selected: List[str] = []
    if args.book_id:
        if args.book_id not in set(book_ids):
            print(f"ERROR: book_id not found: {args.book_id}", file=sys.stderr)
            return 2
        selected = [args.book_id]
    elif args.first:
        selected = [book_ids[0]]
    elif args.all:
        selected = book_ids
    else:
        print("ERROR: specify --book-id, --first, or --all", file=sys.stderr)
        return 2

    out_base = runtime_root / norm_rel_path(args.out_dir)
    out_base.mkdir(parents=True, exist_ok=True)

    versions = tool_versions()
    mapping_mode = (roll.get("mapping") or {}).get("mode")

    any_fail = False
    for bid in selected:
        b = book_by_id[bid]
        closure_ids = b.get("closure_ids", [])
        if not isinstance(closure_ids, list):
            closure_ids = []
        closure_ids = sorted({c for c in closure_ids if isinstance(c, str) and c})

        # Discover existing exports (best-effort; do not require them)
        # - chapter exports live under exports/chapters/<chapter_id>/...
        # - review packs under exports/review_packs/<proposal_id>/...
        roots: List[Tuple[str, Path]] = []

        # Include index files as "inputs" (hash them too)
        input_indices = [
            "indices/book_closure_rollup.json",
            "indices/chapter_closure_rollup.json",
            "indices/chapter_registry.json",
        ]
        for rel in input_indices:
            p = runtime_root / rel
            if p.exists():
                roots.append(("input_index", p))
            elif args.strict:
                print(f"ERROR: missing required input index: {rel}", file=sys.stderr)
                return 2

        # Include existing export roots if present
        chap_exports = runtime_root / "exports" / "chapters"
        if chap_exports.exists():
            roots.append(("chapter_exports", chap_exports))

        review_packs = runtime_root / "exports" / "review_packs"
        if review_packs.exists():
            roots.append(("review_packs", review_packs))

        files, sha_map = collect_export_files(runtime_root, roots)

        manifest = {
            "generated_at": utc_now_iso_z(),
            "book_id": bid,
            "closure_ids": closure_ids,
            "counts": {"closures": len(closure_ids), "export_files": len(files)},
            "inputs": {
                "indices": input_indices,
                "mapping_mode": mapping_mode,
            },
            "exports": {
                "roots_present": [label for (label, p) in roots if p.exists()],
                "files": files,
            },
            "sha256": sha_map,
            "tool_versions": versions,
        }

        # Deterministic JSON formatting (keys + order stable)
        text = json.dumps(manifest, indent=2, sort_keys=True) + "\n"

        out_dir = out_base / bid / "builds" / "latest"
        out_path = out_dir / "build_manifest.json"
        write_text_if_changed(out_path, text)

        rel_out = str(out_path.relative_to(runtime_root)).replace("\\", "/")
        print(f"OK  book={bid} manifest={rel_out} files={len(files)} closures={len(closure_ids)}")

    return 1 if any_fail else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
