# MVP → Full System Backlog (GitHub-Style Issues)

All issues must respect constraints: filesystem-first, human-in-the-loop,
immutable runs/closures, no auto-promotion, canonical read-only.

---

## Content pipeline

- [x] Ingest chapter sources with provenance metadata
  - Labels: pipeline, content, milestone-1
  - Depends on: none
  - Summary: establish a stable ingest format and location for chapters.
  Note: Resolved for M1 (administrative).

- [x] Create excerpt registry with stable IDs and versions
  - Labels: pipeline, content, milestone-1
  - Depends on: Ingest chapter sources with provenance metadata
  - Summary: maintain excerpt ID map for the full book.

- [x] Excerpt alignment index (chapter → excerpt IDs)
  - Labels: pipeline, validator, milestone-1
  - Depends on: Create excerpt registry with stable IDs and versions
  - Summary: machine-readable alignment to drive batch runs.

---

## Editorial workflow

- [x] Generate review packs per run bundle
  - Labels: pipeline, governance, milestone-3
  - Depends on: Batch run orchestration per chapter
  - Summary: structured review artifacts per excerpt/run.

- [x] Standardize proposal and closure formats for batch review
  - Labels: governance, milestone-3
  - Depends on: Generate review packs per run bundle
  - Summary: consistent closure lifecycle across batches.
  Closed after validation with four proposals (P-001..P-004) and one completed human content review (P-002). Item scope explicitly excluded content quality evaluation beyond individual reviews.

---
### Definition of Done (DoD)

This item is DONE when proposal and closure artefacts support batch review in a consistent, human-reviewable way, without changing invariants or requiring code/UI changes.

Scope / constraints:
- Filesystem-first; artefacts are the source of truth (indices are derived).
- No schema validation/enforcement required.
- No UI requirements.
- No content duplication; evidence is referenced by paths/IDs.
- `runtime/data/ingest/page_sources/` remains read-only for agents.
- Excerpt-first runtime remains leading.

A) Proposal requirements (per `runtime/proposals/<proposal_id>/`)
1) Identity & status:
   - `status.json` contains at minimum: `proposal_id`, `status`, `severity`, `created_at`, `linked_run_ids`, and a human-required action indicator.
2) Human explanation (plain language):
   - Exactly one place provides a clear plain-language explanation of:
     - what the uncertainty/problem is,
     - why it is escalated (why automation was insufficient),
     - why human decision is needed.
   - Location: either `status.json` or `review_pack/summary.md` (but not scattered across multiple places).
3) Evidence linkage (no copied content):
   - Proposal explicitly links to the relevant run artefacts (via run IDs and/or paths) so a reviewer can open:
     - run outputs,
     - eval checks,
     - review pack
     without searching.
4) Page-based evidence context (when applicable):
   - If page-based evidence is referenced, it MUST include the target page plus a context window:
     - previous page (N-1), target page (N), next page (N+1),
     referenced as paths/IDs only.

B) Closure requirements (per `runtime/closures/<closure_id>/`)
1) Identity & traceability:
   - `closure.json` includes at minimum: `closure_id`, `proposal_id`, `source_run_id` (or equivalent), `decision_type`, `created_at`, `created_by`.
2) Human rationale (plain language):
   - `closure.json` includes a plain-language rationale explaining what was decided and why.
3) Evidence paths (incl. page context when applicable):
   - `closure.json` includes `evidence_paths` that link to relevant run artefacts and (if page-based) the page context window (N-1/N/N+1), as paths/IDs only.

C) Batch suitability:
- “Standardized for batch review” is only claimed when at least two proposals/closures can be compared side-by-side with the same reviewer mental model:
  - same structure,
  - same evidence-linking conventions,
  - same plain-language explanation placement.

---

### Acceptance Criteria (AC)

AC-1 Proposal is self-reviewable:
- A reviewer can understand the issue and why it is escalated from the proposal artefacts alone (plain language), without opening logs/code.

AC-2 Evidence is directly reachable:
- The proposal explicitly indicates which runs/evidence to open (run IDs/paths) to inspect outputs/evals/review_pack without manual searching.

AC-3 Page context is explicit when page-based evidence is used:
- Target page and context window (prev/next) are explicitly referenced as paths/IDs only.

AC-4 Closure is auditable in plain language:
- The closure states the decision and rationale in plain language and is traceable to the proposal and run.

AC-5 Batch consistency:
- Comparing two proposals, the structure and reviewer workflow is the same (status → explanation → evidence → decision/closure), including page context when applicable.

---

Status: DONE
Evidence: P-001..P-004 conform DoD and AC-1–AC-5 (artefact-level batch consistency).

