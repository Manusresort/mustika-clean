# Implementation Backlog (Book Translation System)

## 0) Current baseline (AS-IS, cited)

- **Runtime entrypoints**: `cd runtime && ./scripts/dev_up.sh` starts API, indexer, UI; QA smoke via `./scripts/qa_full_system.sh` (DEV_WORKFLOW.md:22-48; QA script: overview lines 1-232).  
- **Artefacts**: `runs/<excerpt>/<RUN_...>` plus `outputs/`, `manifest.json`, `logs/` (ADR-001-run-bundle-layout.md:1-24; runner.py:72-327) feed `proposals/`, `closures/`, and derived `indices/*.json` (indexer.py:33-545; GOVERNANCE.md:78-82).  
- **Endpoints**: `/health`, `/inbox`, `/runs/{run_id}`, `/proposals/{proposal_id}`, `POST /closures` already serve governs/closure data; `POST /reindex` regenerates indices (api_server.py:171-762).  

## 1) Phase 1 — Stabilize (contract & enforcement hardening)

### 1.1 API↔UI schema unification (NEW)
- **Problem**: UI expects `InboxResponse.counts` even though API returns only `generated_at` + `items`, creating contract drift (BOOK_MANIFEST_SPEC.md:50; UI/api.ts:17-41).  
- **Tasks**: align API response to include `counts`, update UI client to consume canonical shape, add regression in QA suite for `/inbox`.  
- **DoD**: `/inbox` now emits `{ generated_at, counts, items }` with counts derived server-side from `indices` before responding, UI fetch continues to succeed, and the QA `GET_/inbox_counts` touchpoint verifies the totals match the listed items (`runtime/api_server.py:314-360`; `runtime/scripts/qa_full_system.sh:124-149`).  
- **Risks**: inconsistent reruns if counts logic differs between API and UI.

### 1.2 Inbox index normalization + contract tests (NEW)
- **Problem**: inbox logic relies on derived indices; need automated guard to ensure inbox structure follows deterministic rules (GOVERNANCE.md:17-47; indexer.py:396-545).  
- **Tasks**: enhance QA script (`qa_full_system.sh` lines 83-214) to validate inbox items vs rule list and track discrepancies.  
- **DoD**: QA summary includes PASS for `index_inbox` rule checks, `indices/inbox_index.json` not hand-edited.  
- **Risks**: flaky indexes if run metadata changes unexpectedly.

### 1.3 Governance enforcement extension (NEW)
- **Problem**: governance enforcement is documentary, only canonical write and closure immutability exist (ADR-002-governance-layer-enforcement.md:1-26; api_server.py:706-762).  
- **Tasks**: add runtime checks (e.g., `POST /closures` verifying `required_closure.json` presence) recorded via audit log `audit/api_actions.log` (api_server.py:143-156).  
- **DoD**: new guard logs appear when `POST /closures` runs from QA suite; failure cases blocked.  
- **Risks**: operations team must update audit documentation.

### 1.4 QA suite as CI-grade regressions (NEW)
- **Problem**: QA script is manual; need deterministic coverage of API/indexer/UI per `DEV_WORKFLOW` instructions (QA script lines 1-232).  
- **Tasks**: wrap `qa_full_system.sh` as CI job, capture `summary.tsv`, normalized output, and ensure reindex + closure create runs pass consistently.  
- **DoD**: nightly CI executes script, summary/normalized files exist under `audit/qa/latest_full`, and `book` manifest triggers recorded there.  
- **Risks**: virtualization/timeouts hitting `uvicorn`.

### 1.5 RunnerV2 CLI re-entry (NEW)
- **Problem**: Runner script is documented but not part of stabilized pipeline (BOOK_TRANSLATION_SYSTEM_SPEC.md:21-39).  
- **Tasks**: NEW: introduce `scripts/mustika_run_excerpt.py` entrypoint, document required environ/per excerpt metadata per `ADR-001`.  
- **DoD**: `scripts/mustika_run_excerpt.py` exists, and CLI runs write `manifest.json`, `outputs/`, `logs/`; new entry recorded in `audit/api_actions.log`.  
- **Risks**: missing `.venv`.

