# Canonical Index — What is “Source of Truth” here?

Purpose: kort en duidelijk aangeven welke documenten leidend zijn
(canonical) en waarom — zonder structuur aan te passen.

Canonical docs (bron voor besluiten):
- docs/total_project.md
- docs/VISION_AND_STRATEGY.md
- docs/CONTENT_ROADMAP.md
- docs/WORKFLOW.md
- docs/AGENTS.md
- docs/ANNOTATION_STYLECARD_P4.md
- docs/10-governance/*  (policies, human gate, rollback, incident)

Rules:
- canonical docs worden niet “stilletjes aangepast”
- conflicten worden opgelost door canonical + uitleg
- wijzigingen zijn traceable en human-gated

Deze pagina is informatief — geen policy op zichzelf.

---

## Canonical Decision Records (Phase-7 onward)

This index will begin filling during Phase-7.
Each canonical entry will:

- reference the governing excerpt (id, source, version),
- link to the review note,
- link to the corresponding AI artefacts,
- include a short human-written justification.

Until decisions exist, this section remains intentionally empty.

### 2026

- id: P7_CANONICAL_GLOSSARY_LOBAK_001
  decision_type: glossary/lemma_inclusion
  excerpt:
    id: lobak_034_048
    source: docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md
    version: locked-2026-01-12
  artefacts:
    decision_record: docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSORY_LOBAK_001.md
    run_log: sandbox/crew/run_logs/lobak_034_048/RUN_lobak_034_048_20260106T220558_20260106T220558.log
    annotator_json: sandbox/crew/run_outputs/lobak_034_048/RUN_lobak_034_048_20260106T220558/annotator_primary.json
  rationale_summary: >
    "lobak" is canoniek opgenomen als glossary-lemma (itemisation only);
    betekenis en vertaling blijven open voor latere beslissingen.
