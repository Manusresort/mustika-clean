# Phase-6 — Excerpt-Aware Runner Design

Status: design only (no runtime changes)  
Related: P6_EXCERPT_BINDING_SPEC.md, P6_EXCERPT_BINDING_INTEGRATION_PLAN.md, P6_EDITORIAL_WORKFLOW_MINI.md, P6_SAYUR_INTERNAL_WORK_CASE01.md

---

## 1. Purpose

Dit document beschrijft hoe een toekomstige runner excerpt-metadata
(`excerpt_id`, `excerpt_source`, `excerpt_version`) expliciet:

- ontvangt (via CLI of config),
- logt (run-log header),
- en doorgeeft aan JSON-artefacts (annotator/challenger/crew),

zodat elke excerpt-gebaseerde run in Phase-6:

- herleidbaar is tot een specifiek excerpt,
- consistent is met P6_EXCERPT_BINDING_SPEC.md,
- zonder retro-actief bestaande runs te wijzigen.

Het gaat om **ontwerp**, niet om geïmplementeerde code.

---

## 2. Design Constraints

1. **Documentair, geen enforcement**  
   Excerpt-metadata is traceability-informatie.  
   Het stuurt geen agent-autonomie aan, voert geen automatische validatie uit,
   en verandert geen lifecycle-regels.

2. **Backwards compatible**  
   Bestaande runners blijven werken zonder excerpt-parameters.
   Het excerpt-aware pad is opt-in via config of CLI.

3. **Generic over chapters**  
   Het ontwerp is niet SAYUR-specifiek:
   - SAYUR Case-01 is de eerste toepassing,
   - maar LOBAK of andere hoofdstukken gebruiken exact hetzelfde patroon.

4. **No retrofitting**  
   Oude logs en JSON worden niet herschreven; evaluaties documenteren simpelweg dat excerpt-metadata ontbrak.

---

## 3. Interface Overview

De excerpt-aware runner kent twee hoofd-ingangen:

1. **CLI-parameters** (directe aanroep via Codex/terminal)  
2. **Configbestand** (YAML/JSON) dat door Codex wordt beheerd

In beide gevallen wordt dezelfde set velden gebruikt:

- `excerpt_id`
- `excerpt_source`
- `excerpt_version`

Deze waarden worden ongewijzigd:

- in de run-log header opgenomen,
- in annotator/challenger/crew JSON geplaatst.

---

## 4. CLI Design (conceptueel)

### 4.1 Flags

Voorgestelde CLI-flags:

- `--excerpt-id <ID>`  
- `--excerpt-source <PATH>`  
- `--excerpt-version <TAG>`

Voorbeeld (concept):

```bash
python sandbox/crew/run_excerpt_workflow.py \
  --excerpt-id sayur_052_066 \
  --excerpt-source docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md \
  --excerpt-version locked-2026-01-05 \
  --config sandbox/crew/configs/sayur_case01.yaml
```

Gedrag (design):

- als alle drie flags aanwezig zijn:
  - runner markeert de run als “excerpt-aware”,
  - metadata wordt in log-header + JSON opgenomen.
- als geen van de drie flags aanwezig zijn:
  - runner gedraagt zich als “pre-binding” (backwards compatible),
  - excerpt-metadata velden worden weggelaten of op `null` gezet.
- gemengde gevallen (bijv. id zonder source) worden als configuration error behandeld
  (zie sectie 8).

### 4.2 Subcommands

Het ontwerp laat ruimte voor subcommands, bijv.:

- `run_sayur_case`
- `run_lobak_case`

maar legt geen vaste subcommand-namen vast.  
Belangrijk is dat **ongeacht subcommand** dezelfde excerpt-flags worden gebruikt.

---

## 5. Config Design (YAML/JSON, conceptueel)

Naast CLI-flags kan excerpt-metadata in een configbestand staan.

### 5.1 YAML-voorbeeld

```yaml
run_id: RUN_P6_SAYUR_CASE01_001
runner: excerpt_workflow

excerpt:
  id: sayur_052_066
  source: docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md
  version: locked-2026-01-05

pipeline:
  agents:
    - annotator
    - challenger
    - crew
  mode: sandbox
```

