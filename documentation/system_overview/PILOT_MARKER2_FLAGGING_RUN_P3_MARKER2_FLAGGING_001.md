# Pilot Run — “²” Ambiguity Flagging (P3_MARKER2_FLAGGING_001)
Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Purpose & Constraints
- Detect likely ambiguous “²-derived” OCR cases and flag them as REVIEW_REQUIRED (metadata only).
- No text edits, no normalization, no rule enforcement, no glossary changes.
- Source corpus: sandbox/legacy_imports/ocr_samples/ (read-only).

## Flag Table (Detection Only)
| Excerpt (as-is) | Source | Flag type | Why auto-fix is risky |
| --- | --- | --- | --- |
| Bahan2 : | sandbox/legacy_imports/ocr_samples/RB-0019.txt:357 | FLAG_REDUPLICATION_RISK | Could be a “²” marker; expanding or replacing without context could change format conventions. |
| Bumbu2 . i sdt. gula merah 4 kg. | sandbox/legacy_imports/ocr_samples/RB-0019.txt:1405 | FLAG_PUNCTUATION_COLLISION | Mixed punctuation makes it unclear where the marker belongs; auto-fix could alter spacing or meaning. |
| 1. Nangka di-iris"/diradjang ketjil2. | sandbox/legacy_imports/ocr_samples/RB-0018.txt:6557 | FLAG_PUNCTUATION_COLLISION | OCR punctuation noise ("/) overlaps with the “2” marker; auto-fix might misplace the reduplication cue. |
| 3. Di-potong2 serong. | sandbox/legacy_imports/ocr_samples/RB-0018.txt:8403 | FLAG_REDUPLICATION_RISK | Likely reduplication, but auto-expansion could introduce an editorial choice. |
| 1. Daging ditjutji, di-iris2? berbentuk dadu ketjil. | sandbox/legacy_imports/ocr_samples/RB-0010.txt:371 | FLAG_UNCERTAIN_CONTEXT | “?” suggests OCR uncertainty; auto-correction could choose the wrong reading. |
| 2. Bumbu2 dihaluskan, kemudian ditumis. | sandbox/legacy_imports/ocr_samples/RB-0010.txt:439 | FLAG_REDUPLICATION_RISK | Auto-fix could silently standardize wording without a review step. |
| 1i. Bebekjang sudah dipersiapkan, di-potong2 seperlunja. | sandbox/legacy_imports/ocr_samples/RB-0010.txt:511 | FLAG_REDUPLICATION_RISK | Reduplication likely, but OCR noise ("1i") suggests broader ambiguity in the line. |
| 3, di-aduk2 sampai masak. | sandbox/legacy_imports/ocr_samples/RB-0010.txt:627 | FLAG_REDUPLICATION_RISK | Auto-fix could remove the repetition cue or normalize punctuation inappropriately. |
| 1. Ketimunditjutji, dipotong udjung?2nja, di-tusuk2 dengan garpu | sandbox/legacy_imports/ocr_samples/RB-0010.txt:985 | FLAG_UNCERTAIN_CONTEXT | “?2” indicates ambiguity; auto-fix may alter meaning or structure. |
| 3. Bawang merah di-iris2, digoreng. | sandbox/legacy_imports/ocr_samples/RB-0010.txt:999 | FLAG_REDUPLICATION_RISK | Likely reduplication; auto-fix without context could be premature. |

## Governance Implications (Documentary)
- Human review is needed whenever OCR noise overlaps with potential “²” markers (e.g., “?2”, “"/”).
- Review context should show the original OCR line, neighboring lines, and a note that no normalization is applied.
- Flags are advisory only; they do not alter text and do not trigger automatic edits.

[METHODOLOGY_LOG]
Event: P3_MARKER2_FLAGGING_001 detection-only pilot.
Scope: identify ambiguous “²-derived” OCR cases; assign risk flags.
Method: metadata flagging only; no normalization, no edits.
Result: 10 candidates flagged for review; no rules enforced.
[/METHODOLOGY_LOG]

[FAILURE_NOTEBOOK]
CaseID: P3_MARKER2_FLAGGING_001_F1
Expected: detection-only flagging without normalization.
Observed: temptation to convert “di-iris2?” into a normalized form was noted.
Mitigation: flagged as FLAG_UNCERTAIN_CONTEXT; no edits made.
Lesson: ambiguous punctuation must remain in review-only state.
[/FAILURE_NOTEBOOK]

Rollback: delete this file to revert the pilot record.

## Consolidation Summary (Phase-3)

**What we validated:**  
Ambiguity can be reliably detected and documented without modifying OCR text. “Flag-only” workflows surfaced risk early while preserving reversibility.

**What failed safely:**  
Temptations to normalize (e.g., ingredient headers or punctuation collisions) were captured as flags rather than edits. Ambiguity remained visible to reviewers.

**Governance behavior:**  
Flags functioned as advisory metadata, not commands. No rules were promoted; all decision-making stayed deferred to human review.

**Key insight:**  
Detection is useful even without automation — it reduces the chance of silent, irreversible edits later. However, flags must live *alongside* texts (metadata), not inside them.

**Status:** CONSOLIDATED — learning captured, no policies promoted.
