# Pilot Run — OCR Restore (P3_OCR_RESTORE_001)

**Status:** EXPERIMENTAL — NOT FOR PUBLICATION

## 1. Source Excerpt (sandbox)
ARON

(Tengger)

Bahan” :

djagung putih pipilan

Tjara membuatnja :

1i. Bidjidjagung direndam air 12 djam atau lebih, sehingga kulitnja

mudah terbuang kalau disosoh.

## 2. OCR Candidates
| ID | Excerpt | Type | Action |
|---|---|---|---|
| OCR-001 | "Bahan” :" | OCR_TECHNICAL | normalize stray quote and spacing to "Bahan:" |
| OCR-002 | "Tjara membuatnja :" | OCR_TECHNICAL | normalize spacing to "Tjara membuatnja:" |
| OCR-003 | "1i." | CONTENT_AMBIGUOUS | defer; could be "1." or original marker |
| OCR-004 | "djam" | CONTENT_AMBIGUOUS | defer; historical spelling may be intentional |

## 3. Corrected Text (pilot version)
ARON

(Tengger)

Bahan:

djagung putih pipilan

Tjara membuatnja:

1i. Bidjidjagung direndam air 12 djam atau lebih, sehingga kulitnja

mudah terbuang kalau disosoh.

## 4. Fix Annotations
- OCR-001: Stray quote character removed; heading punctuation normalized (technical).
- OCR-002: Spacing around colon normalized; heading preserved (technical).
- OCR-003: Left unchanged (possible content marker).
- OCR-004: Left unchanged (historical spelling).

## 5. Methodology Log (excerpt)
[METHODOLOGY_LOG]
Event: P3_OCR_RESTORE_001 pilot run.
Scope: OCR-technical-only corrections on a sandbox excerpt.
Boundary: historical spellings and numbering retained; only obvious OCR noise adjusted.
Result: two technical fixes applied; two content-ambiguous items deferred.
Status: EXPERIMENTAL — P3_OCR_RESTORE_001
[/METHODOLOGY_LOG]

## 6. Failure Notebook (safe near-miss)
[FAILURE_NOTEBOOK]
CaseID: P3_OCR_RESTORE_001_F1
Expected: avoid semantic edits disguised as OCR fixes.
Observed: temptation to modernize "djam" and "1i." to modern forms.
Mitigation: classify as CONTENT_AMBIGUOUS and defer.
Lesson: historical orthography must not be normalized in OCR-only passes.
[/FAILURE_NOTEBOOK]

## Methodology Insight — “²” Marker (Phase-3 — Proposal)
**Observation:** In Mustika Rasa, the “²” sign usually indicates reduplication/plural (e.g. *bahan²* ≈ *bahan bahan* = “ingredients”), but not in all cases. OCR often misreads this marker as `2`, `"`, or `?`, especially at line ends.  
**Implication for OCR RESTORE:** When the printed source uses “²” and the OCR layer shows `2`, `"`, `?`, or similar instead, this mismatch should be classified as an OCR_TECHNICAL restoration issue: the goal is to restore the digital text to match the printed book’s “²” marker. Any decisions about expanding or translating that marker (e.g. to *bahan-bahan* or “ingredients”) belong to later editorial/translation passes, not to OCR-only restoration.  
**Status:** PROPOSAL — pending a dedicated analysis pilot on “²” usage across the corpus.  
**Provenance:** P3_OCR_RESTORE_001 + human domain knowledge.

## Consolidation Summary (Phase-3)
**What we validated:** OCR-only restoration can be constrained to mechanical fixes while deferring content-ambiguous cases.  
**What failed safely:** strong temptation to “modernize” (e.g., djam, 1i.) was documented and deferred.  
**Governance behavior:** soft-stops worked; no semantic changes were made; rollback stayed trivial.  
**Key insight:** the “²” marker belongs to the printed text and must be restored when OCR distorts it, but interpretation is deferred.  
**Status:** CONSOLIDATED — learning captured, no decisions promoted.

## 7. Rollback
Delete `docs/PILOT_OCR_RESTORE_RUN_P3_OCR_RESTORE_001.md` to remove all pilot artefacts.

EXPERIMENTAL — pilot only — no changes promoted.
