#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$ROOT/audit"

UI_HOST="${UI_HOST:-0.0.0.0}"
UI_PORT="${UI_PORT:-5173}"

echo "Starting UI (Vite) on host=$UI_HOST port=$UI_PORT ..."
cd "$ROOT/ui"
nohup npm run dev -- --host "$UI_HOST" --port "$UI_PORT" > "$ROOT/audit/ui_dev.log" 2>&1 &
echo $! > "$ROOT/audit/ui_dev.pid"
echo "UI PID: $(cat "$ROOT/audit/ui_dev.pid")"
echo "Try: http://localhost:$UI_PORT  (and http://127.0.0.1:$UI_PORT)"
