# Capability → Agent Mapping

Status: baseline  
Scope: documentary — no behavioural authority  
Changes allowed: via normal governance only

## 1. Purpose

Dit document maakt zichtbaar welke agents welke capabilities dragen,
waar overlap zit, en waar gaten in het systeem bestaan.
Het is een documentair inzicht, geen ontwerpdocument.

## 2. Scope (belangrijk)

- Alleen bestaande capabilities
- Alleen bestaande agents
- GEEN ontwerp van nieuwe agents
- GEEN gedragswijzigingen

## 3. Capability Categories

- Editorial Capabilities (docs/EDITORIAL_CAPABILITIES.md)
- Governance capabilities
- Workflow/Operational capabilities
- Research/Knowledge capabilities
- Repository/Archival capabilities

## 4. Mapping Table (kernstuk)

| Capability | Primary Agent | Supporting Agents | Notes (risk, overlap, gaps) |
|-----------|---------------|-------------------|-----------------------------|
| Meaning Preservation & Semantic Control | Translation Quality Agent | Fidelity Agent, Readability Editor, Challenger Agent | Primair gericht op betekenis/nuance; overlap met Fidelity. |
| Terminology Stewardship | Glossary / Terminology Agent | Cohesion Agent, Research / Historical Knowledge Agent | Agent is ontworpen maar niet geïntegreerd; runtime-gap. |
| Cultural-Historical Interpretation | Cultural-Historical Editor | Research / Historical Knowledge Agent, Annotation Agent | Culturele context wordt inhoudelijk gedragen door Cultural-Historical Editor. |
| Error Recognition & Scholarly Commentary | Fidelity Agent | Annotation Agent, Research / Historical Knowledge Agent | Annotatie nodig voor uitleg; risico op overlap met Annotation Agent. |
| Safety-Aware Editorial Judgement | **GAP** | Annotation Agent, Cultural-Historical Editor | Geen expliciete safety-editing agent; risico op onderdekking. |
| Culinary Validation | Recipe Editor | Annotation Agent, Challenger Agent | Culinaire beoordeling primair bij Recipe Editor. |
| Balanced Readability Craft | Readability Editor | Translation Quality Agent, Fidelity Agent | Overlap tussen leesbaarheid en betekenisbewaking. |
| Interpretation Guidance | **GAP** | Annotation Agent, Cultural-Historical Editor | Geen expliciete agent voor editoriale inleidingen/duiding. |
| Contextual Annotation | Annotation Agent | Cultural-Historical Editor, Research / Historical Knowledge Agent | Context en bronnen dragen annotaties. |
| Document Integrity Awareness | **GAP** | Repository Archivist / Documentation Admin | Integriteit van erfgoed is geen expliciete agent-taak. |
| Governance orchestration & escalation | Orchestrator | Methodology & Accountability Archivist, Incident & Resilience Agent | Orchestrator bewaakt flow; governance agents signaleren. |
| Methodology logging & accountability | Methodology & Accountability Archivist | Orchestrator | Documenteert besluiten; geen beslissingen. |
| Incident recognition & resilience reporting | Incident & Resilience (Troubleshooting) Agent | Orchestrator | Diagnose en rapportage, geen fixes. |
| Technical strategy review | Technical Strategy Advisor | Orchestrator | Adviesrol; geen beslissingen. |
| Template governance & format compliance | Template Agent | Orchestrator | Template-structuren bewaken, geen inhoud. |
| Workflow orchestration & handoff | Orchestrator | Challenger Agent, Cohesion Agent | Workflow-coördinatie en samenhang. |
| Handover facilitation (session context) | Handover Agent | Orchestrator | Agent is ontworpen; nog niet geïntegreerd. |
| Research & evidence gathering | Research / Historical Knowledge Agent | Cultural-Historical Editor | Agent ontworpen; levert evidence voor redactie. |
| Glossary proposal generation | Glossary / Terminology Agent | Research / Historical Knowledge Agent | Proposals only; geen canonieke besluiten. |
| Repository structure & documentation hygiene | Repository Archivist / Documentation Admin | Methodology & Accountability Archivist | Documentair advies; geen moves. |

## 5. Overlap Analysis

- Translation Quality, Fidelity en Readability raken alle drie betekenis vs leesbaarheid; afbakening kan diffuus worden.
- Annotation en Cultural-Historical Editor overlappen bij contextuele toelichting.
- Cohesion/Continuity raakt terminologie en stijl en kan overlappen met Glossary en Readability.

## 6. Capability Gaps (BELANGRIJK)

- Safety-Aware Editorial Judgement — **GAP** (geen expliciete agent toegewezen)
- Interpretation Guidance — **GAP** (geen expliciete agent voor editoriale duiding)
- Document Integrity Awareness — **GAP** (geen expliciete agent met dit mandaat)

## 7. Impact on Phase-3

- Wel veilig te testen: documentaire pilots met bestaande agents voor annotatie,
  glossary-proposals en onderzoek (geen canonieke beslissingen).
- Uitstellen: capabilities met GAP tot er expliciete redactionele dekking is;
  geen impliciete overdracht naar bestaande agents zonder besluit.

## 8. Appendix

Verwijzingen:
- docs/AGENTS.md
- docs/EDITORIAL_CAPABILITIES.md
- docs/10-governance/
- docs/PHASE3_FRAMING.md

## Open Questions

- Wie draagt in de praktijk Safety-Aware Editorial Judgement zonder expliciete agent?
- Wie is eindverantwoordelijk voor Interpretation Guidance (editoriale duiding)?
- Wie bewaakt Document Integrity Awareness als redactionele taak?
