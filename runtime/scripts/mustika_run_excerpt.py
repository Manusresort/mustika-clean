#!/usr/bin/env python3

# --- venv guard (mustika_run_excerpt) ---
import os
if not os.environ.get('VIRTUAL_ENV'):
    raise SystemExit(
        'ERROR: No active venv. Activate runtime/.venv first: '
        'cd runtime && source .venv/bin/activate'
    )

"""
CLI entrypoint for Runner V2 - Phase-6 Excerpt-Aware Runner

Usage:
    python3 scripts/mustika_run_excerpt.py \
        --excerpt-id sayur_052_066 \
        --excerpt-source data/origineel/hoofdstuk1.txt \
        --excerpt-version v1 \
        --english data/origineel/hoofdstuk1.txt \
        --rough-nl data/hoofdstuk1_rough_nl_dummy.txt \
        [--run-id RUN_SAYUR_001]
"""

import argparse
import sys
from pathlib import Path

# Add src to path
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR / "src"))

from runner_v2.runner import RunnerV2


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase-6 Excerpt-Aware Runner V2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    # Required excerpt metadata
    parser.add_argument(
        "--excerpt-id",
        required=True,
        help="Excerpt identifier (e.g., sayur_052_066)"
    )
    parser.add_argument(
        "--excerpt-source",
        required=True,
        help="Excerpt source file path"
    )
    parser.add_argument(
        "--excerpt-version",
        required=True,
        help="Excerpt version (e.g., v1)"
    )
    
    # Optional run ID
    parser.add_argument(
        "--run-id",
        required=False,
        help="Run ID (auto-generated if not provided)"
    )
    
    # Input files
    parser.add_argument(
        "--english",
        required=True,
        help="Path to English source text file"
    )
    parser.add_argument(
        "--rough-nl",
        required=True,
        help="Path to rough Dutch translation file"
    )
    
    args = parser.parse_args()
    
    # Validate input files exist
    english_path = Path(args.english)
    rough_nl_path = Path(args.rough_nl)
    
    if not english_path.exists():
        print(f"Error: English file not found: {english_path}", file=sys.stderr)
        return 1
    
    if not rough_nl_path.exists():
        print(f"Error: Rough NL file not found: {rough_nl_path}", file=sys.stderr)
        return 1
    
    # Read input files
    try:
        english_text = english_path.read_text(encoding="utf-8")
        rough_nl_text = rough_nl_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading input files: {e}", file=sys.stderr)
        return 1
    
    # Create runner and execute
    runner = RunnerV2(BASE_DIR)
    
    success, run_dir, error_msg = runner.run(
        excerpt_id=args.excerpt_id,
        excerpt_source=args.excerpt_source,
        excerpt_version=args.excerpt_version,
        english_text=english_text,
        rough_nl_text=rough_nl_text,
        run_id=args.run_id,
    )
    
    if success:
        print(f"Run completed successfully: {run_dir}")
        return 0
    else:
        print(f"Run failed: {error_msg}", file=sys.stderr)
        if run_dir:
            print(f"Run directory: {run_dir}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
