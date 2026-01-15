# Consolidation Audit — 01

## Scope
Audit uitgevoerd op governance- en workflowdocumentatie in `docs/` en alle agent-prompts
in `prompts/`, met nadruk op samenhang tussen rolbeschrijvingen, triggers, lifecycle,
batch-designs en test-scenario’s.

## Observations (facts only)
- `docs/total_project.md` noemt in de “Docs-map (actuele lijst)” niet: `docs/WORKFLOW.md`,
  `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`, `docs/10-governance/GOVERNANCE_TESTS_PLAN.md`,
  `docs/CHAPTER_BATCH_WORKFLOW.md`, `docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md`,
  `docs/GLOSSARY_PILOT_REPORT.md`, `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`,
  `docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md`.
- `docs/total_project.md` noemt in de “Prompts-map (actuele lijst)” niet `prompts/handover_agent.md`,
  terwijl `prompts/handover_agent.md` bestaat en wordt genoemd in `docs/AGENTS.md` en `docs/WORKFLOW.md`.
- `docs/total_project.md` sectie 8.2 noemt TODO-items die in `docs/CODEX_TODO.md` inmiddels
  anders zijn gemarkeerd (bijv. workflow-documentatie staat daar op [x]).
- `docs/CODEX_TODO.md` bevat de heading “PHASE-2 Roadmap (governed backlog — not started yet)”
  terwijl alle PHASE2-items eronder op [x] staan.
- `docs/CODEX_TODO.md` vermeldt bij **PHASE2_GOVERNANCE_TEST_SCENARIO_1** als output
  `docs/GOVERNANCE_TEST_RUN_01.md`, terwijl het aanwezige document
  `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md` heet.
- In `docs/AGENTS.md` staat in de status-tabel “Continuity/Cohesion Agent” als gecombineerd item,
  terwijl er afzonderlijke secties en prompts bestaan: `prompts/continuity_agent.md`
  en `prompts/cohesion_agent.md`.
- In `docs/AGENTS.md` staat in de status-tabel “Design/Layout Advisor”, terwijl de agentsectie
  en prompt de naam “Design Agent” gebruiken (`prompts/design_agent.md`).
- `docs/WORKFLOW.md` noemt in “Governance Triggers” alleen Methodology/Technical/Troubleshooting,
  terwijl Glossary/Research triggers elders wel expliciet staan (stop-model tabel in
  `docs/WORKFLOW.md` en de lifecycle in `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`).
- Autonomy-secties in prompts zijn niet uniform van stijl: Translation/Readability/Fidelity
  gebruiken een andere (Nederlandse) structuur dan de redactionele prompts
  met een Engelstalige “You MAY”/“You MUST” structuur.
- `docs/CODEX_META_PROMPT.backup.1767359806` wordt genoemd in `docs/total_project.md`,
  maar wordt in de overige gelezen docs/prompts niet verder gerefereerd.

## Risk Assessment (risk-thinking, nog steeds feitelijk)
- Drift-risico: `docs/total_project.md` presenteert “actuele lijsten” die niet overeenkomen
  met de huidige set governance- en workflowdocumenten.
- Naming-risico: afwijkende benamingen in `docs/AGENTS.md` (Design/Layout vs Design Agent,
  Continuity/Cohesion gecombineerd) kunnen tot verwarring leiden bij integratie of statuscontroles.
- Artefact-risico: `docs/CODEX_TODO.md` verwijst naar `docs/GOVERNANCE_TEST_RUN_01.md`,
  terwijl de scenario-documentatie een andere bestandsnaam gebruikt.
- Governance-trigger-risico: triggers voor Glossary/Research staan in sommige documenten
  wel en in andere niet, wat verwachtingen over automatische inschakeling kan uiteen laten lopen.
- Consistentie-risico: variaties in autonomie/stop-model presentatie in prompts kunnen
  bij lezers het beeld geven dat de stop-logica per agent anders is.

## Dead / Orphaned Items
- `docs/CODEX_META_PROMPT.backup.1767359806` wordt alleen genoemd in `docs/total_project.md`
  en niet in de overige gelezen governance-/workflowdocumenten of prompts.
- `docs/GOVERNANCE_TEST_RUN_01.md` wordt genoemd in `docs/CODEX_TODO.md` maar is niet aanwezig
  in de lijst van documenten in `docs/` (wel bestaat `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`).

## Consistency Check — Governance Patterns
- Glossary lifecycle: consistent tussen `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`,
  `prompts/glossary_agent.md` en `docs/GLOSSARY_PILOT_REPORT.md`; in
  `docs/WORKFLOW.md` wordt de Glossary lifecycle niet genoemd in de triggerlijst.
- Soft-stop / governance-stop / human-gate: aanwezig in `docs/WORKFLOW.md` en in alle
  relevante prompts; format/taal verschilt tussen kern-agents en redactionele agents.
