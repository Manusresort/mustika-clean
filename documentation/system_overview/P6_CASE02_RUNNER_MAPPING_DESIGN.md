# Phase-6 — Case-02 Runner Mapping Design (LOBAK)

Status: DESIGN — documentary, non-enforcing  
Related: P6_EXCERPT_AWARE_RUNNER_DESIGN.md,  
P6_EXCERPT_AWARE_RUNNER_IMPLEMENTATION_GUIDE.md,  
P6_LOBAK_INTERNAL_WORK_CASE02.md,  
P6_CASE02_READINESS_PLAN.md,  
P6_CASE02_REAL_RUN_EXECUTION_PLAN.md,  
P6_CASE02_VALIDATION_PLAN.md

---

## 1. Purpose

Case-02 (LOBAK) has:

- a locked excerpt (lobak_034_048),
- a documented readiness/execution/validation plan,
- a sandbox config at: sandbox/crew/configs/lobak_case02.yaml,

but the generic runner currently reports:

> “No runner script found for YAML config: sandbox/crew/configs/lobak_case02.yaml”

The purpose of this document is to describe how this config SHOULD be
mapped to a concrete runner/pipeline, following the Case-01 pattern,
so that future implementation work has a clear target and can be
governed explicitly.

This document does not define or modify any Python or CrewAI code.

---

## 2. Context — what worked for Case-01

Case-01 (SAYUR) established that:

- excerpt-aware runs use:
  - run_excerpt_workflow.py as the entry point,
  - a dedicated YAML config for the case (e.g. sayur_case01 or a
    shakedown config),
- the runner then dispatches to a CrewAI / pipeline definition that:
  - runs annotator + challenger (and optionally crew),
  - writes excerpt-aware JSON artefacts under:
    sandbox/crew/run_outputs/{excerpt_id}/{run_id}/
  - writes an excerpt-aware log under:
    sandbox/crew/run_logs/{excerpt_id}/{run_id}_{timestamp}.log

Case-02 should mirror this pattern, but with LOBAK-specific config
and excerpt metadata.

---

## 3. Desired mapping for LOBAK Case-02

### 3.1 Input config

Primary config for Case-02:

- sandbox/crew/configs/lobak_case02.yaml

Current minimal shape (as of design):

- run_id: RUN_lobak_034_048_case02_001
- mode: sandbox
- excerpt:
  - id: lobak_034_048
  - source: docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md
  - version: locked-2026-01-12
- pipeline:
  - agents:
    - annotator_primary
    - challenger_primary

### 3.2 Mapping requirement (conceptual)

At runtime, the excerpt-aware runner must be able to:

- recognise sandbox/crew/configs/lobak_case02.yaml as a valid config,
- map it to a concrete runner/pipeline that:
  - invokes annotator_primary and challenger_primary for excerpt lobak_034_048,
  - uses the same general orchestration pattern as Case-01,
  - writes excerpt-aware JSON and logs that satisfy the Phase-6 contracts.

This mapping may be implemented via:

- a dispatch table,
- a naming convention,
- or a dedicated loader,

but in all cases it must be:

- explicit,
- testable,
- and documented in the runner implementation notes.

---

## 4. Expected runtime behaviour (once implemented)

Once a mapping exists, a Case-02 run with:

```bash
python sandbox/crew/run_excerpt_workflow.py \
  --excerpt-id lobak_034_048 \
  --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md \
  --excerpt-version locked-2026-01-12 \
  --config sandbox/crew/configs/lobak_case02.yaml
```

should result in:

A log under:

sandbox/crew/run_logs/lobak_034_048/{run_id}_{timestamp}.log

containing:

mode: excerpt-aware

excerpt_id/source/version

run_id, started_at, status

warnings/errors (including JSON parse warnings if any)

JSON artefacts under:

sandbox/crew/run_outputs/lobak_034_048/{run_id}/

including at minimum:

annotator_primary.json

challenger_primary.json

Each JSON must contain:

excerpt { id, source, version }

run { id, timestamp }

raw_output (full console/TUI)

payload (structured) OR null if parsing fails.

Optional:

crew_provisional.json

review_notes.md

run_metadata.json

## 5. Lifecycle & governance constraints

The mapping implementation must:

not promote any decision beyond CREW_PROVISIONAL,

not introduce CANONICAL states,

keep all outputs sandbox-only,

respect STOP-on-mismatch for excerpt metadata (no silent fixes),

treat JSON parse failures as WARN + payload=null, not as success.

Any new runtime behaviour must be:

traceable to this design,

documented in CODEX_SESSION_LOG.md,

and, if relevant, included in P6_CASE02_VALIDATION_PLAN.md.

## 6. Out of scope (Phase-6 boundary)

This design does NOT:

implement the mapping in code,

approve runtime changes,

schedule shakedown runs.

It only defines the expected relationship between:

lobak_case02.yaml (config),

the excerpt-aware runner,

and the resulting artefacts.

Implementation requires a separate governance decision.

End of document.
