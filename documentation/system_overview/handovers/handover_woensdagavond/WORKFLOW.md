# WORKFLOW OVERVIEW

Dit document beschrijft de huidige workflow en waar wijzigingen thuishoren.

## Pipeline (huidige 3 fasen)

1. Translation Quality
2. Readability
3. Fidelity

De pipeline wordt uitgevoerd via `mustikarasa_codex_cli.py` (subcommand `recipe`)
en gebruikt `test_multi_agent_fidelity.py` als 3-fasen engine.

## Rol van de Orchestrator

De Orchestrator is de workflow-conductor: coördineert agents, bewaakt templates
en governance, en zorgt dat outputs conform afspraken zijn. Het formele mandaat
staat in de Mandate and Boundaries-sectie van `prompts/orchestrator.md`.

## Governance-lagen en ondersteunende agents

- Template Agent: definieert output-templates en versiebeleid.
- Research Agent: levert RESEARCH_REPORTS met historische context.
- Glossary Agent: levert GLOSSARY_PROPOSALS met bronverwijzingen.
- Methodology Archivist: legt beslissingen en impact vast.
- Technical Advisor: adviseert model- en architectuurkeuzes.
- Troubleshooting Agent: rapporteert incidenten en herstelopties.

## Governance Triggers

Deze triggers zijn verplicht en leveren governance‑artefacten op:
- Methodology Archivist bij nieuwe workflows, lifecycle‑wijzigingen en SYSTEM_* beslissingen
  → [METHODOLOGY_LOG].
- Technical Advisor bij modelwijzigingen, performance/kosten‑issues of local/cloud‑trade‑offs
  → [MODEL_ADVICE].
- Troubleshooting Agent bij STOP‑criteria, inconsistent gedrag of template‑fouten
  → [INCIDENT_REPORT].

### Glossary Agent — triggers
- terminologie-inconsistentie tussen pipeline-fases
- cultureel gevoelige termen met meerdere vertaalopties
- Fidelity signaleert risico op betekenisdrift
- escalatie vanuit Orchestrator volgens Glossary Decision Lifecycle
- output is ALTIJD proposal-only
- verwijzing: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md

### Research Agent — triggers
- glossary-case vraagt om historische/culturele onderbouwing
- inconsistent archief- of bronmateriaal
- twijfel of een term “moderniseerbaar” is
- noodzaak om bestaande RESEARCH_* rapporten te hergebruiken
- output ondersteunt glossary-voorstellen — beslist niet
- verwijzing: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md

Outputs worden vastgelegd in docs/ en verwerkt in sessielogs en lifecycle‑documenten.

## Autonomy & Escalation (Stop Model)

| Agent | Soft-stop (self-healing) | Governance-stop (no human) | Human gate (hard-stop) |
|------|---------------------------|----------------------------|------------------------|
| Translation | Vraag Fidelity/Research bij onduidelijkheid | Ambiguïteit met betekenisverschuiving | Medisch/allergie/juridisch risico |
| Readability | Betekenisimpact? Check met Fidelity | Conflict met Fidelity/Glossary | Cultureel gevoelige passages met risico |
| Fidelity | Cross-check met Research | Blijvende discrepantie | Gezondheid/geschiedenis met hoog risico |
| Glossary | Onvoldoende bronnen -> Research | Lifecycle + Methodology-log | Terminologie met project-brede impact |
| Research | Bron onbetrouwbaar -> alternatieven | Tegenstrijdige archiefbewijzen | Authenticiteitsconflict onoplosbaar |
| Orchestrator | Herordening, extra context | Troubleshooting + Methodology | Governance-conflict onoplosbaar |
| Troubleshooting | INCIDENT_REPORT + context | Herstelpad + voorwaarden | Veiligheid/gezondheid of onoplosbaar conflict |

Het autonomie-model geldt nu voor alle redactionele agents, niet alleen Translation/Readability/Fidelity.
Elke agent volgt dezelfde escalatielogica: soft-stop, governance-stop, en human-gate bij hoge impact of conflict.

### Batch / Chapter Execution (Design)

- Ontwerpdocument: `docs/CHAPTER_BATCH_WORKFLOW.md` (geen runtime-implementatie).
- Gebruik batching voor test-runs en regressiecontrole over meerdere items.
- Gebruik batching voor samenhangende hoofdstukken of recept-sets met gedeelde context.
- Gebruik batching voor review-rondes met expliciete batch-samenvattingen.

### Governance Agent Runtime Integration (Design)

- Ontwerpdocument: `docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md` beschrijft hoe governance-agents
  straks in de runtime worden aangeroepen.
- Dit is ontwerp, geen implementatie; er verandert nu geen runtime-gedrag.
- Bestaande workflow blijft leidend totdat code expliciet is aangepast.

### Phase-3 (Pilots & Safety — design framing)

- pilots werken alleen met afgeleide kopieën
- governance test gecontroleerd falen
- output is EXPERIMENTAL (niet publiceerbaar)
- verwijzing: docs/PHASE3_FRAMING.md

## Governance Tests

Het testplan voor governance staat in `docs/10-governance/GOVERNANCE_TESTS_PLAN.md` en is leidend\nvoordat er daadwerkelijke testcode wordt geïmplementeerd.

## Where to change what

- Pipeline-logica: `test_multi_agent_fidelity.py` en `mustikarasa_codex_cli.py`.
- Agent-prompts: `prompts/*.md`.
- Governance- en procesdocumentatie: `docs/*.md`.

## Handover Flows

- Een handover wordt typisch gemaakt na afronding van een belangrijke fase
  (bijv. PHASE-1 Foundations) of vóór start van een nieuw projectblok (bijv. PHASE-2).
- Gebruik de Handover Agent (prompts/handover_agent.md) en baseer op:
  - docs/total_project.md (systeemoverzicht)
  - docs/CODEX_META_PROMPT.md (sessiestartgedrag)
