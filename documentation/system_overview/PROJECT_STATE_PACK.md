# Project State Pack (Mustika Rasa Clean Repo)

## What is working end-to-end today (evidence)
- Runner v2 has produced run bundles under `runtime/runs/` (see `sayur_052_066/` runs).
- Validator reports exist in `runtime/runs/*/eval/output_contract_checks.txt`.
- Indexer has generated indices under `runtime/indices/`.
- Review queue index is generated as a derived artefact under `runtime/indices/review_queue_index.json`.
- API and UI are present and wired to the filesystem-first indices and run bundles.
- Coverage dashboard renders page_sources_coverage_index.json via GET /page-sources-coverage (read-only); chapter/excerpt limitations are explicit in UI. (path: runtime/ui/src/components/CoverageDashboard.tsx, lines: 49-51, 132-137; path: runtime/api_server.py, lines: 233-271)
- Review Queue view exists at /review-queue with kind+severity filters and Next/Prev navigation via query params. (path: runtime/ui/src/App.tsx, lines: 31-33; path: runtime/ui/src/components/Inbox.tsx, lines: 82-172; path: runtime/ui/src/components/ReviewPackViewer.tsx, lines: 14-140; path: runtime/ui/src/components/RunDetail.tsx, lines: 14-135)
- Excerpt registry is complete for all chapters with stable IDs/versions; chapter→excerpt alignment is complete for listed chapters.
- Ingest artifacts with provenance exist for hoofdstuk_01 and hoofdstuk_02 under `runtime/data/ingest/chapters/`.
- Review packs exist as derived artefacts under `runtime/proposals/<proposal_id>/review_pack/` (exposed in proposal API response).
- Excerpt coverage validation is ACTIVE via `python3 runtime/scripts/validate_excerpt_coverage.py` and outputs `runtime/audit/coverage_report_latest.md`.
- Proposal/closure review artefacts are standardized and human-reviewable, with batch consistency validated across P-001..P-004.
- Milestone 2 (excerpt-level run orchestration) is DONE; per-chapter batch scripting is out of scope for M2.

This is an MVP system: it demonstrates a filesystem-first editorial lifecycle with
runs, proposals, closures, indices, an API, and a UI. It is not a full end-to-end
book translation pipeline.

 ### Current System State after M2
 
 - M1: DONE — bronversie gedefinieerd, provenance aanwezig, onzekerheden erkend.
 - M2: DONE — operator-triggered, immutable, excerpt-level run orchestration.
 - Per-chapter batch orchestration is out of scope for M2 and remains a blocked subroute for later milestones.
 
### MVP Editorial Phases (Explicit)
ADDED: MVP workflows trace the Input → Proposal → Decision chain without overlapping canonical/publication work—Input (excerpt-bound source ingest), Proposal (run outputs surfaced via review packs and `runtime/proposals/<id>/review_pack/`), Decision (closures recorded under `runtime/closures/<id>/closure.json` plus inbox signals such as `closure_needed`), and Canonical-eligible (kept outside this MVP, governed separately).
ADDED: Pre-MVP work (ingest, OCR correction) and post-MVP canonical/publication activity are explicitly outside this operational scope.
ADDED: Status update — Editorial phase handoffs (MVP): CLOSED. The MVP phase chain is explicitly documented as Input → Proposal → Decision (Closure), with Canonical-eligible explicitly out of scope. Signal/review queue, proposal, and closure semantics are clarified without changing governance or runtime invariants. Pre-MVP (ingest/OCR/correction) and post-MVP (canonical/publication) are explicitly positioned outside this system.

 Handoff note: M1 and M2 are proven at the artefact/workflow level (ingest + excerpt registry + excerpt-level runs); per-chapter batching is explicitly out of scope and remains blocked by chapter↔excerpt context; M3 starts at editorial review packs and proposal/closure lifecycle work.

 ### Milestone 3 — Editorial Review & Closure (DONE)
 
 M3: menselijke beoordeling en besluitvorming vastgelegd via review packs, proposals en closures; herleidbaar en immutable; geen publicatie.
 
ADDED: This milestone proves the Decision (Closure) phase: each closure records a decision artefact (`closure.json`) plus inbox visibility while remaining separate from canonical approval or publication.
ADDED: Closure completion therefore does not imply canonical status, which remains deferred to later governance work.

 ### Editorial Review — Current State

- Proposal and closure artefacts are standardized and batch-consistent (validated across P-001..P-004).
- Batch review capability is proven at artefact/workflow level (uniform structure, evidence navigation, human rationale placement).
- One full human-in-the-loop content review has been executed and recorded (P-002; see review_pack/review_note.md).
- No claims are made about large-scale content quality or multi-run variance; only review workflow and artefact suitability are validated.

