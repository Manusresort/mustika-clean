# Phase-6 — Implement Excerpt-Aware Runner (Task List)

This is a practical task list for implementing `sandbox/crew/run_excerpt_workflow.py`
in line with the Phase-6 implementation guide and the Case-01 plans.
The goal is to make it safe and straightforward to later execute and validate Case-01.

---

## Task 1 — CLI entrypoint and parameters

Description:
- Create the CLI entrypoint and parse excerpt_id, excerpt_source, excerpt_version, config, and run_id.
- Allow run_id to be generated when missing.

Inputs:
- docs/P6_EXCERPT_AWARE_RUNNER_IMPLEMENTATION_GUIDE.md

Outputs:
- CLI interface with the required parameters and defaults

---

## Task 2 — Pre-flight metadata validation (STOP rules)

Description:
- Implement validation of excerpt metadata and run_id validity.
- Apply STOP behavior for missing metadata or invalid run_id.
- Log mismatch between CLI and config with `cli_config_mismatch: true` and continue (config is source of truth).

Inputs:
- docs/P6_EXCERPT_AWARE_RUNNER_IMPLEMENTATION_GUIDE.md
- docs/P6_CASE01_READINESS_PLAN.md

Outputs:
- Pre-flight validation logic and STOP handling

---

## Task 3 — Log creation and header

Description:
- Implement log creation under `sandbox/crew/run_logs/{excerpt_id}/`.
- Write log header fields (excerpt metadata, run_id, timestamp, mode, mismatch flag).

Inputs:
- docs/P6_EXCERPT_AWARE_RUNNER_IMPLEMENTATION_GUIDE.md
- docs/P6_CASE01_VALIDATION_PLAN.md

Outputs:
- Run logs with correct header format and location

---

## Task 4 — Pipeline invocation (no governance changes)

Description:
- Call the existing crew/agent pipeline.
- Do not change prompts, governance, or lifecycle logic.

Inputs:
- Existing sandbox runner patterns (no prompt changes)

Outputs:
- Pipeline execution integrated into the runner

---

## Task 5 — JSON artefact generation and layout

Description:
- Write annotator/challenger output into JSON files under:
  `sandbox/crew/run_outputs/{excerpt_id}/{run_id}/`.
- Ensure each JSON contains `excerpt` and `run` blocks.
- Write `crew_provisional.json` where applicable.

Inputs:
- docs/P6_EXCERPT_AWARE_RUNNER_IMPLEMENTATION_GUIDE.md
- docs/P6_CASE01_VALIDATION_PLAN.md

Outputs:
- JSON artefacts in the required layout with excerpt/run metadata

---

## Task 6 — Exit codes and error handling

Description:
- Implement exit codes and error handling for STOP cases and I/O failures.
- Ensure invalid artefacts are not treated as valid runs.

Inputs:
- docs/P6_EXCERPT_AWARE_RUNNER_IMPLEMENTATION_GUIDE.md

Outputs:
- Deterministic STOP behavior and clean error reporting

---

## Task 7 — Validation tests (Case-01 plan)

Description:
- Run the validation checks from the Case-01 validation plan:
  - happy-path run
  - failure cases (missing metadata, mismatched config, JSON missing excerpt/run blocks).
- Record results in CODEX_SESSION_LOG.md.

Inputs:
- docs/P6_CASE01_VALIDATION_PLAN.md

Outputs:
- Evidence that the runner meets validation requirements

---

## Task 8 — First controlled Case-01 validation run

Description:
- Once tests are green, perform the first controlled Case-01 run.
- Evaluate using the validation plan and log the outcome.

Inputs:
- docs/P6_CASE01_VALIDATION_PLAN.md
- docs/P6_CASE01_READINESS_PLAN.md

Outputs:
- Case-01 validation result and logged reviewer outcome

---

End of task list.
