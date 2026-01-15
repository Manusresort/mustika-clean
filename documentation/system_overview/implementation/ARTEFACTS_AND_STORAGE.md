# Artefacts and Storage — File Structure

## Base Path

All paths are relative to:
```
/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy/
```

## Directory Structure

```
.
├── runs/              # Immutable run bundles
├── proposals/         # Non-canonical proposal records
├── closures/         # Immutable closure records
├── promotion/         # Promotion records (Phase 2)
├── canonical/         # Canonical content (read-only)
├── indices/          # JSON indices (generated)
├── audit/            # Append-only audit logs
├── indexer.py         # Filesystem scanner
└── api_server.py      # FastAPI backend
```

## Runs (`runs/`)

**Purpose**: Immutable run bundles from pipeline execution.

**Structure**:
```
runs/
└── {run_id}/              # Run identifier (directory name)
    ├── manifest.json      # Run metadata (optional)
    ├── signals.json       # Signals from agents (optional)
    ├── incident.json      # Incident report if run failed (optional)
    ├── validator/
    │   ├── report.json    # Validator output (optional)
    │   └── gates.json     # Gate definitions (optional)
    ├── outputs/           # Output files
    │   └── *.txt, *.md, etc.
    └── logs/              # Log files
        └── *.log
```

**Example**:
```
runs/
└── RUN_20260109_001/
    ├── manifest.json
    ├── signals.json
    ├── validator/
    │   ├── report.json
    │   └── gates.json
    ├── outputs/
    │   └── output.txt
    └── logs/
        └── run.log
```

**Immutability**: UI never modifies run directories. They are read-only.

**Indexer behavior**: Scans all subdirectories, reads JSON files, determines status from:
- `incident.json` existence → `failed`
- `validator/report.json` with `overall_status: "FAIL"` → `failed`
- `validator/gates.json` with blocking gates → `gated`
- Otherwise → `completed`

## Proposals (`proposals/`)

**Purpose**: Non-canonical proposal records awaiting review.

**Structure**:
```
proposals/
└── {proposal_id}/         # Proposal identifier (directory name)
    ├── proposal.md        # Proposal content (optional)
    ├── status.json        # Proposal status
    ├── gates.json         # Gate definitions (optional)
    ├── required_closure.json  # Closure requirements (optional)
    │   # as-built: presence-based; observed keys: required, types
    ├── links.json         # Linked runs (optional)
    └── review_pack/       # Review materials (optional)
        └── *.md, *.txt, etc.
```

**As-built (MVP) review_pack**:
- Optional directory at `runtime/proposals/<proposal_id>/review_pack/`.
- Status: derived / non-canonical / read-only consumer artifact.
- Minimal observed contents (may vary per proposal):
  - `summary.md` — short summary of proposal/run context
  - `runs.json` — linked run_ids + paths (as generated)
  - `checks.md` — summary of eval/output checks
- No schema enforcement is present in code; contents are optional.

**Example**:
```
proposals/
└── P-20260109-001/
    ├── proposal.md
    ├── status.json
    ├── gates.json
    ├── required_closure.json
    ├── links.json
    └── review_pack/
        ├── diff.md
        └── evidence.txt
```

**Status file** (`status.json`):
```json
{
  "status": "open",
  "severity": "info",
  "closed_at": "2026-01-09T12:00:00",
  "closure_id": "CL-20260109-abc12345"
}
```

**Links file** (`links.json`):
```json
{
  "run_ids": ["RUN_20260109_001"]
}
```

**Indexer behavior**: Scans directories, reads `status.json`, determines inbox items:
- Status `"open"` or `"in_review"` → Review Required
- `gates.json` exists with gates → Gate Triggered
- `required_closure.json` exists → Closure Needed

## Closures (`closures/`)

**Purpose**: Immutable closure records (decisions).

**Structure**:
```
closures/
└── {closure_id}/          # Closure identifier (directory name)
    ├── closure.json       # Closure data (preferred)
    └── closure.md         # Alternative markdown format
```

**Closure ID format**: `CL-{YYYYMMDD}-{proposal_id_prefix}`

**Example**:
```
closures/
└── CL-20260109-abc12345/
    └── closure.json
```

**Closure file** (`closure.json`):
```json
{
  "closure_id": "CL-20260109-abc12345",
  "created_at": "2026-01-09T12:00:00",
  "created_by": "username",
  "proposal_id": "P-20260109-001",
  "source_run_id": "RUN_20260109_001",
  "decision_type": "APPROVE",
  "rationale": "Rationale text (min 10 chars)",
  "evidence_paths": ["runs/RUN_20260109_001/outputs/file.txt"],
  "sign_off": true
}
```

**Immutability**: Once `closure.json` exists, API returns `400 Bad Request` if creation attempted again.

**Indexer behavior**: Scans directories, reads `closure.json` or `closure.md`, extracts metadata.

## Promotion (`promotion/`)

