#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ -f "$ROOT/.venv/bin/activate" ]]; then
  # shellcheck disable=SC1090
  source "$ROOT/.venv/bin/activate"
else
  echo "ERROR: .venv not found at $ROOT/.venv"
  exit 1
fi

export PYTHONPATH="$ROOT/src"

python "$ROOT/indexer.py" --base-path "$ROOT"