---

- [x] Batch review queue + triage rules in indices
  - Labels: governance, ui, milestone-3
  - Depends on: Standardize proposal and closure formats for batch review
  - Summary: expose review status via derived indices.
  Note: Dependency satisfied with P-001..P-004 (AC-5 met).

---

## Quality / validation

- [x] Add regression check harness for run outputs
  - Labels: validator, ops, milestone-5
  - Depends on: Batch run orchestration per chapter
  - Summary: detect drift across repeated runs.
  - Evidence (as-built 2026-01-14): runtime/scripts/regression_check_run_outputs.py; runtime/scripts/regression_check_indices.py. (path: runtime/scripts/regression_check_run_outputs.py, lines: 1-5; path: runtime/scripts/regression_check_indices.py, lines: 1-9)
  - Evidence (as-built 2026-01-14): runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md; runtime/audit/index_regression_report_latest.md. (path: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md, lines: 1-6; path: runtime/audit/index_regression_report_latest.md, lines: 1-6)

- [x] Add excerpt coverage validation
  - Evidence: runtime/scripts/validate_excerpt_coverage.py; runtime/audit/coverage_report_latest.md; RUNBOOK section.
  - Labels: validator, pipeline, milestone-1
  - Depends on: Excerpt alignment index (chapter → excerpt IDs)
  - Summary: ensure all excerpts are represented in runs.

---

## UI / UX

- [x] UI coverage dashboard (chapter/excerpt progress)
  - Labels: ui, milestone-4
  - Depends on: Excerpt alignment index (chapter → excerpt IDs)
  - Summary: show book-level progress and coverage.
  - UI coverage dashboard (chapter/excerpt progress) — Scope, DoD, AC (B: readability-only formatting)
    - Scope-beslissing:
      - Opmaak = presentatie, niet semantiek.
      - UI mag leesbaarheid verbeteren (markdown/whitespace/panels/monospace) maar mag geen betekenis wijzigen,
        geen structuur infereren, geen content herordenen.
    - DoD:
      1) Coverage Dashboard view bestaat en is zichtbaar in navigatie (read-only).
      2) Coverage wordt getoond op basis van bestaande indices:
         - primair: runtime/indices/page_sources_coverage_index.json
         - secundair (optioneel): runtime/indices/inbox_index.json
      3) Excerpt-level progress zichtbaar (counts + gaps; herleidbaar tot indexvelden).
      4) Chapter-niveau expliciet begrensd met label:
         “Chapter coverage not available (no runtime chapter↔excerpt mapping)”
      5) Book-level progress getoond als aggregatie van excerpt-coverage.
      6) Leesbaarheid verbeterd via niet-semantische opmaak (markdown, whitespace, secties, monospace).
      7) Geen nieuwe runtime-artefacts / geen indexer-wijzigingen / geen canonical writes / geen registry-alignment.
    - AC’s:
      - AC-1 Data-integriteit: UI leest uitsluitend bestaande indices/artefacts; read-only.
      - AC-2 Transparantie: chapter-beperking expliciet vermeld.
      - AC-3 Verifieerbaarheid: na POST /reindex reflecteert dashboard gewijzigde coverage.
      - AC-4 Opmaakbeperking: opmaak verandert geen betekenis, grenzen of structuur; pure presentatie.
      - AC-5 Milestone-4 proof: UI rendert coverage counts vanuit indices.
  - Evidence (as-built 2026-01-14): CoverageDashboard reads page_sources_coverage_index.json via GET /page-sources-coverage and renders counts/gaps. (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 49-51, 138-145; path: runtime/api_server.py, lines: 233-271)
  - Evidence (as-built 2026-01-14): Labels for chapter and excerpt limitations are explicit. (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 132-137)
  - Note: UI remains aggregate-only where chapter↔excerpt mapping is absent; label is explicit. (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 132-137)

