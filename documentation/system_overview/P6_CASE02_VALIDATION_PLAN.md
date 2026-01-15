Phase-6 — Case-02 Validation Plan (LOBAK)
Status: PENDING — excerpt not yet chosen
Related: P6_LOBAK_INTERNAL_WORK_CASE02.md, P6_CASE02_READINESS_PLAN.md,
P6_RUNNER_OUTPUT_LAYOUT.md, P6_RUNNER_PAYLOAD_REFINEMENT_DESIGN.md

Excerpt binding (Phase-6):

excerpt_id: lobak_034_048  
excerpt_source: docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md  
excerpt_version: locked-2026-01-12  

Note: excerpt-metadata is documentary, not enforcing.  
Mismatch = STOP & document, not fix silently.

1. Purpose
This document describes how we will validate the first excerpt-aware
sandbox run for Case-02 (LOBAK), once it happens.

It mirrors P6_CASE01_VALIDATION_PLAN.md with LOBAK-specific context.

2. Validation dimensions
We will validate:

Excerpt-awareness

logs show the correct LOBAK excerpt_id/source/version

JSON artefacts carry the same metadata

Runner layout

run_logs and run_outputs follow the Phase-6 layout

run_id is consistent between log and JSON

Payload structure

excerpt and run blocks are present

raw_output exists and contains the full console/TUI trace

payload is either:

a clean structured value (for successful parsing), or

null with a documented warning in the log

Lifecycle integrity

outputs remain provisional / sandbox

no accidental promotion to canonical

all decisions (if any) respect the Decision Lifecycle docs

3. Validation checklist (to be used after the first run)
- [ ] Excerpt metadata matches across CLI, logs, and JSON.
- [ ] Paths and filenames match P6_RUNNER_OUTPUT_LAYOUT.md.
- [ ] JSON validates and contains the required fields.
- [ ] Any parse warnings are documented and understood.
- [ ] A human reflection (LOBAK case) is written using the
  P6_CASE_REFLECTION_TEMPLATE.md as a guide.
- [ ] Results logged in CODEX_SESSION_LOG.md.

(Do not complete this checklist until there has been at least one
real Case-02 run.)

## Phase-6 Validation — What Counts as Success (Case-02)

Validation is workflow-first, not translation-first.
Case-02 is considered successful when the following hold:

### 1) Excerpt Traceability
- Every artefact (log + JSON) repeats:
  excerpt_id: lobak_034_048,
  excerpt_source,
  excerpt_version.
- Values match the governing selection document.
- Any mismatch is documented and halts further steps.

Evidence: annotator/challenger JSON, run log.

### 2) Runner Output Layout
- Outputs live under:
  sandbox/crew/run_outputs/lobak_034_048/{run_id}/
- Logs live under:
  sandbox/crew/run_logs/lobak_034_048/

Evidence: directory tree + file names.

### 3) Payload Refinement
- Each JSON artefact contains:
  raw_output (full console),
  payload (structured) OR null.
- If payload=null, the run log shows a parse warning.

Evidence: annotator/challenger JSON + log excerpt.

### 4) Lifecycle Discipline
- Annotator outputs are CANDIDATE / proposal-only.
- Challenger flags issues without resolving them.
- Crew (if present) writes CREW_PROVISIONAL only.
- Nothing is marked CANONICAL.

Evidence: lifecycle fields in JSON.

### 5) Review Path
- Review notes exist separately from decisions.
- A reflection document summarizes behaviour and risks.
- No hidden edits to artefacts after the run.

Evidence: review_notes.md, reflection doc.

### 6) Rollback & Supersession
- Old runs remain untouched.
- A newer run supersedes instead of mutating the old.
- Documentation explains why a rerun happened.

Evidence: run directories + session log.

If the above are satisfied, Case-02 passes Phase-6 validation,
even if the translation or annotations are imperfect.

This section is documentary and does not authorize execution.