Design-regel:

Als zowel CLI- als config-waarden aanwezig zijn:

config is de “bron van waarheid”,

CLI mag enkel defaults overschrijven,

conflict (verschillende waarden) → duidelijke config-fout (soft-stop), geen stille override.

5.2 JSON-voorbeeld
{
  "run_id": "RUN_P6_SAYUR_CASE01_001",
  "runner": "excerpt_workflow",
  "excerpt": {
    "id": "sayur_052_066",
    "source": "docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md",
    "version": "locked-2026-01-05"
  },
  "pipeline": {
    "agents": ["annotator", "challenger", "crew"],
    "mode": "sandbox"
  }
}

6. Logging Contract
6.1 Run-log Header

Elke excerpt-aware run-log begint met:

RUN_ID: RUN_P6_SAYUR_CASE01_001
TIMESTAMP: 2026-01-05T15:49:46Z
EXCERPT_ID: sayur_052_066
EXCERPT_SOURCE: docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md
EXCERPT_VERSION: locked-2026-01-05
MODE: sandbox


Header is documentair; geen parser mag aannemen dat dit machine-enforced is.

Niet-excerpt-aware runs laten deze velden weg.

6.2 Errors rond excerpt-metadata

Missing required metadata (in excerpt-aware modus):

runner logt config-error,

voert geen workflow uit (soft/governance-stop).

Conflict CLI vs config:

runner logt het conflict,

stopt vóór agents starten.

7. JSON Contract voor Workflow Artefacts

Runner plaatst metadata consistent in:

annotator_raw.json

challenger_raw.json

crew_decisions_provisional.json

7.1 annotator_raw.json
{
  "excerpt_id": "sayur_052_066",
  "excerpt_version": "locked-2026-01-05",
  "items": [
    {
      "line_id": "052",
      "text": "Ada sajuran jang tak tahan hudjan semasa tumbuhnja, seperti",
      "label": "HISTORICAL",
      "notes": "Seasonal framing; agriculture context."
    }
  ]
}

7.2 challenger_raw.json
{
  "excerpt_id": "sayur_052_066",
  "excerpt_version": "locked-2026-01-05",
  "issues": [
    {
      "issue_type": "GOVERNANCE",
      "severity": "WARNING",
      "span": "bajem",
      "comment": "Glossary pressure; no escalation required."
    }
  ]
}

7.3 crew_decisions_provisional.json
[
  {
    "term_id": "bajem@line066",
    "excerpt_id": "sayur_052_066",
    "excerpt_version": "locked-2026-01-05",
    "decision_status": "CREW_PROVISIONAL",
    "decision_origin": "crew",
    "rationale": "Seasonal leafy vegetable; glossary-relevant but not escalated.",
    "ready_for_human_review": false
  }
]


(term_id, excerpt_id, excerpt_version) vormen samen een unieke sleutel per run.

8. Error & Edge-case Handling (Design)
8.1 Missing excerpt in excerpt-aware context

Config geeft aan dat de run excerpt-based is, maar metadata ontbreekt →
config-fout, geen workflow-uitvoer.

8.2 Mismatch log ↔ JSON

Eventuele tooling mag mismatch signaleren als governance-issue,
maar geen auto-rollback of auto-fix.

9. Toepassing op SAYUR Case-01

Case-01 specificeert:

excerpt_id: sayur_052_066

excerpt_source: docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md

excerpt_version: locked-2026-01-05

Eerste excerpt-aware run moet deze waarden opnemen in:

config,

log-header,

JSON-artefacts,

en evaluatie-docs.

Tot implementatie bestaat, blijft Case-01 pending.

10. Roll-out & Governance

Design (dit document) — geen codewijzigingen.

Prototype (sandbox) — eerste excerpt-aware runner, output blijft sandbox.

Governance Review — Human Gate beoordeelt impact.

Adoptie — andere hoofdstukken volgen hetzelfde patroon.

Dit document autoriseert geen code-changes; wijzigingen lopen via governance-processen.

End of document.