**Purpose**: Promotion records (Phase 2, not yet implemented).

**Structure**: TBD

## Canonical (`canonical/`)

**Purpose**: Read-only canonical content.

**Structure**: TBD (Phase 2)

**Policy**: UI never writes to this directory. Enforced by `check_canonical_write()` function (not yet active in MVP).

## Indices (`indices/`)

**Purpose**: Generated JSON indices for fast UI queries.

**Structure**:
```
indices/
├── inbox_index.json       # Inbox items (derived)
├── run_index.json         # Run metadata list
├── proposal_index.json    # Proposal metadata list
└── closure_index.json     # Closure metadata list
```

**Generated by**: `indexer.py` (via `reindex()` method or `POST /reindex` API call)

**Inbox index** (`inbox_index.json`):
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

**Run index** (`run_index.json`):
```json
{
  "generated_at": "2026-01-09T12:00:00",
  "runs": [
    {
      "run_id": "RUN_20260109_001",
      "status": "completed",
      "created_at": "2026-01-09T10:00:00",
      "validator_status": "PASS",
      "blocking_gates": false,
      "gate_count": 0,
      "signal_count": 2,
      "has_incident": false,
      "manifest": {...}
    }
  ]
}
```

**Proposal index** (`proposal_index.json`):
```json
{
  "generated_at": "2026-01-09T12:00:00",
  "proposals": [
    {
      "proposal_id": "P-20260109-001",
      "title": "Proposal title",
      "status": "open",
      "severity": "info",
      "requires_closure": false,
      "gate_count": 0,
      "created_at": "2026-01-09T10:00:00"
    }
  ]
}
```

**Closure index** (`closure_index.json`):
```json
{
  "generated_at": "2026-01-09T12:00:00",
  "closures": [
    {
      "closure_id": "CL-20260109-abc12345",
      "decision_type": "APPROVE",
      "created_at": "2026-01-09T12:00:00",
      "created_by": "username",
      "proposal_id": "P-20260109-001",
      "run_id": "RUN_20260109_001"
    }
  ]
}
```

**Regeneration**: Indices are regenerated on:
- Manual reindex (`POST /reindex` or `python3 indexer.py`)
- After closure creation (automatic reindex)

## Audit (`audit/`)

**Purpose**: Append-only audit logs.

**Structure**:
```
audit/
└── api_actions.log       # JSON lines format
```

**Format**: One JSON object per line (JSONL):
```json
{"timestamp": "2026-01-09T12:00:00", "message": "Closure created: CL-20260109-abc12345", "metadata": {"closure_id": "CL-20260109-abc12345", "proposal_id": "P-20260109-001", "decision_type": "APPROVE"}}
{"timestamp": "2026-01-09T12:05:00", "message": "Reindex triggered", "metadata": {"result": {"runs": 5, "proposals": 3, "closures": 2, "inbox_items": 8}}}
```

**Append-only**: Never overwritten, only appended to.

**Generated by**: `ensure_audit_log()` function in `api_server.py` (line 93-106)

## File Naming Conventions

- **Run IDs**: Directory name (e.g., `RUN_20260109_001`)
- **Proposal IDs**: Format `P-{YYYYMMDD}-{####}` (e.g., `P-20260109-001`)
- **Closure IDs**: Format `CL-{YYYYMMDD}-{proposal_id_prefix}` (e.g., `CL-20260109-abc12345`)
- **Promotion IDs**: TBD (Phase 2)

## Encoding

All text files use UTF-8 encoding.

## Permissions

- Directories: Created with default OS permissions
- Files: Created with default OS permissions
- No special permission requirements in MVP (assumes single-user local environment)

## Code References

Main source files:

- **`indexer.py`**: Filesystem scanner
  - `scan_runs()`: Reads `runs/` directories and extracts metadata (line 34-115)
  - `scan_proposals()`: Reads `proposals/` directories and extracts metadata (line 117-182)
  - `scan_closures()`: Reads `closures/` directories and extracts metadata (line 184-225)
  - `build_inbox_index()`: Builds inbox items from scans (line 227-326)
  - `reindex()`: Writes all indices to `indices/` directory (line 328-368)

- **`api_server.py`**: FastAPI backend
  - `get_run()`: Reads from `runs/{run_id}/` (line 159-244)
  - `get_proposal()`: Reads from `proposals/{proposal_id}/` (line 247-323)
  - `get_closure()`: Reads from `closures/{closure_id}/` (line 326-355)
  - `create_closure()`: Writes to `closures/{closure_id}/closure.json` and updates `proposals/{proposal_id}/status.json` (line 358-427)
  - `ensure_audit_log()`: Appends to `audit/api_actions.log` (line 93-106)

- **`ui/src/api.ts`**: API client
  - `API_BASE = '/api'`: Base URL configuration
  - All API methods read/write through backend, never directly access filesystem

- **`ui/src/components/`**: All components read data via API, no direct filesystem access
