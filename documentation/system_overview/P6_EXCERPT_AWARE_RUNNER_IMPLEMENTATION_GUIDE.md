# Phase-6 — Excerpt-Aware Runner Implementation Guide

Status: implementation-oriented guidance (documentary)  
Related: docs/P6_EXCERPT_AWARE_RUNNER_DESIGN.md, docs/P6_EXCERPT_BINDING_RUNTIME_DESIGN.md, docs/P6_RUNNER_OUTPUT_LAYOUT.md, docs/P6_CASE01_READINESS_PLAN.md

---

## 1. Purpose

This guide translates the Phase-6 excerpt-aware runner design into an implementation-focused checklist.
It does not change governance and does not authorize runs by itself.
The goal is a first, minimal, excerpt-aware runner suitable for Case-01.

---

## 2. CLI Interface (Required Fields)

An excerpt-aware run accepts explicit metadata:

- excerpt_id
- excerpt_source
- excerpt_version
- run_id (stable identifier for the run; may be generated if missing)

A config file may also be provided, but explicit metadata must be present and coherent.
Do not infer any excerpt metadata from filenames or directory names.

---

## 3. Pre-flight Validation (STOP Conditions)

Before any workflow begins:

- Verify excerpt_id, excerpt_source, excerpt_version are present.
- Verify run_id is valid (generate one if missing).
- If CLI and config both provide metadata:
  - config is the source of truth,
  - continue, but log the mismatch explicitly.
  - set `cli_config_mismatch: true` in the log header.

STOP behavior:
- If any required excerpt field is missing, halt before agents run.
- If run_id is invalid, halt before agents run.
- Emit a short log entry explaining the missing field or mismatch.

---

## 4. Log Header Format and Location

Log outputs must be written under:

- sandbox/crew/run_logs/{excerpt_id}/{run_id}_{timestamp}.log

At minimum, each log header must include:

- excerpt_id
- excerpt_source
- excerpt_version
- run_id
- timestamp
- mode: excerpt-aware

Log headers are documentary; they do not enforce governance.

---

## 5. JSON Output Layout

JSON artefacts must be written under:

- sandbox/crew/run_outputs/{excerpt_id}/{run_id}/

At minimum, the directory contains:

- annotator_primary.json
- challenger_primary.json
- crew_provisional.json
- review_notes.md (optional)

No retro-patching of prior runs. New runs always use a new run_id.

---

## 6. Minimal JSON Schema (Excerpt + Run Blocks)

Each JSON artefact must include both:

- excerpt block (excerpt_id/source/version)
- run block (run_id, timestamp)

Example skeleton:

{
  "excerpt": {
    "id": "sayur_052_066",
    "source": "docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md",
    "version": "locked-2026-01-05"
  },
  "run": {
    "id": "RUN_SAYUR_CASE01_001",
    "timestamp": "2026-01-05T15:49:46Z"
  },
  "items": []
}

If any JSON artefact lacks the excerpt or run block, the run is invalid for evaluation.

---

## 7. Runner Workflow (Step-wise)

1) Pre-flight
   - validate excerpt metadata and run_id
   - STOP on missing metadata or invalid run_id

2) Run
   - execute annotator, challenger, crew as normal

3) Finalize
   - write JSON artefacts with excerpt + run blocks
   - write run log with required header
   - confirm file locations match the layout spec

---

## 8. STOP Mapping (Error Classes)

STOP if:

- missing excerpt_id/source/version
- invalid run_id (missing is allowed if generated)
- log I/O failure
- JSON artefact missing excerpt or run metadata

If any STOP occurs:
- no partial artefacts are treated as valid
- document the failure in the log
- require a clean rerun

---

## 9. Minimal Scope for Case-01

First implementation should support only:

- Case-01 excerpt metadata
- a single excerpt-aware run
- core artefacts (annotator, challenger, crew, log, review notes)

No additional lifecycle or governance changes are permitted in this phase.

---

## 10. Test Matrix (Minimal)

Happy path:
- All metadata present and consistent
- Log header written with excerpt-aware mode
- JSON artefacts created in correct directories

Failure cases:
- Missing excerpt_id
- Mismatched excerpt_version between CLI and config
- Log write failure
- JSON artefact missing excerpt block

Each failure case must STOP before the workflow is considered valid.

---

## 11. Implementation Checklist

- [ ] CLI accepts excerpt_id / excerpt_source / excerpt_version / run_id
- [ ] Pre-flight validation blocks missing metadata or invalid run_id
- [ ] Log header matches required fields and location
- [ ] JSON artefacts written to run output layout
- [ ] Each JSON artefact includes excerpt + run blocks
- [ ] STOP behavior documented and tested
- [ ] Case-01 run executed only after readiness plan conditions are met

---

End of document.
