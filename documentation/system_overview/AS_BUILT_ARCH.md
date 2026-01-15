# AS-BUILT Architecture (Filesystem-First) — 2026-01-13

## 1. Scope
- This is a filesystem-first snapshot of what exists on disk and in code today.
- It does not describe intended design, future states, or roadmap.
- It is evidence-based and limited to as-built artifacts and documented invariants.

## 2. Core invariants (as documented)
- Filesystem-first; indices are derived outputs (documentation/system_overview/PROJECT_STATE_PACK.md, documentation/system_overview/REPO_INVENTORY.md).
- Runs and closures are immutable; canonical is read-only; no auto-promotion (documentation/system_overview/GOVERNANCE.md).
- page_sources is read-only for agents (documentation/operator/AGENT_USAGE_CONTRACT_PAGE_SOURCES.md).

## 3. Data layers (on disk)
- Page sources (read-only): runtime/data/ingest/page_sources/ with png/, ocr_txt/, ocr_tsv/ and PROVENANCE.json.
- Page OCR corrected (prepared): runtime/data/ingest/page_ocr_corrected/pages/ and manifests/ (structure present). [Out of scope for M1 (M2+)]
- Definitive source (prepared): runtime/data/ingest/definitive_source/builds/ and manifests/ (structure present). [Out of scope for M1 (M2+)]
- Legacy chapter ingest (presence only): runtime/data/ingest/chapters/hoofdstuk_01/, hoofdstuk_02/. [Resolved for M1 (administrative)]
- ADDED: Editorial Phase Mapping (MVP) — documentary only:
-   - Input: ingest/page_sources + excerpt metadata that capture read-only source pages and provenance before any run.
-   - Proposal: runtime/runs/<excerpt>/<RUN_*> plus runtime/proposals/<proposal_id>/review_pack/ artefacts and derived indices.
-   - Decision: runtime/closures/<closure_id>/closure.json, runtime/closures/required_closure.json, and inbox signals (review_required/closure_needed) that make review outcomes visible.
-   - Canonical-eligible: canonical/ remains read-only and governed outside this MVP; this mapping does not enact promotion.

## 4. Runtime artefact families
- Runs: runtime/runs/<excerpt_id>/<RUN_*>/ with manifest.json, logs/, outputs/, eval/ (as observed in SYSTEM_WIDE_AUDIT_2026-01-13.md).
- Proposals: runtime/proposals/<proposal_id>/ with status.json and required_closure.json; optional review_pack/.
- Closures: runtime/closures/<closure_id>/ with closure.json.
- Editorial review workflow (M3) is complete with proposals/closures and review packs.

## 5. Indices (derived outputs)
- runtime/indices/run_index.json — keys: generated_at, runs
- runtime/indices/proposal_index.json — keys: generated_at, proposals
- runtime/indices/closure_index.json — keys: generated_at, closures
- runtime/indices/inbox_index.json — keys: generated_at, items
- runtime/indices/review_queue_index.json — keys: generated_at, items
- runtime/indices/page_sources_coverage_index.json — keys: generated_at, base_path, page_sources_path, identity_rule, counts, gaps

## 6. Orchestration & entrypoints (as-built)
- runtime/scripts/mustika_run_excerpt.py — Conceptually mismatched input requirement (afgeleid ≠ bron); script only, not M2 core.
- runtime/scripts/batch_run_chapter.py — Conceptually mismatched input requirement (afgeleid ≠ bron); script only, not M2 core.
- runtime/scripts/generate_review_pack.py — RUNNABLE (proposal + indices present).
- runtime/scripts/validate_excerpt_coverage.py — RUNNABLE (doc-based inputs).
- runtime/scripts/reindex_runtime.sh — RUNNABLE (indexer wrapper).

## 7. Escalation & triage (as-built)
- Inbox and review_queue indices exist (runtime/indices/inbox_index.json, review_queue_index.json).
- Prompt-level escalation rules exist (runtime/prompts/; documented in GOVERNANCE.md and state pack).
- Triage signals are run/proposal-based (no page-level triage artefact recorded).

