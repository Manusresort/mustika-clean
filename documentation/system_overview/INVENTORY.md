# INVENTORY — Mustika Rasa Repo (System View)

## 1. Repository Overview

Local-first system for runs, proposals, closures, and derived indices, backed by a FastAPI server and a Vite UI. Core artifacts live in filesystem directories (`runs/`, `proposals/`, `closures/`), while `indices/` are generated from the filesystem by `indexer.py` and served by `api_server.py`.

---

## 2. Directory Map

Top-level directories (excluding build artifacts):

- `runs/`
  - Doel: run bundles (runner output)
  - Schrijver(s): `scripts/mustika_run_excerpt.py` → `src/runner_v2/runner.py`
  - Lezer(s): `indexer.py`, `api_server.py`, UI (`ui/` via API)
  - Status: immutable (append-only bundles)

- `proposals/`
  - Doel: proposal records
  - Schrijver(s): humans, API (`POST /closures` updates proposal status)
  - Lezer(s): `indexer.py`, `api_server.py`, UI
  - Status: mutable until closed

- `closures/`
  - Doel: closure records
  - Schrijver(s): API (`POST /closures`)
  - Lezer(s): `indexer.py`, `api_server.py`, UI
  - Status: immutable (closure.json not overwritten)

- `promotion/`
  - Doel: promotion records (Phase 2, directory exists)
  - Schrijver(s): none in current code
  - Lezer(s): `indexer.py` (scan target)
  - Status: unused / empty in MVP

- `indices/`
  - Doel: derived JSON indices
  - Schrijver(s): `indexer.py` (direct), `api_server.py` via `/reindex`
  - Lezer(s): `api_server.py`, UI
  - Status: derived (regenerated)

- `audit/`
  - Doel: append-only audit logs
  - Schrijver(s): `api_server.py` (api_actions.log), scripts/dev_up.sh (api_server.log/ui_dev.log)
  - Lezer(s): humans
  - Status: append-only

- `scripts/`
  - Doel: CLI entrypoints + dev scripts
  - Schrijver(s): humans
  - Lezer(s): terminal
  - Status: mutable

- `src/`
  - Doel: Runner v2 implementation and layout adapter
  - Schrijver(s): humans
  - Lezer(s): `scripts/mustika_run_excerpt.py`, `indexer.py`
  - Status: mutable

- `ui/`
  - Doel: Vite frontend
  - Schrijver(s): humans
  - Lezer(s): browser
  - Status: mutable

- `canonical/`
  - Doel: canonical content store
  - Schrijver(s): none in MVP (writes blocked in API)
  - Lezer(s): none in MVP
  - Status: read-only (policy)

- `sandbox/`
  - Doel: validator scripts + experimental runs
  - Schrijver(s): tools and experiments
  - Lezer(s): humans, optional scripts
  - Status: non-canonical / experimental

- `docs/`
  - Doel: documentation
  - Schrijver(s): humans
  - Lezer(s): humans
  - Status: mutable

---

## 3. Core Artifacts (objecten)

### Run
- Locatie: `runs/<excerpt_id>/<RUN_...>/`
- Producer(s): `RunnerV2` (`scripts/mustika_run_excerpt.py` → `src/runner_v2/runner.py`)
- Consumer(s): `indexer.py`, `api_server.py`, UI
- Persistency: immutable bundle
- Belangrijke velden: `run_id`, `excerpt_id`, `excerpt_source`, `excerpt_version`, `created_at`, `validator_status`

### Run Bundle
- Locatie: `runs/<excerpt_id>/<RUN_...>/`
- Inhoud:
  - `inputs/english.txt`, `inputs/rough_nl.txt`
  - `outputs/annotator_primary.json`, `outputs/challenger_primary.json`, `outputs/crew_provisional.json`, `outputs/final.txt`, `outputs/review_notes.md`
  - `logs/run.log`
  - `eval/output_contract_checks.txt`
  - `manifest.json`, `command.txt`, `env_allowlist.txt`
- Producer(s): Runner v2
- Consumer(s): indexer, API, UI
- Persistency: immutable bundle

### Inbox Item
- Locatie: `indices/inbox_index.json`
- Producer(s): `indexer.py` (`build_inbox_index()`)
- Consumer(s): `api_server.py` (`GET /inbox`), UI
- Persistency: regenerated
- Belangrijke velden: `id`, `kind`, `severity`, `source_type`, `source_id`, `reasons`, `path`
- No-duplicates: `(source_type + source_id + kind)`

### Proposal
- Locatie: `proposals/<proposal_id>/`
- Producer(s): humans; API updates `status.json` on closure
- Consumer(s): indexer, API, UI
- Persistency: mutable until closure
- Belangrijke velden: `proposal_id`, `status`, `severity`, `required_closure.json`, `proposal.md`

### Closure
- Locatie: `closures/<closure_id>/closure.json` (or `closure.md`)
- Producer(s): API (`POST /closures`)
- Consumer(s): indexer, API, UI
- Persistency: immutable (API blocks overwrite)
- Belangrijke velden: `closure_id`, `proposal_id`, `source_run_id`, `decision_type`, `rationale`, `evidence_paths`, `sign_off`

### Index (run_index, inbox_index, proposal_index, closure_index)
- Locatie: `indices/*.json`
- Producer(s): `indexer.py`
- Consumer(s): `api_server.py`, UI
- Persistency: regenerated
- Belangrijke velden:
  - `run_index.json`: `runs[]` with `run_id`, `excerpt_id`, `path`, `validator_status`, `status`
  - `inbox_index.json`: `items[]` with `kind`, `severity`, `reasons`
  - `proposal_index.json`: `proposals[]` with `proposal_id`, `status`, `severity`
  - `closure_index.json`: `closures[]` with `closure_id`, `proposal_id`, `created_at`

---

## 4. Executables / Entry Points

- `scripts/mustika_run_excerpt.py`
  - Start: `python3 scripts/mustika_run_excerpt.py --excerpt-id ... --excerpt-source ... --excerpt-version ... --english ... --rough-nl ...`
  - Writes: `runs/<excerpt_id>/<RUN_...>/` (inputs, outputs, logs, eval, manifest)
  - Reads: input files (`--english`, `--rough-nl`)

- `indexer.py`
  - Start: `python3 indexer.py`
  - Writes: `indices/run_index.json`, `indices/inbox_index.json`, `indices/proposal_index.json`, `indices/closure_index.json`
  - Reads: `runs/`, `proposals/`, `closures/` (and `sandbox/phase8_runs`, `sandbox/phase9_runs` via adapter)

- `api_server.py`
  - Start: `uvicorn api_server:app --host 127.0.0.1 --port 8000 --reload`
  - Writes: `audit/api_actions.log`, `closures/<closure_id>/closure.json`, `proposals/<proposal_id>/status.json`
  - Reads: `indices/`, `runs/`, `proposals/`, `closures/`

- UI dev server (`ui/`)
  - Start: `npm run dev` (from `ui/`)
  - Writes: none to filesystem (read-only)
  - Reads: API endpoints `/api/*` (proxy to `127.0.0.1:8000`)

---

## 5. Wat NIET wordt gedaan

- Geen writes naar `canonical/`.
- Geen auto-promotion.
- Geen mutatie van closures.
- Geen directe UI → filesystem writes.
