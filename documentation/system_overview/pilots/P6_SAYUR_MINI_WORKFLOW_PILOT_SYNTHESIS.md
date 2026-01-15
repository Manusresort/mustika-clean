# P6 Synthesis — SAYUR Mini Workflow (Pilots 01–02)

## 1. Scope
- Pilot 01 used the Golongan VI / Sajuran mini-excerpt.
- Pilot 02 used the locked lines 52–66 excerpt (“Ada sajuran jang tak tahan hudjan … ketimun, lobak, … bajem”).

## 2. Lifecycle Comparison
Pilot 01:
- total_items = 1
- crew_provisional_count = 1
- ready_for_human_count = 0
- escalated_to_human_count = 0

Pilot 02:
- total_items = 5
- crew_provisional_count = 5
- ready_for_human_count = 0
- escalated_to_human_count = 0

Interpretation: CREW_PROVISIONAL remained dominant across both pilots; no READY_FOR_HUMAN_REVIEW items appeared.

## 3. Agent Behaviour Patterns
- Annotator: conservative labeling overall; Pilot 01 used HISTORICAL on the line-level excerpt, Pilot 02 used a single GLOSSARY label (“bajem”) with otherwise NONE/HISTORICAL labels.
- Challenger: Pilot 01 showed translation-expectation signaling (EQUIVALENT/WARNING). Pilot 02 showed a GOVERNANCE/WARNING about label use.

## 4. Bias Catalogue (Documentary Only)
- translation-expectation (EQUIVALENT/WARNING): treated as a signal, not an error; indicates possible reviewer attention without requiring escalation.
- governance overreach (GOVERNANCE/WARNING on annotator labeling): treated as a signal; used to note model bias toward Human Gate framing, not as a decision trigger.

## 5. Traceability & Workflow Health
- Pilot 01: crew decision record included span/rationale/lifecycle/origin; annotator and challenger logs included line/span and comments, with empty-span annotator items noted but not promoted to decisions.
- Pilot 02: crew decision records included span/rationale/lifecycle/origin; challenger record included issue_type/severity/comment with empty span.

In latere Phase-6 documentatie is deze binding-gap expliciet geadresseerd
in P6_EXCERPT_BINDING_SPEC.md, waarin excerpt_id/source/version als
verplichte documentaire velden zijn vastgelegd voor toekomstige runs.

Documentary judgement: mini workflow is stable under small-scale load.

## 6. Recommendations for Next Steps (Phase-6)
- Consider a glossary-critical Pilot 03 focusing on a definitional passage.
- Consider a culture/health-claim Pilot 04 to test risk escalation.
- Use the SAYUR mini workflow pattern as a template for other chapters.
