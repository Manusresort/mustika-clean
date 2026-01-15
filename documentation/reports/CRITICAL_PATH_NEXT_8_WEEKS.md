# Critical Path — Next 8 Weeks (MVP → Book-Level)

This plan defines the smallest set of milestones needed to reach a
book-level end-to-end workflow, while preserving existing constraints.

Constraints: filesystem-first, human-in-the-loop, immutable runs/closures,
no auto-promotion, canonical read-only.

---

## Milestone 1 — Book Ingest + Excerpt Registry
Status: DONE
Definition of done:
- Book source exists in document-based form with provenance metadata.
- Excerpt registry exists in document-based form for all chapters with stable IDs and versions (met).
- Registry and alignment are formalized into machine-readable, indexable artifacts (met for alignment).

Tests / proofs:
- Indexer can consume registry/alignment without manual intervention.
- Indexer can list excerpt inventory (even if not yet run).

Known uncertainties (non-blocking):
- Incomplete coverage or inconsistent excerpt IDs.

Artifacts created:
- Excerpt registry files
- Source provenance records

---

## Milestone 2 — Batch Run Orchestration
Status: DONE (excerpt-level)
Definition of done:
- Run bundles are created per excerpt with consistent layouts.
- Per-chapter batch scripting is not required for M2 (subroute; out of scope for M2 completion).

Tests / proofs:
- Multiple run bundles exist under `runtime/runs/<excerpt_id>/` for an excerpt.
- Each bundle includes outputs, logs, and eval reports.

Non-blocking constraints:
- Resource/time constraints for batch runs.

Artifacts created:
- Run bundles per excerpt
- Batch run logs

---

## Milestone 3 — Editorial Review Packs + Closure Workflow
Status: DONE
Definition of done:
- Review packs are generated for each excerpt/run.
- Proposals and closures can be created per excerpt in a consistent format.
- Proposal/closure standardization DoD + AC: see documentation/reports/BACKLOG_GITHUB_ISSUES.md (issue: Standardize proposal and closure formats for batch review).
- Proposal/closure format standardization completed (artefact-level batch consistency validated with P-001..P-004).

Tests / proofs:
- Proposals and closures appear in their directories and indices.
- Inbox index shows review-required items.
- Milestone 3 review/closure standardization is complete; further work concerns content review throughput and quality, not artefact structure.

Non-blocking (M4/M5):
- Review fatigue; inconsistent closure formats.

Artifacts created:
- Proposal files
- Closure files
- Review packs

---

## Milestone 4 — Book-Level UI Workflow
Definition of done:
- UI provides coverage view (chapter/excerpt status).
- UI supports batch review (triage and navigation across runs).

Tests / proofs:
- UI renders chapter coverage counts from indices.
- UI links to run/proposal/closure detail across batches.

Risks:
- UI performance or index completeness at scale.

Artifacts created:
- Updated UI views (non-canonical)

As-built (2026-01-14):
- Run comparison view route: `/compare/runs/:baselineId/:candidateId`. (path: runtime/ui/src/App.tsx, lines: 30-37)
- UI component renders regression report content. (path: runtime/ui/src/components/RunComparisonView.tsx, lines: 1-90)
- API client + endpoints for report/diff: runtime/ui/src/api.ts; runtime/api_server.py. (path: runtime/ui/src/api.ts, lines: 82-105; path: runtime/api_server.py, lines: 278-340)
- Coverage dashboard reads page_sources coverage via GET /page-sources-coverage and renders aggregate counts/gaps. (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 49-51, 138-145; path: runtime/api_server.py, lines: 233-271)
- Coverage UI labels chapter and excerpt limitations explicitly. (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 132-137)
- Review Queue view exists at /review-queue with kind+severity filters and Next/Prev navigation via query params. (path: runtime/ui/src/App.tsx, lines: 31-33; path: runtime/ui/src/components/Inbox.tsx, lines: 82-172; path: runtime/ui/src/components/ReviewPackViewer.tsx, lines: 14-140; path: runtime/ui/src/components/RunDetail.tsx, lines: 14-135)

---

## Milestone 5 — Operational Reliability + Regression Checks
Definition of done:
- Reindexing and run reproducibility documented and repeatable.
- Regression checks exist for run outputs and indices.

Tests / proofs:
- Reindexing reproduces indices consistently.
- Regression check reports saved per batch run.

Risks:
- False positives/negatives in checks.

Artifacts created:
- Regression check reports
- Reproducibility notes/logs

As-built (2026-01-14):
- Scripts: runtime/scripts/regression_check_run_outputs.py; runtime/scripts/regression_check_indices.py. (path: runtime/scripts/regression_check_run_outputs.py, lines: 1-5; path: runtime/scripts/regression_check_indices.py, lines: 1-9)
- Run output report: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md. (path: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md, lines: 1-6)
- Index report: runtime/audit/index_regression_report_latest.md. (path: runtime/audit/index_regression_report_latest.md, lines: 1-6)
- Scope (run outputs): outputs/ and eval/. (path: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md, lines: 18-20)
- Scope (indices): runtime/indices vs runtime/audit/index_snapshot_pre; generated_at ignored. (path: runtime/audit/index_regression_report_latest.md, lines: 5-14)
- Output-dir guard message: "ERROR: output-dir must be under" (path: runtime/scripts/regression_check_run_outputs.py, lines: 163-172)
- Writes constrained to runtime/audit; canonical remains read-only. (path: runtime/scripts/regression_check_run_outputs.py, lines: 163-178; path: documentation/system_overview/GOVERNANCE.md, lines: 10-13, 44-46)
