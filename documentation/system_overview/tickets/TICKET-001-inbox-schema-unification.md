# TICKET-001 — Inbox schema unification (API ↔ UI)

## 1) Problem statement (AS-IS, cited)
- **Contract drift**: the Implementation Backlog (phase 1.1) already flags that the UI expects an `InboxResponse.counts` summary while the API currently returns only `generated_at` plus `items`, which means the two ends are misaligned and there is no canonical counts source to surface in the UI (`mustika-rasa-clean/documentation/system_overview/IMPLEMENTATION_BACKLOG.md:11-15`).
- **UI shape**: the TypeScript `InboxResponse` definition only declares `generated_at` and `items` so any counts-based UI widgets must be derived through ad hoc logic rather than from the API contract (`mustika-rasa-clean/runtime/ui/src/api.ts:17-41`).
- **API shape**: the `/inbox` handler normalizes whatever is in `indices/inbox_index.json` but returns a JSON object with just `generated_at` and `items` (no counts field), even though the FastAPI `InboxResponse` model includes `counts`, so the endpoint cannot satisfy the UI’s implicit counts need (`mustika-rasa-clean/runtime/api_server.py:118-166` and `mustika-rasa-clean/runtime/api_server.py:298-334`).
- **Impact**: without a canonical counts field the inbox signal described in the Governance layer—where signals/gates must be transparent to humans—loses fidelity, and QA regression checks cannot assert the same rollout as the UI (`mustika-rasa-clean/documentation/system_overview/GOVERNANCE.md:3-82`).

## 2) Options (NEW decision)
All options are NEW and will decide where the truth of the counts summary lives.

- **Option A – API-derived counts (preferred path for determinism)**
  - Pros: single source of truth, counts are computed once server-side, distinguishes by severity/status, and directly extends the existing `/inbox` schema.
  - Cons: server must read/per index data, may need to mirror part of the indexer logic.
  - Backward compatibility: additive for API consumers; UI simply binds to the new field.
  - Complexity: moderate, requires injecting counts calculation into `get_inbox`.

- **Option B – UI-derived counts**
  - Pros: keeps API surface unchanged; UI can calculate totals from `items`.
  - Cons: duplicative logic on each client, more fragile if index schema evolves.
  - Backward compatibility: API stays the same; UI change only.
  - Complexity: lower; just change UI components to derive counts.

- **Option C – Versioned response (InboxResponseV2)**
  - Pros: clear version dance, allows incremental rollout.
  - Cons: requires multi-version support in server and UI, increases QA scope.
  - Backward compatibility: requires supporting both v1 and v2 for a transition period.
  - Complexity: highest due to branching in server and QA.

## 3) Recommended option (NEW placeholder)
- **RECOMMENDED**: Option A/B/C (NEW, reference choice in implementation PR once API/UI alignment is decided).
- **Acceptance criteria (applies regardless of chosen option)**:
  1. `/inbox` responses always include a deterministic `counts` object aligned with the inbox items.
  2. The inbox UI renders without runtime or type errors and the QA check for `/inbox` passes against the new schema.

## 4) Implementation plan (NEW)
- **API (`mustika-rasa-clean/runtime/api_server.py`)**: extend `get_inbox` (currently normalizing to `{ generated_at, items }` in lines 298-334) so it also derives `counts` from the inbox payload (or `indices/inbox_index.json` if it already includes counts). Reuse the existing `InboxResponse` Pydantic model that already declares `counts` (`mustika-rasa-clean/runtime/api_server.py:118-166`). Keep normalized payload deterministic and log generation in `audit/api_actions.log` per existing audit helper (`mustika-rasa-clean/runtime/api_server.py:298-334`).
+ **UI (`mustika-rasa-clean/runtime/ui/src/api.ts` + downstream consumers)**: adjust `InboxResponse` type so `counts` is declared, update `api.getInbox` to expect the new field, and ensure UI components (e.g., `Inbox` view tied into `/inbox` via the router in `mustika-rasa-clean/runtime/ui/src/App.tsx:11-32`) render counts safely (`mustika-rasa-clean/runtime/ui/src/api.ts:17-94`).
- **QA (`mustika-rasa-clean/runtime/scripts/qa_full_system.sh`)**: after the existing `GET /inbox` check (lines 124-149), add a step that asserts the response contains a `counts` object whose totals match the number of items (matching the new canonical shape) and record the result in `audit/qa/latest_full/summary.tsv` so regressions surface immediately (`mustika-rasa-clean/runtime/scripts/qa_full_system.sh:124-149`).
- **Docs/Backlog**: mention the schema decision in `IMPLEMENTATION_BACKLOG` (phase 1.1) and in any relevant standards doc so the choice is visible to operations teams (citing the same backlog lines 11-15 that flagged the drift).

