# DEV_WORKFLOW — Mustika Rasa (Mac)

## TL;DR

- `cd /path/to/repo`
- `cd runtime && ./scripts/dev_up.sh`
- open `http://localhost:5173` (or `http://localhost:5174` if 5173 is busy)
- Environment (authoritative): `documentation/system_overview/ENVIRONMENT.md`
- Install steps (Python + UI deps) are in ENVIRONMENT.md; this doc only summarizes commands.

---

## Vereisten

- macOS
- Python 3.11 + `runtime/.venv` (required for CrewAI)
- Node.js + npm
- (optioneel) Ollama lokaal voor LLM-tests

---

## Start

- `cd runtime && ./scripts/dev_up.sh`

Dit start:
- backend (`uvicorn api_server:app` op `127.0.0.1:8010`)
- reindex (`indexer.py` → `indices/*`)
- UI (Vite, meestal `http://localhost:5173`, anders `5174`)

---

## QA (full system)

- `cd runtime && ./scripts/qa_full_system.sh`

Dit draait end-to-end smoke checks (API/indexer/UI).
DEV_WORKFLOW.md is the authoritative source for day-to-day QA commands; other docs should defer to this section for QA procedures.

---

## Stop

- `cd runtime && ./scripts/dev_down.sh`

Dit stopt de processen op poorten:
- `8010` (API)
- `5173` of `5174` (UI)

---

## Debug (snel)

- Health: `curl http://127.0.0.1:8010/health`
- Inbox: `curl http://127.0.0.1:8010/inbox`

Logs:
- `runtime/audit/api_server.log`
- `runtime/audit/ui_dev.log`

---

Voor uitgebreide troubleshooting: `documentation/system_overview/RUNBOOK_TROUBLESHOOTING.md`

---

## Ports

- UI draait op `5173`, of `5174` als `5173` bezet is.
- API draait op `127.0.0.1:8010`.

---

## Veelvoorkomende problemen

- **/health 404** → je draait de verkeerde server → `cd runtime && ./scripts/dev_down.sh` + `cd runtime && ./scripts/dev_up.sh`
- **/inbox 500** → run `cd runtime && ./scripts/dev_up.sh` (reindex) + check `runtime/audit/api_server.log`
