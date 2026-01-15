---
# Phase-6 — Case-02 Readiness Plan (LOBAK)

Status: PENDING — excerpt not yet chosen  
Related: P6_LOBAK_INTERNAL_WORK_CASE02.md, P6_EXCERPT_BINDING_SPEC.md,  
P6_EDITORIAL_WORKFLOW_MINI.md, docs/navigation/EDITORIAL_INDEX.md

## 1. Purpose

This document defines when Case-02 (LOBAK) is allowed to move from
"design/pending" into an actual excerpt-aware sandbox run.

It mirrors the structure of P6_CASE01_READINESS_PLAN.md but keeps the
excerpt technical details explicitly pending until a LOBAK excerpt is locked.

## 2. Preconditions (high-level)

Case-02 may only run when:

- a LOBAK excerpt has been explicitly chosen and locked,
- excerpt_id / excerpt_source / excerpt_version have been recorded
  according to P6_EXCERPT_BINDING_SPEC.md,
- CLI/config, logs, and JSON artefacts are aligned on excerpt metadata,
- the runner and output layout follow the same Phase-6 excerpt-aware design
  as Case-01.

## 3. Excerpt binding (Phase-6)

excerpt_id: lobak_034_048  
excerpt_source: docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md  
excerpt_version: locked-2026-01-12  

Note: excerpt-metadata is documentary, not enforcing.  
Mismatch = STOP & document, not fix silently.

## 4. Readiness checklist (to be filled once excerpt is chosen)

- [ ] Excerpt chosen and documented in LOBAK governing document.
- [ ] Excerpt locked with explicit excerpt_id, excerpt_source, excerpt_version.
- [ ] Runner config prepared for Case-02 (LOBAK).
- [ ] Logging and JSON output paths verified for the new excerpt_id.
- [ ] Human Gate acknowledges that Case-02 is allowed to run in sandbox.

(Do not mark items as complete until a real excerpt and config exist.)
---

## Phase-6 Readiness — Concrete Checklist (Case-02, LOBAK)

### Inputs (locked before run)
- excerpt_id: lobak_034_048
- excerpt_source: docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md
- excerpt_version: locked-2026-01-12
- governing source excerpt (LOBAK) — scholarly copy (read-only)
- runner script: sandbox/crew/run_excerpt_workflow.py
- config file: sandbox/crew/configs/lobak_case02.yaml (design placeholder)

### Expected Outputs (excerpt-aware)
- annotator_primary.json (excerpt + run + raw_output + payload|null)
- challenger_primary.json (excerpt + run + raw_output + payload|null)
- run log under sandbox/crew/run_logs/lobak_034_048/
- structured outputs under sandbox/crew/run_outputs/lobak_034_048/{run_id}/
- optional: crew_provisional.json and review_notes.md

### Stop Criteria (pre-agreed)
- excerpt_id/source/version mismatch → STOP & document
- missing excerpt metadata → STOP
- parsing failure of payload → allowed, must log [WARN]; payload=null

### Review Path (after run, before any decisions)
1) verify excerpt-binding across log + JSON
2) inspect annotator + challenger payloads
3) crew synthesizes provisional trace (no canonization)
4) reflection document only — not a decision log

This section is documentary and does not authorize execution.