## 5) Contract definition (NEW)
Canonical `/inbox` payload that must be emitted by the API (NEW schema placeholder):
```json
{
  "generated_at": "2026-01-22T13:00:00Z",
  "counts": {
    "total": 42,
    "by_severity": { "critical": 3, "warning": 12, "info": 27 },
    "by_status": { "open": 38, "closed": 4 }
  },
  "items": [
    {
      "id": "inbox-0001",
      "type": "closure_needed",
      "severity": "critical",
      "status": "open",
      "required_action": "review",
      "proposal_id": "P-001",
      "run_id": "RUN-001"
    }
  ]
}
```
The UI and QA tests must treat this shape as the canonical contract (counts derived from the same source as `items`).

## 6) Tests & QA (NEW)
- Extend `qa_full_system.sh` to fetch `/inbox`, parse the JSON, and assert that `counts.total` equals the length of `items` and that severity/status buckets sum correctly; record failures like other checks (the script already hits `/inbox` and writes to `summary.tsv` around lines 124-149) (`mustika-rasa-clean/runtime/scripts/qa_full_system.sh:124-149`).
- Add a regression check ensuring `/inbox` response continues to return items (existing QA path) so failure is obvious if counts computation removes or filters entries.
- Include a human-reviewed note in `audit/api_actions.log` (via `ensure_audit_log`) when `/inbox` responses change structure, so governance teams know the schema shift happened without manual guesswork (`mustika-rasa-clean/runtime/api_server.py:143-166`).
- Failure mode: QA summary records `GET_/inbox` as `FAIL` if counts are missing or mismatched, enabling early detection (consistency with existing pass/fail pattern in `qa_full_system.sh:124-149`).

## 7) Definition of Done (DoD)
- `/inbox` endpoint returns `{ generated_at, counts, items }` where `counts` is derived deterministically from `items` or the underlying index.
- UI entrypoint (`api.getInbox` plus routing through `App.tsx`/`Inbox` components) renders the inbox without type/runtime errors.
- QA script (`runtime/scripts/qa_full_system.sh`) asserts the presence and consistency of `counts` and writes a `PASS`/`FAIL` row to `audit/qa/latest_full/summary.tsv`.
- Documentation/backlog reflects the selected option and explains the derivation, linking back to the existing schema-unification epic.

## Evidence index
- `mustika-rasa-clean/documentation/system_overview/IMPLEMENTATION_BACKLOG.md:11-15` (phase 1.1 outlines the contract drift that prompts this ticket).
- `mustika-rasa-clean/runtime/ui/src/api.ts:17-94` (`InboxResponse` shape and `getInbox` client fetch logic).
- `mustika-rasa-clean/runtime/api_server.py:118-166` (Pydantic `InboxResponse` model includes `counts`) and `mustika-rasa-clean/runtime/api_server.py:298-334` (current handler that only returns `generated_at` + `items`).
- `mustika-rasa-clean/runtime/scripts/qa_full_system.sh:124-149` (current QA check that queries `/inbox`).
- `mustika-rasa-clean/documentation/system_overview/GOVERNANCE.md:3-82` (governance emphasis on transparent, derived indices and audit visibility for inbox signals).
