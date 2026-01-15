# Pilot: OCR Automation Boundary
Pilot ID: P3_OCR_AUTOMATION_001
Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Purpose
Explore the line between safe OCR restoration and unintended editorial change. Surface ambiguous edge cases rather than solving them.

## Input Source (documentary)
Use sandbox/legacy_imports/ocr_samples/ and context_reference/ as reference material — read only, never edited.

## Cases to Document (at least 5)

Case 1 — “²” marker ambiguity
- OCR excerpt: “Bahan2 :”
- plausible “technical fix”: restore “²” marker (e.g., bahan²)
- why that fix might change meaning: may imply reduplication where the source is uncertain or stylized differently in print
- classification: REVIEW_REQUIRED

Case 2 — punctuation collision
- OCR excerpt: “1. Daging ditjutji, di-iris2? berbentuk dadu ketjil.”
- plausible “technical fix”: remove “?” as OCR noise
- why that fix might change meaning: “?” may indicate uncertainty or missing glyph; removing it assumes certainty
- classification: DO_NOT_AUTOMATE

Case 3 — line-break grouping
- OCR excerpt: “Bumbu2 . i sdt. gula merah 4 kg.”
- plausible “technical fix”: normalize spacing/punctuation
- why that fix might change meaning: spacing could encode list structure or headings; auto-fix might re-group ingredients
- classification: REVIEW_REQUIRED

Case 4 — character confusion in numbering
- OCR excerpt: “1i. Bebekjang sudah dipersiapkan, di-potong2 seperlunja.”
- plausible “technical fix”: normalize to “1.”
- why that fix might change meaning: could be line-numbering or OCR artifact; fixing might re-order steps
- classification: REVIEW_REQUIRED

Case 5 — line-break restoration
- OCR excerpt: “3, di-aduk2 sampai masak.”
- plausible “technical fix”: normalize punctuation to “3.”
- why that fix might change meaning: punctuation may indicate continuation or alternative numbering; auto-fix assumes format
- classification: REVIEW_REQUIRED

Case 6 — spacing and token merges
- OCR excerpt: “Ketimunditjutji, dipotong udjung?2nja, di-tusuk2 dengan garpu”
- plausible “technical fix”: split tokens into separate words
- why that fix might change meaning: token boundaries are interpretive; splitting could change lexical reading
- classification: DO_NOT_AUTOMATE

## Boundary Table

| Case | Pattern | Tempting Automation | Risk | Classification |
| --- | --- | --- | --- | --- |
| Case 1 | “²” marker ambiguity | replace “2” with “²” | may impose reduplication without proof | REVIEW_REQUIRED |
| Case 2 | punctuation collision | delete “?” as OCR noise | removes uncertainty signal | DO_NOT_AUTOMATE |
| Case 3 | list spacing | normalize spacing/punctuation | may alter list structure | REVIEW_REQUIRED |
| Case 4 | numbering confusion | normalize “1i.” to “1.” | could reorder or mislabel steps | REVIEW_REQUIRED |
| Case 5 | punctuation normalization | change “3,” to “3.” | may mis-handle continuation | REVIEW_REQUIRED |
| Case 6 | token merge | split words automatically | could change lexical meaning | DO_NOT_AUTOMATE |

[METHODOLOGY_LOG]
Event: P3_OCR_AUTOMATION_001 boundary pilot.
Scope: document automation risks in OCR restoration.
Method: identify ambiguous OCR cases and propose classifications.
Result: boundary cases documented; no automation rules created.
[/METHODOLOGY_LOG]

[FAILURE_NOTEBOOK]
CaseID: P3_OCR_AUTOMATION_001_F1
Expected: avoid declaring automation-safe fixes.
Observed: “1i.” normalization felt safe at first glance.
Mitigation: reclassified as REVIEW_REQUIRED; no rule applied.
Lesson: “obvious” OCR fixes can mask structural meaning.
[/FAILURE_NOTEBOOK]

## Exit Criteria
Ambiguous boundary documented, not resolved.

## Rollback
Delete this file → system state unchanged.

## Consolidation Summary (Phase-3)

What we validated:  
“Mechanical” OCR fixes can quietly cross into editorial territory.  
Boundary clarity matters: SAFE_AUTOMATION, REVIEW_REQUIRED, and
DO_NOT_AUTOMATE are useful *labels for thinking*, not rules.

What failed safely:  
We documented edge cases instead of normalizing them. Nothing ran
automatically. Rollback remains trivial because no text or scripts
changed.

Governance behavior:  
Automation pressure was routed into documentation, not action.
Governance would only authorize automation after lifecycle discussion
and Human Gate, not inside a pilot.

Key insight:  
Automation is safest when it proposes flags — not edits. Ambiguity should
move to review, not disappear.

Status: CONSOLIDATED — learning captured, no automation promoted.
