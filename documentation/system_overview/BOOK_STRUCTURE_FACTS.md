# Book Structure Facts (As Observed in Repo)

This document records only what is present in the repository today.
No assumptions, no inferred design.

---

## Wat clean repo weet

- `runtime/data/origineel/hoofdstuk1.txt` bestaat en fungeert als bronbestand
  voor de huidige runner-runs (zie `runtime/runs/*/command.txt`).
- `runtime/data/source_imports/legacy_mr2026_alignment_spine/SOURCE_CANON/step3_canonical/`
  bevat 1214 pagina-bestanden (`page-*.txt`).
- `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/index/canonical_concat.txt`
  is aanwezig als canonieke concatenatie-view.
- `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv`
  definieert RB- en BLK-segmenten met page-ranges.
- `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/page_to_recipe_block.tsv`
  koppelt `page-*` aan RB-IDs (of NONE).
- `runtime/data/source_imports/legacy_mr2026_alignment_spine/ocr_txt/` en `ocr_tsv/`
  bevatten 1214 OCR txt + 1214 OCR tsv bestanden (`page-*.txt` / `page-*.tsv`).
- `runtime/data/source_imports/legacy_mr2026_alignment_spine/pdf/` bevat
  `Mustikarasa_OCR_full.pdf`.
- `runtime/data/source_imports/legacy_mr2026_alignment_spine/images/` bevat
  1214 pagina-afbeeldingen (`page-*.png`).
- `runtime/data/source_imports/sayur_groente_001/EXCERPT_MAP.md` definieert
  `SAJUR-A` en `SAJUR-B` met line ranges in `canonical_concat.txt`.
- Staged hoofdstuk-inputs bestaan onder
  `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_*.txt`.
- Run-bundles bestaan voor `sayur_052_066` onder `runtime/runs/`.

---

## Wat is UNKNOWN

- Geen expliciete hoofdstuk-registry (hoofdstuk-id ↔ bronbestand).
- Geen expliciete hoofdstuk -> segment mapping (RB/BLK of SAJUR-*).
- Geen expliciete mapping tussen run excerpt IDs (`sayur_052_066`) en RB/BLK of SAJUR-*.
- Geen versie/lock metadata voor chapters/segments/excerpts zichtbaar in de gescande paden.

---

## Wat is CONFLICT

- `documentation/legacy_imports/.../DECISIONS.md` stelt dat raw sources niet zijn inbegrepen,
  terwijl canonieke page-sources nu staged aanwezig zijn.

---

## Wat ontbreekt om hoofdstuk->segment->excerpt formeel te maken

- Hoofdstuk-registry (hoofdstuk-id ↔ bronbestand).
- Mapping hoofdstuk -> segment (RB/BLK of andere structurele units).
- Relatie hoofdstuk inputs ↔ canonical text view.
- Relatie run-excerpt IDs ↔ segmenten (RB/BLK of SAJUR-*).

---

## Top blockers (post full staging)

- Geen expliciete hoofdstuk-registry om hoofdstuk-IDs te normaliseren.
- Geen formele hoofdstuk -> segment mapping (RB/BLK ↔ hoofdstuk_*).
- Geen formele run-excerpt ↔ segment mapping.
- Geen versie/lock metadata in staged paden.

---

## Execution layer dependencies (facts-only)

- Runs rely on excerpt metadata (`excerpt_id`, `excerpt_source`, `excerpt_version`) for binding.
- `excerpt_source` currently points to `data/origineel/hoofdstuk1.txt` in run manifests.
- No run metadata references RB/BLK/SAJUR or page ranges.
- Validator report path is expected under `eval/output_contract_checks.txt` per run.
- Indices expose runs by excerpt_id only (no chapter or segment fields).

---

## Next actions (facts-only)

- Locate any chapter registry or mapping ledger in staged project_meta or source_imports.
- Locate any run metadata linking excerpt_id to RB/BLK or SAJUR-*.
- Locate any version/lock metadata in staged project_meta or manifests.

---

## Status: formeel gedefinieerd (documentair)

- Chapter registry structuur vastgelegd: `documentation/system_overview/CHAPTER_REGISTRY.md`.
- Excerpt definitie vastgelegd: `documentation/system_overview/EXCERPT_DEFINITION.md`.
- Excerpt registry structuur vastgelegd (leeg, bewust): `documentation/system_overview/EXCERPT_REGISTRY.md`.
- Excerpt ID & version policy vastgelegd: `documentation/system_overview/EXCERPT_ID_AND_VERSION_POLICY.md`.
- Chapter ↔ excerpt relation model vastgelegd: `documentation/system_overview/CHAPTER_EXCERPT_RELATION_MODEL.md`.
- Architecture consistency check vastgelegd: `documentation/system_overview/ARCHITECTURE_CONSISTENCY_CHECK.md`.
- Source & structure layer DoD vastgelegd: `documentation/system_overview/SOURCE_STRUCTURE_LAYER_DOD.md`.

