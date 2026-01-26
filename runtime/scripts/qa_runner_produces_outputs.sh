#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# Resolve repo root from this script location so paths work no matter where you run from.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# qa script lives at <repo>/runtime/scripts/, so repo root is two levels up
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Canonical run index location is under runtime/indices/ in the same repo as this script.
RUN_INDEX_PATH="$REPO_ROOT/runtime/indices/run_index.json"
if [ ! -f "$RUN_INDEX_PATH" ]; then
  # Backward-compatible fallback (older layout)
  RUN_INDEX_PATH="$REPO_ROOT/indices/run_index.json"
fi
RUN_INDEX="$RUN_INDEX_PATH"

if [ ! -f "$RUN_INDEX" ]; then
  echo "SKIP: missing run_index.json"
  exit 0
fi

RUN_PATH="$(RUN_INDEX_PATH="$RUN_INDEX_PATH" python3 - <<'PY'
import json
from pathlib import Path
import os
p = Path(os.environ["RUN_INDEX_PATH"])
d = json.loads(p.read_text(encoding="utf-8"))
runs = d.get("runs", [])
if not runs:
    print("")
    raise SystemExit(0)
path = runs[0].get("path", "")
print(path)
PY
)"

if [ -z "$RUN_PATH" ]; then
  echo "SKIP: no runs"
  exit 0
fi

OUT_DIR="$RUN_PATH/outputs"
if [ ! -d "$OUT_DIR" ]; then
  echo "FAIL: missing outputs dir for $RUN_PATH"
  exit 1
fi

COUNT="$(find "$OUT_DIR" -type f | wc -l | tr -d ' ')"
if [ "$COUNT" -lt 1 ]; then
  echo "FAIL: outputs empty for $RUN_PATH"
  exit 1
fi

echo "PASS: outputs present for $RUN_PATH"
exit 0
