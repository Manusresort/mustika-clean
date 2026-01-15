# P6 — SAYUR Mini Workflow (Excerpt → Crew-Provisional)

## 1. Scope & Principles
Document-first, sandbox-only workflow for a single SAYUR excerpt; no publication impact.
Decisions remain reversible and challengeable; most outputs should land at CREW_PROVISIONAL,
with Human Gate reserved for selective cases (see `docs/PRODUCTION_GUARDRAILS_P5.md`
and `docs/P5_DECISION_LIFECYCLE.md`). No repo structure changes or moves (see
`docs/GOVERNANCE_BOUNDARIES_NOTE.md`).

## 2. Roles and Autonomy
Annotator produces CANDIDATE_TRANSLATION proposals only; Challenger flags rule-violations
and risks without resolving them (see `docs/P5_AGENT_BEHAVIOUR_CRITERIA.md`). The crew-synthesizer
aggregates annotator + challenger outputs into a CREW_PROVISIONAL trace, with rationale logged.
Codex/meta orchestrates and may reopen weak rationale but does not set CANONICAL; Human Gate
remains the only path to CANONICAL (see `docs/PRODUCTION_GUARDRAILS_P5.md`
and `docs/P5_DECISION_LIFECYCLE.md`).

## 3. Inputs and Outputs (Contracts)
Inputs: locked excerpt + provenance references + run metadata. Outputs: strict JSON; no free-form
decisions outside lifecycle fields (see `docs/WORKFLOW.md` and `docs/P5_DECISION_LIFECYCLE.md`).
Required lifecycle fields:
- `decision_status` (CANDIDATE_TRANSLATION / CREW_PROVISIONAL / READY_FOR_HUMAN_REVIEW)
- `decision_origin` (agent / crew / meta / human)
- `ready_for_human_review` (true/false)
Also required per guardrails: `rationale_logged` and `challenge_open` or `reopen_possible`
(see `docs/PRODUCTION_GUARDRAILS_P5.md`).

Pseudo-JSON example (annotator proposal):
```json
{
  "run_id": "<run_id>",
  "excerpt_id": "<excerpt_id>",
  "decision_status": "CANDIDATE_TRANSLATION",
  "decision_origin": "agent",
  "ready_for_human_review": false,
  "rationale_logged": true,
  "annotations": [
    {
      "line_id": "<line_id>",
      "label": "GLOSSARY",
      "reason": "<text-evidence>"
    }
  ]
}
```

Pseudo-JSON example (crew-provisional trace):
excerpt_source is recorded at the document or run-notes level,
while excerpt_id and excerpt_version are included in each decision record.
```json
{
  "run_id": "<run_id>",
  "term_id": "<term_id>",
  "excerpt_id": "<excerpt_id>",
  "excerpt_version": "<excerpt_version>",
  "decision_status": "CREW_PROVISIONAL",
  "decision_origin": "crew",
  "ready_for_human_review": false,
  "rationale_logged": true,
  "challenge_open": true,
  "crew_trace": {
    "annotations": "<annotator_output_ref>",
    "challenges": "<challenger_output_ref>",
    "provisional_notes": "<crew_rationale>"
  }
}
```

## 4. Step-by-Step Workflow
1) Annotator produces CANDIDATE_TRANSLATION proposals with text-evidence.
2) Challenger reviews for rule-violations/risks and logs issues without fixing them.
3) Crew-synthesizer merges annotator + challenger outputs into a CREW_PROVISIONAL trace
   (rationale + links to both outputs). Most decisions should stop here.
4) Only when criteria in Section 5 apply does the crew mark READY_FOR_HUMAN_REVIEW
   (no automatic promotion to CANONICAL).

Expected failure modes are logged, not suppressed: translation-expectation bias and
over-escalation severity (see `docs/P5_TRANSLATION_EXPECTATION_EVIDENCE.md`
and `docs/P5_MICROPILOT_FOLLOWUP_NOTES.md`).

## 5. Escalation Rules
Escalate to Human Gate selectively when criteria in
`docs/10-governance/HUMAN_GATE_POLICY_P4_SANDBOX.md` and
`docs/PRODUCTION_GUARDRAILS_P5.md` apply. Typical triggers:
- safety / harm / legal risk
- cultural or historical impact with publication relevance
- glossary or meaning decisions with downstream impact
- unresolved ambiguity or policy conflict
- any action implying structural repo change (see `docs/GOVERNANCE_BOUNDARIES_NOTE.md`)

Do not escalate for normal uncertainty or routine wording nuance; keep those at
CREW_PROVISIONAL with rationale logged (see `docs/PRODUCTION_GUARDRAILS_P5.md`).

## 6. Logging Requirements
Each step logs run ID, provenance, inputs, outputs, and lifecycle fields
(`decision_status`, `decision_origin`, `ready_for_human_review`, plus `rationale_logged`
and `challenge_open`/`reopen_possible`). Logs must preserve traceability and reversibility
per `docs/WORKFLOW.md`. Known failure modes (translation-expectation bias,
over-escalation) must be recorded as signals, not suppressed.

## 7. Repo Mapping (document-only)
All artefacts map to `sandbox/workflows/p6_sayur_mini/*` for traceability
(documented only; no file moves or restructuring).

## 8. Definition of Done
Workflow executed with majority CREW_PROVISIONAL outputs, minimal escalations, and complete logs.
The pilot demonstrates at least one clear CREW_PROVISIONAL promotion (see
`docs/P5_MICROPILOT_FOLLOWUP_NOTES.md`), and all observed biases/overreach are logged
as signals without policy changes.
