# Pilot Run — “²” Marker Analysis (P3_MARKER2_ANALYSIS_001)
Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Sampling Method (Continuation: P3_MARKER2_ANALYSIS_001_CONT)
- Source: sandbox/legacy_imports/ocr_samples/
- Selection: up to 10 excerpts where OCR shows distortion (e.g., "2", "?", "\"") likely standing in for the printed “²” marker.
- Action: observe and classify only; no normalization or text edits.

## Evidence Table (OCR Samples)
| Excerpt (as-is) | Source | Classification | Risk note |
| --- | --- | --- | --- |
| Bahan2 : | sandbox/legacy_imports/ocr_samples/RB-0019.txt:357 | REDUPLICATION_LIKELY | Auto-cleaner may expand or replace without review, losing original marker context. |
| Bumbu2 . i sdt. gula merah 4 kg. | sandbox/legacy_imports/ocr_samples/RB-0019.txt:1405 | REDUPLICATION_LIKELY | Auto-normalization could incorrectly separate or rewrite spacing/punctuation. |
| 1. Nangka di-iris"/diradjang ketjil2. | sandbox/legacy_imports/ocr_samples/RB-0018.txt:6557 | REDUPLICATION_UNCERTAIN | OCR punctuation noise ("/) could hide a “²” marker; auto-fix might alter meaning. |
| 3. Di-potong2 serong. | sandbox/legacy_imports/ocr_samples/RB-0018.txt:8403 | REDUPLICATION_LIKELY | Automated cleanup might silently expand to a different form (e.g., potong-potong). |
| 1. Daging ditjutji, di-iris2? berbentuk dadu ketjil. | sandbox/legacy_imports/ocr_samples/RB-0010.txt:371 | AMBIGUOUS | “?” suggests OCR uncertainty; auto-correction could pick a wrong reading. |
| 2. Bumbu2 dihaluskan, kemudian ditumis. | sandbox/legacy_imports/ocr_samples/RB-0010.txt:439 | REDUPLICATION_LIKELY | Auto-cleaner could standardize without preserving original marker. |
| 1i. Bebekjang sudah dipersiapkan, di-potong2 seperlunja. | sandbox/legacy_imports/ocr_samples/RB-0010.txt:511 | REDUPLICATION_LIKELY | Risk of removing the reduplication signal when cleaning OCR. |
| 3, di-aduk2 sampai masak. | sandbox/legacy_imports/ocr_samples/RB-0010.txt:627 | REDUPLICATION_LIKELY | Auto-fix might normalize to a single verb, losing repetition cue. |
| 1. Ketimunditjutji, dipotong udjung?2nja, di-tusuk2 dengan garpu | sandbox/legacy_imports/ocr_samples/RB-0010.txt:985 | AMBIGUOUS | “?2” suggests OCR confusion; auto-correction could distort the original phrase. |
| 3. Bawang merah di-iris2, digoreng. | sandbox/legacy_imports/ocr_samples/RB-0010.txt:999 | REDUPLICATION_LIKELY | Automated cleanup could silently choose a modernized form. |

## Synthesis / Observations
- Patterns: “2” frequently appears attached to verbs or nouns (e.g., di-iris2, Bumbu2), likely representing the “²” reduplication marker.
- Distortion signals: OCR punctuation noise (" and "?") appears adjacent to “2” in several cases, increasing ambiguity.
- Highest ambiguity: cases with mixed punctuation (e.g., di-iris2?, udjung?2nja) where OCR noise obscures the marker’s intended placement.
- Governance questions: when should OCR restoration treat “2” as a technical “²” recovery vs. a candidate for human review? How should ambiguity be flagged without rewriting?

[METHODOLOGY_LOG]
Event: P3_MARKER2_ANALYSIS_001_CONT sampling continuation.
Scope: OCR-only evidence collection from sandbox/legacy_imports/ocr_samples.
Method: identify likely “²” distortions; classify and note risks without normalizing or editing text.
Result: evidence table completed; ambiguity documented for governance review; no rules enforced.
[/METHODOLOGY_LOG]

Rollback: delete this file to revert the continuation record.

## Consolidation Summary (Phase-3)

**What we validated:**  
OCR distortions of the historical “²” marker follow recognizable patterns (e.g., `bahan?`, `bahan2`, `bahan"`), yet contain edge cases where punctuation and OCR artifacts overlap and meaning becomes ambiguous.

**What failed safely:**  
Instead of correcting text, the pilot documented ambiguity and deferred decisions. Canonical context was consulted only as interpretation support, not as a replacement layer.

**Governance behavior:**  
Soft-stops worked: observation remained separate from editing. No normalization was applied; rollback stays trivial.

**Key insight:**  
Some “²-like” cases are strong automation candidates (e.g., ingredient list headers), while mixed-punctuation cases must be treated as REVIEW_REQUIRED — but **this is a proposal, not policy.**

**Status:** CONSOLIDATED — learning captured, no rules promoted.
