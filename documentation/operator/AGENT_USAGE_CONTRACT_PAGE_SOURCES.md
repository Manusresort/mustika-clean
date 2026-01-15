# Agent Usage Contract — Page Sources

## Status
Normatief en bindend. Dit contract is van toepassing op alle agent-activiteiten
rond page-based sources in deze repository.

## Scope
Paden en types:
- `runtime/data/ingest/page_sources/png/` (PNG)
- `runtime/data/ingest/page_sources/ocr_txt/` (TXT)
- `runtime/data/ingest/page_sources/ocr_tsv/` (TSV)

## Hard invariants
- `page_sources` is read-only voor agents.
- Geen auto-promotion; `runtime/canonical/` blijft read-only.
- Page identity is bindend: `page_id = filename stem` (alles vóór extensie).
- Geen aannames over volledigheid of correctheid van OCR.
- Ontbrekende TXT/TSV is toegestaan; geen impliciete aanvulling.

## Allowed READ actions
- Lezen van PNG/TXT/TSV op basis van `page_id`.
- Correlatie tussen bestanden uitsluitend op basis van identieke filename stem.

## Forbidden actions
- Geen writes, overwrites, renames of deletes in `page_sources`.
- Geen herstructurering of verplaatsing van `page_sources`.
- Geen wijzigingen in `runtime/canonical/`.

## Allowed output locations
Voor nieuwe artefacten (alleen voorbeelden; geen autorisatie):
- `runtime/proposals/`
- `runtime/runs/`
- `experiments/`
- `documentation/`

## OCR re-run policy
- OCR re-run is toegestaan, maar output mag nooit terug naar `page_sources`.
- OCR output moet naar een nieuwe locatie met duidelijke rationale en provenance.

## Provenance requirements
Elke afgeleide output moet minimaal vastleggen:
- `page_id`
- bronpaden (exacte input files)
- doel van de verwerking
- outputlocatie(s)

## Out of scope
- Mapping naar excerpts of chapters.
- Canonical publishing of any form of auto-promotion.
- Normalisatie of correctie van bronbestanden in `page_sources`.

## Samenvatting
- `page_sources` is read-only bronlaag.
- `page_id` = filename stem (bindend).
- Ontbrekende OCR-varianten zijn toegestaan; geen aannames.
- Output mag alleen buiten `page_sources` plaatsvinden met provenance.
