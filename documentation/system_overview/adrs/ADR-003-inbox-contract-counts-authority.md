# ADR-003 — Inbox contract counts authority
Status: Accepted
Date: 2026-01-22

## Context (AS-IS, cited)
- **UI inbox types** declared `InboxResponse` with only `generated_at` and `items`, so prior behavior left count logic to the client; this remains true before the new change (`runtime/ui/src/api.ts:17-41`).
- **API response model** already defined `InboxResponse` with a `counts` field, yet the handler at the time only normalized `generated_at` + `items`, missing the counts object the UI implicitly expected (`runtime/api_server.py:118-166`).
- **/inbox handler** previously returned only `generated_at` and `items`, so the UI assumed counts from a local derivation; now the decision upstream will reintroduce counts into the response (`runtime/api_server.py:298-334`).
- **QA pipeline** hit `/inbox` to verify presence of items but never asserted counts consistency, leaving the previous API drift undetected (`runtime/scripts/qa_full_system.sh:124-149`).

## Decision (NEW)
- The **API is authoritative** for the inbox counts summary (Option A from TICKET-001-inbox-schema-unification.md). The server will compute and return the canonical `counts` object alongside `items` so clients and QA can rely on a single source of truth.

## Consequences
- `/inbox` must emit `{ generated_at, counts, items }` with counts derived deterministically from the underlying index (new logic in `runtime/api_server.py`).
- UI consumers must read the new `counts` field and be tolerant of its absence only during a controlled rollout (per the optional backward-compat guidance in `TICKET-001-inbox-schema-unification.md`).
- `qa_full_system.sh` must validate that `counts.total` matches `items.length`, turning QA into a regression guard for the new shape.

## Implementation notes
- Implementation tracked in `documentation/system_overview/tickets/TICKET-001-inbox-schema-unification.md`.
