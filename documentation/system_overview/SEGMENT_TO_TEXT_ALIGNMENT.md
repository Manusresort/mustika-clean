# Segment -> Text Alignment (Facts Only)

Scope: scanned paths under `runtime/data/source_imports/` and `documentation/legacy_imports/`.

Evidence found:
- `runtime/data/source_imports/sayur_groente_001/EXCERPT_MAP.md`
  - IDs: SAJUR-A, SAJUR-B
  - Text reference: `canonical_concat.txt` line ranges
- `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv`
  - RB/BLK ids with start_page/end_page

| segment_id | text_ref | origin | confidence | evidence_path | notes |
|---|---|---|---|---|---|
| SAJUR-A | canonical_concat.txt line_range 3400-3555 | CLEAN_REPO_STAGED | MED | `runtime/data/source_imports/sayur_groente_001/EXCERPT_MAP.md` | canonical_concat.txt is staged. |
| SAJUR-B | canonical_concat.txt line_range 9640-10000 | CLEAN_REPO_STAGED | MED | `runtime/data/source_imports/sayur_groente_001/EXCERPT_MAP.md` | canonical_concat.txt is staged. |
| RB-0001 | page-0186..page-0187 | CLEAN_REPO_STAGED | HIGH | `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv` | Sample row. Full RB range mapping in manifest. |
| BLK-0009 | page-0186..page-0187 | CLEAN_REPO_STAGED | HIGH | `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv` | Sample row via source_block_id. |

Notes:
- RB/BLK mappings are page-range based; no line-offset mapping is present in scanned paths.
