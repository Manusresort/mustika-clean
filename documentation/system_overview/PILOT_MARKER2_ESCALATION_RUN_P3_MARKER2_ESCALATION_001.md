# Pilot Run — “²” Escalation Simulation (P3_MARKER2_ESCALATION_001)
Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Scenario Overview
This pilot simulates a disagreement between two reviewers over flagged “²-derived” OCR ambiguity cases. No text is edited; all outcomes are provisional and documentary.

## Selected Flagged Excerpts (Reference Only)
- “Bahan2 :” (from docs/PILOT_MARKER2_FLAGGING_RUN_P3_MARKER2_FLAGGING_001.md)
- “1. Daging ditjutji, di-iris2? berbentuk dadu ketjil.” (from docs/PILOT_MARKER2_FLAGGING_RUN_P3_MARKER2_FLAGGING_001.md)

## Disagreement Scenario
### Case A — “Bahan2 :”
- Reviewer A (RESTORE_CANDIDATE): Likely a “²” marker in a header; restoration to the printed marker seems low-risk but should still follow lifecycle review.
- Reviewer B (HISTORICAL_KEEP): Keep OCR line unchanged; any normalization, even to “²”, should wait for a verified scan comparison.

### Case B — “di-iris2?”
- Reviewer A (RESTORE_CANDIDATE): Could be a simple reduplication marker with OCR noise; treat as a future restoration candidate.
- Reviewer B (DEFER): The “?” indicates uncertainty; defer until context and printed source confirm placement.

## Escalation Record
- Trigger: conflicting provisional decisions between reviewers.
- Action: cases are queued to governance review with both rationales and the original OCR lines attached.
- Status: no edits; decisions remain provisional.

## Human Gate Stage (Simulated)
### Options Considered
- STAY_DEFERRED
- APPROVE_RESTORE_AS_FUTURE_CANDIDATE
- REQUIRE_RESEARCH_NOTE

### Risks Discussed
- Premature normalization may alter historical fidelity.
- Mixed punctuation can mask where the marker truly belongs.
- “²” is a format signal; restoring it without confirmation risks introducing editorial interpretation.

### Provisional Outcome (Documentary)
- Case A: REQUIRE_RESEARCH_NOTE (verify printed header formatting before any restoration candidate is accepted).
- Case B: STAY_DEFERRED (ambiguity too high without additional context).

## Governance Notes
- Reviewers can log provisional decisions only.
- Human Gate can authorize future lifecycle steps, but does not modify text in this pilot.
- Rollback is trivial because no content is altered and all records are documentary.

[METHODOLOGY_LOG]
Event: P3_MARKER2_ESCALATION_001 escalation simulation.
Scope: model disagreement handling and Human Gate escalation for ambiguity flags.
Method: documentary-only; no edits, no automation, no policy changes.
Result: escalation pathway demonstrated; outcomes remain provisional.
[/METHODOLOGY_LOG]

[FAILURE_NOTEBOOK]
CaseID: P3_MARKER2_ESCALATION_001_F1
Expected: escalation records only, no decisions applied to text.
Observed: temptation to resolve Case A immediately was noted.
Mitigation: routed to Human Gate with REQUIRE_RESEARCH_NOTE; no edits made.
Lesson: disagreement must trigger escalation, not quick fixes.
[/FAILURE_NOTEBOOK]

Rollback: delete this file to revert the pilot record.

## Consolidation Summary (Phase-3)

What we validated:
Reviewer disagreement on ambiguous “²-derived” cases can be handled through a structured escalation path and Human Gate discussion, with all outcomes kept provisional and no text changes applied.

What failed safely:
Temptations to “just decide” were redirected into documented outcomes (STAY_DEFERRED, RESTORE_CANDIDATE, REQUIRE_RESEARCH_NOTE) instead of silent corrections.

Governance behavior:
Escalation was triggered only by conflicting provisional decisions. Human Gate operated as a forum for reasoning, not as an automatic policy engine. All decisions remained metadata; rollback stayed trivial.

Key insight:
Disagreement is a feature, not a bug, when it is documented and escalated transparently. Human Gate must always be tied to explicit evidence (e.g., scans, research notes) before any future normalization is even considered.

Status: CONSOLIDATED — learning captured, no policies promoted.
