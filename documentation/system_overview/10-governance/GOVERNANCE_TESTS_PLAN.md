# Governance Test Plan

## Purpose
Dit testplan borgt dat governance-mechanismen correct werken.
Scope is proceslogica en beleidsafspraken, niet taalkwaliteit.

## Principles
- reproduceerbaar
- geen inline-workarounds
- fail-fast bij policybreuk
- audit-trail verplicht

## Test Categories

### 1) Template Compliance Tests
Doel: bewijzen dat outputs het juiste format volgen.
Scenario’s:
- agent produceert fout format -> Orchestrator retry
- blijvende fout -> Troubleshooting + INCIDENT_REPORT
Expected artifacts:
- log entries
- incident rapport
- geen stilzwijgende acceptatie

### 2) Lifecycle Enforcement (Glossary)
Scenario’s:
- Glossary doet een voorstel met onzekerheid
- Orchestrator probeert het per ongeluk als definitief te gebruiken
Expected:
- STOP -> lifecycle verwijzing
- human gate vereist
- Methodology log

### 3) Governance Trigger Tests
Scenario’s:
- nieuwe workflow -> Methodology wordt aangeroepen
- modelkeuze voorstel -> Technical Advisor wordt geraadpleegd
- pipeline-fout -> Troubleshooting maakt INCIDENT_REPORT

### 4) Soft-Stop / Self-Healing
Scenario’s:
- ambigu zin -> Translation vraagt Research/Fidelity
- vraag wordt opgelost zonder mens
Expected:
- LOG entry
- geen onnodige escalatie

### 5) Hard-Stop (Human-Gate)
Scenario’s:
- medische/allergische claims
- cultureel beladen passage met betekenisrisico
Expected:
- escalatiepad gevolgd
- human decision wordt vastgelegd

## Test Data & Mocks
Leg vast hoe we later synthetische cases gaan maken
(maar implementeer nog niets in code).

## Execution Model
- tests draaien per CLI workflow
- resultaten worden als documenten opgeslagen
- PASS/FAIL criteria zijn tekstueel vastgelegd

## Maintenance
Hoe het testplan wordt geüpdatet wanneer governance verandert.
