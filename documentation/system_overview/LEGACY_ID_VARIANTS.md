# Legacy ID Variants (Observed)

This list records ID formats in the legacy repo without renaming or normalizing.

---

## Page IDs
- Format: `page-XXXX`
- Example: `page-0001`
- Location: `Mustikarasa 2026/SOURCE_CANON/step3_canonical/`

## Recipe block IDs (RB)
- Format: `RB-####`
- Example: `RB-0001`
- Location: `Mustikarasa 2026/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv`

## Source block IDs (BLK)
- Format: `BLK-####`
- Example: `BLK-0012`
- Location: `recipe_block_manifest.tsv`

## Chapter files (hoofdstuk)
- Format: `hoofdstuk_XX` (sometimes with suffix)
- Examples:
  - `hoofdstuk_01.txt`
  - `hoofdstuk_03_part1.txt`
  - `hoofdstuk_06_memasak.txt`
  - `hoofdstuk_07_combined.txt`
- Location: `Mustikarasa/Agentic Creation of Mustika rasa/mustikarasa_agents/workspace/00_input/`

## Scan signal IDs
- Format: `signal_id` (TSV)
- Location: `Mustikarasa 2026/project_meta/SCAN_SIGNALS/signals.tsv`

## Ambiguity
- No explicit mapping between hoofdstuk IDs and RB/page IDs was found.
- RB IDs appear sequential and mapped to page ranges, but not to chapter labels.

