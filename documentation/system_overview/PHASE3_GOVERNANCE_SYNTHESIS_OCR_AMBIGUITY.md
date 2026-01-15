# Phase-3 Governance Synthesis — OCR & Ambiguity

## 1. Scope
This synthesis summarizes Phase-3 pilot learning on OCR ambiguity handling and governance behavior. It captures observations and risks without introducing policy or behavior changes.

## 2. What We Tested (Overview)
- OCR RESTORE: docs/PILOT_OCR_RESTORE_RUN_P3_OCR_RESTORE_001.md
- ²-sampling: docs/PILOT_MARKER2_ANALYSIS_RUN_P3_MARKER2_ANALYSIS_001.md
- ambiguity-flagging: docs/PILOT_MARKER2_FLAGGING_RUN_P3_MARKER2_FLAGGING_001.md
- review-handoff: docs/PILOT_MARKER2_REVIEW_HANDOFF_RUN_P3_MARKER2_REVIEW_HANDOFF_001.md
- escalation / Human Gate: docs/PILOT_MARKER2_ESCALATION_RUN_P3_MARKER2_ESCALATION_001.md

## 3. Patterns We Observed
- OCR ambiguity appears predictable but remains context-dependent.
- Detection without editing reduced the risk of silent normalization.
- Flag metadata increased visibility without altering text.
- Review decisions were clearer when provenance and rationale were logged.

## 4. Where Governance Worked
- Soft-stops prevented premature edits.
- Governance-stops created documentation instead of action.
- Human Gate provided reasoning rather than automatic authority.
- Rollback remained trivial at every step.

## 5. Known Risk Zones (Documentary)
- Mixed punctuation cases
- Structural markers (headers, lists)
- Health-related historical claims
- Terminology conflicts tied to culture/history
- Temptation to “just modernize” during OCR or translation

## 6. Methodology Principles (Phase-3, Not Policy)
- observe → log → annotate → defer
- metadata lives alongside text, not inside it
- ambiguity is documented, not hidden
- humans decide — agents signal

## 7. Implications for Future Phases (Non-binding)
- Tooling may support flagging queues before editing tools.
- Glossary lifecycle benefits from consistent evidence references.
- Research notes should remain first-class artifacts.

## 8. Open Questions (to revisit later)
- When (if ever) should ² normalization be automated?
- How should reviewer disagreement feed into final editions?
- What audit evidence must always accompany Human Gate?

## 9. Rollback Note
Deleting this file fully removes the synthesis.

## Status
EXPERIMENTAL — NOT FOR PUBLICATION