## 8. Evidence pointers
- documentation/system_overview/PROJECT_STATE_PACK.md
- documentation/system_overview/STATE_EVIDENCE_MAP.md
- documentation/system_overview/REPO_INVENTORY.md
- documentation/system_overview/SYSTEM_WIDE_AUDIT_2026-01-13.md
- documentation/system_overview/ARCHITECTURE_CONSISTENCY_CHECK_2026-01-13.md
- documentation/operator/AGENT_USAGE_CONTRACT_PAGE_SOURCES.md
- documentation/operator/VALIDATOR_CONTRACT_PAGE_BASED_OUTPUTS.md
- documentation/operator/OCR_CORRECTION_CONTRACT.md
- documentation/operator/DEFINITIVE_SOURCE_BUILD_CONTRACT.md

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
  - documentation/operator/RUNBOOK.md (reindex section)
- Verification evidence:
  - runtime/audit/index_regression_report_latest.md
  - runtime/audit/index_snapshot_pre/
  - runtime/audit/api_actions.log

As-built (2026-01-14):
- Scripts present: runtime/scripts/regression_check_run_outputs.py; runtime/scripts/regression_check_indices.py. (path: runtime/scripts/regression_check_run_outputs.py, lines: 1-5; path: runtime/scripts/regression_check_indices.py, lines: 1-9)
- Run output report present: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md. (path: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md, lines: 1-6)
- Index report present: runtime/audit/index_regression_report_latest.md. (path: runtime/audit/index_regression_report_latest.md, lines: 1-6)
- Detail diffs directory present: runtime/audit/regression_runs/. (path: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md, lines: 32)
- Run output scope observed: outputs/ and eval/. (path: runtime/audit/run_regression_does_not_exist_a_vs_does_not_exist_b.md, lines: 18-20)
- Index scope observed: runtime/indices vs runtime/audit/index_snapshot_pre; generated_at ignored. (path: runtime/audit/index_regression_report_latest.md, lines: 5-14)
- Output-dir guard message: "ERROR: output-dir must be under" (path: runtime/scripts/regression_check_run_outputs.py, lines: 163-172)
- Writes constrained to runtime/audit; canonical remains read-only. (path: runtime/scripts/regression_check_run_outputs.py, lines: 163-178; path: documentation/system_overview/GOVERNANCE.md, lines: 10-13, 44-46)
- Run comparison view (UI) route and component present. (path: runtime/ui/src/App.tsx, lines: 30-37; path: runtime/ui/src/components/RunComparisonView.tsx, lines: 1-90)
- Run regression report/diff API endpoints present. (path: runtime/api_server.py, lines: 278-340)
- UI API client exposes report/diff functions. (path: runtime/ui/src/api.ts, lines: 82-105)

As-built (2026-01-14) — Milestone 4 UI:
- Coverage dashboard uses GET /page-sources-coverage (read-only) and renders page_sources_coverage_index.json aggregates; excerpt-level breakdown is explicitly not available. (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 49-51, 132-145; path: runtime/api_server.py, lines: 233-271)
- Chapter coverage limitation label is explicit. (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 135-137)
- Coverage view uses read-only formatting (pre/sections) for counts/gaps. (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 138-145)
- Review Queue view is routed at /review-queue and reuses Inbox with review-queue mode and label. (path: runtime/ui/src/App.tsx, lines: 31-33; path: runtime/ui/src/components/Inbox.tsx, lines: 13-109)
- Review Queue supports kind+severity filters and Next/Prev navigation using query params. (path: runtime/ui/src/components/Inbox.tsx, lines: 82-172, 202-206; path: runtime/ui/src/components/ReviewPackViewer.tsx, lines: 14-140; path: runtime/ui/src/components/RunDetail.tsx, lines: 14-135)
