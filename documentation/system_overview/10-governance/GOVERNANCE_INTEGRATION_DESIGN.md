# Governance Agent Runtime Integration Design

## Purpose
Legt vast hoe governance-agents (Methodology, Technical, Troubleshooting, Glossary, Research)
in de toekomst in de runtime kunnen worden geïntegreerd:
- wanneer ze worden aangeroepen (events),
- welke inputs ze krijgen,
- welke outputs/artefacten ze produceren,
- hoe logging en audit-trails werken.

Geen code; alleen ontwerp en afspraken.

## Scope
- Geldt voor de bestaande multi-agent pipeline
  (Translation -> Readability -> Fidelity + redactionele agents).
- Richt zich op call-points in de Python-runtime,
  NIET op implementatiedetails.
- Batch/Chapter workflow wordt meegenomen als context voor events.

## Runtime Events & Triggers

- PipelineStart (per item / per batch)
  - Start van een item of batch; initieert context en logging.
  - Mogelijke governance-agents: Methodology, Research.
- PhaseCompleted (Translation/Readability/Fidelity)
  - Fase afgerond; controle op format en risk flags.
  - Mogelijke governance-agents: Troubleshooting, Methodology.
- TemplateViolationDetected
  - Output wijkt af van afgesproken template.
  - Mogelijke governance-agents: Troubleshooting, Methodology.
- HighRiskContentDetected (gezondheid/veiligheid/culturele gevoeligheid)
  - Risico op onjuiste of gevoelige inhoud.
  - Mogelijke governance-agents: Troubleshooting, Research.
- GlossaryConflictDetected
  - Terminologie-conflict met bestaande keuzes of lifecycle.
  - Mogelijke governance-agents: Glossary, Methodology, Research.
- ModelChangeProposal
  - Voorstel voor wijziging in LLM/config.
  - Mogelijke governance-agents: Technical, Methodology.
- WorkflowChangeProposal
  - Voorstel om proces te wijzigen.
  - Mogelijke governance-agents: Methodology, Troubleshooting.
- BatchFailure / PartialBatchFailure
  - Een batch faalt of is incompleet.
  - Mogelijke governance-agents: Troubleshooting, Methodology.

## Agent Integration Points

### Methodology & Accountability Archivist
- Typical Call Points:
  - bij grote workflow-wijzigingen,
  - bij afronden van SYSTEM_* of PHASE2_* items,
  - bij uitzonderingen op standaardproces.
- Expected Inputs (runtime):
  - context over de actie (ID, type),
  - betrokken documenten/artefacten,
  - eventuele error/incident metadata.
- Outputs:
  - [METHODOLOGY_LOG] entries gekoppeld aan ID's.
- Logging:
  - verwijzing naar docs/CODEX_SESSION_LOG.md,
  - hergebruik van ID's voor traceerbaarheid.

### Technical Strategy Advisor
- Typical Call Points:
  - voordat een modelconfig wordt aangepast,
  - bij performance/cost alerts,
  - bij twijfel over lokaal vs cloud.
- Inputs:
  - huidige modelconfig, metrics, constraints.
- Outputs:
  - [MODEL_ADVICE] met aanbevelingen en trade-offs.
- Constraint:
  - advies is NIET automatisch bindend.

### Incident & Resilience (Troubleshooting) Agent
- Typical Call Points:
  - templatefouten na meerdere retries,
  - inconsistent gedrag tussen agents,
  - batch-failures.
- Inputs:
  - foutcontext (event, betrokken agenten, logs).
- Outputs:
  - [INCIDENT_REPORT]
- Behaviour:
  - beslist of workflow veilig kan doorgaan of human gate nodig is.

### Glossary / Terminology Agent
- Typical Call Points:
  - GlossaryDecisionLifecycle events,
  - detectie van terminologieconflict.
- Inputs:
  - termen, context, relevante RESEARCH_* data.
- Outputs:
  - [GLOSSARY_PROPOSALS]
- Constraint:
  - blijft proposal-only; beslissingen via Human Gate.

### Research / Historical Knowledge Agent
- Typical Call Points:
  - behoefte aan extra context / bronnen,
  - conflicts in historical/cultural interpretation.
- Inputs:
  - onderzoeksvraag, verwijzing naar bestaande RESEARCH_* documenten.
- Outputs:
  - [RESEARCH_REPORT]
- Constraint:
  - verleent context, geen eindbeslissingen.

## Data & Logging Model
- events krijgen een ID dat consistent is met batch- en item-ID's.
- governance-calls worden gelogd met event-ID, agentnaam en artefacttype.
- outputs worden gekoppeld aan sessies en runs via docs/CODEX_SESSION_LOG.md.
- traceerbaarheid verloopt via sessielog, batch/hoofdstuk-ID's en runtime-logs
  zodra die worden geïmplementeerd.

## Failure Modes & Safeguards
- Failure modes:
  - governance-agent niet aangeroepen wanneer dat wel had gemoeten.
  - governance-agent levert geen geldig artefact terug.
  - logging faalt (ontbrekende ID's / incomplete logs).
  - batch-partial failure wordt niet goed geisoleerd.
- Safeguards:
  - soft-stop verplicht bij inconsistente of ontbrekende governance-output.
  - Orchestrator mag batch NIET stilzwijgend laten doorgaan wanneer een governance-stap faalt;
    log en markeer incident-status.
  - bij logging-falen:
    - pipeline mag geen "definitieve" status aan outputs geven.
    - incident naar Methodology Archivist sturen.
  - alle beslissingen blijven reversibel zolang governance-artefacten incompleet zijn.
- Referenties:
  - stop-model: docs/WORKFLOW.md
  - testplan: docs/10-governance/GOVERNANCE_TESTS_PLAN.md
  - voorbeelden: docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md en docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md

## Non-Goals
- geen automatische deployment of ops tooling,
- geen automatische live-rollback van code,
- geen bypass van bestaande Human Gates.

## Relationship to Other Docs
- docs/WORKFLOW.md
- docs/CHAPTER_BATCH_WORKFLOW.md
- docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md
- docs/10-governance/GOVERNANCE_TESTS_PLAN.md
- docs/CODEX_META_PROMPT.md
