# Phase-6 — Excerpt Binding Integration Plan

Status: documentary design (no runtime changes)  
Related: P6_EXCERPT_BINDING_SPEC.md, P6_EDITORIAL_WORKFLOW_MINI.md, P6_WORKFLOW_SAYUR_MINI.md, P6_SAYUR_INTERNAL_WORK_CASE01.md

---

## 1. Purpose & Background

Pilot 03 en de SAYUR Case-01 voorbereiding hebben laten zien dat:

- glossary- en workflow-pilots kunnen draaien zonder dat excerpt-keuze goed “gebonden” is aan logs en artefacts;
- het mogelijk is dat een runner een ander excerpt gebruikt dan het ontwerpdocument bedoelt.

P6_EXCERPT_BINDING_SPEC.md definieert daarom de drie documentaire excerpt-velden:

- `excerpt_id`
- `excerpt_source`
- `excerpt_version`

Deze integration plan beschrijft **waar** die velden in de lifecycle moeten leven en **hoe** ze zich verplaatsen tussen:

- plannen & case-files,
- runners & config,
- logs & JSON-artefacts,
- evaluaties & syntheses.

Dit plan beschrijft GEEN runtime-implementatie; het is een documentair ontwerp.

---

## 2. Design Principles

1. **Documentair, niet dwingend**  
   Excerpt-metadata maakt runs herleidbaar, maar verandert geen agent-autonomie en voegt geen automatische validatie toe.

2. **Geen retroactieve geschiedenis-herschrijving**  
   Bestaande runs uit Phase-4/5/6 blijven zoals ze zijn; we annoteren hoogstens dat excerpt-metadata ontbrak.

3. **Layered integration**  
   Elke lifecycle-laag heeft een duidelijke plek voor excerpt-metadata:
   - design (pilot-plannen, case-files),
   - runtime-config (CLI / YAML, design only),
   - run-logs,
   - workflow JSON,
   - evaluatie- en synthese-docs,
   - Codex-session logs.

4. **Shared conventions**  
   De drie keys (`excerpt_id`, `excerpt_source`, `excerpt_version`) worden overal met dezelfde naam gebruikt.

---

## 3. Integration Map over de Lifecycle

### 3.1 Design Layer — Pilots & Cases

Artefacten:
- pilot-plannen (bijv. P6_SAYUR_MINI_WORKFLOW_PILOT_PLAN.md),
- case-bestanden (bijv. P6_SAYUR_INTERNAL_WORK_CASE01.md),
- excerpt-selectie-notes.

Vereisten:
- Elk excerpt-gebaseerd ontwerpdocument bevat een blok:

  - `excerpt_id` — korte, stabiele ID (bijv. `sayur_052_066`)
  - `excerpt_source` — pad naar governing excerpt-document
  - `excerpt_version` — tag (bijv. `v1` of `locked-YYYY-MM-DD`)

- De rationale voor de keuze (waarom dit fragment) verwijst naar deze ID.

Doel:
- Ontwerp en uitvoering delen exact dezelfde excerpt-referentie.

---

### 3.2 Runtime Config Layer — Runner / CLI (Design Only)

