#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

API_PORT="${API_PORT:-8010}"

echo "== Mustika Rasa DEV DOWN =="

kill_port () {
  local port="$1"
  local pids
  pids="$(lsof -ti tcp:"$port" 2>/dev/null || true)"
  if [[ -n "$pids" ]]; then
    echo "Stopping processes on port $port: $pids"
    kill -9 $pids || true
  else
    echo "Port $port: nothing running"
  fi
}

kill_port "$API_PORT"
kill_port 5173
kill_port 5174

if [[ -f "$ROOT/audit/api_server.pid" ]]; then
  rm -f "$ROOT/audit/api_server.pid"
fi

if [[ -f "$ROOT/audit/ui_dev.pid" ]]; then
  rm -f "$ROOT/audit/ui_dev.pid"
fi

echo "DONE."
