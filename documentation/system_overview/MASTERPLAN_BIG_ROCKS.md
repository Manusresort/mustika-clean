# MASTERPLAN — Mustika Rasa Clean (Big Rocks)

## 0) Status / Blockers (nu)

1) **CI-invariant breach: runtime/ tracked but workflow blocks runtime/**
   - Impact: CI faalt op elke push; repository kan niet groen worden.
   - Evidence: `.github/workflows/verify-repo.yml` (blokkeert runtime/); runtime is tracked (e.g. `runtime/api_server.py`).
   - Owner-action: beslis of runtime/ wél een tracked surface mag zijn of workflow moet worden aangepast.

2) **API host mismatch (IPv6 vs IPv4) → health checks inconsistent**
   - Impact: `/health` via `127.0.0.1` kan falen als API op `::1` bindt; QA scripts en docs zijn inconsistent.
   - Evidence: `runtime/scripts/dev_start_api.sh` (host `::1`), `runtime/scripts/qa_full_system.sh` (curl `127.0.0.1:8010`).
   - Owner-action: kies canonical host/port en update scripts + docs.

3) **QA scripts wijzen naar frozen snapshot i.p.v. runtime**
   - Impact: QA meet niet de actieve runtime; regressies blijven onzichtbaar.
   - Evidence: `runtime/scripts/qa_suite_x.sh` + `runtime/scripts/qa_verify_inbox.sh` (RUNTIME_ROOT = cursor snapshot).
   - Owner-action: herpoint QA naar `runtime/` of expliciet frozen-snapshot regime vastleggen.

## 1) Doel en werkwijze

- Scope: runtime-first stabilisatie van `runtime/` (runner, indexer, API, UI, QA) + minimale docs-alignment. (evidence: `runtime/` tree)
- Non-goals: geen nieuwe productfeatures, geen inhoudelijke policy-wijzigingen buiten bestaande docs. (evidence: `docs/REPO_FREEZE.md`)
- Fact-first: alleen claims met evidence; onzekerheden labelen als `FACT REQUEST` of `UNKNOWN`.
- Filesystem-first: `runs/`, `proposals/`, `closures/` zijn leidend; `indices/` is afgeleid. (evidence: `runtime/indexer.py`)
- Eerst masterplan dan cleanup: fasen + acceptance criteria bepalen, daarna pas opruimen/stabiliseren.

## 2) Architectuurkaart (as-is)

### 2.1 Entrypoints (runtime-first)

- `runtime/scripts/mustika_run_excerpt.py` — CLI entrypoint voor RunnerV2 (start run bundle). (evidence: `runtime/scripts/mustika_run_excerpt.py`)
- `runtime/src/runner_v2/runner.py` — RunnerV2 core: maakt run bundle + outputs + validator call. (evidence: `runtime/src/runner_v2/runner.py`)
- `runtime/indexer.py` — filesystem scan → `indices/*.json`. (evidence: `runtime/indexer.py`)
- `runtime/api_server.py` — FastAPI API voor inbox/runs/proposals/closures. (evidence: `runtime/api_server.py`)
- `runtime/ui/` — Vite UI (via proxy `/api` → API). (evidence: `runtime/ui/vite.config.ts`)
- `runtime/scripts/qa_full_system.sh` — end-to-end smoke checks API/indexer/UI. (evidence: `runtime/scripts/qa_full_system.sh`)
- `runtime/scripts/dev_up.sh` — start API + reindex + UI. (evidence: `runtime/scripts/dev_up.sh`)

### 2.2 Dataflow (filesystem-first)

- Input → Runner → Pipeline → Outputs → Validator → Indices → API → UI → Human Review → Proposals/Closures.
- Run bundle layout (RunnerV2): `runs/<excerpt_id>/<RUN_...>/` met `inputs/`, `outputs/`, `logs/`, `eval/`, `manifest.json`. (evidence: `runtime/src/runner_v2/runner.py`)

### 2.3 Artefacts & directories

- `runs/` — run bundles (immutable). (evidence: `runtime/src/runner_v2/runner.py`)
- `indices/` — derived JSON indices. (evidence: `runtime/indexer.py`)
- `proposals/` — proposal records; status update via API closures. (evidence: `runtime/api_server.py`)
- `closures/` — closure records; immutable. (evidence: `runtime/api_server.py`)
- `audit/` — logs (API + dev scripts). (evidence: `runtime/scripts/dev_start_api.sh`)
- `canonical/` — conceptueel genoemd, maar directory ontbreekt. (UNKNOWN; evidence: `runtime/api_server.py`, `MISSING: runtime/canonical`)

## 3) System contract (as-is)

### 3.1 Input contract

- RunnerV2 verwacht `--excerpt-id`, `--excerpt-source`, `--excerpt-version`, `--english`, `--rough-nl`. (evidence: `runtime/scripts/mustika_run_excerpt.py`)
- Input files bestaan en zijn UTF-8 leesbaar. (evidence: `runtime/scripts/mustika_run_excerpt.py`)
- Inputs worden gekopieerd naar `runs/<excerpt_id>/<RUN_...>/inputs/`. (evidence: `runtime/src/runner_v2/runner.py`)

### 3.2 Pipeline contract

- Pipeline entry: `runtime/test_multi_agent_fidelity.py::run_pipeline`. (evidence: `runtime/src/runner_v2/runner.py`)
- Fases: Translation Quality → Readability → Fidelity. (evidence: `runtime/test_multi_agent_fidelity.py`)
- Agent builder: `runtime/src/mustikarasa_agents.py::build_agents`. (evidence: `runtime/src/mustikarasa_agents.py`)
- Stub mode wanneer CrewAI/agents ontbreken; returnt rough_nl + remarks. (evidence: `runtime/test_multi_agent_fidelity.py`)

### 3.3 Output contract

- Outputs (minimaal): `outputs/annotator_primary.json`, `outputs/challenger_primary.json`, `outputs/crew_provisional.json`, `outputs/final.txt`. (evidence: `runtime/src/runner_v2/runner.py`)
- Eval: `eval/output_contract_checks.txt` (validator output). (evidence: `runtime/src/runner_v2/runner.py`)
- Logs + manifest: `logs/run.log`, `manifest.json`, `command.txt`, `env_allowlist.txt`. (evidence: `runtime/src/runner_v2/runner.py`)

### 3.4 Index contract

- `indexer.py` genereert `indices/run_index.json`, `proposal_index.json`, `closure_index.json`, `inbox_index.json`. (evidence: `runtime/indexer.py`)
- Inbox regels: validator FAIL → incident; blocking gate → gate; challenger issues → review_required; proposal open → review_required; required_closure → closure_needed (met closure lookup guard). (evidence: `runtime/indexer.py`)
- Indexer ondersteunt meerdere layouts via adapter. (evidence: `runtime/indexer.py`, `runtime/src/runner_v2/run_layout_adapter.py`)

### 3.5 API contract

- `GET /health`, `GET /version`, `POST /reindex`. (evidence: `runtime/api_server.py`)
- `GET /inbox`, `GET /runs/{run_id}`, `GET /proposals/{proposal_id}`, `GET /closures/{closure_id}`. (evidence: `runtime/api_server.py`)
- `POST /closures` schrijft closure + update proposal status. (evidence: `runtime/api_server.py`)

### 3.6 UI contract

- Vite proxy `/api` → `http://localhost:8010`. (evidence: `runtime/ui/vite.config.ts`)
- UI leest uitsluitend via API; geen direct filesystem access. (evidence: `runtime/ui/src/api.ts`)

## 4) Current Reality: divergences / risico’s (fact-first)

1) **CI invariant breach: runtime/ tracked vs workflow block**
   - Impact: CI fail op elke push.
   - Evidence: `.github/workflows/verify-repo.yml` + tracked runtime files (`runtime/api_server.py`).
   - Next decision / fix target: workflow aanpassen of runtime/ uit git halen.

2) **IPv6 vs IPv4 mismatch in API host**
   - Impact: health checks/QA kunnen falen afhankelijk van resolver.
   - Evidence: `runtime/scripts/dev_start_api.sh` (`--host ::1`), `runtime/scripts/qa_full_system.sh` (curl `127.0.0.1`).
   - Next decision / fix target: canonical host bepalen en harmoniseren.

3) **Docs command path mismatch (DEV_WORKFLOW vs runtime/scripts)**
   - Impact: operators draaien verkeerde commands vanuit verkeerde cwd.
   - Evidence: `documentation/system_overview/DEV_WORKFLOW.md` (uses `./scripts/dev_up.sh`), scripts bevinden zich onder `runtime/scripts/`.
   - Next decision / fix target: DEV_WORKFLOW expliciet maken als source-of-truth en correct pad beschrijven.

4) **Validator is minimal + gate semantics beperkt**
   - Impact: validator detecteert nauwelijks kwaliteitsissues; gates kunnen false positives/negatives geven.
   - Evidence: `sandbox/tools/phase8_output_contract_validator.sh` (enkel check op “definitieve”).
   - Next decision / fix target: contract uitbreiden of validator scope documenteren.

5) **Pipeline import boundary: runner importeert test module**
   - Impact: “test” module wordt productie-pipeline; risico op drift.
   - Evidence: `runtime/src/runner_v2/runner.py` import `test_multi_agent_fidelity`.
   - Next decision / fix target: pipeline module verplaatsen naar runtime/src of expliciet markeren.

6) **Duplicate sys.path inserts in indexer**
   - Impact: onnodige side-effects, onduidelijke import chain.
   - Evidence: `runtime/indexer.py` (meerdere BASE_DIR/sys.path insert blokken).
   - Next decision / fix target: single insertion, duidelijke comment.

7) **QA scripts target frozen snapshot**
   - Impact: QA tests lopen niet tegen runtime; regressies onzichtbaar.
   - Evidence: `runtime/scripts/qa_suite_x.sh`, `runtime/scripts/qa_verify_inbox.sh` (RUNTIME_ROOT naar cursor snapshot).
   - Next decision / fix target: RUNTIME_ROOT → `runtime/` of expliciete “frozen snapshot QA” policy.

## 5) Big Rocks Roadmap (6 fases)

### Fase 1 — Stabilisatie

**Doel**
Runtime moet met 1 command starten en indexeren zonder handmatige fixes.

**Scope**
Scripts, venv, ports, basic smoke tests.

**Deliverables**
- Dev/QA scripts consistent met runtime/.venv
- Port/host eenduidig
- Basic health checks groen

**To-do checklist**
- [x] Harmoniseer API host/port in scripts + docs (localhost/127.0.0.1/::1). (evidence: `runtime/scripts/dev_start_api.sh`, `runtime/scripts/qa_full_system.sh`)
- [x] dev_start_api healthcheck retry/backoff (removes transient 000). (evidence: `runtime/scripts/dev_start_api.sh`)
- [x] QA scripts herpointen naar runtime (geen frozen snapshot). (evidence: `runtime/scripts/qa_suite_x.sh`, `runtime/scripts/qa_verify_inbox.sh`)
- [x] QA validator contract path corrected (runtime suite uses repo-root validator). (evidence: `runtime/scripts/qa_suite_x.sh`, `sandbox/tools/phase8_output_contract_validator.sh`)
- [x] Venv + deps vastleggen in single source-of-truth doc. (evidence: `documentation/system_overview/ENVIRONMENT.md`)
- [x] CI invariant oplossen (runtime tracked vs workflow). (evidence: `.github/workflows/verify-repo.yml`)
- [x] `runtime/canonical/` directory status beslissen (maken of policy aanpassen). (UNKNOWN)

**Done means**
- `cd runtime && ./scripts/dev_up.sh` → `/health` = 200 en UI opent. (evidence: `runtime/scripts/dev_up.sh`)
- `cd runtime && ./scripts/qa_full_system.sh` green. (evidence: `runtime/scripts/qa_full_system.sh`)
- CI workflow passeert zonder runtime conflict. (evidence: `.github/workflows/verify-repo.yml`)

### Fase 2 — Productkwaliteit (output discipline + editorial)

**Doel**
Pipeline output voldoet aan output discipline (NL-only, no meta), validator consistent.

**Scope**
Pipeline prompts, validator, output files.

**Deliverables**
- Strakke prompt constraints
- Validator rules aligned met output contract

**To-do checklist**
- [x] Versterk output discipline in pipeline prompts. (evidence: `runtime/test_multi_agent_fidelity.py`)
- [x] Documenteer validator scope (wat is “PASS/FAIL”). (evidence: `sandbox/tools/phase8_output_contract_validator.sh`)
  Validator scope (as-is):
  - Input: `run_dir` argument; only checks `run_dir/outputs/final.txt` if present. (evidence: `sandbox/tools/phase8_output_contract_validator.sh`)
  - Invocation: `phase8_output_contract_validator.sh <run_dir>` writes `eval/output_contract_checks.txt`. (evidence: `sandbox/tools/phase8_output_contract_validator.sh`)
  - PASS: `final.txt` does not contain the word “definitieve” (case-insensitive). (evidence: `sandbox/tools/phase8_output_contract_validator.sh`)
  - FAIL: `final.txt` contains “definitieve”; exit code 1; `overall_status: FAIL`. (evidence: `sandbox/tools/phase8_output_contract_validator.sh`)
  - Limitations / non-goals:
    - Does not validate language, structure, or completeness beyond the single keyword check. (evidence: `sandbox/tools/phase8_output_contract_validator.sh`)
    - Does not fail if `final.txt` is missing (status remains PASS). (evidence: `sandbox/tools/phase8_output_contract_validator.sh`)
- [x] Check “final.txt” is always produced. (evidence: `runtime/src/runner_v2/runner.py`)
- [x] Define “remarks” format policy (consistent with UI). (evidence: `runtime/src/runner_v2/runner.py`)
  Remarks format policy:
  - remarks is optional string.
  - If present, must start with a category prefix: STUB:, WARNING:, NOTE:.
  - Remarks are NL-only, except the prefix token itself (e.g., STUB:).
  - Max 5 bullet points OR one short sentence.
  - No duplication of main text.

**Done means**
- Pipeline output is 100% NL and one-block (manual smoke). (evidence: `runtime/test_multi_agent_fidelity.py`)
- `output_contract_checks.txt` exists for each run. (evidence: `runtime/src/runner_v2/runner.py`)

### Fase 3 — Integratie (indices/API/UI)

**Doel**
Indices, API en UI tonen consistente status en data.

**Scope**
Indexer, API endpoints, UI data mapping.

**Deliverables**
- Inbox rules stable
- UI shows proposal_md, run detail, closure creation

**To-do checklist**
- [x] Verify proposal/closure inbox rules (no closure_needed for closed). (evidence: `runtime/indexer.py`)
- [x] UI contract check: `proposal_md` mapping in UI. (evidence: `runtime/api_server.py`, `runtime/ui/src/components/ReviewPackViewer.tsx`)
- [x] Verify API `/reindex` uses correct base_path. (evidence: `runtime/api_server.py`)
- [x] Ensure indices deterministic across two runs. (evidence: `runtime/indexer.py`, commit `ae37211`; reindex x2 produced no diffs for indices/{inbox,run,proposal,closure}_index.json (generated_at-only diffs ignored).)
- [x] Document run layout adapter behavior. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)

**Done means**
- UI shows proposal content for existing `proposal.md`. (evidence: `runtime/api_server.py`, `runtime/ui/src`)
- `indices/inbox_index.json` matches rules. (evidence: `runtime/indexer.py`)

### Fase 4 — Governance (canonical + human gate)

**Doel**
Human gate + closure rules consistent met policy.

**Scope**
Policy docs in monorepo vs runtime, stub-mode signals.

**Deliverables**
- Canon policy pointers
- Human gate checklists

**To-do checklist**
- [x] Policy pointers consolidated to canonical docs. (evidence: `docs/OPERATOR_ENTRYPOINT.md` pointer)
- [x] Human gate checklist visible in runtime docs. (evidence: `documentation/system_overview/GOVERNANCE.md`)
- [x] Explicit stub-mode note (CrewAI missing) in runbook. (evidence: `documentation/system_overview/RUNBOOK_TROUBLESHOOTING.md`, `runtime/test_multi_agent_fidelity.py`)

**Done means**
- Operator can find canonical gate rules in 1 hop. (evidence: doc link)
- No conflicting status/gate definitions. (FACT REQUEST)

### Fase 5 — QA/CI/Release gates

**Doel**
Repeatable QA and CI checks for minimal regressies.

**Scope**
qa_full_system.sh, qa_suite_x.sh, CI invariants.

**Deliverables**
- CI-friendly smoke tests
- Runtime state excluded from git

**To-do checklist**
- [ ] CI rule: runtime state ignored or workflow updated. (evidence: `.github/workflows/verify-repo.yml`)
- [ ] QA suite produces deterministic audit logs. (evidence: `runtime/scripts/qa_full_system.sh`)
- [ ] L0/L1 checks in Suite X align with runtime path. (evidence: `runtime/scripts/qa_suite_x.sh`)
- [x] Ensure `sandbox/tools` scripts are tracked (ignore rules). (evidence: `.gitignore`, `sandbox/tools/*.sh`)

**Done means**
- CI passes on main. (FACT REQUEST)
- `audit/qa/latest/summary.tsv` generated for QA run. (evidence: `runtime/scripts/qa_full_system.sh`)

### Fase 6 — Ops & Sustainability (local-first)

**Doel**
Local ops are reliable, repeatable, documented.

**Scope**
Runbooks, troubleshooting, env checks.

**Deliverables**
- Runbook with minimal steps
- Troubleshooting checklist

**To-do checklist**
- [x] Single source-of-truth runbook (dev up + QA). (evidence: `documentation/system_overview/DEV_WORKFLOW.md`)
- [x] Troubleshooting matrix (ports, venv, API). (evidence: `documentation/system_overview/RUNBOOK_TROUBLESHOOTING.md`)
- [x] Clarify Python version + CrewAI dependency in runbook. (evidence: `documentation/system_overview/RUNBOOK_TROUBLESHOOTING.md`, `runtime/requirements-ui.txt`)

**Done means**
- New operator can start system in <10 min. (FACT REQUEST)
- Fewer than 3 manual steps after `dev_up.sh`. (FACT REQUEST)

## 6) Patch Plan (exact files, nog niet toepassen)

- File: `.github/workflows/verify-repo.yml`
  - Edit intent: reconcile invariant with tracked runtime/ (either allow runtime or move runtime out of git).
  - Risk: CI could ignore necessary checks if too broad.
  - Rollback: revert workflow.

- File: `runtime/scripts/dev_start_api.sh`
  - Edit intent: canonical host/port (choose localhost/127.0.0.1/::1) + healthcheck consistent with QA.
  - Risk: local bind issues on macOS.
  - Rollback: revert file.

- File: `runtime/scripts/mustika_run_excerpt.py`
  - Edit intent: explicit venv enforcement + PYTHONPATH, no PATH python fallback.
  - Risk: breaking CLI usage if venv missing.
  - Rollback: revert file.

- File: `runtime/src/runner_v2/runner.py`
  - Edit intent: move pipeline import to a non-test module; clarify validator behavior.
  - Risk: pipeline break if module path changes.
  - Rollback: revert file.

- File: `runtime/indexer.py`
  - Edit intent: remove duplicate sys.path inserts; clean import block.
  - Risk: import errors if refactor is wrong.
  - Rollback: revert file.

- File: `runtime/api_server.py`
  - Edit intent: clarify contract surfaces; ensure closure schema stable.
  - Risk: API response shape changes.
  - Rollback: revert file.

- File: `documentation/system_overview/DEV_WORKFLOW.md`
  - Edit intent: make it single source for dev commands and ports; link other docs to it.
  - Risk: doc drift if other docs not aligned.
  - Rollback: revert file.

## 7) Golden Path (1-command)

**Dev up**
- `cd runtime && ./scripts/dev_up.sh` (evidence: `runtime/scripts/dev_up.sh`)

**QA full system**
- `cd runtime && ./scripts/qa_full_system.sh` (evidence: `runtime/scripts/qa_full_system.sh`)

**Expected ports/logs**
- API: `http://localhost:8010/health` (evidence: `runtime/ui/vite.config.ts`, `runtime/scripts/qa_full_system.sh`)
- UI: `http://localhost:5173` (evidence: `runtime/scripts/dev_start_ui.sh`)
- Logs: `runtime/audit/api_server.log`, `runtime/audit/ui_dev.log` (evidence: `runtime/scripts/dev_start_api.sh`, `runtime/scripts/dev_start_ui.sh`)

**Troubleshooting (6 bullets)**
- Venv missing → `source runtime/.venv/bin/activate`. (evidence: `runtime/scripts/dev_start_api.sh`)
- API not reachable → check `runtime/audit/api_server.log`. (evidence: `runtime/scripts/dev_start_api.sh`)
- Port conflict → `lsof -i :8010` and `lsof -i :5173`. (evidence: `runtime/scripts/dev_up.sh`)
- UI not loading → check `runtime/audit/ui_dev.log`. (evidence: `runtime/scripts/dev_start_ui.sh`)
- Inbox empty → run `./scripts/reindex_runtime.sh`. (evidence: `runtime/scripts/reindex_runtime.sh`)
- QA fails on CrewAI → verify venv + `crewai` installed. (evidence: `runtime/requirements-ui.txt`)

### Weekly Operator Checklist (10 min)

- [ ] `/health` returns 200 (API). (evidence: `runtime/api_server.py`)
- [ ] Run `./scripts/reindex_runtime.sh`. (evidence: `runtime/scripts/reindex_runtime.sh`)
- [ ] `/inbox` loads and items look plausible (non-empty if work is pending). (evidence: `runtime/api_server.py`)
- [ ] `audit/` log size sane (no runaway). (evidence: `runtime/scripts/dev_start_api.sh`)
- [ ] `npm run build` in `runtime/ui/` succeeds. (evidence: `runtime/scripts/qa_full_system.sh`)
- [ ] Run bundle created for a test excerpt (optional). (evidence: `runtime/scripts/mustika_run_excerpt.py`)
- [ ] Validator report exists for latest run. (evidence: `runtime/src/runner_v2/runner.py`)
- [ ] `indices/*.json` parse OK. (evidence: `runtime/indexer.py`)

## 8) FACT REQUESTS backlog

- [ ] Vraag: welke host/port is canonical (localhost vs 127.0.0.1 vs ::1)?
  - Command/file: `runtime/scripts/dev_start_api.sh`, `runtime/scripts/qa_full_system.sh`.
  - Unlocks: consistent health checks.

- [ ] Vraag: QA target pad is runtime of frozen snapshot?
  - Command/file: `runtime/scripts/qa_suite_x.sh`, `runtime/scripts/qa_verify_inbox.sh`.
  - Unlocks: accurate QA results.

- [ ] Vraag: canonical runbook locatie?
  - Command/file: `documentation/system_overview/DEV_WORKFLOW.md` vs `docs/REPO_MIGRATION_VERIFICATION.md`.
  - Unlocks: doc single source of truth.

- [ ] Vraag: status van `runtime/canonical/` (bestaat of niet)?
  - Command/file: `runtime/api_server.py`, filesystem check. 
  - Unlocks: canonical write policy clarity.

- [ ] Vraag: expected run layouts (runner_v2 vs phase8/phase9)?
  - Command/file: `runtime/src/runner_v2/run_layout_adapter.py`.
  - Unlocks: indexer determinism.

- [ ] Vraag: CrewAI version pin + model env vars (OPENAI_MODEL/LITELLM_MODEL)?
  - Command/file: `runtime/src/mustikarasa_agents.py`, `runtime/requirements-ui.txt`.
  - Unlocks: stable pipeline execution.

- [ ] Vraag: API base path/host for UI proxy (localhost vs 127.0.0.1)?
  - Command/file: `runtime/ui/vite.config.ts`.
  - Unlocks: consistent UI/API connectivity.

- [ ] Vraag: which docs are authoritative for QA? 
  - Command/file: `documentation/system_overview/DEV_WORKFLOW.md`, `docs/REPO_MIGRATION_VERIFICATION.md`.
  - Unlocks: avoid QA drift.

## 9) Status log (append-only)

### 2026-01-21
- Verified /reindex response includes `base_path_used` (evidence: `runtime/api_server.py`, QA PASS line below).
- Verified Phase 3 verification script exists and is executable (evidence: `runtime/scripts/qa_verify_phase3_contracts.sh`).
- Verified closure_needed rule is guarded for closed proposals (evidence: `runtime/indexer.py`, guard comment + `not is_closed`).

### 2026-01-21
- QA: `runtime/scripts/qa_verify_phase3_contracts.sh`
- Output lines:
  PASS: /health HTTP 200
  PASS: /reindex base_path_used=/Users/vwvd/Millway/AI-folder/Crew-AI/mustika-rasa-clean/runtime
  PASS: proposal_id=P-001
  PASS: /proposals/P-001 contains proposal_md
  PASS: no closure_needed for closed proposal P-001
  PASS: Phase 3 contracts OK

### 2026-01-21
- Documented RunLayoutAdapter behavior in `documentation/system_overview/RUN_LAYOUT_ADAPTER.md`.
- Evidence: `runtime/src/runner_v2/run_layout_adapter.py`, `runtime/src/runner_v2/runner.py`, `documentation/system_overview/RUN_LAYOUT_ADAPTER.md`.

### 2026-01-21
- OPERATOR_ENTRYPOINT points to in-repo canonical docs (no absolute path). (evidence: `docs/OPERATOR_ENTRYPOINT.md`)
- GOVERNANCE.md includes human gate checklist and aligns required_closure/closure_needed to runtime behavior. (evidence: `documentation/system_overview/GOVERNANCE.md`, `runtime/api_server.py`, `runtime/indexer.py`)

- 2026-01-20 — MASTERPLAN_BIG_ROCKS.md updated to fact-first masterplan with blockers, contracts, and patch plan. (evidence: `documentation/system_overview/MASTERPLAN_BIG_ROCKS.md`)
- 2026-01-20 — CI workflow allows runtime, forbids runtime state; API host canon 127.0.0.1; QA scripts no snapshot. (evidence: `.github/workflows/verify-repo.yml`, `runtime/scripts/dev_start_api.sh`, `runtime/scripts/qa_suite_x.sh`, `runtime/scripts/qa_verify_inbox.sh`, `documentation/system_overview/DEV_WORKFLOW.md`)
- 2026-01-20 — Scope correction: reverted unintended edits to runner/pipeline files back to HEAD; Phase 1 fixes remain limited to workflow + scripts + docs.
- 2026-01-20 — QA validator path fix + dev_start_api retry/backoff. (evidence: `runtime/scripts/qa_suite_x.sh`, `sandbox/tools/phase8_output_contract_validator.sh`, `runtime/scripts/dev_start_api.sh`, `runtime/audit/qa/runs/20260120T125537/summary.tsv`)
- 2026-01-20 — Pipeline boundary fixed: canonical pipeline moved to `runtime/src/pipeline_fidelity.py`; RunnerV2/CLI no longer import `test_multi_agent_fidelity`. (evidence: `runtime/src/pipeline_fidelity.py`, `runtime/src/runner_v2/runner.py`, `runtime/mustikarasa_codex_cli.py`, `runtime/test_multi_agent_fidelity.py`, `runtime/audit/qa/latest/summary.tsv`)
- 2026-01-20 — Session closeout: QA Suite X green + validator path resolved + dev_start_api retry/backoff. (evidence: `runtime/audit/qa/runs/20260120T131807/summary.tsv`, `sandbox/tools/phase8_output_contract_validator.sh`, `runtime/scripts/dev_start_api.sh`)
- 2026-01-20 — Fase 5: sandbox/tools/*.sh bevestigd tracked + .gitignore allowlist voor sandbox/tools/*.sh. (evidence: `git ls-files sandbox/tools`, `.gitignore`)
- 2026-01-20 — Fase 6: DEV_WORKFLOW canonicalized (dev_up + qa_full_system) + troubleshooting matrix added. (evidence: `documentation/system_overview/DEV_WORKFLOW.md`, `documentation/system_overview/RUNBOOK_TROUBLESHOOTING.md`)
- 2026-01-20 — Fase 6: ENVIRONMENT + RUNBOOK updated (venv/deps, CrewAI, stub-mode) with evidence. (evidence: `documentation/system_overview/ENVIRONMENT.md`, `documentation/system_overview/RUNBOOK_TROUBLESHOOTING.md`, `runtime/requirements-ui.txt`, `runtime/test_multi_agent_fidelity.py`, `runtime/src/pipeline_fidelity.py`)

### Session Closeout — 2026-01-20
Done:
- [x] CI invariant updated: workflow allows tracked `runtime/` while forbidding tracked runtime state (`runtime/{indices,runs,audit,proposals,closures}/`, `runtime/.venv*`) and top-level `indices/`, with explicit match reporting.
- [x] Canonical API host/port aligned to `127.0.0.1:8010` in `runtime/scripts/dev_start_api.sh` and documented in `documentation/system_overview/DEV_WORKFLOW.md`.
- [x] QA scripts re-pointed to active `runtime/` via script-derived root (removed frozen snapshot paths; guards added).
- [x] `documentation/system_overview/issues/` now tracked with README + evidence notes.
Next:
- [x] Pipeline boundary cleanup (runner imports test module) (Phase 2/3 prep).
Blockers:
- None known inside `mustika-rasa-clean` (verify CI green after push).
Evidence:
- Commit `1d06a4e`
- `.github/workflows/verify-repo.yml`
- `runtime/scripts/dev_start_api.sh`
- `runtime/scripts/qa_suite_x.sh`
- `runtime/scripts/qa_verify_inbox.sh`
- `documentation/system_overview/DEV_WORKFLOW.md`
- `documentation/system_overview/MASTERPLAN_BIG_ROCKS.md`
- `documentation/system_overview/issues/README.md`
- `documentation/system_overview/issues/20260120_runtime_pipeline_status.md`
- `documentation/system_overview/issues/ENV_VENV_CREWAI_MISMATCH.md`
- `documentation/system_overview/ENVIRONMENT.md`
- `documentation/system_overview/DEV_WORKFLOW.md`
- `documentation/operator/RUNBOOK.md`
- `docs/REPO_MIGRATION_VERIFICATION.md`
- `runtime/README_UI.md`
- `documentation/system_overview/issues/ENV_VENV_CREWAI_MISMATCH.md`
- `runtime/requirements-ui.txt`
