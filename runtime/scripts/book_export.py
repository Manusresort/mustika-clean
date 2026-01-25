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
  - release_manifest.json
  - CHECKSUMS.sha256
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

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
    ap.add_argument("--book-id", "--book_id", dest="book_id", default=None, help="Export a single book_id")
    ap.add_argument("--release-id", default="latest", help="Release id (default: latest)")
    ap.add_argument("--create-release-id", action="store_true", help="Generate a new release_id and print it")
    ap.add_argument("--manifest", default=str(DEFAULT_MANIFEST), help="Path to book_manifest.json")
    ap.add_argument("--out-dir", default="exports/books", help="Output base dir relative to runtime root")
    ap.add_argument("--dry-run", action="store_true", help="Print actions without writing files")
    return ap.parse_args(argv)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def generate_release_id(book_id: str, manifest_path: Path, nonce: Optional[str] = None) -> str:
    ts = datetime.now(timezone.utc).strftime("R%Y%m%dT%H%M%SZ")
    seed = manifest_path.read_bytes() + book_id.encode("utf-8")
    if nonce:
        seed += nonce.encode("utf-8")
    short = hashlib.sha256(seed).hexdigest()[:8]
    return f"{ts}_{short}"


def write_checksums(release_dir: Path, files_dir: Path, rels: List[str]) -> None:
    lines = []
    for rel in sorted(rels):
        fp = files_dir / rel
        h = hashlib.sha256()
        with fp.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        lines.append(f"{h.hexdigest()}  files/{rel}")
    out = release_dir / "CHECKSUMS.sha256"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_release_manifest(
    release_dir: Path,
    book_id: str,
    release_id: str,
    book_manifest_path: Path,
    build_manifest_path: Optional[Path],
) -> None:
    resolved_build_manifest = None
    if build_manifest_path:
        resolved_build_manifest = build_manifest_path
        if not build_manifest_path.is_absolute():
            resolved_build_manifest = (RUNTIME_ROOT / build_manifest_path).resolve()
    manifest = {
        "book_id": book_id,
        "release_id": release_id,
        "created_at": utc_now(),
        "book_manifest_path": "runtime/manifests/book_manifest.json",
        "book_manifest_sha256": sha256_file(book_manifest_path) if book_manifest_path.exists() else None,
        "build_manifest_path": str(build_manifest_path) if build_manifest_path else None,
        "build_manifest_sha256": sha256_file(resolved_build_manifest) if resolved_build_manifest and resolved_build_manifest.exists() else None,
        "checksums_path": "CHECKSUMS.sha256",
        "exporter": f"book_export.py (python {sys.version.split()[0]})",
    }
    (release_dir / "release_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = (RUNTIME_ROOT / manifest_path).resolve()

    if not manifest_path.exists():
        print(f"Missing book_manifest.json: {manifest_path}", file=sys.stderr)
        return 1

    if args.create_release_id:
        book_id_for_id = args.book_id or "BOOK-DEFAULT"
        print(generate_release_id(book_id_for_id, manifest_path))
        return 0

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

        releases_base = out_base / book_id / "releases"
        release_id = args.release_id
        update_latest = False
        if release_id == "latest":
            update_latest = True
            nonce = str(datetime.now(timezone.utc).timestamp())
            release_id = generate_release_id(book_id, manifest_path, nonce=nonce)

        release_dir = releases_base / release_id
        temp_dir = releases_base / f"{release_id}.tmp"
        if update_latest:
            for _ in range(5):
                if not release_dir.exists() and not temp_dir.exists():
                    break
                nonce = f"{datetime.now(timezone.utc).timestamp()}-{release_dir.name}"
                release_id = generate_release_id(book_id, manifest_path, nonce=nonce)
                release_dir = releases_base / release_id
                temp_dir = releases_base / f"{release_id}.tmp"
        files_dir = temp_dir / "files"

        build_manifest_refs: List[str] = []
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
            if bm_ref not in build_manifest_refs:
                build_manifest_refs.append(bm_ref)

        if not build_manifest_paths:
            print(f"No build_manifest references found for book_id={book_id}")
            continue
        build_manifest_paths = sorted(build_manifest_paths, key=lambda p: p.as_posix())
        build_manifest_refs = sorted(build_manifest_refs)

        if release_dir.exists():
            print(f"Release already exists (immutable): {release_dir}", file=sys.stderr)
            return 4
        if temp_dir.exists():
            print(f"Temporary release dir already exists: {temp_dir}", file=sys.stderr)
            return 5

        if not args.dry_run:
            temp_dir.mkdir(parents=True, exist_ok=True)
            files_dir.mkdir(parents=True, exist_ok=True)

        copied_files = set()
        for idx, bm_path in enumerate(build_manifest_paths, start=1):
            dst_name = "build_manifest.json" if idx == 1 else f"build_manifest_{idx}.json"
            if not args.dry_run:
                shutil.copy2(bm_path, temp_dir / dst_name)

            data = load_json(bm_path)
            exports_block = data.get("exports", {}) if isinstance(data, dict) else {}
            file_list = exports_block.get("files", []) if isinstance(exports_block, dict) else []
            for rel in sorted(file_list):
                if not isinstance(rel, str) or not is_safe_rel_path(rel):
                    continue
                src = (RUNTIME_ROOT / rel).resolve()
                if not src.exists() or not src.is_file():
                    continue
                dst = files_dir / rel
                if not args.dry_run:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                copied_files.add(rel)

        copied_files_list = sorted(copied_files)

        readme_lines = [
            "Exporter: B9 skeleton",
            f"Generated at: {utc_now()}",
            f"Input book_manifest: {manifest_path}",
            f"Book id: {book_id}",
            f"Release id: {release_id}",
            "Notes: deterministic ordering + CHECKSUMS.sha256; no packaging.",
            f"Build manifests: {len(build_manifest_paths)}",
            f"Files copied: {len(copied_files_list)}",
        ]

        build_manifest_path = build_manifest_paths[0] if build_manifest_paths else None
        build_manifest_ref = build_manifest_refs[0] if build_manifest_refs else None
        if not args.dry_run:
            write_checksums(temp_dir, files_dir, copied_files_list)
            (temp_dir / "EXPORTER_README.txt").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")
            write_release_manifest(
                temp_dir,
                book_id=book_id,
                release_id=release_id,
                book_manifest_path=manifest_path,
                build_manifest_path=Path(build_manifest_ref) if build_manifest_ref else build_manifest_path,
            )
            try:
                temp_dir.rename(release_dir)
            except Exception:
                if temp_dir.exists():
                    shutil.rmtree(temp_dir, ignore_errors=True)
                raise

            if update_latest:
                latest_json = releases_base / "latest.json"
                latest_payload = {"release_id": release_id, "updated_at": utc_now()}
                latest_json.write_text(json.dumps(latest_payload, indent=2) + "\n", encoding="utf-8")
                latest_link = releases_base / "latest"
                try:
                    if latest_link.is_symlink():
                        latest_link.unlink()
                    if not latest_link.exists():
                        latest_link.symlink_to(release_dir.name)
                except Exception:
                    pass

        print(f"Export written to {release_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
