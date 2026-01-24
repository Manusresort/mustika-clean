#!/usr/bin/env python3
"""
B8 — Build manifest contract validation.

Validates that:
- Every book_manifest export references an existing build_manifest.json
- Export files + sha256 match exactly
- tool_versions are present in build manifests
"""
from pathlib import Path
import json
import sys

BASE = Path(__file__).resolve().parents[1]
BOOK_MANIFEST = BASE / "manifests" / "book_manifest.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_files_list(files):
    return [f for f in files if isinstance(f, str) and f]


def main() -> int:
    if not BOOK_MANIFEST.exists():
        print("Missing book_manifest.json", file=sys.stderr)
        return 1

    bm = load(BOOK_MANIFEST)
    books = bm.get("books")
    entries = books if isinstance(books, list) else [bm]

    for entry in entries:
        exports = entry.get("exports", []) if isinstance(entry, dict) else []
        if not isinstance(exports, list):
            print("Invalid exports in book_manifest.json", file=sys.stderr)
            return 2

        for exp in exports:
            if not isinstance(exp, dict):
                print("Export entry is not a dict", file=sys.stderr)
                return 3
            ref = exp.get("build_manifest")
            if not isinstance(ref, str) or not ref:
                print(f"Export missing build_manifest ref: {exp}", file=sys.stderr)
                return 4

            ref_path = (BASE / ref).resolve()
            if not ref_path.exists():
                print(f"Referenced build_manifest not found: {ref}", file=sys.stderr)
                return 5

            bld = load(ref_path)
            tool_versions = bld.get("tool_versions")
            if not isinstance(tool_versions, dict) or not tool_versions:
                print(f"tool_versions missing in {ref}", file=sys.stderr)
                return 6

            bld_exports = bld.get("exports", {}) if isinstance(bld, dict) else {}
            bld_files = normalize_files_list(bld_exports.get("files", [])) if isinstance(bld_exports, dict) else []
            bld_sha = bld.get("sha256", {}) if isinstance(bld.get("sha256"), dict) else {}

            exp_files = normalize_files_list(exp.get("files", []))
            exp_sha = exp.get("sha256", {}) if isinstance(exp.get("sha256"), dict) else {}

            if sorted(bld_files) != sorted(exp_files):
                print(f"File list mismatch between book_manifest and {ref}", file=sys.stderr)
                return 7
            if bld_sha != exp_sha:
                print(f"Checksum mismatch between book_manifest and {ref}", file=sys.stderr)
                return 8

    print("Build manifest validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
