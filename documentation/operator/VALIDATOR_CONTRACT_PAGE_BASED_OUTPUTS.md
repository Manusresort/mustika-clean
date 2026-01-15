# Validator Contract — Page-Based Agent Outputs

## Status
Normatief en bindend. Dit contract definieert minimale validatie-eisen
voor agent-output die page-based sources gebruikt.

## Scope
Van toepassing op alle agent-output die verwijst naar:
- `runtime/data/ingest/page_sources/png/`
- `runtime/data/ingest/page_sources/ocr_txt/`
- `runtime/data/ingest/page_sources/ocr_tsv/`

## Relationship to Agent Usage Contract
Dit contract sluit expliciet aan op:
- `documentation/operator/AGENT_USAGE_CONTRACT_PAGE_SOURCES.md`

## Validation goals
- Alleen structurele en provenance-eisen verifiëren.
- Geen inhoudelijke kwaliteit, interpretatie of correctheid beoordelen.

## Required provenance fields
Elke agent-output MUST expliciet bevatten:
- `page_id`
- gebruikte bronbestanden (volledige paden)
- doel van de agent-actie
- outputlocatie

## Required filesystem evidence
- `page_id` MUST exact overeenkomen met de filename-stem in `page_sources`.
- Referenties naar niet-bestaande `page_sources` files ⇒ VALIDATION FAIL.
- Ontbrekende OCR/TSV is toegestaan indien expliciet vermeld.

## Validation rules (normatief)
- Validator MAY uitsluitend read-only inspectie uitvoeren.
- Validator MUST NOT bestanden wijzigen of genereren.
- Validator MUST NOT inhoudelijke juistheid of taal evalueren.

## Explicit non-goals
- Geen inhoudelijke beoordeling of redactionele validatie.
- Geen normalisatie of correctie van bronbestanden.
- Geen auto-promotion; `runtime/canonical/` blijft read-only.

## Validation outcomes
- PASS: structureel correct + provenance volledig.
- FAIL: ontbrekende of inconsistente provenance.
- INCONCLUSIVE: bronbestanden ontbreken maar dit is expliciet verklaard.

## Samenvatting
- Validatie is puur structureel en provenance-gedreven.
- `page_id`-matching met `page_sources` is bindend.
- Validator is read-only en wijzigt niets.
