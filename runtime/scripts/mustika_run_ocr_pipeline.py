#!/usr/bin/env python3
"""
OCR-first runner for run bundles.

Reads run inputs from runtime/runs/<excerpt_id>/<run_id>/inputs and produces
English + Rough-NL stub artifacts under outputs/.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def locate_run_dirs(runs_root: Path, run_id: str) -> List[Path]:
    matches: List[Path] = []
    direct = runs_root / run_id
    if direct.exists() and direct.is_dir():
        matches.append(direct)
    if runs_root.exists():
        for excerpt_dir in runs_root.iterdir():
            if not excerpt_dir.is_dir():
                continue
            nested = excerpt_dir / run_id
            if nested.exists() and nested.is_dir():
                matches.append(nested)
    return matches


def build_english_text(pages: List[Dict[str, str]]) -> str:
    chunks = []
    for page in pages:
        page_id = page.get("page_id", "")
        txt_path = Path(page.get("txt", ""))
        if txt_path.exists():
            raw = txt_path.read_text(encoding="utf-8", errors="replace")
        else:
            raw = ""
        chunks.append(f"[PAGE {page_id}]\n{raw}\n")
    return "\n".join(chunks).strip() + "\n"


def build_rough_nl_text(english_text: str) -> str:
    return (
        "[ROUGH_NL_STUB]\n"
        "This is a placeholder Rough-NL output derived from English.\n\n"
        + english_text
    )


def process_run_dir(run_dir: Path) -> None:
    inputs_dir = run_dir / "inputs"
    if not inputs_dir.exists():
        raise FileNotFoundError(f"missing inputs/ in {run_dir}")

    run_cfg = read_json(inputs_dir / "run_config.json")
    pages_manifest = read_json(inputs_dir / "pages_manifest.json")
    excerpt_id = run_cfg.get("excerpt_id") or run_cfg.get("recipe_block_id")
    if not excerpt_id:
        excerpt_id = run_dir.parent.name

    pages = pages_manifest if isinstance(pages_manifest, list) else []
    english_text = build_english_text(pages)
    rough_nl_text = build_rough_nl_text(english_text)

    outputs_dir = run_dir / "outputs"
    english_dir = outputs_dir / "english"
    rough_dir = outputs_dir / "rough_nl"
    english_path = english_dir / "english.json"
    rough_path = rough_dir / "rough_nl.json"

    write_json(
        english_path,
        {
            "language": "english",
            "created_at": utc_now_iso(),
            "excerpt_id": excerpt_id,
            "run_id": run_cfg.get("run_id") or run_dir.name,
            "source_pages": [p.get("page_id") for p in pages],
            "text": english_text,
            "note": "ocr_first_stub",
        },
    )
    write_json(
        rough_path,
        {
            "language": "rough_nl",
            "created_at": utc_now_iso(),
            "excerpt_id": excerpt_id,
            "run_id": run_cfg.get("run_id") or run_dir.name,
            "source_pages": [p.get("page_id") for p in pages],
            "text": rough_nl_text,
            "note": "ocr_first_stub",
        },
    )

    manifest = {
        "run_id": run_cfg.get("run_id") or run_dir.name,
        "excerpt_id": excerpt_id,
        "produced_languages": ["english", "rough_nl"],
        "artifacts": {
            "english": [str(english_path.relative_to(run_dir))],
            "rough_nl": [str(rough_path.relative_to(run_dir))],
        },
        "created_at": utc_now_iso(),
    }
    write_json(outputs_dir / "manifest.json", manifest)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True, help="Run ID to process")
    ap.add_argument("--runs-root", default="runs", help="Runs root (default: runtime/runs)")
    args = ap.parse_args()

    runs_root = Path(args.runs_root).resolve()
    run_dirs = locate_run_dirs(runs_root, args.run_id)
    if not run_dirs:
        print(f"ERROR: run_id not found under {runs_root}: {args.run_id}")
        return 1

    for run_dir in run_dirs:
        process_run_dir(run_dir)
        print(f"OK: outputs written for {run_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
