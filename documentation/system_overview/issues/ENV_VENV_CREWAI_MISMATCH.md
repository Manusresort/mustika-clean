# Clarify authoritative Python/venv for RunnerV2 + translation pipeline (CrewAI mismatch)

## TL;DR

* Repo docs + runtime scripts imply `runtime/.venv` is the intended runtime.
* RunnerV2/QA/pipeline scripts run via PATH `python3` (no venv activation).
* CrewAI is installed only in monorepo root `.venv` (Python 3.11), not in `runtime/.venv` (Python 3.14), causing
  `ModuleNotFoundError`.

---

## What we observed (evidence, fact-first)

### 1) Strong signals `runtime/.venv` is intended

* `runtime/scripts/dev_start_api.sh` activates `runtime/.venv` and runs `python -m uvicorn`
  **Evidence:** `runtime/scripts/dev_start_api.sh:7–13`, `28`
* `runtime/scripts/reindex_runtime.sh` activates `runtime/.venv` and runs `python indexer.py`
  **Evidence:** `runtime/scripts/reindex_runtime.sh:6–16`
* Docs explicitly prefer `runtime/.venv`
  **Evidence:** `docs/REPO_MIGRATION_VERIFICATION.md:10` (“venv in `runtime/.venv` preferred”), `118` (“Activate venv … in `runtime/.venv`”)

### 2) Scripts that bypass `runtime/.venv` (use PATH `python3`)

* RunnerV2 CLI uses shebang `/usr/bin/env python3` and does not activate a venv
  **Evidence:** `runtime/scripts/mustika_run_excerpt.py:1`
* QA suite calls `python3` directly for pipeline + runner smoke
  **Evidence:** `runtime/scripts/qa_suite_x.sh:73–74`
* Full-system QA uses `python3` directly (no venv activation)
  **Evidence:** `runtime/scripts/qa_full_system.sh:28–29`, `72–73`

### 3) CrewAI is not declared for runtime, but runtime code expects it

* `runtime/requirements-ui.txt` now pins `crewai==0.11.2`
  (note: earlier docs referenced `1.8.1`; current repo pin is `0.11.2`). Evidence: `runtime/requirements-ui.txt`
  **Evidence:** `runtime/requirements-ui.txt`
* `runtime/src/runner_v2/llm_client.py` imports `crewai` and raises “CrewAI not installed…”
  **Evidence:** `runtime/src/runner_v2/llm_client.py:25–32`

### 4) Measured interpreter mismatch (reproducible on this machine)

* `runtime/.venv` python (3.14.2): `import crewai` **FAIL**
* PATH python3 (brew, 3.14.2): `import crewai` **FAIL**
* monorepo root `.venv` python (3.11.14): `import crewai` **OK** (crewai 1.7.2)

---

## Impact / symptom

RunnerV2 via `runtime/scripts/mustika_run_excerpt.py` fails when the pipeline imports CrewAI-dependent code:
`ModuleNotFoundError: No module named 'crewai'`

---

## Questions for maintainers (seeking authoritative clarification; no fix proposed yet)

1. Which venv/interpreter is authoritative for:

* RunnerV2 (`runtime/scripts/mustika_run_excerpt.py`)
* `test_multi_agent_fidelity.py` pipeline
* `qa_suite_x.sh` and `qa_full_system.sh`

Is it `runtime/.venv`, monorepo-root `.venv`, or something else?

2. Where should CrewAI be installed (runtime venv vs root venv), and which Python version is supported?

3. Is there a source-of-truth doc or config (runbook, lockfile, Make target, CI) that explicitly pins the intended interpreter/venv for these scripts?

---

## Context

* Repo currently has untracked copies of `test_multi_agent_fidelity.py` under `runtime/` and repo root (created during local debugging), but the core mismatch exists regardless: scripts + docs are inconsistent about which Python is used.

2026-01-20: Updated to reflect current dependency declaration in `runtime/requirements-ui.txt`.

Thanks — once the intended environment is confirmed, we can align entrypoints/QA or dependency declarations accordingly.