### 1.6 Audit log structure (NEW)
- **Problem**: Book-level changes need traceable audit records; API already writes to `audit/api_actions.log` but backlog lacks summary (api_server.py:143-156).  
- **Tasks**: define log schema for reindex/closure/book manifest events, surface in `BOOK_TRANSLATION_SYSTEM_SPEC.md`.  
- **DoD**: `audit/api_actions.log` contains entries for each reindex/book manifest generation, verifiable via QA run logs.  
- **Risks**: log rotation missing.

## 2) Phase 2 — Editorialize (chapter workflow)

### 2.1 Indexer: generate `chapter_manifest.json` (NEW)
-- **Problem**: CHAPTER_MANIFEST_SPEC notes no runtime manifest yet (CHAPTER_MANIFEST_SPEC.md:5-50).  
- **Tasks**: extend indexer to read runs/proposals/closures, emit `runtime/manifests/chapter_manifest.json`, and update indices. NEW decision: prefer single file vs per-chapter files.  
- **DoD**: `runtime/manifests/chapter_manifest.json` exists (descriptor tracked via `.gitkeep`), indexer run writes the derived manifest with `generated_at`, and QA guard confirms the file and `generated_at` (see `reports/audit/evidence/session_20260123-1510/qa/summary.tsv`).  
- **Risks**: manifest growth/performance.  

### 2.2 Chapter registry + chapter-level indices (NEW)
- **Problem**: no aggregated chapter registry currently exists (NOT FOUND in spec discovery).  
- **Tasks**: build chapter registry index referencing summaries per chapter, store under `indices/chapter_registry.json`.  
- **DoD**: indexer run produces registry file with chapter metadata, QA script validates contents.  
- **Risks**: syncing with book manifest.

### 2.3 UI: chapter filters in inbox/review queue (NEW)
- **Problem**: UI currently only offers run/proposal views (App.tsx routes, ui/api.ts).  
- **Tasks**: add chapter filter controls referencing new chapter registry, update inbox endpoints to expose chapter_id in items.  
- **DoD**: UI filters show chapter names, `inbox` items include chapter_id field verified by QA.  
- **Risks**: proxy adjustments.

### 2.4 Chapter closure rollup logic (NEW)
- **Problem**: book manifest requires radiating status from chapter closures to book approvals (BOOK_MANIFEST_SPEC.md:40-76).  
- **Tasks**: create chapter closure rollup service that flags book-level `required_closure` when all chapters approved.  
- **DoD**: book manifest `required_closures` list populated with closure IDs once each chapter closure exists; `book_manifest.status` transitions accordingly.  
- **Risks**: partial chapter completion.

### 2.5 Glossary lifecycle integration gates (NEW)
- **Problem**: Glossary decisions currently documented but not tied to manifests (BOOK_TRANSLATION_SYSTEM_SPEC.md:28-39).  
- **Tasks**: tie `glossary_decision.md` to `closures`, include evidence paths in `chapter_manifest` entries.  
- **DoD**: each chapter manifest entry references `glossary` closure evidence, and book manifest provenance includes these files.  
- **Risks**: inconsistent evidence.

### 2.6 Review pack bundling per chapter (NEW)
- **Problem**: review packs may not align with chapter boundaries (BOOK_MANIFEST_SPEC.md:50).  
- **Tasks**: produce chapter-sized `proposals/<id>/review_pack/` bundles linking to runs and closures, surface in `book_manifest.provenance`.  
- **DoD**: file bundles exist and API returns `review_pack_files` entries; QA verifies existence via `/proposals/{id}`.  
- **Risks**: manual pack maintenance.

## 3) Phase 3 — Book-ready (exports & book closure)

### 3.1 Indexer: generate `book_manifest.json` (NEW)
- **Problem**: book manifest is yet to be derived (NOT FOUND).  
- **Tasks**: aggregate chapter manifests/closures, write `runtime/manifests/book_manifest.json`, reference exports.  
- **DoD**: file includes `chapters`, `required_closures`, `exports`, `provenance`; QA reindex run regenerates it.  
- **Risks**: data drift if chapters change mid-export.

