# System-Wide Audit — 2026-01-13

## 1. Scope & method (read-only)
Read-only inspection of filesystem, documentation, and code. No execution of runs or reindex.

## 2. Snapshot: repo structure (high level)
- `runtime/` (present): `scripts/`, `src/`, `indices/`, `runs/`, `proposals/`, `closures/`, `prompts/`, `data/`
- `documentation/` (present): `system_overview/`, `operator/`, `reports/`, `reading_paths/`, `architecture_sources/`, `legacy_imports/`
- `historical/` (present)
- `experiments/` (present)

Evidence: `ls -la` at repo root shows these directories.

## 3. Data layers (ingest/derived): EXISTS / PREPARED / MISSING

### Page sources (EXISTS)
- `runtime/data/ingest/page_sources/` contains `png/`, `ocr_txt/`, `ocr_tsv/` and `PROVENANCE.json`.
- Counts (read-only): 1214 files in each of `png/`, `ocr_txt/`, `ocr_tsv/`.

Evidence:
- `ls -la runtime/data/ingest/page_sources/`
- `find runtime/data/ingest/page_sources/png -type f | wc -l`
- `find runtime/data/ingest/page_sources/ocr_txt -type f | wc -l`
- `find runtime/data/ingest/page_sources/ocr_tsv -type f | wc -l`

### Page OCR corrected (PREPARED)
- Structure exists: `runtime/data/ingest/page_ocr_corrected/pages/`, `runtime/data/ingest/page_ocr_corrected/manifests/`.
- No corrected page outputs observed; only structure/README present.

Evidence: `ls -la runtime/data/ingest/page_ocr_corrected/`

### Definitive source (PREPARED)
- Structure exists: `runtime/data/ingest/definitive_source/builds/`, `runtime/data/ingest/definitive_source/manifests/`.
- No builds/manifests observed; only structure/README present.

Evidence: `ls -la runtime/data/ingest/definitive_source/`

### Legacy chapter ingest (EXISTS, legacy staging)
- `runtime/data/ingest/chapters/hoofdstuk_01/`, `runtime/data/ingest/chapters/hoofdstuk_02/` present.

Evidence: `ls -la runtime/data/ingest/chapters/`

## 4. Runtime artefact families (runs/proposals/closures): schemas + counts

### Runs
- Count: 3 run bundles under `runtime/runs/`.
- Layout (example): `runtime/runs/sayur_052_066/RUN_sayur_052_066_20260109T202745/`.
- Manifest schema keys (example): `excerpt_id`, `excerpt_source`, `excerpt_version`, `run_id`, `created_at`, `inputs`, `output_files`.

Evidence:
- `find runtime/runs -mindepth 2 -maxdepth 2 -type d -name "RUN_*" | wc -l`
- `runtime/runs/sayur_052_066/RUN_sayur_052_066_20260109T202745/manifest.json`

### Proposals
- Count: 1 proposal directory (`runtime/proposals/P-001/`).
- Status schema keys (example): `status`, `closed_at`, `closure_id`, `proposal_id`, `type`, `severity`, `created_at`, `required_action`, `linked_run_ids`.
- required_closure schema keys (example): `required`, `types`.

Evidence:
- `find runtime/proposals -mindepth 1 -maxdepth 1 -type d | wc -l`
- `runtime/proposals/P-001/status.json`
- `runtime/proposals/P-001/required_closure.json`

### Closures
- Count: 1 closure directory (`runtime/closures/CL-20260109-P-001/`).
- Closure schema keys (example): `closure_id`, `created_at`, `created_by`, `proposal_id`, `source_run_id`, `decision_type`, `rationale`, `evidence_paths`, `sign_off`.

Evidence:
- `find runtime/closures -mindepth 1 -maxdepth 1 -type d | wc -l`
- `runtime/closures/CL-20260109-P-001/closure.json`

## 5. Indices overview (file list + keys + item counts)

Indices present in `runtime/indices/`:
- `run_index.json` — keys: `generated_at`, `runs` (runs_count: 3)
- `proposal_index.json` — keys: `generated_at`, `proposals` (proposals_count: 1)
- `closure_index.json` — keys: `generated_at`, `closures` (closures_count: 1)
- `inbox_index.json` — keys: `generated_at`, `items` (items_count: 1)
- `review_queue_index.json` — keys: `generated_at`, `items` (items_count: 0)
- `page_sources_coverage_index.json` — keys: `generated_at`, `base_path`, `page_sources_path`, `identity_rule`, `counts`, `gaps`

Evidence: python inspection of `runtime/indices/*.json` (keys + items_count).

## 6. Entrypoints overview (per script: required args + runnable classification)

### `runtime/scripts/mustika_run_excerpt.py`
- Required args: `--excerpt-id`, `--excerpt-source`, `--excerpt-version`, `--english`, `--rough-nl`.
- Required inputs: English and rough NL files must exist.
- Classification: **BLOCKED-BY-INPUT** (no english files found under `runtime/data/`; only `runtime/data/hoofdstuk1_rough_nl_dummy.txt` exists).

