# RUNBOOK_TROUBLESHOOTING — Mustika Rasa (facts-only)

## Ports / listeners

- API: `8010`
- UI: `5173` (fallback `5174`)
- Check listeners:
  - `lsof -nP -iTCP:8010 -sTCP:LISTEN`
  - `lsof -nP -iTCP:5173 -sTCP:LISTEN`
  - `lsof -nP -iTCP:5174 -sTCP:LISTEN`

## Venv / Python

- Python 3.11 + `runtime/.venv` is required for runtime scripts (see `documentation/system_overview/ENVIRONMENT.md`).
- Activate: `cd runtime && source .venv/bin/activate`.

## CrewAI dependency

- `crewai==0.11.2` is part of runtime deps (see `runtime/requirements-ui.txt`).

## Stub-mode wanneer CrewAI ontbreekt

Observable (agents missing): `runtime/test_multi_agent_fidelity.py` prints: mustikarasa_agents missing; running stub mode.

Behavior (CrewAI/agents missing): `runtime/src/pipeline_fidelity.py` skips agent processing and returns stub output using the provided rough NL, with remarks starting with STUB: (e.g. STUB: crewai not installed; returned rough_nl without agent processing.).

Fix: `cd runtime && source .venv/bin/activate && pip install -r requirements-ui.txt`

## Env vars (LLM)

- LLM/keys/model env vars staan in `documentation/system_overview/ENVIRONMENT.md` (OPENAI_API_KEY, OPENAI_MODEL/LITELLM_MODEL, optional base URL).

## API checks

- Health: `curl http://127.0.0.1:8010/health`
- Inbox: `curl http://127.0.0.1:8010/inbox`
- API log: `runtime/audit/api_server.log`

## UI checks

- UI: `http://localhost:5173` (or `http://localhost:5174`)
- UI log: `runtime/audit/ui_dev.log`

## Reindex

- `cd runtime && ./scripts/reindex_runtime.sh`
