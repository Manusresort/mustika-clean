# Legacy Migration Manifest (Plan Only)

Legacy roots:
1) `/Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/`
2) `/Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa/`

Clean repo root:
- `/Users/vwvd/Millway/AI-folder/Crew-AI/mustika-rasa-clean`

This is a **plan only**. No files are copied.

---

## Target staging layout (read-only, no runtime impact)

- `runtime/data/source_imports/<batch_id>/...` (BOOK/STRUCTURE/EXTRACTION sources)
- `documentation/legacy_imports/<batch_id>/...` (PROJECT_META, GOVERNANCE/PILOTS)

Each batch will include:
- `README_SOURCE_IMPORT.md` (source, scope, exclusions, date)
- `CHECKSUMS.txt` (optional; sha256)

---

## Proposed batches

- **batch_id: legacy_2026_core_001**
  - Scope: SOURCE_CANON + DERIVED step4/step5 structure
- **batch_id: legacy_2026_meta_001**
  - Scope: project_meta, scan signals, governance docs
- **batch_id: legacy_agentic_inputs_001**
  - Scope: hoofdstuk_*.txt inputs (agentic workspace)
- **batch_id: legacy_optional_pilots_001**
  - Scope: phaseA_safety_science (observation-only)

---

## Manifest Items

| legacy_root | legacy_path | category | target_path | why_it_matters | provenance_status | notes |
|---|---|---|---|---|---|---|
| Mustikarasa 2026 | `SOURCE_CANON/step3_canonical/` | BOOK_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/step3_canonical/` | Canonical page-level sources | OK | Canon declared in `project_meta/SOURCE_OF_TRUTH.md`. |
| Mustikarasa 2026 | `ocr_txt/` | BOOK_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/ocr_txt/` | Raw OCR per page | CONFLICT | `DECISIONS.md` says raw sources not included, but present. |
| Mustikarasa 2026 | `ocr_tsv/` | BOOK_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/ocr_tsv/` | OCR TSV per page | CONFLICT | Same as above. |
| Mustikarasa 2026 | `pdf/` | BOOK_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/pdf/` | PDF scans | CONFLICT | `DECISIONS.md` notes raw sources not included. |
| Mustikarasa 2026 | `images/` | BOOK_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/images/` | Page images | CONFLICT | Same conflict. |
| Mustikarasa 2026 | `DERIVED/step4_structure/index/canonical_concat.txt` | STRUCTURE_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/step4_structure/index/` | Concatenated canonical text | OK | Referenced by other mappings. |
| Mustikarasa 2026 | `DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv` | STRUCTURE_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/step4_structure/ledgers/` | RB↔page range mapping | OK | Primary RB/page alignment signal. |
| Mustikarasa 2026 | `DERIVED/step4_structure/ledgers/page_to_recipe_block.tsv` | STRUCTURE_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/step4_structure/ledgers/` | page↔RB mapping | OK | Used for alignment. |
| Mustikarasa 2026 | `DERIVED/step4_structure/ledgers/recipe_block_pages.tsv` | STRUCTURE_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/step4_structure/ledgers/` | RB→pages list | OK | Alignment detail. |
| Mustikarasa 2026 | `DERIVED/step4_structure/ledgers/recipe_block_file_manifest.tsv` | STRUCTURE_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/step4_structure/ledgers/` | RB→file mapping | OK | Traceability for extracts. |
| Mustikarasa 2026 | `DERIVED/step4_structure/ledgers/step4_outputs_index.tsv` | STRUCTURE_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/step4_structure/ledgers/` | Structure output index | OK | Index of step4 outputs. |
| Mustikarasa 2026 | `DERIVED/step5_extraction/` | EXTRACTION_SOURCES | `runtime/data/source_imports/legacy_2026_core_001/step5_extraction/` | Extraction outputs | OK | Step5 inputs/outputs. |
| Mustikarasa | `step4_extraction/` | EXTRACTION_SOURCES | `runtime/data/source_imports/legacy_agentic_inputs_001/step4_extraction/` | Older extraction tree | MISSING | Provenance unclear; older legacy tree. |
| Mustikarasa | `step5_extraction/` | EXTRACTION_SOURCES | `runtime/data/source_imports/legacy_agentic_inputs_001/step5_extraction/` | Older extraction tree | MISSING | Provenance unclear; older legacy tree. |
| Mustikarasa 2026 | `project_meta/SOURCE_OF_TRUTH.md` | PROJECT_META | `documentation/legacy_imports/legacy_2026_meta_001/` | Canon source definition | OK | Policy-level provenance. |
| Mustikarasa 2026 | `project_meta/STEP3_BRONTEXT_STATUS.md` | PROJECT_META | `documentation/legacy_imports/legacy_2026_meta_001/` | OCR clean constraints | OK | Canonical status/constraints. |
| Mustikarasa 2026 | `project_meta/DECISIONS.md` | PROJECT_META | `documentation/legacy_imports/legacy_2026_meta_001/` | Decision notes | OK | Mentions raw sources not included. |
| Mustikarasa 2026 | `project_meta/SCAN_SIGNALS/` | PROJECT_META | `documentation/legacy_imports/legacy_2026_meta_001/SCAN_SIGNALS/` | OCR signal logs | OK | Observation-only evidence. |
| Mustikarasa 2026 | `project_meta/readme_mustika_rasa_project.md` | PROJECT_META | `documentation/legacy_imports/legacy_2026_meta_001/` | Project overview | OK | Multi-step pipeline description. |
| Mustikarasa | `Agentic Creation of Mustika rasa/mustikarasa_agents/workspace/00_input/hoofdstuk_*.txt` | AGENTIC_INPUTS | `runtime/data/source_imports/legacy_agentic_inputs_001/hoofdstuk_inputs/` | Chapter-labeled inputs | MISSING | No mapping to RB/page IDs. |
| Mustikarasa 2026 | `OPTIONAL/phaseA_safety_science/` | GOVERNANCE_PILOTS | `documentation/legacy_imports/legacy_optional_pilots_001/phaseA_safety_science/` | Safety annotations | OK | Explicitly optional/ended. |
| Mustikarasa | `phaseA_safety_science/` | GOVERNANCE_PILOTS | `documentation/legacy_imports/legacy_optional_pilots_001/phaseA_safety_science_older/` | Older safety outputs | OK | Observation-only. |

---

## Conflict & gaps (book→chapter→excerpt)

1) **Hoofdstuk‑register ontbreekt**
- Candidate inputs: `.../workspace/00_input/hoofdstuk_*.txt`
- No registry ties these to canonical pages or RB IDs.

2) **Hoofdstuk↔RB/page mapping ontbreekt**
- Existing signals: `recipe_block_manifest.tsv`, `page_to_recipe_block.tsv`, `canonical_concat.txt`.
- Missing: a mapping file linking hoofdstuk_XX to RB or page ranges.

3) **ID‑taxonomie mismatch**
- Present IDs: `page-XXXX`, `RB-####`, `BLK-####`, `hoofdstuk_XX`.
- Existing mapping only for RB↔page (no hoofdstuk relation).

4) **canonical_concat.txt zonder labeling**
- Exists at `DERIVED/step4_structure/index/canonical_concat.txt`.
- No chapter/excerpt labels embedded.

5) **Versies / locks**
- Freeze status documented in `project_meta/SOURCE_OF_TRUTH.md` and step6 annotations.
- Ledgers lack explicit version fields.

6) **Raw source presence conflicts with decision note**
- `project_meta/DECISIONS.md` notes raw sources not included,
  but `ocr_txt/`, `ocr_tsv/`, `pdf/`, `images/` exist.

---

## Provenance notes
- Primary provenance docs: `project_meta/SOURCE_OF_TRUTH.md`, `STEP3_BRONTEXT_STATUS.md`.
- Scan signal logs: `project_meta/SCAN_SIGNALS/` (observation-only).

