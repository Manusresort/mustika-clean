# Delivery Plan — Book Translation System

## 0) What this document is
- Doel: één bron voor fase- en batchstatus van het boekvertalingsysteem, zodat repo lezers precies weten waar implementatie staat (IMPLEMENTATION_BACKLOG.md; BOOK_TRANSLATION_SYSTEM_SPEC.md).
- Regel: koppel elke batch aan artefacts en QA gates, zodat status traceerbaar blijft zonder externe tooling (IMPLEMENTATION_BACKLOG.md; DEV_WORKFLOW.md).

- ## 1) Current phase marker
- CURRENT_PHASE: **Phase 2 — Editorialize**, with `PROJECT_STATUS.md` as the authoritative source.
- CURRENT_BATCH: **B2 — Chapter manifest derivation** (DONE; evidence: `reports/audit/evidence/session_20260123-1510/qa/summary.tsv`).
- LAST_COMPLETED: **B2 — Chapter manifest derivation + QA guard** (matrix recorded in `reports/audit/evidence/session_20260123-1510/qa/summary.tsv`).
- NEXT_BATCH: **B3 — Book manifest** (see `PROJECT_STATUS.md`).

## 2) Batch model
| Batch | Name | Goals | Deliverables | Entry points | QA gates | DoD | Risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B0 | Baseline discovery | Verkrijg inzicht in canonical artefacts, governance en runtime entrypoints. | Documentatie in IMPLEMENTATION_BACKLOG en GOVERNANCE die de huidige state beschrijven. | `DEV_WORKFLOW.md` commands (`dev_up`, `qa_full_system`) en API endpoints. | QA smoke run + validation dat `indices/*.json` bestaan (qa script checks rest). | Base line is recorded in docs (see `IMPLEMENTATION_BACKLOG.md` and `GOVERNANCE.md`). | Geen artifacts; geen blockers. |
| B1 | Contract discipline + QA guards | Maak API-UI contract consistent en voeg QA guard toe. | `ADR-003` plus updated `api_server.py`, `ui/src/api.ts`, `qa_full_system.sh`. | GET `/inbox`, QA script. | `qa_full_system.sh` includes `GET_/inbox_counts`. | `/inbox` returns counts and QA ensures totals match items (ADR-003 and QA guard). | Inconsistent counts derivation, QA failure. |
| B2 (NEW) | Chapter manifest derivation | Indexer emits `runtime/manifests/chapter_manifest.json` referencing runs/proposals/closures. | Chapter manifest spec + indexer updates. | `POST /reindex`, `indexer.py`. | Reindex run, `indices/run_index.json` validation, and QA guard (chapter_manifest exists + generated_at) documented in `reports/audit/evidence/session_20260123-1510/qa/summary.tsv`. | `runtime/manifests/chapter_manifest.json` exists and is derived-only (see `CHAPTER_MANIFEST_SPEC.md`). | Manifest growth/performance. |
| B3 (NEW) | Chapter registry & UI filters | Surface chapters in UI/inbox via chapter registry. | `indices/chapter_registry.json`, UI filters. | `/inbox` + UI components consuming `chapter_id`. | QA ensures inbox items contain `chapter_id`. | UI filters show chapter names, registry validated (see `IMPLEMENTATION_BACKLOG.md`). | Proxy/UI mismatch. |
| B4 (NEW) | Chapter closure rollups | Tighten book-level gating by aggregating chapter closures. | Rollup service referencing `closures/<id>`. | `POST /closures`, indexer. | Closure creation + reindex ensures book manifest `required_closures`. | Book manifest (once created) lists closure IDs when all chapter closures exist (see `BOOK_MANIFEST_SPEC.md`). | Partial chapter completion bugs. |
| B5 (NEW) | Glossary lifecycle gates | Link glossary decisions to closures evidence. | `glossary` references in chapter manifest entries and `book_manifest.provenance`. | Closure creation, proposal metadata reads. | QA ensures glossary evidence paths recorded. | Each chapter entry references glossary evidence (see `BOOK_TRANSLATION_SYSTEM_SPEC.md`). | Evidence drift. |
| B6 (NEW) | Review pack bundling | Bundle per-chapter review packs and surface them via API. | `proposals/<id>/review_pack/` manifest plus book manifest provenance. | `/proposals/{id}` + UI review view. | QA validates review_pack entries exist. | API returns `review_pack_files`, QA verifies (see `IMPLEMENTATION_BACKLOG.md`). | Manual pack maintenance. |
| B7 (NEW) | Book manifest generation | Aggregate chapter manifests, closures, exports. | `runtime/manifests/book_manifest.json`, `book_manifest.exports`. | `POST /reindex`, indexer. | Reindex run and audit log entries (api_server logging). | File contains chapters, required closures, exports, provenance (see `BOOK_MANIFEST_SPEC.md`). | Data drift when chapters change mid-export. |
| B8 (NEW) | Build manifest generator | Record export metadata (checksums, tools, closure inputs). | `runtime/exports/<book>/<build>/build_manifest.json`. | Export script (planned), QA verifying existence. | Build manifest referenced in `book_manifest.exports`. | Build manifest includes format, path, sha256, tool versions, closure IDs (see `BOOK_MANIFEST_SPEC.md`). | Tool-version mismatch. |
| B9 (NEW) | Exporter skeleton | Provide script packaging deterministic outputs. | `runtime/scripts/book_export.sh`, exports dir. | Export script, `qa_full_system.sh` optional release step. | QA optionally runs exporter (ensures not failing if missing). | Exporter writes runtime/exports and build manifest; QA optional call recorded (see `IMPLEMENTATION_BACKLOG.md`). | Env dependencies. |
| B10 (NEW) | Book closure object | Represent book-level decision via closures. | New `closures/BOOK-.../closure.json`, book manifest status gating. | `POST /closures`. | Closure creation + reindex. | Book manifest transitions to `locked/exported` when closure exists (see `BOOK_MANIFEST_SPEC.md` and `runtime/api_server.py`). | Duplicate closure IDs. |
| B11 (NEW) | Deterministic exports & checksums | Ensure reproducible outputs with digest logging. | Export tool records SHA256 + tool versions; QA compares to build manifest. | Export script + QA script. | Export artifacts pass checksum validation (see `BOOK_MANIFEST_SPEC.md` and QA script). | Checksum mismatch. |
| B12 (NEW) | Release packaging/handoff | Document final release steps and evidence. | Runbook referencing `book_manifest.json`, `project` docs. | Hand-off doc, QA summary. | Documentation under `documentation/system_overview/` describing handoff (see `IMPLEMENTATION_BACKLOG.md`). | Incomplete hand-offs. |

