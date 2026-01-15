# Docs Information Architecture — Phase 5

Status: documentation — canonical map  
Purpose: duidelijk maken welke documenten leidend zijn, welke sandbox zijn,
en welke archief/geschiedenis — zodat iedereen weet "waar wat leeft".

> Motto: structuur toevoegen, niets verplaatsen (tenzij later besloten).

---

## 1. Canonical (leidende documenten)

Deze documenten representeren de "waarheid van het project" in hun domein
en mogen alleen bewust worden aangepast (met log en review).

- docs/total_project.md
- docs/VISION_AND_STRATEGY.md
- docs/CONTENT_ROADMAP.md
- docs/WORKFLOW.md
- docs/AGENTS.md
- docs/ANNOTATION_STYLECARD_P4.md
- docs/10-governance/*  (policies, gates, rollback, incident playbooks)

> Regel: canonical = bron voor besluiten.  
> Als iets conflicteert, wint canonical (met uitleg).

---

## 2. Sandbox & Pilots (geregisseerde experimenten)

Alle documentaire sporen die laten zien WAT we getest hebben,
zonder dat ze beleid dicteren.

- docs/pilots/*
- docs/PILOT_SET_P4_V1.md
- docs/P4_CONSOLIDATION_REPORT_SAYUR_SANDBOX.md
- docs/P4_HANDOVER_PACK_SAYUR_SANDBOX.md
- sandbox/crew/* (runners, prompts, logs)
- logs/sandbox/* (indien aanwezig)

> Regel: sandbox = bewijs en context, niet automatisch productie.

---

## 3. Phase-5 Consolidation & Preparation

Documenten die helpen begrijpen, ordenen en voorbereiden:

- docs/AGENT_PROMPT_PATTERN_P5.md
- docs/P5_PROMPT_CONSOLIDATION_NOTE.md
- docs/pattern_reviews/*
- docs/P5_TRANSLATION_EXPECTATION_EVIDENCE.md
- docs/P5_TODO.md
- docs/CODEX_TODO.md
- docs/CODEX_SESSION_LOG.md

> Regel: deze documenten maken dingen expliciet,  
> maar veranderen gedrag niet zonder governance-approval.

---

## 4. Data & Source Handling

Waar originele bronnen, imports en mappings leven:

- data/source_imports/*
- README_SOURCE_IMPORT.md (per bronmap)
- EXCERPT_MAP.md (waar van toepassing)

> Regel: brondata blijft intact; aanpassingen zijn traceable.

---

## 5. Prompts & Crews

- sandbox/crew/prompts/*
- crew-config YAML’s
- micropilot system-prompts

> Regel: prompts volgen het Phase-5 pattern —  
> wijzigingen = documentair + human-gated.

---

## 6. Manifest (machine-leesbaar overzicht)

Zie: `docs/manifest_p5.yaml`

---

## 7. Repository Archivist (ondersteunende rol)

De Repository Archivist bewaakt de documentstructuur en signaleert
sprawl, duplicatie en onduidelijke plaatsing. De archivist:

- wijzigt GEEN bestanden, namen of structuur
- levert alleen rapporten (ARCHIVIST_REPORT) en voorstellen
- werkt altijd in lijn met:
  - docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md
  - manifest_p5.yaml

Alle archivist-rapporten worden bewaard in:

`docs/archivist_reports/`

Doel: navigatie verbeteren en risico op document-sprawl vroeg signaleren,
zonder onnodige herstructurering.

(De bestaande nummering van secties hoeft NIET te worden aangepast.)

## 7. Navigatie-afspraken

- nieuwe docs: plaats ze in de juiste categorie  
- twijfel? label voorlopig **sandbox**  
- nooit canonical-documenten herschrijven zonder uitleg/log

Einde document.