---

## Status: leeg maar bewust

- Excerpt registry is leeg by design (geen IDs toegewezen).
- Chapter → excerpt mapping is niet ingevuld (geen mapping-artefact aanwezig).
- Chapter → segment mapping is niet ingevuld (geen mapping-artefact aanwezig).

---

## Bevestiging: laag 1 structureel aanwezig

- Physical sources, OCR layers, canonical views, segment ledgers en chapter inputs
  zijn staged en geregistreerd in de relevante registries (facts-only).

---

## Bron- & Structuurlaag — Definitieve Status

### Wat formeel bestaat

- Physical sources (PDF + page images) zijn staged en geregistreerd.
- OCR layers (ocr_txt + ocr_tsv) zijn staged en geregistreerd.
- Canonical text views (page-*.txt + canonical_concat.txt) zijn staged en geregistreerd.
- Segmenten (RB/BLK + SAJUR-*) zijn geregistreerd via ledgers en EXCERPT_MAP.
- Chapter inputs (hoofdstuk_*.txt) zijn staged en geregistreerd.

### Wat bewust NIET bestaat (en waarom)

- Chapter → excerpt mapping: geen mapping-artefact aangetroffen.
- Excerpt registry: bewust leeg, omdat geen mapping-artefact beschikbaar is.
- Excerpt versiebeleid in data: alleen policy-documentair, geen toegepaste versions.
- Hoofdstuk → segment alignment: geen mapping-artefact aangetroffen.

### Buiten scope van deze laag

- Runtime gedrag en runs (runner, validator, indexer).
- Agentic verwerking of evaluatie.
- Canonieke beslissingen of publicatie.

---

## Afsluitende verklaring

Deze bron- & structuurlaag is voldoende om:
- volledigheid te definiëren (wat er wel of niet is),
- verantwoordelijkheid te dragen voor bron- en segment-inventaris.

Verdere invulling (mappings, excerpt-populatie, workflow) hoort bij bovenliggende lagen.

---

## Tabellen

### Chapters inventory

| hoofdstuk-id | titel/label | source path | origin | status |
|---|---|---|---|---|
| hoofdstuk1 | (none) | `runtime/data/origineel/hoofdstuk1.txt` | CLEAN_REPO | implicit / naming-only |
| hoofdstuk_01 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_01.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_02 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_02.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_03_part1 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_03_part1.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_03 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_03.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_04 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_04.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_05_classification | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_05_classification.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_05 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_05.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_06_memasak | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_06_memasak.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_06 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_06.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_07_combined | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_07_combined.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_07_part1 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_07_part1.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_07_part2 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_07_part2.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_07_part3 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_07_part3.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_08 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_08.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_09 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_09.txt` | CLEAN_REPO_STAGED | implicit / naming-only |
| hoofdstuk_10 | (none) | `runtime/data/source_imports/legacy_agentic_inputs/workspace/00_input/hoofdstuk_10.txt` | CLEAN_REPO_STAGED | implicit / naming-only |

### Excerpt / Segment inventory + format

| id | format | where found | origin |
|---|---|---|---|
| sayur_052_066 | `[a-z]+_\d{3}_\d{3}` | `runtime/runs/` + `runtime/indices/run_index.json` | CLEAN_REPO |
| SAJUR-A / SAJUR-B | `[A-Z]+-[A-Z]` | `runtime/data/source_imports/sayur_groente_001/EXCERPT_MAP.md` | CLEAN_REPO_STAGED |
| RB-0001..RB-0028 | `RB-\d{4}` | `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv` | CLEAN_REPO_STAGED |
| BLK-0009..BLK-0036 | `BLK-\d{4}` | `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv` | CLEAN_REPO_STAGED |

### Huidige alignment-signalen (facts-only)

| signal | path | origin | notes |
|---|---|---|---|
| EXCERPT_MAP line ranges | `runtime/data/source_imports/sayur_groente_001/EXCERPT_MAP.md` | CLEAN_REPO_STAGED | References canonical_concat.txt (staged). |
| canonical_concat.txt | `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/index/canonical_concat.txt` | CLEAN_REPO_STAGED | Line ranges referenced by EXCERPT_MAP. |
| recipe_block_manifest.tsv | `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/recipe_block_manifest.tsv` | CLEAN_REPO_STAGED | RB/BLK -> page ranges. |
| page_to_recipe_block.tsv | `runtime/data/source_imports/legacy_mr2026_alignment_spine/DERIVED/step4_structure/ledgers/page_to_recipe_block.tsv` | CLEAN_REPO_STAGED | page -> RB mapping (NONE for non-RB pages). |
| run command params | `runtime/runs/*/command.txt` | CLEAN_REPO | excerpt_source + excerpt_version for runs. |
| run index manifest | `runtime/indices/run_index.json` | CLEAN_REPO | excerpt metadata for completed run only. |