Evidence:
- `runtime/scripts/mustika_run_excerpt.py` (argparse required=True)
- `find runtime/data -type f -iname "*english*" -o -iname "*rough*nl*"` (only rough_nl dummy found)

### `runtime/scripts/batch_run_chapter.py`
- Required args: `--chapter-id`; optional `--english`, `--rough-nl`, `--dry-run`, `--run-id-prefix`.
- Execution requires `--english` and `--rough-nl`; script marks missing inputs as SKIPPED.
- Classification: **BLOCKED-BY-INPUT** (english inputs not present).

Evidence:
- `runtime/scripts/batch_run_chapter.py` (argparse + SKIPPED on missing inputs)

### `runtime/scripts/generate_review_pack.py`
- Required args: `proposal_id` (positional).
- Reads proposal status/links and run index; writes review_pack under proposal.
- Classification: **RUNNABLE** (proposal `P-001` exists + indices present).

Evidence:
- `runtime/scripts/generate_review_pack.py` (argparse)
- `runtime/proposals/P-001/`
- `runtime/indices/run_index.json`

### `runtime/scripts/validate_excerpt_coverage.py`
- No CLI args; reads EXCERPT_REGISTRY and alignment files; writes report under `runtime/audit/`.
- Classification: **RUNNABLE** (docs present; writes audit report).

Evidence:
- `runtime/scripts/validate_excerpt_coverage.py`

### `runtime/scripts/reindex_runtime.sh`
- Wrapper to run indexer with `--base-path runtime`.
- Classification: **RUNNABLE** (requires python runtime environment).

Evidence:
- `runtime/scripts/reindex_runtime.sh`

### `runtime/scripts/dev_start_api.sh` / `dev_start_ui.sh`
- Start API/UI processes.
- Classification: **UNKNOWN** (environment-dependent: venv/node required).

Evidence:
- `runtime/scripts/dev_start_api.sh`, `runtime/scripts/dev_start_ui.sh`
- `documentation/operator/RUNBOOK.md` (notes about venv/node)

## 7. Contracts & governance coverage (what exists; missing references)

### Operator contracts present
- `documentation/operator/AGENT_USAGE_CONTRACT_PAGE_SOURCES.md`
- `documentation/operator/VALIDATOR_CONTRACT_PAGE_BASED_OUTPUTS.md`
- `documentation/operator/OCR_CORRECTION_CONTRACT.md`
- `documentation/operator/DEFINITIVE_SOURCE_BUILD_CONTRACT.md`

### Referenced paths in contracts
- `runtime/data/ingest/page_sources/png/`, `ocr_txt/`, `ocr_tsv/` exist.
- `runtime/data/ingest/page_ocr_corrected/pages/`, `manifests/` exist.
- `runtime/data/ingest/definitive_source/builds/`, `manifests/` exist.

Evidence: `ls -la` on paths and contract files.

## 8. Cross-doc consistency findings

Observed consistency:
- `PROJECT_STATE_PACK.md`, `REPO_INVENTORY.md`, and `STATE_EVIDENCE_MAP.md` all reference
  `runtime/data/ingest/page_sources/` and `runtime/indices/page_sources_coverage_index.json`.

Potential mismatch noted elsewhere:
- `STATE_EVIDENCE_MAP.md` gap entry still states “Excerpt registry is only partially populated”
  while `EXCERPT_ALIGNMENT_INDEX.md` claims full chapter coverage (not in scope for this audit).

Evidence: `documentation/system_overview/STATE_EVIDENCE_MAP.md`.

## 9. Fact-first conclusion (system position on MVP → full system scale)
- Page-based ingest is present and complete (PNG/TXT/TSV + provenance).
- Coverage index exists and reports no gaps for page_sources.
- Corrected-page and definitive-source layers exist as empty structures.
- Runs, proposals, and closures exist with concrete JSON schemas.
- Indices are present for runs/proposals/closures/inbox/review_queue/coverage.
- Entrypoints exist; run execution is blocked by missing english inputs.
- Review pack generation is runnable for existing proposal IDs.
- Governance invariants are documented and no code writes to canonical were found.

## 10. Evidence index (paths referenced)
- `runtime/data/ingest/page_sources/`
- `runtime/data/ingest/page_ocr_corrected/`
- `runtime/data/ingest/definitive_source/`
- `runtime/data/ingest/chapters/`
- `runtime/runs/`
- `runtime/proposals/`
- `runtime/closures/`
- `runtime/indices/`
- `runtime/scripts/mustika_run_excerpt.py`
- `runtime/scripts/batch_run_chapter.py`
- `runtime/scripts/generate_review_pack.py`
- `runtime/scripts/validate_excerpt_coverage.py`
- `runtime/scripts/reindex_runtime.sh`
- `runtime/api_server.py`
- `runtime/indexer.py`
- `documentation/system_overview/PROJECT_STATE_PACK.md`
- `documentation/system_overview/REPO_INVENTORY.md`
- `documentation/system_overview/STATE_EVIDENCE_MAP.md`
- `documentation/operator/*.md`
