#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "== Mustika Rasa DEV UP =="
echo "Project: $ROOT"
echo

API_PORT="${API_PORT:-8010}"

# 1) Kill anything on ports we use (API + UI)
kill_port () {
  local port="$1"
  local pids
  pids="$(lsof -ti tcp:"$port" 2>/dev/null || true)"
  if [[ -n "$pids" ]]; then
    echo "Stopping processes on port $port: $pids"
    kill -9 $pids || true
  fi
}

kill_port "$API_PORT"
kill_port 5173
kill_port 5174

# 2) Start backend
echo
"$ROOT/scripts/dev_start_api.sh"

# 3) Reindex once (best effort)
echo "Running indexer once..."
"$ROOT/scripts/reindex_runtime.sh" >/dev/null 2>&1 || true

# 4) Start UI
echo
"$ROOT/scripts/dev_start_ui.sh"

echo
echo "DONE."
echo "Check health:  curl -s http://localhost:${API_PORT}/health"
echo "Open UI:      http://localhost:5173  (or 5174 if taken)"
echo "Logs:         audit/api_server.log and audit/ui_dev.log"