Artefacten:
- runner-scripts (bijv. sandbox/crew/*_runner.py),
- toekomstige config (YAML/JSON),
- toekomstige P6_EXCERPT_AWARE_RUNNER_DESIGN.md (nog te schrijven).

Vereisten (design, geen implementatie):

- Excerpt-metadata wordt doorgegeven aan de runner via één van de volgende, nog te kiezen patronen:
  - CLI-argumenten, bijv.:
    - `--excerpt-id`
    - `--excerpt-source`
    - `--excerpt-version`
  - of config-velden in een run-config (YAML/JSON), bijv.:

    ```yaml
    excerpt:
      id: sayur_052_066
      source: docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md
      version: locked-2026-01-05
    ```

- De runner is verantwoordelijk om deze waarden onveranderd in logs en JSON-artefacts door te geven.
- Concrete keuzes (CLI vs YAML) worden later vastgelegd in een apart document, bijv. `P6_EXCERPT_AWARE_RUNNER_DESIGN.md`.

Non-goal:
- Dit plan schrijft geen code en verandert geen bestaande runners.

---

### 3.3 Logging Layer — Run Logs

Artefacten:
- sandbox/crew/run_logs/*.log
- andere run-logs die een excerpt behandelen.

Vereisten (voor toekomstige runs):

- Elk excerpt-gebaseerd logbestand start met een klein metadata-blok, bijvoorbeeld:

EXCERPT_ID: sayur_052_066
EXCERPT_SOURCE: docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md
EXCERPT_VERSION: locked-2026-01-05 
- Dit blok wordt beschouwd als documentaire header; het wordt niet gebruikt voor automatische gating.
- Bestaande logs worden NIET retroactief aangepast; een evaluatienote kan aangeven dat metadata ontbreekt.

---

### 3.4 Workflow JSON Layer — Annotator / Challenger / Crew

Artefacten:
- annotator_raw.json
- challenger_raw.json
- crew_decisions_provisional.json
- human_review_notes.md

Vereisten:

**annotator_raw.json / challenger_raw.json**

- Top-level JSON-object bevat:

- `excerpt_id`
- `excerpt_version`

- Deze waarden zijn identiek voor alle items in het bestand.

**crew_decisions_provisional.json**

- Elke decision-record bevat:

- `excerpt_id`
- `excerpt_version`

- De combinatie van (term_id, excerpt_id, excerpt_version) identificeert de beslissing ondubbelzinnig binnen een run.

**human_review_notes.md**

- De kop of metadata van het bestand bevat een korte verwijzing:

- `Excerpt: <excerpt_id> (source: <excerpt_source>, version: <excerpt_version>)`

Non-goal:
- Geen automatische validatie dat JSON en logheaders overeenkomen; dit blijft een menselijke audit-taak.

---

### 3.5 Evaluation & Synthesis Layer

Artefacten:
- P6_SAYUR_MINI_WORKFLOW_PILOT*_EVALUATION.md
- P6_SAYUR_MINI_WORKFLOW_PILOT_SYNTHESIS.md
- toekomstige evaluatie-templates.

Vereisten:

- Evaluatiedocumenten bevatten in hun contextsectie:

- `excerpt_id`
- `excerpt_source`
- `excerpt_version`

- Wanneer een evaluatie historisch is (pre-binding), wordt expliciet vermeld:
- dat de originele run deze metadata niet droeg,
- dat excerpt-binding later als design-safeguard is toegevoegd.

- Synthese-documenten vermelden excerpt-binding wanneer traceability een rol speelt in de beoordeling van workflow-gezondheid.

---

### 3.6 Codex Session Logging Layer

Artefact:
- docs/CODEX_SESSION_LOG.md

Richtlijn:

- Wanneer een SESSION direct gekoppeld is aan een excerpt-gebaseerde run, wordt in de Summary of een korte extra regel opgenomen, bijv.:

- `Excerpt: excerpt_id=<...>, source=<...>, version=<...>`

- Dit is een conventie, geen verplicht schema; het doel is terugzoeken te vergemakkelijken.
- Bestaande SESSION-blocks worden NIET aangepast; nieuwe sessies kunnen deze conventie volgen.

---

## 4. Application to Current Workflows

### 4.1 SAYUR Case-01

- Case-01 (lijnen 52–66) is voorbereid, maar nog niet uitgevoerd omdat de huidige runner niet excerpt-aware is.
- Dit plan vereist dat:

- Case-01 case-file een expliciet excerpt-blok heeft (id/source/version),
- de toekomstige Case-01 run een excerpt-aware runner gebruikt die deze metadata:

  - in het log-header schrijft,
  - en in annotator/challenger/crew JSON integreert.

- Totdat zo’n run bestaat, blijft Case-01 op pending en worden er geen kunstmatige bindings gemaakt.

### 4.2 Andere hoofdstukken (niet-SAYUR)

- Dezelfde excerpt-metadata regels gelden voor:
- LOBAK,
- andere hoofdstukken,
- toekomstige pilots.
- Er wordt geen SAYUR-specifieke logica geïntroduceerd; alles is generiek.

---

## 5. Phasing & Next Steps

We onderscheiden drie stappen:

**Phase A — Documentation & Templates (NOW)**  
- Spec (P6_EXCERPT_BINDING_SPEC) is vastgesteld.  
- Workflow-docs en evaluatie-templates noemen nu expliciet excerpt-metadata.  
- Dit integration plan definieert waar metadata moet landen op elke laag.

**Phase B — Runner Design (LATER, documentair)**  
- Een nieuw document (bijv. `P6_EXCERPT_AWARE_RUNNER_DESIGN.md`) beschrijft:
- concrete CLI/config-velden,
- hoe metadata vanuit config naar log + JSON wordt doorgegeven,
- testcases voor excerpt-binding (design only).

**Phase C — Runtime Instrumentation (DEFERRED)**  
- Pas na governance-goedkeuring wordt de Python-runtime aangepast.
- Alle wijzigingen zijn:
- expliciet,
- gelogd,
- en getest met rollback-plan.

Dit plan dekt alleen Phase A en de ontwerp-randvoorwaarden voor B/C.

---

## 6. Governance & Boundaries

- Excerpt-metadata:

- verandert geen agent-autonomie,
- geeft geen toestemming voor automatische correctie,
- bepaalt niet welke excerpt “juist” is — dat blijft een menselijk oordeel.

- Human Gate blijft vereist voor:
- canonieke editorial beslissingen,
- workflow-wijzigingen met publicatie-impact,
- brede repo-migraties.

- Bestaande runs uit Phase-3/4/5/6 worden niet herschreven om excerpt-binding te simuleren.

---

## 7. Checklist for Future Work

Bij nieuwe excerpt-gebaseerde workflows:

- [ ] Excerpt-selection doc bevat excerpt_id/source/version.
- [ ] Case-file verwijst naar deze excerpt-metadata.
- [ ] Runner-config neemt de metadata over (volgens toekomstige runner-design).
- [ ] Run-log bevat een excerpt-metadata header.
- [ ] annotator_raw.json / challenger_raw.json hebben top-level excerpt_id/version.
- [ ] crew_decisions_provisional.json bevat excerpt_id/version per record.
- [ ] Evaluatie-docs herhalen excerpt-metadata in de contextsectie.
- [ ] Codex-session log bevat een korte excerpt-notitie in de Summary.

Dit checklist-blok mag door toekomstige sessies worden gebruikt als referentie,
maar voert zelf geen gedrag af.
