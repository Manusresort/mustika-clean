# Segment Registry (Facts Only)

Scope: scanned paths under `runtime/data/source_imports/` and `documentation/legacy_imports/`.

Segments found:

| segment_id | segment_type | origin | source_paths | page_range | canonical_text_offsets | provenance_status | governance_flags | notes |
|---|---|---|---|---|---|---|---|---|
| SAJUR-A | EXCERPT_LABEL | CLEAN_REPO_STAGED | `runtime/data/source_imports/sayur_groente_001/EXCERPT_MAP.md` | line_range: 3400-3555 | canonical_concat.txt line range | OK | OCR_REDUCTION_MARKER_RISK (unspecified) | References canonical_concat.txt (staged). |
| SAJUR-B | EXCERPT_LABEL | CLEAN_REPO_STAGED | `runtime/data/source_imports/sayur_groente_001/EXCERPT_MAP.md` | line_range: 9640-10000 | canonical_concat.txt line range | OK | OCR_REDUCTION_MARKER_RISK (unspecified) | References canonical_concat.txt (staged). |
| RB-0001..RB-0028 (28) | RECIPE_BLOCK | CLEAN_REPO_STAGED | `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv` | per-RB page range in manifest | UNKNOWN | OK | none | Manifest defines RB id, start_page, end_page. |
| BLK-0009..BLK-0036 (28) | BLOCK | CLEAN_REPO_STAGED | `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv` | per-BLK page range in manifest | UNKNOWN | OK | none | Manifest provides source_block_id per RB. |

Notes:
- Full RB/BLK listing is in the manifest ledger; registry uses ranges for brevity.
