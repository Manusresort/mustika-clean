# Page -> Segment Alignment (Facts Only)

Scope: scanned paths under `runtime/data/source_imports/` and `documentation/legacy_imports/`.

Evidence found:
- `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/page_to_recipe_block.tsv`
  - 1214 rows (page_id -> recipe_block_id)

| page_id | segment_id | origin | confidence | evidence_path | notes |
|---|---|---|---|---|---|
| ledger_rows (1214) | recipe_block_id or NONE | CLEAN_REPO_STAGED | HIGH | `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/page_to_recipe_block.tsv` | Full mapping available in ledger (includes NONE for non-RB pages). |
| page-0001 | NONE | CLEAN_REPO_STAGED | HIGH | `.../page_to_recipe_block.tsv` | Sample row. |
| page-0186 | RB-0001 | CLEAN_REPO_STAGED | HIGH | `.../page_to_recipe_block.tsv` | Sample row. |

Notes:
- This ledger provides page -> RB alignment only; it does not map chapters or excerpts.
