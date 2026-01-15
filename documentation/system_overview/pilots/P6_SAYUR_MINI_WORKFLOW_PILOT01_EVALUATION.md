# Evaluation — P6 SAYUR Mini Workflow (Pilot 01)

## 1. Context
Date: 2026-01-05
Run log paths:
- `sandbox/crew/run_logs/P5_MICROPILOT_PROVISIONAL_20260105T135739.log`
- `sandbox/workflows/p6_sayur_mini/annotator_raw.json`
- `sandbox/workflows/p6_sayur_mini/challenger_raw.json`
- `sandbox/workflows/p6_sayur_mini/crew_decisions_provisional.json`
- `sandbox/workflows/p6_sayur_mini/human_review_notes.md`

### Excerpt metadata (Phase-6 note)
Deze pilot is uitgevoerd vóór de introductie van P6_EXCERPT_BINDING_SPEC.
Excerpt_id/source/version zijn daarom niet in de originele run-artefacts aanwezig.
We passen de spec niet retro-actief toe op bestaande logs; toekomstige runs
moeten de excerpt-metadata wel expliciet registreren.

## 2. Lifecycle Outcomes
- total_items = 1
- crew_provisional_count = 1
- ready_for_human_count = 0
- escalated_to_human_count = 0
- % provisional = 100%
- % escalated = 0%

## 3. Observed Escalations
No items were marked READY_FOR_HUMAN_REVIEW; no escalations occurred.

## 4. Bias & Behaviour Notes
Challenger flagged an EQUIVALENT issue at WARNING severity for “Sajuran,”
consistent with translation-expectation pressure noted in prior logs.
Annotator labeled the line as HISTORICAL with text-based rationale.

## 5. Traceability Check
Traceability is partial. The crew decision includes source span, rationale,
decision_status, and decision_origin. The annotator output contains line and
span with a reason, and the challenger output contains span and comment.
The empty-span annotator items (lines 15–17) remain present but do not
feed a crew decision record in this pilot.

## 6. Follow-ups (Documentary Only)
- Note that challenger severity was WARNING for an equivalent signal; log as bias-signal.
- Consider whether empty-span annotator entries should be filtered in future pilots (documentary only).
