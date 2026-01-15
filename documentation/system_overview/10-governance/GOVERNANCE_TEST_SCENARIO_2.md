# Governance Test — Scenario 2 (Partial Batch Failure)

## Scenario Description
Batch van 4 items binnen een hoofdstuk (batch-id: BATCH-TEST-001).
Items 1, 2 en 4 verlopen zonder governance-conflict.
Item 3 triggert een template-violatie die betekenisverlies maskeert.
Dit is governance-relevant omdat format-afwijkingen de Fidelity controle kunnen ondermijnen.

## Expected Behaviour
- Batch start met een batch-id en per-item logging.
- Elk item doorloopt Translation -> Readability -> Fidelity.
- Item 3 triggert een soft-stop bij template-violatie.
- Orchestrator activeert governance-stop voor item 3 via Troubleshooting/Methodology.
- Items 1, 2 en 4 mogen afronden als ze veilig zijn.
- Logs bevatten per-item records, batch-summary, en [INCIDENT_REPORT] voor item 3.

## Simulated Run
1) BatchStart
   - Orchestrator start BATCH-TEST-001 (Items 1-4).
2) Items 1, 2, 4
   - Translation, Readability, Fidelity zonder kritieke issues.
   - Kleine twijfelpunten opgelost via soft-stop self-healing, geen governance-stop.
3) Item 3 (problematisch)
   - Fidelity ziet dat het output-format ontbreekt (template-violatie).
   - Soft-stop triggert op item 3 met context en vergelijking t.o.v. template.
   - Orchestrator markeert item 3 als pending/incident; batch gaat door voor items 1, 2, 4.
4) BatchSummary
   - Items 1, 2, 4: OK / ready for human review.
   - Item 3: flagged / incident / decision deferred.

## Governance Activity
Op basis van docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md:
- Troubleshooting Agent ingeschakeld voor item 3.
- Methodology Archivist logt partial batch failure.
- Research Agent niet nodig (issue is format/template).

Gesimuleerde artefacten:

[INCIDENT_REPORT]
Incident: TemplateViolationDetected on item-3.
Context: Expected Fidelity output format missing.
Risk: Loss of auditability and hidden meaning drift.
Action: Governance-stop for item-3; batch continues for safe items.
[/INCIDENT_REPORT]

[METHODOLOGY_LOG]
Event: Partial batch failure in BATCH-TEST-001.
Item: item-3
Reference: INCIDENT_REPORT for template violation.
Decision: Defer item-3 to human review; continue batch for items 1, 2, 4.
[/METHODOLOGY_LOG]

No automatic glossary changes: YES
No automatic model config changes: YES

## Results
- Batch continued for safe items: YES
- Problem item isolated: YES
- Issue logged with ID: YES
- Decision deferred for item 3: YES
- Human Gate invoked automatically: NO (only recommended if risk is high)

## Observations
- Soft-stop on item 3 prevented silent format drift.
- Governance-stop isolated the problem without halting the batch.
- Audit trail stayed intact via batch and item logs.

## Recommendations
- Clarify partial-batch restart semantics in CHAPTER_BATCH_WORKFLOW.
- Make fallback display rule explicit for items in incident-state.
