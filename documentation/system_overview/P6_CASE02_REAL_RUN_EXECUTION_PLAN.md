---
# Phase-6 — Case-02 Real Run Execution Plan (LOBAK)

Status: PENDING — excerpt not yet chosen  
Related: P6_LOBAK_INTERNAL_WORK_CASE02.md, P6_EDITORIAL_WORKFLOW_MINI.md,  
P6_EXCERPT_BINDING_SPEC.md, P6_RUNNER_OUTPUT_LAYOUT.md

## 1. Purpose

This document describes how the first real excerpt-aware sandbox run
for Case-02 (LOBAK) should be executed once the excerpt is chosen.

It mirrors P6_CASE01_REAL_RUN_EXECUTION_PLAN.md, but keeps the excerpt
parameters as placeholders until we lock LOBAK lines.

## 2. Planned CLI invocation (excerpt-aware)

```bash
python sandbox/crew/run_excerpt_workflow.py \
  --config sandbox/crew/CASE02_LOBAK_CONFIG_TBD.yaml \
  --excerpt-id lobak_034_048 \
  --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md \
  --excerpt-version locked-2026-01-12
```

The config file remains TBD; excerpt metadata is locked.

Note: excerpt-metadata is documentary, not enforcing.  
Mismatch = STOP & document, not fix silently.

## 3. Logging and outputs (excerpt-aware)

The first Case-02 run is expected to:

create a log under: sandbox/crew/run_logs/{excerpt_id}/...

create JSON outputs under:
sandbox/crew/run_outputs/{excerpt_id}/{run_id}/...

The exact excerpt_id will be defined after excerpt selection.

## 4. Execution checklist (to be filled later)

- [ ] Excerpt metadata (id/source/version) is final.
- [ ] Config file for Case-02 exists and is committed.
- [ ] Dry-run or pre-flight checks have been done.
- [ ] First real run executed and logged.
- [ ] Outputs verified against P6_RUNNER_OUTPUT_LAYOUT.md.

(Do not execute this plan until the readiness checklist is satisfied.)
---

## Excerpt-Aware Execution Shape (documentary)

This plan does not authorize execution. It records how
an excerpt-aware Case-02 run is expected to be invoked
once governance explicitly approves a real run.

### Example CLI (shape only)

```bash
python sandbox/crew/run_excerpt_workflow.py \
  --excerpt-id lobak_034_048 \
  --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md \
  --excerpt-version locked-2026-01-12 \
  --config sandbox/crew/configs/lobak_case02.yaml
```

## Expected Layout (Phase-6)

Logs:
sandbox/crew/run_logs/lobak_034_048/{run_id}_{timestamp}.log

Outputs (JSON):
sandbox/crew/run_outputs/lobak_034_048/{run_id}/
annotator_primary.json
challenger_primary.json
(optional) crew_provisional.json
review_notes.md
run_metadata.json (recommended)

## Payload Contract (runner refinement)

Each JSON artefact contains:

excerpt { id, source, version }

run { id, timestamp }

raw_output (full console/TUI)

payload (structured JSON) OR null if parsing fails

Parsing failures MUST be logged as WARN but are acceptable.

## Stop Conditions

excerpt metadata mismatch anywhere → STOP & document

missing excerpt fields → STOP

any attempt to silently change metadata → record incident, do not proceed

This section is documentary only and introduces no runtime changes.
