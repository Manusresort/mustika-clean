# Vision & Strategy — Mustikarasa Project

## 1. Why this project exists
- Mustika Rasa is een historisch document, niet alleen een kookboek.
- Digitale bronnen zijn incompleet en technisch onbetrouwbaar (OCR, scans, structuur).
- Doel is een eerlijk, controleerbaar en herbruikbaar toegankelijk systeem.
- Het doel is niet alleen “een mooie vertaling”, maar een traceerbaar proces.
- Het project bedient meerdere doelgroepen: onderzoekers, redacteurs, liefhebbers.

## Governance Layers: Project vs System

### Governance Layer A — Project Governance (GOV-A)
- GOV-A is governance over the design and development of the Mustika Rasa system.
- GOV-A is fully human and governs strategy, capability definition, phasing, workflows, agents, validators, and contracts.
- GOV-A artefacts include `docs/VISION_AND_STRATEGY.md`, `docs/CODEX_TODO.md`, and `docs/WORKFLOW.md`.
- GOV-A decisions are design-time decisions, not runtime enforcement.

### Governance Layer B — System Governance (GOV-B)
- GOV-B is governance embedded in the system and enforced at runtime.
- GOV-B operates through formal roles, output contracts, validators, gates, and canonical trails.
- GOV-B governs what runs may produce and what can be considered canonical.
- GOV-B emerges progressively as capabilities are implemented.

Project phases describe how GOV-A designs and formalizes GOV-B over time.
Phases do NOT imply increased agent autonomy or transfer of decision authority.
Authority remains human unless explicitly and procedurally governed.

## 2. Three sequential missions

### 2.1 Phase 0 — Source Restoration (technical, reversible)
- Doel: een betrouwbare digitale master die het originele boek zo goed mogelijk weerspiegelt.
- Kernactiviteiten:
  - OCR-correctie
  - reconstructie van tabellen, pagina’s en structuur
  - koppelen en registreren van afbeeldingen
  - detectie en registratie van ontbrekende of beschadigde elementen

> Technische fouten herstellen we.  
> Inhoudelijke fouten behouden we — en documenteren we.

- Alle herstelacties zijn traceable en reproduceerbaar.
- Rollbacks zijn documentair verplicht: per herstelactie moeten vastliggen:
  - oorspronkelijke staat
  - herstelde staat
  - reden van wijziging
- Bronrestauratie herschrijft geen geschiedenis; het herstelt dragers (scans, OCR, structuur).

### 2.2 Phase 1 — Scholarly Edition (preserve, but illuminate)
- Doel: een editie die trouw is aan het origineel en fouten/tegenstrijdigheden zichtbaar maakt.
- We corrigeren inhoud niet, maar annoteren en documenteren.
- Onderscheid:
  - pure brontekst (ID, Indonesisch, Engels)
  - geannoteerde wetenschappelijke editie (voetnoten/annotaties)
- Inhoudelijke fouten blijven staan, maar:
  - worden expliciet benoemd
  - worden vastgelegd als beslispunten voor latere fasen
- Glossary‑lifecycle en Research‑rol leveren bewijs en context.

### 2.3 Phase 2 — Public Edition (modernise with accountability)
- Doel: een veilige, leesbare, inspirerende publiekseditie (koffietafelboek‑ambitie).
- Recepten mogen herschreven/gecorrigeerd worden.
- Veiligheid en uitvoerbaarheid krijgen prioriteit.
- Design, narratief en leesbaarheid tellen mee.
- Elke modernisering is herleidbaar:
  - wat is er veranderd
  - waarom
  - hoe verhoudt dit zich tot de wetenschappelijke editie

## 3. Capability-Driven Strategy

Strategie volgt deze volgorde:
objective → goal → capability → phase → agent.

