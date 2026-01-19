# API Contract — Mustika Rasa Human UI

## Base URL

- Development: `http://127.0.0.1:8010`
- Frontend proxy: `/api` (proxied to `http://127.0.0.1:8010`)

## Endpoints

### GET /

**Description**: Root endpoint, service info.

**Response**:
```json
{
  "service": "Mustika Rasa Human UI API",
  "version": "1.0.0",
  "base_path": "/absolute/path/to/repo"
}
```

---

### POST /reindex

**Description**: Trigger filesystem reindex.

**Request**: None (empty body)

**Response**:
```json
{
  "status": "success",
  "result": {
    "runs": 5,
    "proposals": 3,
    "closures": 2,
    "inbox_items": 8
  }
}
```

**Errors**:
- `500 Internal Server Error`: Reindex failed (details in response)

---

### GET /inbox

**Description**: Get inbox items from index.

**Response**:
```json
{
  "generated_at": "2026-01-09T12:00:00",
  "counts": {
    "review_required": 2,
    "gate_triggered": 1,
    "closure_needed": 1,
    "incidents": 0,
    "total": 4
  },
  "items": [
    {
      "id": "P-20260109-001",
      "type": "review",
      "title": "Proposal title",
      "severity": "info",
      "status": "open",
      "age": "2026-01-09T10:00:00",
      "required_action": "Review proposal",
      "proposal_id": "P-20260109-001"
    }
  ]
}
```

**Item types**: `review`, `gate`, `closure`, `incident`

**Severity levels**: `critical`, `warning`, `info`

**Auto-indexing**: If `indices/inbox_index.json` doesn't exist, triggers reindex automatically.

**Errors**:
- `500 Internal Server Error`: Failed to read index

---

### GET /runs/{run_id}

**Description**: Get run details.

**Path parameters**:
- `run_id` (string): Run identifier (directory name in `runs/`)

**Response**:
```json
{
  "run_id": "RUN_20260109_001",
  "manifest": {
    "input_files": ["..."],
    "config": {...}
  },
  "validator_report": {
    "overall_status": "PASS",
    "checks": [...]
  },
  "gates": [
    {
      "type": "output_contract",
      "blocking": true,
      "reason": "..."
    }
  ],
  "signals": [
    {
      "type": "fidelity_warning",
      "severity": "warning",
      "message": "..."
    }
  ],
  "output_files": [
    {
      "name": "output.txt",
      "path": "runs/RUN_20260109_001/outputs/output.txt",
      "size": 1234
    }
  ],
  "log_files": [
    {
      "name": "run.log",
      "path": "runs/RUN_20260109_001/logs/run.log",
      "size": 5678
    }
  ]
}
```

**Optional fields**: `manifest`, `validator_report`, `gates`, `signals` may be `null` or empty arrays if files don't exist.

**Errors**:
- `404 Not Found`: Run directory doesn't exist

---

### GET /proposals/{proposal_id}

**Description**: Get proposal details.

**Path parameters**:
- `proposal_id` (string): Proposal identifier (directory name in `proposals/`)

**Response**:
```json
{
  "proposal_id": "P-20260109-001",
  "content": "# Proposal Title\n\nContent...",
  "status": {
    "status": "open",
    "severity": "info"
  },
  "gates": [
    {
      "type": "required_closure",
      "blocking": true
    }
  ],
  "required_closure": true,
  "review_pack_files": [
    {
      "name": "diff.md",
      "path": "proposals/P-20260109-001/review_pack/diff.md"
    }
  ],
  "linked_runs": ["RUN_20260109_001"]
}
```

**Optional fields**: `content` may be empty string, `gates`, `required_closure`, `review_pack_files`, `linked_runs` may be empty arrays/null.

**Compatibility note**: as-built, `required_closure` is boolean presence-based.
File contents of `required_closure.json` are not parsed by API/indexer.

**Errors**:
- `404 Not Found`: Proposal directory doesn't exist

---

### GET /closures/{closure_id}

**Description**: Get closure details.

**Path parameters**:
- `closure_id` (string): Closure identifier (directory name in `closures/`)

**Response** (JSON format):
```json
{
  "closure_id": "CL-20260109-abc12345",
  "created_at": "2026-01-09T12:00:00",
  "created_by": "username",
  "proposal_id": "P-20260109-001",
  "source_run_id": "RUN_20260109_001",
  "decision_type": "APPROVE",
  "rationale": "Rationale text...",
  "evidence_paths": ["runs/RUN_20260109_001/outputs/file.txt"],
  "sign_off": true
}
```

