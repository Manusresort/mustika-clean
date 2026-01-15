# Pilot Run — “²” Review Handoff (P3_MARKER2_REVIEW_HANDOFF_001)
Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Purpose & Constraints
- Demonstrate a human-review handoff for flagged OCR ambiguity cases.
- No text edits, no normalization, no rule enforcement, no glossary changes.
- Input references: docs/PILOT_MARKER2_FLAGGING_RUN_P3_MARKER2_FLAGGING_001.md (read-only).

## Review Table (Decision Logging Only)
| Excerpt (as-is) | Flag type | Reviewer note | Provisional decision type | Rationale |
| --- | --- | --- | --- | --- |
| Bahan2 : | FLAG_REDUPLICATION_RISK | Likely a “²” marker in an ingredient header; confirm layout conventions in adjacent lines. | HISTORICAL_KEEP | Preserve OCR line; treat normalization as a later lifecycle step. |
| Bumbu2 . i sdt. gula merah 4 kg. | FLAG_PUNCTUATION_COLLISION | Mixed punctuation suggests OCR noise; check neighboring lines for header continuity. | DEFER | Punctuation collision makes placement uncertain; needs more context. |
| 1. Nangka di-iris"/diradjang ketjil2. | FLAG_PUNCTUATION_COLLISION | OCR noise ("/) may mask the marker; verify against printed layout before any action. | DEFER | Ambiguity high; keep as-is until verified. |
| 1. Daging ditjutji, di-iris2? berbentuk dadu ketjil. | FLAG_UNCERTAIN_CONTEXT | “?” indicates uncertainty; reviewer should inspect nearby instruction steps. | DEFER | Risk of misreading if normalized; defer to human context check. |
| 3, di-aduk2 sampai masak. | FLAG_REDUPLICATION_RISK | Likely reduplication but punctuation is atypical; confirm whether “3,” is a step marker. | RESTORE_CANDIDATE | Candidate for “²” restoration later, pending lifecycle review. |
| 1. Ketimunditjutji, dipotong udjung?2nja, di-tusuk2 dengan garpu | FLAG_UNCERTAIN_CONTEXT | OCR noise could impact multiple words; evaluate for consistent pattern within recipe. | DEFER | Multiple ambiguities; do not select a normalization yet. |

## Governance Flow (Documentary)
- Trigger: any FLAG_* case from the detection pilot.
- Review packet includes: original OCR line, adjacent lines, source reference, and a note that text is unchanged.
- Provisional decisions are logged only; they do not update OCR text.
- Human Gate required only if a decision would alter canonical text or introduce a normalization policy.
- Rollback remains possible because the pilot stores metadata only; deleting this file fully reverts the run.

[METHODOLOGY_LOG]
Event: P3_MARKER2_REVIEW_HANDOFF_001 review handoff pilot.
Scope: document how ambiguity flags become human review notes and provisional decisions.
Method: copy flagged excerpts verbatim; log review notes without edits.
Result: decision log created; no text modified; no rules enforced.
[/METHODOLOGY_LOG]

[FAILURE_NOTEBOOK]
CaseID: P3_MARKER2_REVIEW_HANDOFF_001_F1
Expected: review-only workflow without normalization.
Observed: temptation to standardize “di-aduk2” into a normalized form was noted.
Mitigation: marked as RESTORE_CANDIDATE only; no changes applied.
Lesson: provisional decisions must remain metadata until lifecycle approval.
[/FAILURE_NOTEBOOK]

Rollback: delete this file to revert the pilot record.

## Consolidation Summary (Phase-3)

**What we validated:**  
Flagged ambiguity can move through a structured human review process where reasoning is documented and outcomes remain provisional — without modifying any text.

**What failed safely:**  
Cases that were tempting to “fix” were explicitly deferred into reviewed decisions (DEFER / HISTORICAL_KEEP / RESTORE_CANDIDATE), preserving reversibility.

**Governance behavior:**  
Review decisions acted as metadata only. Human Gate is triggered only when a decision would change canonical content or create policy. Rollback remains trivial.

**Key insight:**  
Review workflows add value even without automation: they reduce the risk of silent changes and ensure ambiguity is confronted transparently. Metadata must live alongside texts, never written into OCR files.

**Status:** CONSOLIDATED — learning captured, no policies promoted.