**Resume point**:
- Next logical continuation is either:
  - performing additional real content reviews on existing proposals, or
  - generating new proposals from new runs to test review workflow under content diversity.
- No architectural changes are required to continue.

## Exact start/stop commands (API/UI)

Start API (recommended script):
- `runtime/scripts/dev_start_api.sh`

Start UI (recommended script):
- `runtime/scripts/dev_start_ui.sh`

Stop dev processes (ports 8000/5173/5174):
- `runtime/scripts/dev_down.sh`

Reindex (runtime root):
- `runtime/scripts/reindex_runtime.sh`
- `python3 runtime/indexer.py --base-path runtime`

Python note:
- If `runtime/.venv` exists, activate it before running scripts.
- Otherwise use `python3` for all commands and ensure dependencies are installed.

## Current invariants (non-negotiable)
- `runtime/canonical/` is read-only (no direct writes).
- Closures are immutable once created.
- No auto-promotion to canonical.
- Indices (`runtime/indices/*.json`) are derived artifacts; regenerate via indexer or API.
- Filesystem is the source of truth; API/UI are views over derived indices.

## Known limitations (MVP scope)
- Not a full end-to-end book translation system.
- Limited run inputs (excerpt-driven runs).
- Proposal/closure lifecycle is filesystem-based and manual.
- No automated canonical publication.
- Chapter-level english and rough_nl inputs are missing (ingest has source_nl + provenance only). [Out of scope for M1 (M2+)]
- Indexer/API are excerpt-centric; registry/alignment are not consumed by indexer/API/UI; chapter↔excerpt exists only as documentation (no runtime index). [Out of scope for M1 (M2+)]

## Book/chapter/excerpt structure facts
See `documentation/system_overview/BOOK_STRUCTURE_FACTS.md` for a factual inventory
of source locations, excerpt IDs, and alignment signals.

## Current data shapes (as observed)

Run bundle layout:
- `runtime/runs/<excerpt_id>/<RUN_id>/`
  - `inputs/english.txt`
  - `inputs/rough_nl.txt`
  - `outputs/annotator_primary.json`
  - `outputs/challenger_primary.json`
  - `outputs/crew_provisional.json`
  - `outputs/final.txt` (may be present)
  - `outputs/review_notes.md` (may be present)
  - `eval/output_contract_checks.txt`
  - `logs/run.log`

Indices:
- `runtime/indices/run_index.json`
- `runtime/indices/inbox_index.json`
- `runtime/indices/proposal_index.json`
- `runtime/indices/closure_index.json`
- `runtime/indices/review_queue_index.json`

## Authoritative runtime location
- Runtime system lives under: `runtime/`

## Frozen legacy path (do not work here)
- Frozen historical MVP snapshot:
  `/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy`
- Reason: preserve historical context; active development and runtime are here in the clean repo.

## State Update — 2026-01-13

### 1. Completed / As-Built (Facts)
- Page-based ingest (`runtime/data/ingest/page_sources/`) is compleet:
  - PNG, OCR TXT, OCR TSV aanwezig (1214 pages)
  - PROVENANCE.json aanwezig
- Page sources coverage is gevalideerd via
  `runtime/indices/page_sources_coverage_index.json` (geen gaps).
- Page-based ingest is het primaire startpunt van de workflow.

### 2. Prepared but Not Yet Populated
- `runtime/data/ingest/page_ocr_corrected/`
  - directory-structuur bestaat
  - geen corrected page outputs aanwezig per heden
- `runtime/data/ingest/definitive_source/`
  - directory-structuur bestaat
  - geen builds of manifests aanwezig per heden

### 3. Contracts & Rules (Established)
- `documentation/operator/AGENT_USAGE_CONTRACT_PAGE_SOURCES.md` — agent gebruik van page_sources (read-only).
- `documentation/operator/VALIDATOR_CONTRACT_PAGE_BASED_OUTPUTS.md` — structurele validatie van page-based outputs.
- `documentation/operator/OCR_CORRECTION_CONTRACT.md` — output + provenance voor page-level correctie.
- `documentation/operator/DEFINITIVE_SOURCE_BUILD_CONTRACT.md` — build manifest voor definitive source.
- Expliciet niet: auto-promotion, canonical writes, inhoudelijke beoordeling.

### 4. Runtime & Indices (As-Built Changes)
- Nieuwe derived index: `runtime/indices/page_sources_coverage_index.json`.
- `runtime/indexer.py` schrijft deze index in de bestaande reindex-flow.

### 5. Escalation & Triage — Current State
- Escalatie- en triagemechanismen bestaan:
  - governance/inbox niveau
  - agent/orchestrator niveau (prompts)
  - runtime niveau (FAILED / SKIPPED)
