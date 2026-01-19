# Mustika Rasa Human UI - Setup & Usage

## Overview

De Human UI is een local-first interface voor het beheren van de Mustika Rasa governance workflow. Het biedt een MVP met:
- Dashboard met inbox counters
- Inbox met filtering en severity sorting
- Review Pack Viewer voor proposals
- Closure Composer voor het maken van closures
- Run Detail viewer

## Setup

## Local Dev (Mac)

Zie `docs/DEV_WORKFLOW.md` voor de volledige dev-flow.

TL;DR:
```bash
cd /path/to/repo
source .venv/bin/activate   # optional if scripts handle venv
./scripts/dev_up.sh
```
Open `http://localhost:5173` (of `http://localhost:5174` als 5173 bezet is).

Docs:
- `docs/SYSTEM_OVERVIEW.md`
- `docs/DEV_WORKFLOW.md`
- `docs/QA/SMOKE_RUNBOOK.md`
- `docs/GOVERNANCE.md`

### Backend (FastAPI)

1. Installeer dependencies:
```bash
pip install -r requirements-ui.txt
```

2. Start de API server:
```bash
python api_server.py
```

Of met uvicorn:
```bash
uvicorn api_server:app --reload --host 127.0.0.1 --port 8000
```

De API draait op http://127.0.0.1:8000

### Frontend (React + Vite)

1. Ga naar de ui directory:
```bash
cd ui
```

2. Installeer dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

De UI is beschikbaar op http://localhost:5173

## Eerste gebruik

1. Zorg dat de directory structuur bestaat:
   - `runs/`
   - `proposals/`
   - `closures/`
   - `promotion/`
   - `canonical/`
   - `indices/`
   - `audit/`

2. Genereer indices:
   - Via de UI: klik op "Reindex" in het Dashboard
   - Via CLI: `python indexer.py`

3. Start beide servers (backend en frontend)

## API Endpoints

- `GET /inbox` - Haal inbox items op
- `GET /runs/{run_id}` - Haal run details op
- `GET /proposals/{proposal_id}` - Haal proposal details op
- `GET /closures/{closure_id}` - Haal closure details op
- `POST /closures` - Maak nieuwe closure
- `POST /reindex` - Trigger filesystem reindex

## MVP Features

✅ Inbox browsing met filters
✅ Review Pack Viewer
✅ Closure Composer
✅ Run Detail viewer
✅ Dashboard met counters

❌ Promote Wizard (Phase 2)
❌ Canonical Viewer (Phase 2)
❌ Observability dashboards (Phase 2)

## Governance Rules

- Canonical is read-only in de UI
- Closures zijn immutable na creatie
- Alle writes vereisen sign-off en rationale
- Policy checks worden uitgevoerd in de API
