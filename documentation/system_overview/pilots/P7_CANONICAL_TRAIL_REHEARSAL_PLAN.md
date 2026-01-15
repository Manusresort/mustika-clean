# Phase-7 — Canonical Trail Rehearsal Plan (Dry-Run)

## Purpose

This rehearsal tests the canonical-decision lifecycle
without producing any real canonical decisions.

We verify that the full trail works end-to-end:

source → excerpt → run → AI proposal → human review → decision record → rollback.

The outcome of this rehearsal is **DISCARD** — it is not part of the real editorial history.

---

## Scope & Constraints

- uses one existing excerpt and one existing AI artefact
- no content changes to the scholarly edition
- no real promotion to CANONICAL
- rollback must be demonstrated explicitly
- everything is documented as a pilot

---

## Candidate Excerpt (confirmed)

- excerpt_id: lobak_034_048  
- excerpt_source: docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md  
- excerpt_version: locked-2026-01-12  

Selected artefacts for rehearsal:

- annotator JSON:  
  sandbox/crew/run_outputs/lobak_034_048/RUN_lobak_034_048_20260106T220558/annotator_primary.json
- challenger JSON:  
  sandbox/crew/run_outputs/lobak_034_048/RUN_lobak_034_048_20260106T220558/challenger_primary.json
- run log:  
  sandbox/crew/run_logs/lobak_034_048/RUN_lobak_034_048_20260106T220558_20260106T220558.log

Notes:
This excerpt was chosen because the runner, mapping, artefacts,
and reflections are already stable, making it ideal for lifecycle rehearsal.

---

## Rehearsal Flow (Checklist)

### 1) Select Artefact
- identify run_id and JSON files
- verify excerpt metadata
- log selection decision

### 2) Create Provisional Decision Draft
- simulate a decision record using the Phase-7 schema
- clearly mark status: **REHEARSAL_ONLY**

### 3) Link into Trail
- add references (excerpt + artefacts)
- verify traceability from index → record → run

### 4) Rollback Simulation
- create a superseding record that cancels the rehearsal result
- confirm earlier record remains in archive (no deletion)

### 5) Reflection
- note any gaps in schema, workflow, or archive structure

---

## Success Criteria

Rehearsal is considered successful if:

- no ambiguity exists in the excerpt trail
- every artefact can be located via documented links
- rollback produces a NEW record instead of overwriting
- documentation clearly shows each state transition

---

## Risks & Watchpoints

- confusion between rehearsal and real canonical decisions
- accidental promotion to CANONICAL
- human review notes missing or unlinked
- excerpt metadata drift

If any of these occur, stop, document, and treat as design feedback.

---

## Output of This Pilot

This pilot must produce:

- one rehearsal decision record
- one rollback decision record
- a short reflection note
- updates to indices only if they improve clarity (never to store rehearsal results)

---

## Reflection (after rehearsal)

### What worked

- excerpt-binding remained consistent and visible through every step  
- rehearsal decision records were easy to trace back to runs and logs  
- rollback via NEW record (not overwrite) felt clear and safe  
- there was no realistic path for accidental auto-promotion to CANONICAL

### What felt fragile or manual

- decision records require careful metadata entry and cross-links  
- small mistakes could make records hard to trace  
- indexes must stay disciplined: no silent edits, always additive  
- reviewers must remain aware that rehearsal files are not canonical

### Suggested design refinements (future work)

- optional helper for generating decision-record templates  
- validation checklist (pre-merge) for canonical records  
- visible label for rehearsal vs real records in the navigation index  
- keep refining decision-types matrix as real editorial questions appear

---

END OF FILE
