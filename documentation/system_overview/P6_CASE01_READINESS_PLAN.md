# Phase-6 — Case-01 Readiness Plan (SAYUR, lines 52–66)

Status: PENDING — readiness documented, execution deferred  
Related: P6_SAYUR_INTERNAL_WORK_CASE01.md, P6_EXCERPT_BINDING_SPEC.md,  
P6_EXCERPT_BINDING_RUNTIME_DESIGN.md, P6_EXCERPT_AWARE_RUNNER_DESIGN.md,  
P6_RUNNER_OUTPUT_LAYOUT.md, P6_PHASE_STATUS_SNAPSHOT.md

---

## 1. Context

Case-01 is prepared but intentionally not executed.
Previous logs referenced a different excerpt, so Case-01 remains pending.
Binding rules require that logs and excerpts match by design, not by assumption.
The locked excerpt is SAYUR lines 52–66 with:
- excerpt_id: sayur_052_066
- excerpt_source: docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md
- excerpt_version: locked-2026-01-05

> "Case-01 remains pending until excerpt-aware runs exist for this exact excerpt."

---

## 2. Preconditions (Before Any Run)

A real Case-01 run can only start when all of the following are true:

- excerpt metadata locked and documented in the governing excerpt doc,
- excerpt-aware runtime propagation contract is defined,
- runner output layout is READY_FOR_IMPLEMENTATION,
- sandbox-only scope is confirmed (proposal-only, no canonical edits).

> "If ANY uncertainty remains, postpone the run — do not improvise."

---

## 3. Runner & CLI Readiness

Expected CLI inputs for excerpt-aware execution:

- --excerpt-id
- --excerpt-source
- --excerpt-version

Required log header fields (key:value lines at top of each log):

- excerpt_id
- excerpt_source
- excerpt_version
- run_id
- timestamp
- mode: excerpt-aware

STOP rules:

- Missing or mismatched excerpt metadata = SOFT-STOP; do not start the workflow.
- No inference from filenames or paths; only explicit metadata counts.

---

## 4. Required Artefacts for a Valid First Run

A valid Case-01 run must produce:

- one log file under sandbox/crew/run_logs/{excerpt_id}/ with the required header,
- annotator JSON under sandbox/crew/run_outputs/{excerpt_id}/{run_id}/ with a top-level "excerpt" object,
- challenger JSON under sandbox/crew/run_outputs/{excerpt_id}/{run_id}/ with the same "excerpt" object,
- optional: crew_provisional.json and review_notes.md in the same run root.

The top-level excerpt object must look like:

{
  "excerpt": {
    "id": "...",
    "source": "...",
    "version": "..."
  }
}

If any required artefact is missing, the run is INCOMPLETE.

---

## 5. Triage & Review Path

Roles:

- Codex records the run summary and artefact paths.
- A human reviewer checks alignment and lifecycle correctness.

Outcomes (for the runner design and traceability, not the text itself):

- GO: artefacts align and run is traceable.
- REWORK: mismatches exist; a fresh run is required.
- NO-GO: runner design is insufficient; halt until design gaps are resolved.

All outcomes are logged in docs/CODEX_SESSION_LOG.md.

---

## 6. Rollback Plan

Rollback means:

- delete the affected sandbox outputs under run_outputs/{excerpt_id}/{run_id},
- remove the corresponding run log entry from the session log,
- keep docs/ and canonical texts untouched.

This rollback is documentary and does not delete historical canonical material.

---

## 7. READINESS_CHECKLIST

- [ ] Preconditions ok
- [ ] Runner implemented according to design
- [ ] Dry-run executed
- [ ] First Case-01 run executed
- [ ] Review completed

---

End of document.
