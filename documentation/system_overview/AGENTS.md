# Mustikarasa Agents

Dit document geeft een overzicht van de agents in de multi-agent workflow
en verwijst naar hun prompt-bestanden in `prompts/`.

Ownership en verantwoordelijkheidsverdeling tussen agents
wordt formeel beschreven in docs/CAPABILITY_AGENT_MAP.md.

## Translation Quality Agent
- Rol: Controleert en verbetert de vertaling met focus op betekenis en nuance.
- Prompt: `prompts/translation.md`

- Autonomy & Escalation:
  - Soft-stop: vraag Fidelity/Research bij onduidelijkheid.
  - Governance-stop: ambiguïteit met mogelijke betekenisverschuiving.
  - Hard-stop: medische/allergie/juridische betekenis.

## Readability Editor
- Rol: Verbetert leesbaarheid en stijl zonder betekenis te veranderen.
- Prompt: `prompts/readability.md`

- Autonomy & Escalation:
  - Soft-stop: mogelijke betekenisimpact -> check met Fidelity.
  - Governance-stop: conflict met Fidelity of Glossary-richtlijnen.
  - Hard-stop: cultureel gevoelige passages met risico.

## Fidelity Agent
- Rol: Bewaakt trouw aan het origineel en noteert eventuele afwijkingen.
- Prompt: `prompts/fidelity.md`

- Autonomy & Escalation:
  - Soft-stop: cross-check met Research.
  - Governance-stop: blijvende discrepantie na hercontrole.
  - Hard-stop: riskante betekenisverschuiving rond gezondheid/geschiedenis.

## Orchestrator
- Rol: Regisseert het redactieproces en bewaakt voortgang en samenhang.
- Prompt: `prompts/orchestrator.md`
- Mandaat en grenzen zijn vastgelegd in de Mandate and Boundaries-sectie van `prompts/orchestrator.md`.
- Kernverantwoordelijkheid: workflow-coördinatie, agents aansturen, templates en governance bewaken.
- De Orchestrator is geen inhoudelijke eindbeslisser; terminologie/publicatie gaat via mens en/of meta-agents met human gate.

- Autonomy & Escalation:
  - Soft-stop: herordening, extra context, aanvullende agent-call.
  - Governance-stop: Troubleshooting + Methodology voor incident/proceslog.
  - Hard-stop: governance-conflicten die niet oplosbaar zijn.

## Cultural-Historical Editor
- Rol: Bewaakt culturele en historische juistheid en context.
- Prompt: `prompts/cultural_historical_editor.md`
- **Autonomy & Escalation**
- local decisions allowed (within remit)
- soft-stop on contradictions/template issues
- governance-stop on high-risk cultural/structural issues
- human-gate only for high-impact / governance conflicts

## Book Structure Agent
- Rol: Ontwerpt en optimaliseert de structuur van het boek.
- Prompt: `prompts/book_structure_agent.md`
- **Autonomy & Escalation**
- local decisions allowed (within remit)
- soft-stop on contradictions/template issues
- governance-stop on high-risk cultural/structural issues
- human-gate only for high-impact / governance conflicts

## Annotation Agent
- Rol: Schrijft annotaties en contextkaders bij recepten en verhalen.
- Prompt: `prompts/annotation_agent.md`
- **Autonomy & Escalation**
- local decisions allowed (within remit)
- soft-stop on contradictions/template issues
- governance-stop on high-risk cultural/structural issues
- human-gate only for high-impact / governance conflicts

## Recipe Editor
- Rol: Controleert culinaire juistheid en praktische uitvoerbaarheid.
- Prompt: `prompts/recipe_editor.md`
- **Autonomy & Escalation**
- local decisions allowed (within remit)
- soft-stop on contradictions/template issues
- governance-stop on high-risk cultural/structural issues
- human-gate only for high-impact / governance conflicts

## Table Editor
- Rol: Harmoniseert tabellen en maakt ze consistent en leesbaar.
- Prompt: `prompts/table_editor.md`
- **Autonomy & Escalation**
- local decisions allowed (within remit)
- soft-stop on contradictions/template issues
- governance-stop on high-risk cultural/structural issues
- human-gate only for high-impact / governance conflicts

