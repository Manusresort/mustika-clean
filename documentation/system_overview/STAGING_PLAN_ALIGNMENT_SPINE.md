# Staging Plan — Alignment Spine (Documentation Only)

This plan defines the minimal alignment spine to stage in the clean repo.
No files are copied or modified here.

---

## Scope (legacy sources to stage)

The following legacy paths are required to build the alignment spine:

1) `SOURCE_CANON/step3_canonical/`
2) `DERIVED/step4_structure/index/canonical_concat.txt`
3) `DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv`
4) `DERIVED/step4_structure/ledgers/page_to_recipe_block.tsv`
5) `workspace/00_input/hoofdstuk_*.txt`

---

## Proposed target paths (clean repo)

All staged content should be placed under:
- `runtime/data/source_imports/<batch_id>/`

Suggested batch_id:
- `alignment_spine_legacy_2026_001`

---

## Item-by-item staging plan

### 1) SOURCE_CANON/step3_canonical
- **Legacy path:** `/Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/SOURCE_CANON/step3_canonical/`
- **Target path:** `runtime/data/source_imports/alignment_spine_legacy_2026_001/step3_canonical/`
- **Why alignment‑critical:** canonical page IDs (page-XXXX) are the base layer for page↔RB mapping.
- **Blockers resolved:** provides canonical page IDs referenced by RB ledgers and alignment tables.
- **UNKNOWN after staging:** chapter↔page mapping remains unknown.

### 2) canonical_concat.txt
- **Legacy path:** `/Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/DERIVED/step4_structure/index/canonical_concat.txt`
- **Target path:** `runtime/data/source_imports/alignment_spine_legacy_2026_001/step4_structure/index/canonical_concat.txt`
- **Why alignment‑critical:** referenced by EXCERPT_MAP line ranges (SAJUR-A/B).
- **Blockers resolved:** enables line-range alignment from EXCERPT_MAP to actual text.
- **UNKNOWN after staging:** SAJUR-A/B still not linked to run excerpt IDs.

### 3) recipe_block_manifest.tsv
- **Legacy path:** `/Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv`
- **Target path:** `runtime/data/source_imports/alignment_spine_legacy_2026_001/step4_structure/ledgers/recipe_block_manifest.tsv`
- **Why alignment‑critical:** defines RB↔page ranges + BLK IDs.
- **Blockers resolved:** provides primary page↔segment alignment spine.
- **UNKNOWN after staging:** RB↔chapter mapping still unknown.

### 4) page_to_recipe_block.tsv
- **Legacy path:** `/Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/DERIVED/step4_structure/ledgers/page_to_recipe_block.tsv`
- **Target path:** `runtime/data/source_imports/alignment_spine_legacy_2026_001/step4_structure/ledgers/page_to_recipe_block.tsv`
- **Why alignment‑critical:** explicit page→RB mapping.
- **Blockers resolved:** supports reverse lookup (page→segment).
- **UNKNOWN after staging:** no chapter labels in mapping.

### 5) workspace/00_input/hoofdstuk_*.txt
- **Legacy path:** `/Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa/Agentic Creation of Mustika rasa/mustikarasa_agents/workspace/00_input/hoofdstuk_*.txt`
- **Target path:** `runtime/data/source_imports/alignment_spine_legacy_2026_001/hoofdstuk_inputs/`
- **Why alignment‑critical:** only explicit chapter‑labeled inputs found.
- **Blockers resolved:** provides chapter identifiers for future mapping.
- **UNKNOWN after staging:** no explicit linkage to canonical pages or RB IDs.

---

## Remaining UNKNOWN after staging

- No authoritative hoofdstuk→RB/page mapping.
- No version/lock metadata for RB/BLK segments.
- No proof that hoofdstuk inputs match canonical page ranges.
- No equivalence proof between legacy_2026 OCR sources and legacy_old OCR sources.

