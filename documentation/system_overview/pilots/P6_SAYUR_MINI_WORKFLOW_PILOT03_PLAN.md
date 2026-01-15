# Pilot 03 — SAYUR Mini Workflow (Glossary-Critical)

## 1. Purpose
This pilot tests the SAYUR mini-workflow on a glossary-critical excerpt:
a passage where a term is defined, classified, or contextually explained
such that any translation or editorial decision would meaningfully affect
future uses of the term.

## 2. What We Want to Observe
- whether annotator agents correctly flag glossary-relevant spans
- whether challenger agents produce bias signals without blocking
- whether the crew produces at least one
  READY_FOR_HUMAN_REVIEW item with a clear rationale
- whether traceability remains complete across the lifecycle

## 3. Scope & Safety
- sandbox only
- no edits to source
- no publication impact
- decisions remain provisional unless escalated to Human Gate
- escalation, if it happens, is documentary (reasoning only)

## 4. Workflow Reference
This pilot reuses:
- docs/P6_WORKFLOW_SAYUR_MINI.md
- P5_DECISION_LIFECYCLE.md
- PRODUCTION_GUARDRAILS_P5.md

## 5. Success Criteria (Documentary)
The pilot counts as successful if:
- glossary-relevant material is detected
- at least one item reasonably ends up READY_FOR_HUMAN_REVIEW
- logs clearly show why escalation occurred (if it does)
- no canonical decisions are made automatically

## 6. Out-of-Scope
- no glossary publication
- no translation locking
- no repo restructuring

## 7. Expected Outputs
- excerpt selection record
- annotator + challenger raw JSON
- crew_decisions_provisional.json
- human review notes (if any)
- evaluation document

This pilot is evidence-building, not policy-changing.

## Status

Status: INCONCLUSIVE

Outcome:
Pilot 03 did not run on the intended glossary-critical excerpt (lines ~118–132).
The runner reused the earlier Golongan VI / Sajuran excerpt, producing behaviour equivalent to Pilot 01.
This indicates a workflow binding issue (excerpt not governed as an explicit input), not an agent failure.
