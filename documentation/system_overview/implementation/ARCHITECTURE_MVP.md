# Architecture — MVP Implementation

## Overview

The Mustika Rasa Human UI MVP is a local-first, filesystem-based system with a FastAPI backend and React frontend. It provides governance workflows for reviewing proposals and creating closures.

## System Architecture

```
┌─────────────┐
│   Browser   │ (http://localhost:5173)
│  (React UI) │
└──────┬──────┘
       │ HTTP (via Vite proxy)
       ▼
┌─────────────┐
│  FastAPI    │ (http://127.0.0.1:8010)
│   Backend   │
└──────┬──────┘
       │
       ├──► Reads/Writes Filesystem
       │    ├── runs/
       │    ├── proposals/
       │    ├── closures/
       │    ├── indices/
       │    └── audit/
       │
       └──► Calls Indexer
            └── indexer.py
```

## Components

### Backend (`api_server.py`)

- **FastAPI application** running on `127.0.0.1:8010`
- **CORS enabled** for `localhost:5173` and `localhost:3000`
- **Indexer integration** via `indexer.py` module
- **Policy enforcement**:
  - Blocks writes to `canonical/`
  - Enforces closure immutability
  - Validates required fields (decision_type, rationale, sign_off)

### Indexer (`indexer.py`)

- **Filesystem scanner** that reads:
  - `runs/` directories
  - `proposals/` directories
  - `closures/` directories
- **Generates JSON indices**:
  - `indices/inbox_index.json`
  - `indices/run_index.json`
  - `indices/proposal_index.json`
  - `indices/closure_index.json`
- **Idempotent**: Safe to run multiple times

### Frontend (`ui/`)

- **React 18** with TypeScript
- **Vite** build tool
- **React Router** for navigation
- **API client** (`src/api.ts`) that calls `/api/*` endpoints
- **Components**:
  - `Dashboard.tsx` - Inbox counters and recent activity
  - `Inbox.tsx` - Filterable table of items
  - `ReviewPackViewer.tsx` - Proposal review interface
  - `ClosureComposer.tsx` - Form to create closures
  - `RunDetail.tsx` - View run details

## Data Flow

### Reading Data

1. Frontend calls API endpoint (e.g., `GET /api/inbox`)
2. API reads from `indices/inbox_index.json` (or triggers reindex if missing)
3. API returns JSON response
4. Frontend renders data

### Writing Data (Closures)

1. User fills form in `ClosureComposer`
2. Frontend calls `POST /api/closures` with closure data
3. API validates:
   - Proposal exists
   - Closure doesn't already exist (immutability)
   - Required fields present
4. API writes:
   - `closures/{closure_id}/closure.json`
   - Updates `proposals/{proposal_id}/status.json`
   - Appends to `audit/api_actions.log`
5. API triggers reindex
6. API returns created closure

## Storage Structure

See `ARTEFACTS_AND_STORAGE.md` for detailed file structure.

## Security Model

- **Local-only**: No network exposure beyond localhost
- **No authentication**: Assumes single-user local environment
- **Filesystem permissions**: Relies on OS-level file permissions
- **Policy checks**: Enforced in API layer, not frontend

## Limitations (MVP)

- No Promote Wizard (Phase 2)
- No Canonical Viewer (Phase 2)
- No Observability dashboards (Phase 2)
- No user authentication
- No multi-user support
- CLI validator integration is placeholder

## Code References

Main source files:

- **`indexer.py`**: Filesystem scanner
  - `build_inbox_index()`: Builds inbox items from runs/proposals/closures
  - `reindex()`: Generates all JSON indices (inbox_index, run_index, proposal_index, closure_index)

- **`api_server.py`**: FastAPI backend
  - `GET /inbox`, `GET /runs/{id}`, `GET /proposals/{id}`, `POST /closures`, `POST /reindex`: API endpoints
  - `create_closure()`: Closure creation with immutability check
  - `check_canonical_write()`: Policy check for canonical directory (Phase 2)

- **`ui/src/api.ts`**: API client
  - `API_BASE = '/api'`: Base URL configuration
  - `api.getInbox()`, `api.createClosure()`, etc.: API method wrappers

- **`ui/src/App.tsx`**: Main router with routes for Dashboard, Inbox, Review, Closure, Run Detail
- **`ui/src/components/Dashboard.tsx`**: Dashboard with inbox counters
- **`ui/src/components/Inbox.tsx`**: Filterable inbox table
- **`ui/src/components/ClosureComposer.tsx`**: Closure creation form
