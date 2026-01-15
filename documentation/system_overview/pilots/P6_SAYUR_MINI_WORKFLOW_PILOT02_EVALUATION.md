# Evaluation — P6 SAYUR Mini Workflow (Pilot 02)

## 1. Context
Date: 2026-01-05  
Run log paths:
- `sandbox/crew/run_logs/P6_PILOT02_SAYUR_MINI_20260105T141836.log`
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
- total_items = 5
- crew_provisional_count = 5
- ready_for_human_count = 0
- escalated_to_human_count = 0
- % provisional = 100%
- % escalated = 0%

## 3. Reasons for Escalation (categorised)
No escalations recorded in this pilot.

## 4. Bias & Behaviour Notes
Challenger issued a GOVERNANCE/WARNING that annotator labels should be Human Gate
decisions. This is logged as a bias/behavior signal; no escalation followed.

## 5. Traceability Check
Each crew decision record includes source span, rationale, decision_status,
and decision_origin. Annotator records include line/span and reason; challenger
record includes issue_type/severity/comment but has an empty span.

## 6. Recommendations (Documentary Only)
- Continue monitoring challenger governance warnings under higher item counts.
- Watch for empty-span entries in agent outputs and how they affect counts.
