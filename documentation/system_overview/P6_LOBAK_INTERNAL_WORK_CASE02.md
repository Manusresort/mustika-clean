# Phase-6 — LOBAK Internal Workflow — Case 02

Status: PENDING — excerpt not yet chosen  
Related: P6_EDITORIAL_WORKFLOW_MINI.md, P6_EXCERPT_BINDING_SPEC.md,  
P6_CASE01_READINESS_PLAN.md, docs/navigation/EDITORIAL_INDEX.md

---

## 1. Purpose

Case-02 exists to prove that the Phase-6 editorial mini-workflow:

- applies to **any** chapter (not only SAYUR),
- supports excerpt-aware logging from the start,
- keeps all outputs provisional and traceable.

This case is **design-only** until excerpt metadata is locked.

---

## 2. Excerpt Selection Will Be Locked Later

For LOBAK, the excerpt is **not yet chosen**.

Before Case-02 can move forward, we will create:

- an excerpt selection file under `docs/pilots/`,
- with fields:
  - excerpt_id (e.g., `lobak_0XX_0YY`)
  - excerpt_source (path to the selection file)
  - excerpt_version (locked-YYYY-MM-DD)

Rule:

> No artefacts are produced until this metadata is explicit.

---

## 3. Lifecycle Expectations

Case-02 follows the same lifecycle:

CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL

Clarifications:

- agents only produce **provisional** outputs,
- promotion beyond provisional requires human review,
- canonical outcomes are **out of scope** for this case.

---

## 4. Excerpt-Aware Preconditions

Case-02 may not run until:

- CLI/config explicitly passes excerpt_id/source/version,
- logs record the same values,
- JSON artefacts embed them consistently.

If any field is missing:

> Case-02 stays pending — run may exist only as sandbox noise.

---

## 5. Alignment With Case-01

Case-02 mirrors Case-01, but ensures generality:

- same excerpt-binding discipline,
- same readiness logic,
- no chapter-specific shortcuts.

When differences arise, they are documented — not improvised.

---

## 6. What This Case Does NOT Do

Case-02 does NOT:

- produce canonical glossary entries,
- translate text,
- bypass Human Gate,
- enforce runtime behavior.

It coordinates documentation and safe preparation only.

---

## 7. Current Status

- excerpt not chosen,
- no runs expected,
- index entry pending.

Case-02 remains PENDING until excerpt metadata is locked and reviewed.

---

End of document.

---

## 8. Runner mapping status (Phase-6, documentary)

### 8.1 Current state (after two shakedown runs)

- Excerpt-binding works as intended for LOBAK:
  - excerpt_id: lobak_034_048
  - excerpt_source: docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md
  - excerpt_version: locked-2026-01-12
- Case-02 config exists:
  - sandbox/crew/configs/lobak_case02.yaml
- Two excerpt-aware shakedown runs have been executed:

  1) First run:
     - failure reason: config path not found
     - lesson: LOBAK config did not exist yet.
  2) Second run:
     - failure reason: “No runner script found for YAML config: sandbox/crew/configs/lobak_case02.yaml”
     - lesson: LOBAK pipeline/runner mapping is not implemented, while excerpt-binding + logging are correct.

No JSON artefacts have been produced yet for LOBAK. This is intentional at this stage.

### 8.2 Desired mapping (conceptual, no code)

For a future implementation, this case requires a mapping from:

- config: sandbox/crew/configs/lobak_case02.yaml

to a concrete runner/pipeline that can:

- invoke annotator_primary and challenger_primary for excerpt lobak_034_048,
- write excerpt-aware JSON artefacts under:
  - sandbox/crew/run_outputs/lobak_034_048/{run_id}/
- write an excerpt-aware log under:
  - sandbox/crew/run_logs/lobak_034_048/{run_id}_{timestamp}.log

The mapping pattern should mirror whatever is used for the successful SAYUR Case-01 run
(e.g. how sayur_case01 or shakedown_sayur configs are wired to a CrewAI runner),
but with LOBAK-specific config and excerpt metadata.

### 8.3 Out of scope (Phase-6 boundary)

This section is documentary:

- it does NOT define actual Python or CrewAI code,
- it does NOT authorize new runs,
- it ONLY records that:
  - LOBAK Case-02 is ready at the excerpt + config level,
  - the remaining gap is implementation of the runner script mapping
    for sandbox/crew/configs/lobak_case02.yaml.

Once a mapping exists and is approved, a new shakedown run should be planned
to validate the full pipeline end-to-end.

---