Capabilities zijn de stabiele as door de tijd; fases en agents kunnen wisselen
zonder dat de kern-doelen veranderen. Phases zijn strategische containers
voor capability‑maturatie, niet harde delivery‑milestones. Agents zijn
embodiments van capabilities (zie docs/CAPABILITY_AGENT_MAP.md,
docs/P8_CAPABILITY_MAP.md, docs/AGENTS.md), geen autonome beslissers.
Phase-4 cross-capability structural levers are analysed separately in
docs/PHASE4_CROSS_CAPABILITY_STRUCTURAL_LEVERS.md to avoid agent-first or solution-first design.
Agent roles and agent-gap analyses are derived only after cross-capability structural levers have been identified.
This prevents agent-first or solution-first system design and preserves editorial authority.

Governance‑grenzen:
- Strategie definieert legitimiteit en scope.
- TODO/backlog bevat alleen uitvoeringskandidaten.
- Agents confereren nooit autoriteit of canoniek gewicht op zichzelf.

## 4. Strategic Phasing Rationale

Strategische phasing bestaat om capabilities gecontroleerd te laten rijpen,
risico’s te isoleren, en herhaalbaarheid te borgen. Fase‑besluiten horen
bij strategie (dit document), niet bij TODO’s of workflows.

## 5. Central principle: “zo was het — zo is het — en dit is waarom het veranderde”

> Het systeem moet — waar mogelijk — kunnen tonen:
> “zo was het — zo is het — en dit is waarom het veranderde.”

Dit geldt voor:
- tekst
- tabellen
- afbeeldingen
- terminologie
- annotaties
- veiligheidsaanpassingen
- designkeuzes

Het principe verbindt traceability en auditability:
oorsprong → huidige staat → rationale.

## 6. Agents, governance and “organised doubt”

### 6.1 Agents as signalers, not deciders
- Agents signaleren, analyseren, annoteren en adviseren.
- Agents nemen geen onomkeerbare inhoudelijke beslissingen.
- Human Gate en governance zijn eindverantwoordelijk bij betekenisvolle risico’s.
- Rollen omvatten o.a.: Translation, Fidelity, Readability, Glossary, Annotation, Recipe,
  Cohesion/Continuity, Design, Table, Image, Source Integrity.

### 6.2 Governance layer
- Orchestrator bewaakt proces, templates en escalaties.
- Methodology & Accountability Archivist bewaakt audit‑trail en rationale.
- Troubleshooting / Incident & Resilience detecteert en classificeert incidenten.
- Technical Strategy Advisor adviseert over modelkeuzes.
- Glossary & Research agents werken binnen lifecycle‑context en leveren proposals/evidence.
- Governance bewaakt stop‑model (soft‑stop, governance‑stop, human gate) en logging.
- Beslissingen moeten herleidbaar zijn tot governance‑artefacten en logs.

### 6.3 Red-teaming as “organised doubt”
- Red‑teaming is gestructureerde twijfel bij grote, gevoelige of moeilijk herleidbare besluiten.
- Niet “overal tegen”, maar systematisch aannames en alternatieven toetsen.
- Levert een gestructureerde review (bijv. [RED_TEAM_REVIEW]).
- Kan escalatie adviseren, heeft geen absolute veto‑macht.
- Detailuitwerking volgt later; dit is het strategisch kader.

## 7. Definition of Done

“Done” betekent in dit project:
- relevante agents hebben binnen hun domein gecontroleerd
- alle belangrijke beslissingen zijn traceable
- risico’s zijn benoemd en niet stil genegeerd

> Done betekent NIET: er zijn geen fouten meer — maar: fouten zijn begrepen, benoemd en gelogd.

- Elke betrokken agent kan PASS/FAIL terugmelden binnen zijn scope.
- Als één cruciaal domein FAIL meldt → het artefact is niet done.
- Bij FAIL volgt governance‑stop en eventueel human gate.
- Dit sluit aan bij governance tests en het stop‑model.

## 8. Long-term vision
- Een betrouwbare digitale master (bronrestauratie).
- Een wetenschappelijke editie als stabiele referentie.
- Een publiekseditie die waardig, veilig en aantrekkelijk is.
- Een documentair spoor waarmee toekomstige redacties en onderzoekers verder kunnen.
- Het project bouwt een kennisinfrastructuur, niet alleen een eenmalige vertaling.