## Image Agent
- Rol: Selecteert en positioneert beelden die de inhoud ondersteunen.
- Prompt: `prompts/image_agent.md`
- **Autonomy & Escalation**
- local decisions allowed (within remit)
- soft-stop on contradictions/template issues
- governance-stop on high-risk cultural/structural issues
- human-gate only for high-impact / governance conflicts

## Cohesion Agent (historisch: Continuity Agent)
- Rol: Bewaakt consistentie in terminologie, toon en vormgeving.
- Prompt: `prompts/cohesion_agent.md`
- **Autonomy & Escalation**
- local decisions allowed (within remit)
- soft-stop on contradictions/template issues
- governance-stop on high-risk cultural/structural issues
- human-gate only for high-impact / governance conflicts

## Challenger Agent
- Rol: Daagt aannames en middelmatige keuzes uit om kwaliteit te verhogen.
- Prompt: `prompts/challenger_agent.md`
- **Autonomy & Escalation**
- local decisions allowed (within remit)
- soft-stop on contradictions/template issues
- governance-stop on high-risk cultural/structural issues
- human-gate only for high-impact / governance conflicts

## Design Agent (voorheen: Layout Agent)
- Rol: Vertaalt inhoud naar een aantrekkelijke boekvorm en vormgeving.
- Prompt: `prompts/design_agent.md`
- **Autonomy & Escalation**
- local decisions allowed (within remit)
- soft-stop on contradictions/template issues
- governance-stop on high-risk cultural/structural issues
- human-gate only for high-impact / governance conflicts

## Cohesion Agent (historisch: Continuity Agent) — continuity prompt
- Rol: Bewaakt consistente toepassing van terminologie, stijl en structuur.
- Prompt: `prompts/continuity_agent.md`
- **Autonomy & Escalation**
- local decisions allowed (within remit)
- soft-stop on contradictions/template issues
- governance-stop on high-risk cultural/structural issues
- human-gate only for high-impact / governance conflicts

## Repository Archivist / Documentation Admin
- Rol: Bewaakt docs-structuur, naming conventions en consolidatie-voorstellen.
- Prompt: `prompts/repository_archivist.md`
- Type: governance/support
- Triggers: groei in docs, nieuwe fases (Phase-3 pilots), CONSOLIDATION_AUDIT.
- Autonomy: signaleert en adviseert; beslist niet; verplaatst niets.

## Methodology & Accountability Archivist
Bewaker van verantwoording en reproduceerbaarheid.  
Legt vast wat er is besloten, waarom, en met welke impact.  
Schrijft gestructureerde logs — verandert zelf niets.
- Trigger conditions:
  - nieuwe workflow of procesvariant;
  - templates of lifecycle-structuren wijzigen;
  - belangrijke SYSTEM_* beslissingen of glossary decisions;
  - uitzonderingen op standaardproces.

Prompt: prompts/methodology_archivist.md  
Runtime integration design: see docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md.  

---

## Technical Strategy Advisor
Beoordeelt model- en architectuurkeuzes met aandacht voor kwaliteit,
kosten, stabiliteit en hardware-beperkingen.  
Geeft adviezen — voert niets door.
- Trigger conditions:
  - model change proposals (LLM/temperature/context-size);
  - cost/performance concerns;
  - local vs. cloud trade-offs;
  - veiligheid/privacy rond modellen relevant.

Prompt: prompts/technical_advisor.md  
Runtime integration design: see docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md.  

---

## Incident & Resilience (Troubleshooting) Agent
Herkenning, classificatie en rapportage van pipeline-storingen,
OCR-problemen en risico’s.  
Stelt veilige herstelopties voor — fixt zelf niets.
- Trigger conditions:
  - STOP-criteria of inconsistent gedrag;
  - tegenstrijdige outputs tussen agents;
  - herhaaldelijke template-fouten na retries;
  - conflicterende kern-documenten.

Prompt: prompts/troubleshooting_agent.md  
Runtime integration design: see docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md.  

---

- Autonomy & Escalation:
  - Soft-stop: INCIDENT_REPORT produceren en context vragen.
  - Governance-stop: herstelpad en voorwaarden voor veilig vervolg.
  - Hard-stop: veiligheid/gezondheid of onoplosbaar conflict.

## Agent Status Overview

Deze tabel geeft weer welke agents volledig operationeel zijn,
welke ontworpen zijn maar nog niet zijn geïntegreerd,
en welke nog conceptueel zijn.

