#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
API_HOST="${API_HOST:-127.0.0.1}"
API_PORT="${API_PORT:-8010}"

if [[ -f "$ROOT/.venv/bin/activate" ]]; then
  # shellcheck disable=SC1090
  source "$ROOT/.venv/bin/activate"
else
  echo "ERROR: .venv not found at $ROOT/.venv"
  exit 1
fi

export PYTHONPATH="$ROOT/src"

mkdir -p "$ROOT/audit"

if command -v lsof >/dev/null 2>&1; then
  pids="$(lsof -ti tcp:"$API_PORT" 2>/dev/null || true)"
  if [[ -n "${pids:-}" ]]; then
    echo "Stopping processes on port $API_PORT: $pids"
    kill -9 $pids || true
  fi
fi

echo "Starting API on http://${API_HOST}:${API_PORT} ..."
nohup python -m uvicorn api_server:app --host "$API_HOST" --port "$API_PORT" > "$ROOT/audit/api_server.log" 2>&1 &
echo $! > "$ROOT/audit/api_server.pid"
echo "API PID: $(cat "$ROOT/audit/api_server.pid")"

if command -v curl >/dev/null 2>&1; then
  health="$(curl -s -o /dev/null -w "%{http_code}" "http://${API_HOST}:${API_PORT}/health" || true)"
  echo "Health check: http://${API_HOST}:${API_PORT}/health => ${health}"
fi
