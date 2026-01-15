# Known Issues and TODO — MVP Implementation

## Known Issues

### 1. CLI Validator Integration Not Implemented

**Location**: `api_server.py` line 430-461

**Issue**: `POST /cli/validate` endpoint is a placeholder. It attempts to call `mustikarasa_codex_cli.py validate --run {run_id}`, but this CLI command may not exist.

**Workaround**: Run validator manually via CLI if needed.

**Status**: Placeholder for Phase 2.

---

### 2. No User Authentication

**Location**: `api_server.py` line 88-90

**Issue**: Uses `getpass.getuser()` for `created_by` field. No authentication or user identity management.

**Impact**: Single-user local environment only. No multi-user support.

**Status**: Acceptable for MVP, enhancement for Phase 2.

---

### 3. No Promote Wizard

**Location**: Not implemented (Phase 2 feature)

**Issue**: No UI or API endpoint for promoting proposals to canonical.

**Workaround**: Use CLI directly (if implemented) or manual filesystem operations.

**Status**: Planned for Phase 2.

---

### 4. No Canonical Viewer

**Location**: Not implemented (Phase 2 feature)

**Issue**: No UI for viewing canonical content.

**Status**: Planned for Phase 2.

---

### 5. No Observability Dashboards

**Location**: Not implemented (Phase 2 feature)

**Issue**: No dashboards for signal trends, gate frequency, run health.

**Status**: Planned for Phase 2.

---

### 6. Indexer Doesn't Handle Corrupted JSON Gracefully

**Location**: `indexer.py` throughout

**Issue**: If JSON files are corrupted, indexer catches exceptions but doesn't log which files failed.

**Impact**: Silent failures. User may not know which files have issues.

**Workaround**: Check JSON files manually:
```bash
python3 -m json.tool runs/{run_id}/manifest.json
```

**Status**: Minor issue, acceptable for MVP.

---

### 7. No Validation of Evidence Paths

**Location**: `api_server.py` line 389

**Issue**: `evidence_paths` in closure creation are not validated to exist.

**Impact**: Users can reference non-existent files.

**Status**: Enhancement for Phase 2.

---

### 8. Closure ID Generation May Collide

**Location**: `api_server.py` line 367-368

**Issue**: Closure ID format `CL-{YYYYMMDD}-{proposal_id_prefix}` may collide if multiple closures created for same proposal on same day.

**Impact**: Low (unlikely in practice), but possible.

**Status**: Enhancement for Phase 2 (add random suffix or counter).

---

### 9. No Pagination for Large Lists

**Location**: All list endpoints (`GET /inbox`, etc.)

**Issue**: All items returned in single response. No pagination.

**Impact**: Performance issues with large datasets.

**Status**: Enhancement for Phase 2.

---

### 10. No Search/Filtering in API

**Location**: All endpoints

**Issue**: Frontend filtering only. No server-side search or advanced filtering.

**Impact**: All data must be loaded to frontend.

**Status**: Enhancement for Phase 2.

---

## TODO (Phase 2)

### High Priority

1. **Implement Promote Wizard**
   - UI component for selecting artefacts
   - API endpoint `POST /cli/promote`
   - Validation of output contracts
   - Atomic promotion with rollback

2. **Implement Canonical Viewer**
   - Read-only view of canonical content
   - Provenance trail display
   - Related decisions list

3. **Complete CLI Validator Integration**
   - Implement actual CLI command or wrapper
   - Proper error handling
   - Status reporting

4. **Add Evidence Path Validation**
   - Validate `evidence_paths` exist before closure creation
   - Return clear error if paths invalid

### Medium Priority

5. **User Authentication**
   - Basic auth or local user management
   - User identity in audit logs
   - Multi-user support

6. **Observability Dashboards**
   - Signal frequency charts
   - Gate frequency charts
   - Run health metrics
   - Audit log timeline

7. **Improve Closure ID Generation**
   - Add random suffix or counter
   - Prevent collisions

8. **Add Pagination**
   - Paginate inbox items
   - Paginate run lists
   - Paginate proposal lists

### Low Priority

9. **Server-Side Search/Filtering**
   - Search proposals by title
   - Filter runs by status
   - Advanced query language

10. **Indexer Error Logging**
    - Log which files failed to parse
    - Summary of errors in reindex response

11. **Batch Operations**
    - Batch approve/reject proposals
    - Batch closure creation (if needed)

12. **Export Functionality**
    - Export inbox to CSV/JSON
    - Export run data
    - Export audit logs

## Not Planned (Out of Scope)

- **Database**: Staying filesystem-first
- **Cloud deployment**: Local-only design
- **Real-time updates**: Polling-based for MVP
- **Mobile UI**: Desktop-focused
- **Offline mode**: Requires network for API calls

## Code References

Main source files:

- **`indexer.py`**: Filesystem scanner
  - `build_inbox_index()`: Builds inbox items from runs/proposals/closures
  - `reindex()`: Generates all JSON indices (inbox_index, run_index, proposal_index, closure_index)
  - Issue #6: Corrupted JSON handling (exceptions caught but not logged)

- **`api_server.py`**: FastAPI backend
  - `POST /cli/validate`: Placeholder endpoint (line 430-461) - Issue #1
  - `create_closure()`: Closure ID generation (line 367-368) - Issue #8
  - `create_closure()`: Evidence path validation missing (line 389) - Issue #7
  - `get_username()`: Uses `getpass.getuser()` (line 88-90) - Issue #2

- **`ui/src/api.ts`**: API client
  - `API_BASE = '/api'`: Base URL configuration
  - All API methods: No pagination support - Issue #9

- **`ui/src/components/Inbox.tsx`**: Frontend filtering only, no server-side search - Issue #10
- **`ui/src/components/ClosureComposer.tsx`**: Closure creation form (Phase 2: Promote Wizard not implemented)