| Agent | Prompt (.md) | Implementatie (code) | Status |
|------|--------------|----------------------|--------|
| Translation Quality | ✔ | ✔ | actief |
| Readability Editor | ✔ | ✔ | actief |
| Fidelity Agent | ✔ | ✔ | actief |
| Orchestrator | ✔ | ✔ | actief |
| Cultural/Historical Editor | ✔ | ✔ | actief (inhoudelijk uitbreidbaar) |
| Annotation Agent | ✔ | ✔ | actief (conceptannotaties) |
| Cohesion Agent (historisch: Continuity Agent) | ✔ | ✔ | actief |
| Design Agent (voorheen: Layout Agent) | ✔ | ✔ | actief |
| Repository Archivist / Documentation Admin | ✔ | ⚠ | ontworpen — documentair, geen moves |
| Challenger Agent | ✔ | ✔ | actief |
| Methodology Archivist | ✔ | ⚠ | ontworpen — nog niet geïntegreerd in runs |
| Technical Advisor | ✔ | ⚠ | ontworpen — geeft adviezen, beslist niets |
| Troubleshooting Agent | ✔ | ⚠ | ontworpen — diagnose, geen fixes |
| Glossary / Terminology Manager | ✔ | ✖ | ontworpen — prompt aanwezig, nog niet geïntegreerd |
| Research / Historical Knowledge Agent | ✔ | ✖ | ontworpen — nog niet geïntegreerd |
| OCR / Source Integrity Agent | ✖ | ✖ | concept |
| Batch Governor | ✖ | ✖ | concept |
| Meeting / Redaction Agent | ✖ | ✖ | concept |

Legenda:
✔ = aanwezig en gebruikt  
⚠ = ontworpen, gedeeltelijk aanwezig of nog niet geïntegreerd  
✖ = nog niet geïmplementeerd


---

## Template Agent
Ontwerpt en bewaakt output-templates voor alle workflows.  
Voorkomt format-drift, ondersteunt evolutie met versies en EXPERIMENTAL-labels.  
Schrijft **structuren**, geen inhoud.

Prompt: prompts/template_agent.md

---

## Glossary / Terminology Agent
Detecteert en structureert belangrijke termen (ingrediënten, technieken, gereedschap,
culturele begrippen) op basis van bestaande bronnen (research-rapporten, annotaties,
oude glossaries).  
Levert gestructureerde GLOSSARY_PROPOSALS met bronverwijzingen, contextvoorbeelden
en statuslabels (candidate/historical/avoid) voor menselijke beoordeling.
Volgt de Glossary Decision Lifecycle en levert geen definitieve beslissingen.
Zie docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md.

Prompt: prompts/glossary_agent.md
Runtime integration design: see docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md.

---

- Autonomy & Escalation:
  - Soft-stop: onvoldoende bronnen -> Research.
  - Governance-stop: Glossary Decision Lifecycle + Methodology-log.
  - Hard-stop: terminologie met project-brede impact.

## Research / Historical Knowledge Agent
Onderzoekt bestaande repositories en documenten (bijv. oude OCR-output,
notities, eerdere vertalingen) om relevante bronnen en kennis boven water te halen.  
Levert gestructureerde onderzoeksrapporten met relevante bestanden, inzichten
en aanbevelingen voor verdere verwerking.
Levert evidence voor de Glossary Decision Lifecycle en verwijst naar eerdere reports.

Prompt: prompts/research_agent.md
Runtime integration design: see docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md.

- Autonomy & Escalation:
  - Soft-stop: bron onbetrouwbaar -> alternatieven zoeken.
  - Governance-stop: tegenstrijdige archiefbewijzen.
  - Hard-stop: authenticiteitsconflicten die niet oplosbaar zijn.

---

## Handover Agent (Session Handover & Templates)
Genereert handover-templates en concrete handover-notes voor nieuwe ChatGPT-
en Codex CLI-sessies op basis van repo-documentatie.
Output: [HANDOVER_TEMPLATE] en [HANDOVER_NOTE].
Triggers: op expliciet verzoek van gebruiker, of wanneer Codex/Orchestrator
een nieuwe sessie structureert.
Status: Ontworpen (prompt aanwezig, nog niet geïntegreerd in Python-runtime).

Prompt: prompts/handover_agent.md