- [x] UI batch review navigation
  - Labels: ui, governance, milestone-4
  - Depends on: Batch review queue + triage rules in indices
  - Summary: review multiple runs and closures efficiently.
  - UI batch review navigation — Scope, DoD, AC (inbox-based, read-only)
    - Scope:
      - Batch review navigation is gebaseerd op bestaande inbox_index.json.
      - Geen nieuwe queue semantics, geen prioriteit, geen workflow engine.
      - Read-only navigatie (list → detail → next/prev).
    - DoD:
      1) UI toont expliciete “Review Queue” view.
      2) View is gebaseerd op inbox_index.json via GET /inbox.
      3) Items zijn filterbaar op kind/severity (bestaande velden).
      4) Vanuit een item kan de gebruiker:
         - naar proposal/run detail
         - naar volgend/vorig item in dezelfde gefilterde lijst.
      5) Geen nieuwe runtime artefacts of indexer-wijzigingen.
    - AC’s:
      - AC-1 Data-integriteit: UI leest uitsluitend inbox_index.json; read-only.
      - AC-2 Determinisme: next/prev volgt expliciete sortering (bijv. stable array order).
      - AC-3 Transparantie: UI vermeldt “signal-based review queue (not priority-ranked)”.
      - AC-4 Milestone-4 proof: batch navigation aantoonbaar via UI (list → detail → next).
  - Evidence (as-built 2026-01-14): Review Queue route and label in Inbox (mode=review-queue). (path: runtime/ui/src/App.tsx, lines: 31-33; path: runtime/ui/src/components/Inbox.tsx, lines: 13-109)
  - Evidence (as-built 2026-01-14): Kind+severity filters and review-queue query params. (path: runtime/ui/src/components/Inbox.tsx, lines: 82-172; path: runtime/ui/src/components/Inbox.tsx, lines: 73-80)
  - Evidence (as-built 2026-01-14): Next/Prev navigation in ReviewPackViewer and RunDetail. (path: runtime/ui/src/components/ReviewPackViewer.tsx, lines: 14-140; path: runtime/ui/src/components/RunDetail.tsx, lines: 14-135)

- [x] Run comparison view (iteration diff)
  - Labels: ui, validator, milestone-4
  - Depends on: Regression check harness for run outputs
  - Summary: visualize differences between runs.
  - Evidence (as-built 2026-01-14): UI route + component: runtime/ui/src/App.tsx; runtime/ui/src/components/RunComparisonView.tsx. (path: runtime/ui/src/App.tsx, lines: 30-37; path: runtime/ui/src/components/RunComparisonView.tsx, lines: 1-90)
  - Evidence (as-built 2026-01-14): API client + endpoints: runtime/ui/src/api.ts; runtime/api_server.py. (path: runtime/ui/src/api.ts, lines: 82-105; path: runtime/api_server.py, lines: 278-340)

---

## Ops

- [ ] Batch run reproducibility notes + log aggregation
  - Labels: ops, milestone-5
  - Depends on: Batch run orchestration per chapter
  - Summary: consistent log collection and replay notes.

- [x] Backup and restore workflow for runs/proposals/closures
  - Labels: ops, governance, milestone-5
  - Depends on: Standardize proposal and closure formats for batch review
  - Summary: protect immutable history.
  - Completion: documented copy-only workflow + reindex verification (see documentation/operator/BACKUP_AND_RESTORE_RUNTIME.md; documentation/operator/RUNBOOK.md reindex section; runtime/audit/index_regression_report_latest.md; runtime/audit/index_snapshot_pre/; runtime/audit/api_actions.log)

---

## Batch run orchestration (core)

- [ ] Batch run orchestration per chapter
  - Labels: pipeline, ops, milestone-2
  - Summary: repeatable execution for a chapter-sized set of excerpts.

  Status
  Blocked subroute — requires valid chapter↔excerpt context (future).

  Blocker(s)
  - Geen runtime-verifieerbare chapter↔excerpt relatie (alleen documentair beschreven; excerpt-centric indices).

  Not-blocked-by
  - Ontbreken van chapter-level rough_nl / english (afgeleide outputs; geen geldige bron-blokker).
  - Canonical writes of auto-promotion (expliciet verboden invariants).

  Probleemstelling
  Dit item vraagt om operator-triggered batch-orchestratie per chapter/excerpt set, met herhaalbare run
  bundles per excerpt op de filesystem. Verifieerbaarheid moet uitsluitend volgen uit bron-excerpt context
  en bestaande run-artefacten.

  Anti-requirements
  - Geen autonome beslisser; operator-trigger blijft vereist.
  - Geen UI-functionaliteit.
  - Geen nieuwe artefacttypes.
  - Geen writes naar runtime/canonical/; geen auto-promotion.
  - Geen gebruik van afgeleide outputs als bron-input.

  Epistemologische vastlegging
  - Bron: historische pagina’s/transcripties (excerpt-first).
  - Afgeleid: rough_nl, english en andere interpretatieve resultaten.
  - Gevolg: batch orchestration mag uitsluitend steunen op bron-excerpt context en operator-actie;
    afgeleide outputs zijn nooit vereiste bron-inputs.

  Change note
  - Heretikettering: eerdere impliciete blokkade (‘missing english/rough_nl’) gecorrigeerd naar
    ‘missing verifieerbare chapter-context op bron-niveau’ op basis van as-built analyse.
