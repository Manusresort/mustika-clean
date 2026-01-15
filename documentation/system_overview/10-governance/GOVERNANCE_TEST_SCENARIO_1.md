# Governance Test — Scenario 1

## Scenario Description
Een cultureel gevoelige term ("arem arem") wordt inconsistent vertaald tussen
Translation en Readability, waardoor Fidelity een betekenisafwijking signaleert.
Dit is governance-gevoelig omdat terminologie-consistentie en culturele context
onder de Glossary Decision Lifecycle vallen.

## Expected Behaviour
- Soft-stop bij detectie van inconsistentie in terminologie.
- Governance-stop bij mogelijke culturele betekenisverschuiving.
- Orchestrator schakelt governance-agents in volgens het ontwerpdocument.
- Geen automatische beslissing; de term blijft proposal-only.

## Simulated Run
1) Translation
   - Output bevat "arem-arem" als behouden term met korte gloss.
2) Readability
   - Vervangt "arem-arem" door "rijstrol" zonder gloss voor leesbaarheid.
3) Fidelity
   - Signaleert betekenisafwijking en verlies van cultureel specifieke term.
4) Probleem ontstaat
   - Terminologie-inconsistentie en risico op cultural drift.

Soft-stop:
- Trigger: Fidelity detecteert inconsistente termbehandeling.
- Vastgelegd: term, context, verschillen tussen fasen, voorgestelde vervolgstap.
- Orchestrator: pauzeert item en vraagt governance-agents.

## Governance Activity
Op basis van docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md:
- Glossary Agent -> [GLOSSARY_PROPOSALS]
- Research Agent -> [RESEARCH_REPORT]
- Troubleshooting Agent -> [INCIDENT_REPORT]
- Methodology Archivist -> [METHODOLOGY_LOG]

Voorbeeldfragmenten (gesimuleerd):

[INCIDENT_REPORT]
Incident: Terminology inconsistency detected for "arem arem".
Context: Translation retained term; Readability replaced with generic gloss.
Risk: Cultural meaning loss.
Action: Governance-stop triggered; awaiting Glossary/Research inputs.
[/INCIDENT_REPORT]

[GLOSSARY_PROPOSALS]
Terms:
  - term: arem arem
    proposed_equivalents: ["arem-arem (stuffed rice roll)", "retain original + gloss"]
    notes: Preserve cultural specificity; avoid generic replacement.
Meta:
  source: simulated pipeline event
  lifecycle_stage: proposal
[/GLOSSARY_PROPOSALS]

[RESEARCH_REPORT]
Scope: "arem arem" terminology consistency.
Summary: Term is culturally specific; replacement with generic gloss risks meaning drift.
RelevantFiles: docs/GLOSSARY_PILOT_REPORT.md
KeyInsights: Prior pilot treated term as proposal-only with gloss suggestions.
OpenQuestions: Standardize spelling? retain original term?
Recommendations: Human Gate needed before final glossary decision.
[/RESEARCH_REPORT]

[METHODOLOGY_LOG]
Event: Governance-stop for terminology inconsistency (arem arem).
Rationale: Cultural specificity and glossary lifecycle requirements.
Next: Human Gate review required before final decision.
[/METHODOLOGY_LOG]

## Results
- soft-stop: JA
- governance-stop: JA
- human-gate automatisch: NEE
- issue gelogd: JA
- beslissing uitgesteld: JA

## Observations
- Soft-stop werkte als vroege waarschuwing.
- Governance-stop voorkwam onbedoelde terminologie-beslissingen.
- Artefacten gaven voldoende context zonder inhoudelijke eindbesluitvorming.

## Recommendations
- Behoud in Readability een expliciete check op glossary-sensitive termen.
- Koppel Fidelity-signalen direct aan Glossary proposals (proposal-only).