### 3.2 Build manifest generator (NEW)
- **Problem**: exports need per-build verification (BOOK_MANIFEST_SPEC.md:59-76).  
- **Tasks**: add script creating `runtime/exports/<book_id>/<build_id>/build_manifest.json` listing checksums/tool_versions/input closures.  
- **DoD**: build manifest exists per export in exports directory and referenced by `book_manifest.exports`.  
- **Risks**: tool version mismatch.

### 3.3 Exporter skeleton (NEW)
- **Problem**: no export tooling yet, only documentation.  
- **Tasks**: create placeholder `runtime/scripts/book_export.sh` that packages assets into `runtime/exports/` directories, invokes `build_manifest`.  
- **DoD**: script runs locally, produces exports folder, and NEW: extend `qa_full_system.sh` to optionally call `book_export.sh` as a release check while remaining optional (QA should not fail if exporter is missing).  
- **Risks**: environment dependencies.

### 3.4 Book closure object (NEW)
- **Problem**: There’s no book-level closure despite closure model for excerpt/proposal (api_server.py:692-762).  
- **Tasks**: define book closure structure referencing required closures; enforce via `book_manifest.status`.  
- **DoD**: new closure record stored under `closures/BOOK-...`, `book_manifest` status updates to `locked/exported`.  
- **Risks**: duplicate closure IDs.

### 3.5 Deterministic exports + checksums (NEW)
- **Problem**: deterministic-ish requirement (BOOK_MANIFEST_SPEC.md:69).  
- **Tasks**: ensure export script records SHA256, tool versions, and uses `build_manifest` data to detect drift.  
- **DoD**: QA script verifies export artifacts’ checksums against `build_manifest`.  
- **Risks**: checksum mismatch on regenerations.

### 3.6 Release packaging / handoff procedure (NEW)
- **Problem**: final publication process lacks documented workflow.  
- **Tasks**: codify steps (chapter approval, build manifest, exports, book manifest) in `BOOK_MANIFEST_SPEC.md` addition and in a runbook.  
- **DoD**: new document under `documentation/system_overview/` describing handoff, referencing actual files for verification.  
- **Risks**: incomplete hand-offs.

## 4) Acceptance checklist (global)

- [ ] `runtime/manifests/chapter_manifest.json` present and derived from `runs/` + proposals + closures (indexer output).  
- [ ] `/inbox`, `/runs/{id}`, `/proposals/{id}` continue to behave while new manifest files exist (QA hits via `qa_full_system.sh`).  
- [ ] `book_manifest.json` reflects `required_closures` and `exports` with checksums (derived file).  
- [ ] All new automation runs are recorded in `audit/api_actions.log` (API ensure_audit_log helper).  
- [ ] Build manifests exist alongside exports and match `book_manifest.exports` (filesystem check).  
- [ ] Closure records remain immutable; new book closure adds only new directories (GOvernance immutability evidence).

## Evidence index

- `mustika-rasa-clean/documentation/system_overview/BOOK_TRANSLATION_SYSTEM_SPEC.md`: defines book manifest concepts and exporter metadata.  
- `mustika-rasa-clean/documentation/system_overview/CHAPTER_MANIFEST_SPEC.md`: chapter manifest discovery/vision.  
- `mustika-rasa-clean/documentation/system_overview/GOVERNANCE.md`: derived-only policy, human gate semantics.  
- `mustika-rasa-clean/documentation/system_overview/DEV_WORKFLOW.md`: dev/QA entrypoints.  
- `docs/adrs/ADR-001-run-bundle-layout.md`: runtime run layout.  
- `docs/adrs/ADR-002-governance-layer-enforcement.md`: governance enforcement limits.  
- `mustika-rasa-clean/runtime/scripts/qa_full_system.sh`: canonical QA workflow.  
- `mustika-rasa-clean/runtime/api_server.py`: API endpoints, `ensure_audit_log`, closure/reindex handling.  
- `mustika-rasa-clean/runtime/indexer.py`: derived indexes, `_write_index_json_if_changed`.
