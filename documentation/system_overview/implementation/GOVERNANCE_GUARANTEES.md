# Governance Guarantees — MVP Implementation

## Core Principles

The MVP implementation enforces the following governance guarantees:

### 1. Immutability

**Runs**: Once created, run directories are never modified by the UI.
- Location: `runs/{run_id}/`
- UI behavior: Read-only viewing only
- Enforcement: No API endpoints for editing runs

**Closures**: Once created, closures cannot be modified.
- Location: `closures/{closure_id}/closure.json`
- Enforcement: API checks if `closure.json` exists before creating
- Error: `400 Bad Request` if closure already exists

**Validator Reports**: Immutable once written.
- Location: `runs/{run_id}/validator/report.json`
- UI behavior: Display only

### 2. Canonical Read-Only

**Policy**: UI never writes to `canonical/` directory.

**Enforcement**:
- Function `check_canonical_write()` in `api_server.py` (line 109-116)
- Currently not actively used (no promote endpoint in MVP)
- Will be enforced when Promote Wizard is implemented (Phase 2)

**UI behavior**: No edit controls for canonical content.

### 3. Required Fields Validation

**Closure Creation** (`POST /api/closures`):
- `decision_type`: Required (Pydantic Field)
- `rationale`: Required, minimum 10 characters (Pydantic Field with `min_length=10`)
- `sign_off`: Required, must be `true` (Pydantic validator)
- `proposal_id`: Required, must exist in filesystem

**Enforcement**:
- Pydantic model validation (`ClosureCreate` in `api_server.py` lines 38-52)
- API checks proposal exists (line 363)
- Frontend also validates before submission

### 4. Audit Trail

**All write operations** are logged to:
- `audit/api_actions.log` (append-only)

**Logged events**:
- Closure creation (with metadata: closure_id, proposal_id, decision_type)
- Reindex operations (with result summary)

**Format**: JSON lines (one JSON object per line)

**Example entry**:
```json
{"timestamp": "2026-01-09T12:00:00", "message": "Closure created: CL-20260109-abc12345", "metadata": {"closure_id": "CL-20260109-abc12345", "proposal_id": "P-20260109-001", "decision_type": "APPROVE"}}
```

### 5. Proposal Status Updates

**When closure is created**:
- `proposals/{proposal_id}/status.json` is updated
- Status set to `"closed"`
- `closed_at` timestamp added
- `closure_id` reference added

**Enforcement**: Automatic in `create_closure()` endpoint (lines 400-412)

### 6. No Silent Authority

**Principle**: Every write action produces an artefact.

**Implementation**:
- Closure creation → `closure.json` + `status.json` update + audit log
- No "hidden" state changes
- All state derived from filesystem artefacts

### 7. Deterministic UI State

**Principle**: UI state computed from filesystem, no hidden UI-only state.

**Implementation**:
- Inbox items derived from `indices/inbox_index.json`
- Run details read from `runs/{run_id}/` files
- Proposal details read from `proposals/{proposal_id}/` files
- No client-side state that affects governance outcomes

## Policy Enforcement Points

1. **API Layer** (`api_server.py`):
   - Closure immutability check (line 374)
   - Proposal existence check (line 363)
   - Field validation via Pydantic (lines 38-52)
   - Audit logging (line 415)

2. **Indexer** (`indexer.py`):
   - Reads filesystem structure
   - Generates indices (no writes to source data)
   - Idempotent (safe to run multiple times)

3. **Frontend** (`ui/src/components/`):
   - Form validation before submission
   - No direct filesystem access
   - All writes go through API

## Limitations (MVP)

- **No Promote Wizard**: Canonical writes not yet implemented
- **No CLI integration**: Validator endpoint is placeholder (line 430-461)
- **No user identity**: Uses `getpass.getuser()` for `created_by` field
- **No access control**: Assumes single-user local environment

## Future Enhancements (Phase 2)

- Promote Wizard with canonical write enforcement
- User authentication and authorization
- Multi-user support with proper access control
- Full CLI validator integration

## Code References

Main source files:

- **`indexer.py`**: Filesystem scanner
  - `build_inbox_index()`: Builds inbox items from runs/proposals/closures
  - `reindex()`: Generates all JSON indices (inbox_index, run_index, proposal_index, closure_index)

- **`api_server.py`**: FastAPI backend
  - `GET /inbox`, `GET /runs/{id}`, `GET /proposals/{id}`, `POST /closures`, `POST /reindex`: API endpoints
  - `create_closure()`: Closure creation with immutability check (line 358-427)
  - `check_canonical_write()`: Policy check for canonical directory (line 109-116)
  - `ensure_audit_log()`: Append-only audit logging (line 93-106)

- **`ui/src/api.ts`**: API client
  - `API_BASE = '/api'`: Base URL configuration
  - `api.getInbox()`, `api.createClosure()`, etc.: API method wrappers

- **`ui/src/components/ClosureComposer.tsx`**: Closure creation form with validation
- **`ui/src/components/Inbox.tsx`**: Filterable inbox table (read-only)
- **`ui/src/components/RunDetail.tsx`**: Run detail viewer (read-only)
