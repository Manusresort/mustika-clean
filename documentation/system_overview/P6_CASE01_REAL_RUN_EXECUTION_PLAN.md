# Phase-6 — Case-01 Real-Run Execution Plan (SAYUR 052–066)

Status: DESIGN — real run NOT executed  
Related: P6_CASE01_READINESS_PLAN.md, P6_EXCERPT_BINDING_SPEC.md,  
P6_EXCERPT_AWARE_RUNNER_DESIGN.md, P6_EXCERPT_AWARE_PRACTICE_RUN_CASE01.md

---

## 1. Purpose

This document defines the **safe procedure** for the first real
excerpt-aware run for Case-01.

It ensures that the run:

- is traceable,
- respects lifecycle boundaries,
- and produces artefacts that match the locked excerpt.

This plan does NOT authorize execution by itself.

---

## 2. Preconditions (Must Be True Before Any Run)

A real Case-01 run can only start when all of the following are true:

- excerpt locked (id/source/version confirmed),
- runner accepts excerpt metadata explicitly,
- logging format includes excerpt metadata,
- readiness plan checklist is satisfied,
- human reviewer confirms “GO” for a sandbox attempt.

Rule:

> If ANY uncertainty remains, postpone the run — do not improvise.

---

## 3. Expected CLI Shape (Reminder)

The real run should resemble:

```bash
python sandbox/crew/run_excerpt_workflow.py \
  --excerpt-id sayur_052_066 \
  --excerpt-source docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md \
  --excerpt-version locked-2026-01-05 \
  --config sandbox/crew/configs/sayur_case01.yaml
```

This is a shape reminder only; real execution must be logged separately.

The exact command may differ — but excerpt metadata must match the locked document.

---

## 4. Expected Outputs (Minimal Set)

A valid run must produce:

annotator_raw.json

challenger_raw.json

crew_decisions_provisional.json

a runtime log containing excerpt metadata

Optional artefacts may exist, but these four are required.

Missing any required artefact → run is INCOMPLETE.

---

## 5. Validation Steps After the Run

After the run, perform the following checks:

 log includes excerpt_id/source/version

 JSON files contain identical metadata values

 no artefact references another excerpt

 lifecycle state stays at CREW_PROVISIONAL

 no glossary decisions claim canonical authority

If any box fails:

mark the run as REVIEW_REQUIRED and halt further processing.

---

## 6. Human Reviewer Role

Reviewer verifies:

provenance,

metadata coherence,

lifecycle correctness,

absence of silent edits.

Reviewer may:

accept the run as VALID,

request re-run,

or freeze Case-01 pending clarification.

Silent corrections are explicitly forbidden.

---

## 7. Incident Scenarios & Responses

List common failure scenarios:

reused logs from another excerpt

mismatching excerpt_version

crew JSON missing excerpt block

unexpected automatic escalation to READY_FOR_HUMAN_REVIEW

Response rule:

document → stop → investigate — never patch artefacts after the fact.

---

## 8. What Success Looks Like

A successful real run means:

artefacts exist,

excerpt-binding is consistent,

lifecycle remains provisional,

reviewer signs off as “traceable and valid”.

Success does NOT mean:

canonical decisions,

publication,

glossary finalization,

or translation.

---

## 9. Next Steps After a Valid Run

When a valid run exists, we may:

perform analytic review,

prepare human review materials,

optionally re-run with improvements (logged separately).

Any promotion beyond provisional requires Human Gate involvement.

---

## 10. Out-of-Scope

This plan does NOT:

deploy enforcement systems,

modify runner code,

change governance rules,

authorize production work.

It simply coordinates a safe first execution.

---

End of document.
