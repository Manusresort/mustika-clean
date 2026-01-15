# Legacy Repo Inventory (Mustika Archive)

Legacy repo path:
- `/Users/vwvd/Millway/AI-folder/mustika_archive`

This is a factual inventory of sources, chapter/excerpt artifacts, alignment
signals, and governance/pilot materials in the legacy archive.

---

## Sources (book / chapter / OCR)

| Path | Types | Notes / Provenance |
|---|---|---|
| `Mustikarasa 2026/SOURCE_CANON/step3_canonical/` | `page-XXXX.txt` | Canonical source pages; provenance described in `project_meta/SOURCE_OF_TRUTH.md`. |
| `Mustikarasa 2026/DERIVED/step4_structure/index/canonical_concat.txt` | `.txt` | Concatenated canonical text; referenced by other maps/notes. |
| `Mustikarasa 2026/ocr_txt/` | `.txt` | OCR text per page (raw OCR outputs). |
| `Mustikarasa 2026/ocr_tsv/` | `.tsv` | OCR text per page (TSV form). |
| `Mustikarasa 2026/pdf/` | `.pdf` | PDF sources (raw). |
| `Mustikarasa 2026/images/` | images | Scan images (raw). |
| `Mustikarasa/ocr_txt/`, `Mustikarasa/ocr_tsv/`, `Mustikarasa/pdf/`, `Mustikarasa/images/` | mixed | Older parallel OCR/image sets. |
| `Mustikarasa/Agentic Creation of Mustika rasa/mustikarasa_agents/workspace/00_input/` | `.txt` | Chapter-level inputs (hoofdstuk_*.txt). |

Provenance / source-of-truth docs:
- `Mustikarasa 2026/project_meta/SOURCE_OF_TRUTH.md`
- `Mustikarasa 2026/project_meta/STEP3_BRONTEXT_STATUS.md`
- `Mustikarasa 2026/project_meta/readme_mustika_rasa_project.md`

---

## Chapters (explicit and implicit)

Explicit chapter-like files appear in the agentic workspace inputs:

| hoofdstuk-id | label (if any) | path | status |
|---|---|---|---|
| hoofdstuk_01 | (none) | `.../workspace/00_input/hoofdstuk_01.txt` | explicit file |
| hoofdstuk_02 | (none) | `.../workspace/00_input/hoofdstuk_02.txt` | explicit file |
| hoofdstuk_03 | (none) | `.../workspace/00_input/hoofdstuk_03.txt` | explicit file |
| hoofdstuk_03_part1 | part | `.../workspace/00_input/hoofdstuk_03_part1.txt` | explicit file |
| hoofdstuk_04 | (none) | `.../workspace/00_input/hoofdstuk_04.txt` | explicit file |
| hoofdstuk_05 | (none) | `.../workspace/00_input/hoofdstuk_05.txt` | explicit file |
| hoofdstuk_05_classification | (classification) | `.../workspace/00_input/hoofdstuk_05_classification.txt` | explicit file |
| hoofdstuk_06 | (none) | `.../workspace/00_input/hoofdstuk_06.txt` | explicit file |
| hoofdstuk_06_memasak | (memasak) | `.../workspace/00_input/hoofdstuk_06_memasak.txt` | explicit file |
| hoofdstuk_07_part1 | part | `.../workspace/00_input/hoofdstuk_07_part1.txt` | explicit file |
| hoofdstuk_07_part2 | part | `.../workspace/00_input/hoofdstuk_07_part2.txt` | explicit file |
| hoofdstuk_07_part3 | part | `.../workspace/00_input/hoofdstuk_07_part3.txt` | explicit file |
| hoofdstuk_07_combined | combined | `.../workspace/00_input/hoofdstuk_07_combined.txt` | explicit file |
| hoofdstuk_08 | (none) | `.../workspace/00_input/hoofdstuk_08.txt` | explicit file |
| hoofdstuk_09 | (none) | `.../workspace/00_input/hoofdstuk_09.txt` | explicit file |
| hoofdstuk_10 | (none) | `.../workspace/00_input/hoofdstuk_10.txt` | explicit file |

No central chapter registry was found outside the agentic workspace.

---

## Excerpts / Blocks / Extracts

Legacy repo uses multiple granular units:

| Unit | Example IDs | Where | Notes |
|---|---|---|---|
| Recipe blocks | `RB-0001`..`RB-0028` | `Mustikarasa 2026/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv` | Maps RB IDs to page ranges. |
| Source blocks | `BLK-0009`.. | `recipe_block_manifest.tsv` | Internal block IDs associated with RBs. |
| Page IDs | `page-0001`.. | `SOURCE_CANON/step3_canonical/` | Canonical page files. |

Excerpt registries / maps:
- `Mustikarasa 2026/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv`
- `Mustikarasa 2026/DERIVED/step4_structure/ledgers/page_to_recipe_block.tsv`
- `Mustikarasa 2026/DERIVED/step4_structure/ledgers/recipe_block_pages.tsv`
- `Mustikarasa 2026/DERIVED/step4_structure/ledgers/recipe_block_file_manifest.tsv`
- `Mustikarasa 2026/DERIVED/step4_structure/ledgers/step4_outputs_index.tsv`
- `Mustikarasa 2026/DERIVED/step5_extraction/ledgers/step5_outputs_index.tsv`

Versions / locks:
- No explicit version fields found in these ledgers.
- Freeze status is documented in `project_meta/SOURCE_OF_TRUTH.md` and
  `DERIVED/step6_annotations_frozen/...`.

---

## Alignment signals (chapter → excerpt)

Explicit alignment tables:
- `recipe_block_manifest.tsv` (RB → page range)
- `page_to_recipe_block.tsv` (page → RB)
- `recipe_block_pages.tsv` (RB → pages)

Implicit alignment signals:
- `canonical_concat.txt` (full concatenation of canonical pages)
- `RB-0001..RB-0028` sequence implies ordered blocks; no chapter labels attached.
- Agentic workspace chapter files (`hoofdstuk_*.txt`) do not reference RB IDs.

What is missing for chapter→excerpt alignment:
- A registry mapping hoofdstuk_XX to RB IDs or page ranges.
- A documented link between agentic chapter files and canonical page ranges.

---

## Governance / pilot artifacts (legacy)

| Path | Type | Classification | Notes |
|---|---|---|---|
| `Mustikarasa 2026/project_meta/readme_mustika_rasa_project.md` | governance overview | POLICY | Defines multi-step OCR→canonical→extraction process. |
| `Mustikarasa 2026/project_meta/SOURCE_OF_TRUTH.md` | governance | POLICY | Declares canonical sources and derived layers. |
| `Mustikarasa 2026/project_meta/STEP3_BRONTEXT_STATUS.md` | governance | POLICY | Canonical status and OCR-clean constraints. |
| `Mustikarasa 2026/project_meta/SCAN_SIGNALS/*` | scan signals | OBSERVATION_ONLY | Signal logs for OCR/scan anomalies. |
| `Mustikarasa 2026/OPTIONAL/phaseA_safety_science/` | annotations/TSV | OBSERVATION_ONLY | Safety science outputs; explicitly optional/ended. |
| `Mustikarasa/phaseA_safety_science/...` | annotations/TSV | OBSERVATION_ONLY | Older safety outputs. |

Note: These artifacts must not be auto-promoted into normalization rules.

