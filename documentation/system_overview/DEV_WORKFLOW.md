# DEV_WORKFLOW — Mustika Rasa (Mac)

## TL;DR

- `cd /path/to/repo`
- `./scripts/dev_up.sh`
- open `http://localhost:5173` (or `http://localhost:5174` if 5173 is busy)

---

## Vereisten

- macOS
- Python 3 + `.venv` aanwezig
- Node.js + npm
- (optioneel) Ollama lokaal voor LLM-tests

---

## Start

- `./scripts/dev_up.sh`

Dit start:
- backend (`uvicorn api_server:app` op `127.0.0.1:8000`)
- reindex (`indexer.py` → `indices/*`)
- UI (Vite, meestal `http://localhost:5173`, anders `5174`)

---

## Stop

- `./scripts/dev_down.sh`

Dit stopt de processen op poorten:
- `8000` (API)
- `5173` of `5174` (UI)

---

## Debug (snel)

- Health: `curl http://127.0.0.1:8000/health`
- Inbox: `curl http://127.0.0.1:8000/inbox`

Logs:
- `audit/api_server.log`
- `audit/ui_dev.log`

---

## Ports

- UI draait op `5173`, of `5174` als `5173` bezet is.
- API draait op `127.0.0.1:8000`.

---

## Veelvoorkomende problemen

- **/health 404** → je draait de verkeerde server → `./scripts/dev_down.sh` + `./scripts/dev_up.sh`
- **/inbox 500** → run `./scripts/dev_up.sh` (reindex) + check `audit/api_server.log`
