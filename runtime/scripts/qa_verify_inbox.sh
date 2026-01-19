#!/usr/bin/env bash
# Ensure runtime venv is active (avoid PATH python mismatches)
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [ -f "$ROOT/.venv/bin/activate" ]; then
  # shellcheck disable=SC1090
  source "$ROOT/.venv/bin/activate"
else
  echo "ERROR: missing runtime/.venv. Create it under runtime/.venv (Python 3.11) and install deps."
  exit 1
fi

set -euo pipefail

RUNTIME_ROOT="/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
API_URL="http://127.0.0.1:8010"

cd "${RUNTIME_ROOT}"

echo "== Inbox verification =="
python3 indexer.py >/dev/null

echo "[indices] inbox_index.json:"
cat indices/inbox_index.json

if curl -s "${API_URL}/health" >/dev/null 2>&1; then
  echo "[api] /inbox:"
  curl -s "${API_URL}/inbox"
else
  echo "[api] /inbox skipped (API not running)"
fi

if rg -n "\"proposal_P-002_closure\"" indices/inbox_index.json; then
  echo "FAIL: closure_needed still present for P-002"
  exit 1
fi

echo "PASS: no closure_needed item for P-002"
