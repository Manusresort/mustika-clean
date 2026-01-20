# RUNBOOK_TROUBLESHOOTING — Mustika Rasa (facts-only)

## Ports / listeners

- API: `8010`
- UI: `5173` (fallback `5174`)
- Check listeners:
  - `lsof -nP -iTCP:8010 -sTCP:LISTEN`
  - `lsof -nP -iTCP:5173 -sTCP:LISTEN`
  - `lsof -nP -iTCP:5174 -sTCP:LISTEN`

## Venv / Python

- Python 3.11 + `runtime/.venv` (see `documentation/system_overview/ENVIRONMENT.md`).
- Activate: `cd runtime && source .venv/bin/activate`.

## API checks

- Health: `curl http://127.0.0.1:8010/health`
- Inbox: `curl http://127.0.0.1:8010/inbox`
- API log: `runtime/audit/api_server.log`

## UI checks

- UI: `http://localhost:5173` (or `http://localhost:5174`)
- UI log: `runtime/audit/ui_dev.log`

## Reindex

- `cd runtime && ./scripts/reindex_runtime.sh`
