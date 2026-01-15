# ID Taxonomy Crosswalk (Draft, Evidence-Only)

This draft crosswalk lists only **hard evidence** from legacy ledgers.
No inferred mappings are added.

Evidence sources:
- `Mustikarasa 2026/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv`
- `Mustikarasa 2026/DERIVED/step4_structure/ledgers/page_to_recipe_block.tsv`

---

## A) page IDs ↔ RB IDs (from recipe_block_manifest.tsv)

| page range | RB ID | evidence path |
|---|---|---|
| page-0186..page-0187 | RB-0001 | `.../recipe_block_manifest.tsv` |
| page-0189..page-0191 | RB-0002 | `.../recipe_block_manifest.tsv` |
| page-0193..page-0211 | RB-0003 | `.../recipe_block_manifest.tsv` |
| page-0214..page-0243 | RB-0004 | `.../recipe_block_manifest.tsv` |
| page-0245..page-0275 | RB-0005 | `.../recipe_block_manifest.tsv` |

(Full mapping exists in the manifest file.)

---

## B) RB IDs ↔ BLK IDs (from recipe_block_manifest.tsv)

| RB ID | BLK ID | evidence path |
|---|---|---|
| RB-0001 | BLK-0009 | `.../recipe_block_manifest.tsv` |
| RB-0002 | BLK-0010 | `.../recipe_block_manifest.tsv` |
| RB-0003 | BLK-0011 | `.../recipe_block_manifest.tsv` |
| RB-0004 | BLK-0012 | `.../recipe_block_manifest.tsv` |
| RB-0005 | BLK-0013 | `.../recipe_block_manifest.tsv` |

(Full mapping exists in the manifest file.)

---

## C) RB/BLK ↔ hoofdstuk_XX

| RB/BLK ID | hoofdstuk_XX | evidence path |
|---|---|---|
| (none) | UNKNOWN | No explicit mapping files found. |

---

## Notes
- `hoofdstuk_*.txt` files exist under agentic workspace inputs, but do not
  include RB/page references.
- Without an explicit mapping file, the hoofdstuk alignment remains UNKNOWN.