- Session logging: vereiste logging staat in `docs/CODEX_META_PROMPT.md` en
  `prompts/orchestrator.md`; `docs/CODEX_SESSION_LOG.md` bevat entries voor recente PHASE2-items.
- Proposal-only vs final decisions: consistent in `prompts/glossary_agent.md`,
  `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md` en `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`.
- Research before automation: Research Agent wordt in prompts en in
  `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md` expliciet vereist; in `docs/WORKFLOW.md`
  staat Research niet in de governance-triggerlijst maar wel in de stop-model tabel.

## Open Questions (for humans)
- Is `docs/total_project.md` bedoeld als “actueel overzicht”, en zo ja, wanneer wordt
  die lijst met documenten en prompts bijgewerkt?
- Moet het PHASE-2 header-label “not started yet” in `docs/CODEX_TODO.md` blijven staan
  nu alle PHASE2-items op [x] staan?
- Is `docs/GOVERNANCE_TEST_RUN_01.md` een verwachte output die nog moet bestaan,
  of moet de verwijzing wijzen naar `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`?
- Is de naam “Design/Layout Advisor” in de status-tabel bewust afwijkend van “Design Agent”?
- Is het combineren van Continuity/Cohesion in de status-tabel een bewuste keuze
  ondanks aparte prompts en secties?
- Moeten Glossary/Research triggers ook expliciet in de “Governance Triggers”-lijst
  van `docs/WORKFLOW.md` staan voor volledigheid?

## Recommendation Type (NO CHANGES)
→ Needs consolidation pass (document-only)

- P3_LOBAK_002 — CONSOLIDATED  
  Scope: terminology divergence test.  
  Outcome: governance handled ambiguity; insight recorded; reversible.

- P3_OCR_RESTORE_001 — CONSOLIDATED  
  Scope: OCR technical vs. content discipline.  
  Outcome: mechanical fixes only; orthography preserved; ²-marker insight logged.
- P3_MARKER2_ANALYSIS_001 — CONSOLIDATED  
  Scope: OCR marker behavior (“²”).  
  Outcome: patterns documented; ambiguity preserved; proposals deferred.
- P3_MARKER2_FLAGGING_001 — CONSOLIDATED  
  Scope: ambiguity detection for OCR “²-derived” artifacts.  
  Outcome: detection proven; edits deferred; governance handoff identified as next capability.
- P3_MARKER2_REVIEW_HANDOFF_001 — CONSOLIDATED  
  Scope: human review workflow for ambiguity flags.  
  Outcome: decision logging worked; edits remained deferred; governance triggers clarified.
- P3_MARKER2_ESCALATION_001 — CONSOLIDATED  
  Scope: reviewer disagreement and governance escalation.  
  Outcome: escalation and Human Gate behavior documented; no edits applied.
- P3_SANTAN_002 — CONSOLIDATED  
  Scope: terminology conflict run for “santan”.  
  Outcome: ambiguity preserved; glossary decisions deferred; lifecycle documented.
- P3_ANNOTATION_001 — CONSOLIDATED  
  Scope: annotation vs translation retention pilot.  
  Outcome: documented retention patterns; decisions deferred; lifecycle emphasized.
- P3_ANNOTATION_READABILITY_001 — CONSOLIDATED  
  Scope: readability-pressure pilot.  
  Outcome: observed degradation thresholds without creating rules.
- P3_DAGING_002 — CONSOLIDATED  
  Scope: cultural-terminology conflict run.  
  Outcome: disagreement captured; decisions deferred; lifecycle respected.
- P3_WORKFLOW_001 — CONSOLIDATED  
  Scope: workflow synthesis (documentary).  
  Outcome: ambiguity lifecycle documented; no policy created.
- P3_WORKFLOWMAP_001 — CONSOLIDATED  
  Scope: workflow diagram (documentary).  
  Outcome: ambiguity flow clarified; no operational change.
- P3_FAILURE_001 — CONSOLIDATED  
  Scope: governance failure-drill (documentary).  
  Outcome: rollback and incident-handling process clarified.
- P3_UBI_002 — CONSOLIDATED  
  Scope: terminology conflict (ubi/ketela).  
  Outcome: ambiguity documented; glossary unchanged.
- P3_LIFECYCLE_001 — CONSOLIDATED  
  Scope: lifecycle rehearsal (ubi/ketela).  
  Outcome: lifecycle understood; glossary unchanged.
- P3_OCR_AUTOMATION_001 — CONSOLIDATED  
  Scope: automation boundary.  
  Outcome: boundaries documented; no automation enabled.
- P3_OCR_FLAGSCANNER_001 — CONSOLIDATED  
  Scope: automation proposal.  
  Outcome: proposal documented; implementation explicitly deferred.
- P3_READER_001 — CONSOLIDATED  
  Scope: reader-impact observation.  
  Outcome: effects documented; no policy issued.
