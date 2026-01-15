# Repo Inventory (Mode C — Facts Only)

Scope: top-level and major subdirectories of the clean repo.
No behavior changes; documentation only.

## Top-level directories

| path | purpose (observed) |
|---|---|
| `config/` | configuration placeholders for the clean repo |
| `docs/` | entrypoint docs (overview, freeze, operator entrypoint, migration verification) |
| `documentation/` | system documentation, reports, operators, reading paths, architecture sources |
| `experiments/` | sandbox runs and pilot notes (non-canonical) |
| `governance/` | governance docs (policies, lifecycles, decision types, ADRs) |
| `historical/` | legacy docs/scripts/runs retained for reference |
| `meta/` | metadata snapshots (project state) |
| `runtime/` | active runtime system (api, indexer, runner, ui, data, runs, indices) |

## Runtime layout (high-level)

| path | purpose |
|---|---|
| `runtime/api_server.py` | API server entrypoint |
| `runtime/indexer.py` | filesystem indexer (generates indices) |
| `runtime/scripts/` | runtime scripts (dev start/stop, runner, reindex) |
| `runtime/src/` | runner + supporting code |
| `runtime/ui/` | UI application |
| `runtime/data/` | source inputs and imports |
| `runtime/runs/` | run bundles (per excerpt/run) |
| `runtime/indices/` | derived indices for UI/API (run, inbox, proposal, closure, review_queue) |
| `runtime/data/ingest/` | ingest artefacts (page_sources, chapters, prepared layers) |
| `runtime/data/ingest/page_ocr_corrected/` | prepared corrected-page layer (structure only; out of scope for M1) |
| `runtime/data/ingest/definitive_source/` | prepared definitive source layer (structure only; out of scope for M1) |
| `runtime/proposals/` | proposals (filesystem-first) |
| `runtime/closures/` | closures (filesystem-first) |
| `runtime/canonical/` | canonical outputs (read-only by invariant) |
| `runtime/audit/` | logs (if present) |
| `runtime/promotion/` | promotion staging (if used) |
| `runtime/prompts/` | prompt files (if used) |
| `runtime/sandbox_tools/` | sandbox tools (if present) |

As-built (2026-01-14) — regression checks:
- Scripts: runtime/scripts/regression_check_run_outputs.py; runtime/scripts/regression_check_indices.py. (path: runtime/scripts/regression_check_run_outputs.py, lines: 1-5; path: runtime/scripts/regression_check_indices.py, lines: 1-9)
- Reports: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md; runtime/audit/index_regression_report_latest.md. (path: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md, lines: 1-6; path: runtime/audit/index_regression_report_latest.md, lines: 1-6)
- Scope: outputs/ + eval; indices vs snapshot_pre; generated_at ignored. (path: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md, lines: 18-20; path: runtime/audit/index_regression_report_latest.md, lines: 5-14)

As-built (2026-01-14) — run comparison view:
- UI route + component: `/compare/runs/:baselineId/:candidateId`, `runtime/ui/src/components/RunComparisonView.tsx`. (path: runtime/ui/src/App.tsx, lines: 30-37; path: runtime/ui/src/components/RunComparisonView.tsx, lines: 1-90)
- API endpoints + UI client: `/run-regression/{baseline_id}/{candidate_id}`, `/run-regression/diff`, `getRunRegressionReport`, `getRunRegressionDiff`. (path: runtime/api_server.py, lines: 278-340; path: runtime/ui/src/api.ts, lines: 82-105)

As-built (2026-01-14) — coverage dashboard + review queue:
- Coverage dashboard uses GET /page-sources-coverage and renders page_sources_coverage_index.json aggregates with explicit chapter/excerpt limitations. (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 49-51, 132-145; path: runtime/api_server.py, lines: 233-271)
- Review Queue view exists at /review-queue with kind+severity filters and Next/Prev navigation via query params. (path: runtime/ui/src/App.tsx, lines: 31-33; path: runtime/ui/src/components/Inbox.tsx, lines: 82-172; path: runtime/ui/src/components/ReviewPackViewer.tsx, lines: 14-140; path: runtime/ui/src/components/RunDetail.tsx, lines: 14-135)

## Documentation layout (high-level)

| path | purpose |
|---|---|
| `documentation/system_overview/` | system state, registries, layer facts |
| `documentation/operator/` | runbooks and operator guidance (contracts included) |
| `documentation/reports/` | planning/backlog reports |
| `documentation/reading_paths/` | prompt packs and reading paths |
| `documentation/architecture_sources/` | architecture source materials |
| `documentation/legacy_imports/` | staged legacy project meta |

## Notable exclusions

- No `architecture/` directory in this repo.
- Legacy sources are staged under `documentation/legacy_imports/` and `runtime/data/source_imports/`.