## 3) Progress dashboard (repo-native)
| Batch | Status | Evidence | Notes |
| --- | --- | --- | --- |
| B0 | DONE | Baseline captured in existing docs (`IMPLEMENTATION_BACKLOG.md`, `GOVERNANCE.md`). | Discovery complete. |
| B1 | DONE | Counts authority documented in ADR-003 and enforced by QA guard (`runtime/scripts/qa_full_system.sh`). | QA ensures `/inbox` totals match `items`. |
| B2 | DONE | `runtime/manifests/chapter_manifest.json` emitted and QA guard passes (see `reports/audit/evidence/session_20260123-1510/qa/summary.tsv`). | Indexer work completed for manifest derivation; QA guard and evidence recorded. |
| B3 | NOT_STARTED | No registry yet; concept described in backlog (`IMPLEMENTATION_BACKLOG.md`). | UI filters pending. |
| B4 | NOT_STARTED | Rollup logic defined but not implemented (`BOOK_MANIFEST_SPEC.md`). | Need closure aggregation. |
| B5 | NOT_STARTED | Glossary integration described in spec/backlog (`BOOK_TRANSLATION_SYSTEM_SPEC.md`, `IMPLEMENTATION_BACKLOG.md`). | Evidence paths missing. |
| B6 | NOT_STARTED | Review pack bundling concept exists in backlog (`IMPLEMENTATION_BACKLOG.md`). | Bundles missing. |
| B7 | NOT_STARTED | Book manifest spec describes required fields, no runtime file (`BOOK_MANIFEST_SPEC.md`). | File absent. |
| B8 | NOT_STARTED | Build manifest described but tools missing (`BOOK_MANIFEST_SPEC.md`). | Build manifest absent. |
| B9 | NOT_STARTED | Exporter skeleton planned in backlog (`IMPLEMENTATION_BACKLOG.md`). | Script not created. |
| B10 | NOT_STARTED | Book closure object defined in spec but not recorded (`BOOK_MANIFEST_SPEC.md`, `runtime/api_server.py`). | Closure catalog absent. |
| B11 | NOT_STARTED | Export determinism requirement outlined but not implemented (`BOOK_MANIFEST_SPEC.md`). | Checksums coverage absent. |
| B12 | NOT_STARTED | Release packaging definition is speculative (`IMPLEMENTATION_BACKLOG.md`). | Runbook pending. |

## 4) Operating rhythm (way of working)
+ Discovery → ADR/spec → implement → QA gate → closure/release note (BOOK_TRANSLATION_SYSTEM_SPEC.md; ADR-003-inbox-contract-counts-authority.md).
- No merge without QA + docs: `DEV_WORKFLOW.md` nominates `qa_full_system.sh` as canonical QA gate, and all tooling changes must be documented in `documentation/system_overview` (DEV_WORKFLOW.md).

## 5) Canonical entrypoints (AS-IS)
- `cd runtime && ./scripts/dev_up.sh` orchestrates API, reindex, UI startup (DEV_WORKFLOW.md; runtime/scripts/dev_up.sh).
- `runtime/scripts/dev_start_api.sh` starts UVicorn, populates audit logs, and verifies `/health` (runtime/scripts/dev_start_api.sh).
- `runtime/scripts/dev_start_ui.sh` launches Vite (runtime/scripts/dev_start_ui.sh).
- `runtime/scripts/qa_full_system.sh` exercises API/indexer/UI and closure/reindex flows, writing `audit/qa/latest_full/summary.tsv` (runtime/scripts/qa_full_system.sh).
- POST `/reindex` triggers `indexer.py`, logs outputs, and reports generated indices (runtime/api_server.py).

## 6) Governance checkpoints (AS-IS + NEW)
- AS-IS: human-in-the-loop, immutable closures, canonical/checkpoint rules, and derived indices as documented in `GOVERNANCE.md` (GOVERNANCE.md).
+ NEW: progress must be visible through `PROJECT_STATUS.md` so governance reviewers can verify current phase without additional tooling (PROJECT_STATUS.md).