- Deze mechanismen zijn run/proposal-gebaseerd.
- Er bestaat geen expliciet page-level triage-artefact.
- Geen configuratielaag voor escalatie/triage.

### 6. Explicitly Deferred (By Design)
- Herijking van escalatie/triage naar page-scale.
- Centrale triage/configuratie.
- Mapping van bestaande triage-signalen naar OCR-correctie per page.
- Deferred pending empirical use at page-scale.

### 7. Current System Position
- Ingest + contracts: MVP+.
- OCR-correctie: voorbereid.
- Definitive source: voorbereid.
- Vertaling / synthesis: nog niet gestart.

## State Consolidation — Architecture & System Audit (2026-01-13)

### System-wide audit

- A system-wide, read-only audit has been performed.
- Report: `documentation/system_overview/SYSTEM_WIDE_AUDIT_2026-01-13.md`
- Scope: ingest layers, runtime artefacts, indices, entrypoints, contracts, document consistency.
- Result:
  - No confirmed architecture violations.
  - Entrypoints classified (runnable vs blocked-by-input).
- Indices confirmed as derived outputs.

### Excerpt coverage validation (as-built)

- Excerpt coverage validation is runnable via `python3 runtime/scripts/validate_excerpt_coverage.py`.
- Output artifact: `runtime/audit/coverage_report_latest.md` (derived; regenerable).

### As-built architecture documentation

- `documentation/system_overview/AS_BUILT_ARCH.md` exists.
- It documents the as-built architecture (filesystem-first) based on:
  - Project state
  - Evidence map
  - System-wide audit
  - Architecture consistency check
- It contains no intended design or roadmap.

### Baseline status

- The combination of:
  - `documentation/system_overview/PROJECT_STATE_PACK.md`
  - `documentation/system_overview/SYSTEM_WIDE_AUDIT_2026-01-13.md`
  - `documentation/system_overview/ARCHITECTURE_CONSISTENCY_CHECK_2026-01-13.md`
  - `documentation/system_overview/AS_BUILT_ARCH.md`
  forms the formal as-built baseline as of 2026-01-13.

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
Status: DONE (artefacts defined, workflows documented; runtime snapshot staging present)

ADDED: ### DoD — Run logging & reproducibility (MVP)
Reproducible in this MVP means editorial artefacts are audit- and comparison-ready for decision-making, not deterministic replay.
- Required minimum artefacts:
  - excerpt binding metadata (excerpt_id/source/version) accompanies each run/closure.
  - run logs exist under `runtime/runs/*/logs/run.log` or equivalent archival log files.
  - preserved outputs and eval files are kept as reviewed.
  - regression checks for run outputs and indices run via `runtime/scripts/regression_check_run_outputs.py` and `runtime/scripts/regression_check_indices.py`, producing reports under `runtime/audit/`.
  - traceability from run → proposal → closure when decisions are recorded.
- Explicit non-goals: no deterministic reruns, no automatic replay, no implied canonical publication.

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

ADDED: ### Closed topics (administrative)

1) MVP editorial phase handoffs — CLOSED  
   The MVP phase chain (Input → Proposal → Decision (Closure), Canonical-eligible out of scope)
   is explicitly documented and consistent across system overview, governance, architecture,
   and pilot documentation. Review queue is positioned as a visibility aid; closure does not
   imply publication or canonical status.

2) Segmentherdefinitie / Re-excerpting — CLOSED  
   A documentary-only policy defines how incorrect input scope is handled via explicit
   re-excerpting (version bump or new excerpt_id). Agents may signal mismatches; humans decide.
   Silent reuse or patching of existing artefacts is explicitly disallowed.

3) Backup / restore & regression evidence (Milestone 5) — CLOSED  
   Copy-only backup/restore workflows and regression evidence artefacts are documented and
   mapped to MVP phases without introducing automation or new runtime behavior.

4) Run logs & reproducibility (MVP) — CLOSED  
   An explicit Definition of Done defines “reproducible” as audit- and comparison-ready for internal editorial
   decision support. Required artefacts (run logs, audit trail, regression checks, and run→proposal→closure traceability)
   are documented; deterministic reruns, auto-replay, and canonical publication are explicitly out of scope.

5) Review queue semantiek — CLOSED  
   The inbox/review queue is explicitly documented as a visibility aid; only
   `closure_needed` marks an explicit decision requirement. Other signals indicate
   attention or review without implying urgency or mandatory resolution.

6) Explorative pilots and structural impact — CLOSED  
   Pilots are treated as exploratory proof artefacts without predefined
   governance escalation. If conclusions acquire structural impact, this
   becomes evident through reuse or friction and is addressed explicitly
   at that time rather than by prior definition.

### References (non-normative)

ADDED: - External reference: `documentation/references/external/Clarifying_Agent_Signals_and_Governance_Implications.pdf` (informational; no policy changes).
