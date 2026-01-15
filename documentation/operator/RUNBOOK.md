# Operator Runbook (Mustika Rasa MVP)

## Start system (API + UI)

1) Start API:
- `runtime/scripts/dev_start_api.sh`

2) Start UI:
- `runtime/scripts/dev_start_ui.sh`

Notes:
- If `runtime/.venv` exists, activate it before running scripts.
- Use `python3` if `python` is not available.

## Run a new excerpt job (Runner v2)

Template command:

```bash
python3 runtime/scripts/mustika_run_excerpt.py \
  --excerpt-id <excerpt_id> \
  --excerpt-source <path_to_source_text> \
  --excerpt-version <version_tag> \
  --english <path_to_english> \
  --rough-nl <path_to_rough_nl>
```

Outputs will land in:
- `runtime/runs/<excerpt_id>/<RUN_id>/`

## Reindex

CLI reindex (filesystem → indices):
- `runtime/scripts/reindex_runtime.sh`
- `python3 runtime/indexer.py --base-path runtime`
Generates:
- `runtime/indices/page_sources_coverage_index.json`

API reindex (if API is running):
- `POST /reindex`

## Excerpt coverage validation

Purpose:
- Checks registry entries against alignment entries and reports run coverage per excerpt.

Command:
- `python3 runtime/scripts/validate_excerpt_coverage.py`

Preconditions:
- `documentation/system_overview/EXCERPT_REGISTRY.md` exists.
- `documentation/system_overview/EXCERPT_ALIGNMENT_INDEX.md` exists.
- `runtime/runs/` contains run bundles.

Output:
- `runtime/audit/coverage_report_latest.md` (derived; can be regenerated).

Interpreting results:
- `check_a_alignment_to_registry`: PASS if all aligned excerpt_ids exist in the registry.
- `check_b_registry_duplicates`: PASS if no duplicate excerpt_ids are found in the registry.
- `run_coverage_status`: value reported in `runtime/audit/coverage_report_latest.md` (see report section for details).

Non-goals:
- Does not create or modify runs.
- Does not write to canonical.
- Does not generate indices.

## Troubleshooting

- Port busy:
  - If UI does not start on the default port, it will try the next available.
  - Stop existing processes with `runtime/scripts/dev_down.sh`.

- `uvicorn` missing:
  - Ensure the runtime venv is active or install dependencies.
  - Use `python3 -m uvicorn` (scripts already do this).

- `python` vs `python3`:
  - Use `python3` explicitly to avoid PATH issues.

- Logs:
  - Run logs: `runtime/runs/*/logs/run.log`
  - API/UI logs: check `runtime/audit/` if present and script output streams.
ADDED: See `documentation/system_overview/PROJECT_STATE_PACK.md` (DoD — Run logging & reproducibility) for the definition of “reproducible” as audit- and comparison-ready, not deterministic reruns.

## Run output regression check

Command:
- `python3 runtime/scripts/regression_check_run_outputs.py <baseline_run_dir> <candidate_run_dir>`
- `python3 runtime/scripts/regression_check_indices.py`

Output:
- `runtime/audit/run_regression_<baseline_id>_vs_<candidate_id>.md`
- `runtime/audit/index_regression_report_latest.md`

As-built (2026-01-14):
- Run comparison view route: `/compare/runs/:baselineId/:candidateId`. (path: runtime/ui/src/App.tsx, lines: 30-37)
- UI component reads run regression report via API client. (path: runtime/ui/src/components/RunComparisonView.tsx, lines: 1-33; path: runtime/ui/src/api.ts, lines: 82-105)
- API endpoints (read-only) for report and diff:
  - `GET /run-regression/{baseline_id}/{candidate_id}`
  - `GET /run-regression/diff` (path: runtime/api_server.py, lines: 278-340)
- Coverage dashboard uses read-only page sources coverage endpoint: `GET /page-sources-coverage`. (path: runtime/api_server.py, lines: 233-271; path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 49-51)
- Coverage UI labels (chapter/ excerpt limitations): “Chapter coverage not available (no runtime chapter↔excerpt mapping)” and “Excerpt-level breakdown not available in this index (only aggregate coverage).” (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 132-137)

## Milestone 5 — Operational Reliability + Regression Checks

- Index regression audit artefact definition (expected path):
  - runtime/audit/index_regression_report_latest.md
  - Scope: semantic diff of runtime/indices/ vs runtime/audit/index_snapshot_pre/, ignoring generated_at.
- Run output regression audit artefact definition (expected path):
  - runtime/audit/run_regression_sayur_052_066_RUN_sayur_052_066_20260109T172343_vs_RUN_sayur_052_066_20260109T173327.md
  - Scope: compare outputs/ and eval/ between two runs; record if empty (informational).
- Pre-regression snapshot staging directory (observed on disk):
  - runtime/audit/index_snapshot_pre/
- Copy-only backup and restore workflow documented:
  - documentation/operator/BACKUP_AND_RESTORE_RUNTIME.md