**Response** (Markdown format, if JSON doesn't exist):
```json
{
  "closure_id": "CL-20260109-abc12345",
  "format": "markdown",
  "content": "# Closure\n\nMarkdown content..."
}
```

**Errors**:
- `404 Not Found`: Closure directory or file doesn't exist

---

### POST /closures

**Description**: Create a new closure.

**Request body**:
```json
{
  "proposal_id": "P-20260109-001",
  "run_id": "RUN_20260109_001",
  "decision_type": "APPROVE",
  "rationale": "This is my rationale (min 10 chars)",
  "evidence_paths": ["runs/RUN_20260109_001/outputs/file.txt"],
  "sign_off": true,
  "created_by": "username"
}
```

**Field requirements**:
- `proposal_id`: Required, must exist in `proposals/`
- `run_id`: Optional
- `decision_type`: Required (string)
- `rationale`: Required, minimum 10 characters
- `evidence_paths`: Optional array of strings
- `sign_off`: Required, must be `true`
- `created_by`: Optional (defaults to `getpass.getuser()`)

**Response** (201 Created):
```json
{
  "closure_id": "CL-20260109-abc12345",
  "created_at": "2026-01-09T12:00:00",
  "created_by": "username",
  "proposal_id": "P-20260109-001",
  "source_run_id": "RUN_20260109_001",
  "decision_type": "APPROVE",
  "rationale": "This is my rationale (min 10 chars)",
  "evidence_paths": ["runs/RUN_20260109_001/outputs/file.txt"]
}
```

**Side effects**:
- Creates `closures/{closure_id}/closure.json`
- Updates `proposals/{proposal_id}/status.json` (sets status to "closed")
- Appends to `audit/api_actions.log`
- Triggers reindex

**Errors**:
- `400 Bad Request`: Closure already exists (immutability)
- `404 Not Found`: Proposal doesn't exist
- `422 Unprocessable Entity`: Validation error (missing/invalid fields)

---

### POST /cli/validate

**Description**: Run validator on a run (CLI wrapper).

**Query parameters**:
- `run_id` (string): Run identifier

**Response** (if implemented):
```json
{
  "status": "success",
  "output": "Validator output..."
}
```

**Response** (placeholder):
```json
{
  "status": "not_implemented",
  "message": "CLI validator not yet integrated"
}
```

**Errors**:
- `404 Not Found`: Run doesn't exist
- `500 Internal Server Error`: Validator failed

**Note**: This endpoint is a placeholder in MVP. Actual CLI integration depends on CLI structure.

---

## Error Responses

All errors follow this format:

```json
{
  "detail": "Error message"
}
```

**Status codes**:
- `400 Bad Request`: Invalid request (e.g., closure already exists)
- `404 Not Found`: Resource doesn't exist
- `422 Unprocessable Entity`: Validation error
- `500 Internal Server Error`: Server error

## CORS

CORS is enabled for:
- `http://localhost:5173` (Vite dev server)
- `http://localhost:3000` (alternative port)
- `http://127.0.0.1:5173` (IP variant)

All methods and headers are allowed for local development.

## Code References

Main source files:

- **`api_server.py`**: FastAPI backend
  - `GET /`, `POST /reindex`, `GET /inbox`, `GET /runs/{id}`, `GET /proposals/{id}`, `GET /closures/{id}`, `POST /closures`, `POST /cli/validate`: All API endpoints
  - `ClosureCreate`, `ClosureResponse`, `InboxResponse`: Pydantic models for request/response validation
  - `create_closure()`: Closure creation endpoint (line 358-427)
  - `get_inbox()`: Inbox endpoint with auto-indexing (line 142-156)

- **`ui/src/api.ts`**: API client
  - `API_BASE = '/api'`: Base URL configuration
  - `api.getInbox()`, `api.getRun()`, `api.getProposal()`, `api.createClosure()`, `api.reindex()`: API method wrappers

- **`ui/src/components/Dashboard.tsx`**: Uses `api.getInbox()` and `api.reindex()`
- **`ui/src/components/Inbox.tsx`**: Uses `api.getInbox()`
- **`ui/src/components/ClosureComposer.tsx`**: Uses `api.createClosure()`
- **`ui/src/components/RunDetail.tsx`**: Uses `api.getRun()`
- **`ui/src/components/ReviewPackViewer.tsx`**: Uses `api.getProposal()`
