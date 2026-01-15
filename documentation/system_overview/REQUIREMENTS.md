# System Requirements — Mustikarasa Multi-Agent Platform

## 1. Purpose & Scope
- Dit document verzamelt expliciete eisen voor het Mustikarasa multi‑agent systeem.
- Alle eisen zijn afgeleid van bestaande projectdocumenten; er is geen nieuw ontwerp.
- Scope: pipeline, agents, governance, pilots en documentatie‑workflow.

## 2. Terminology
- MUST / MUST NOT: bindende eis; afwijking is niet toegestaan.
- SHOULD: sterke voorkeur; alleen afwijken met expliciete onderbouwing.
- MAY: optionele mogelijkheid; geen verplichting.
- Agent: uitvoerende rol met prompt en taakafbakening.
- Governance Agent: adviserend/loggend; neemt geen definitieve beslissingen.
- Human Gate: expliciete menselijke beslissing bij high‑risk of finale besluiten.
- Proposal‑only: output is voorstel; geen definitieve beslissing.

## 3. Functional Requirements
- FR-001: The system MUST support a multi‑phase recipe pipeline
  (Translation → Readability → Fidelity). Source: docs/WORKFLOW.md, docs/total_project.md.
- FR-002: The system MUST load agent prompts from `prompts/*.md` (no inline prompts in code).
  Source: docs/total_project.md, docs/CODEX_META_PROMPT.md.
- FR-003: The Glossary Agent MUST produce proposal‑only term suggestions and MUST NOT
  make final decisions. Source: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md, prompts/glossary_agent.md.
- FR-004: The Research Agent MUST provide context/evidence via [RESEARCH_REPORT] and MUST NOT
  make final editorial decisions. Source: prompts/research_agent.md, docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md.
- FR-005: The Orchestrator MUST enforce template‑aware behaviour via Template Agent
  and treat template definitions as contracts. Source: prompts/orchestrator.md, prompts/template_agent.md.
- FR-006: Governance agents MUST be invokable via runtime events as designed
  (events, inputs, outputs, logging). Source: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md.
- FR-007: Batch/chapter processing MUST follow the documented batch design
  (input definition, per‑item processing, batch summary, artifacts). Source: docs/CHAPTER_BATCH_WORKFLOW.md.

## 4. Non-Functional Requirements
- NFR-001: The system MUST be traceable; significant actions MUST be logged
  in docs/CODEX_SESSION_LOG.md. Source: docs/CODEX_META_PROMPT.md, docs/WORKFLOW.md.
- NFR-002: The system MUST be reproducible; decisions MUST be reconstructable
  from prompts, docs and logs. Source: docs/CODEX_META_PROMPT.md, docs/total_project.md.
- NFR-003: The system MUST NOT rely on unlogged, ad‑hoc prompts or hidden rules.
  Source: docs/CODEX_META_PROMPT.md, docs/total_project.md.
- NFR-004: The system SHOULD treat model choice as advisory input from Technical Advisor,
  not as an automatic decision. Source: docs/AGENTS.md, prompts/technical_advisor.md.

## 5. Governance Requirements
- GR-001: Agents MUST treat their outputs as signals, not final decisions,
  and MUST follow the stop‑model (soft‑stop → governance‑stop → human‑gate).
  Source: docs/WORKFLOW.md, docs/AGENTS.md.
- GR-002: Glossary decisions MUST follow the Glossary Decision Lifecycle and pass
  through Human Gate before finalization. Source: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md.
- GR-003: Governance‑stop MUST precede Human Gate in high‑risk situations.
  Source: docs/WORKFLOW.md.
- GR-004: Governance Agents MUST NOT unilaterally change code, config or publications.
  Source: docs/AGENTS.md, prompts/technical_advisor.md, prompts/troubleshooting_agent.md,
  prompts/methodology_archivist.md.

## 6. Automation & Safety Requirements
- ASR-001: The system MUST NOT automatically publish content without human review.
  Source: docs/CHAPTER_BATCH_WORKFLOW.md.
- ASR-002: The system MUST NOT automatically apply glossary changes without Human Gate approval.
  Source: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md, docs/GLOSSARY_PILOT_REPORT.md.
- ASR-003: Pilot/test outputs MUST be labeled as such and MUST NOT overwrite production artifacts.
  Source: docs/GLOSSARY_PILOT_REPORT.md, docs/10-governance/GOVERNANCE_TESTS_PLAN.md.
- ASR-004: In case of logging failure, outputs MUST be treated as non‑final and MUST trigger
  an incident path. Source: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md.
- ASR-005: The system MUST NOT automatically apply glossary changes to the
  authoritative glossary or downstream content without BOTH Human Gate
  approval AND a documented rollback plan.
  (Sources: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md, docs/WORKFLOW.md, docs/REQUIREMENTS_CHANGE_PROCESS.md)
- ASR-006: When an incident is raised by any agent or subsystem,
  the pipeline MUST enter governance-stop and MUST NOT continue
  towards publication or batch completion until explicitly released
  through the Human Gate.
  (Sources: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md, docs/WORKFLOW.md, docs/REQUIREMENTS_CHANGE_PROCESS.md)
- ASR-007: The system MUST support batch rollback in such a way that
  already-approved or unaffected items are preserved, and rollback
  operations are fully logged and reversible.
  (Sources: docs/CHAPTER_BATCH_WORKFLOW.md, docs/WORKFLOW.md, docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md, docs/REQUIREMENTS_CHANGE_PROCESS.md)

## 7. Pilot & Phase-Transition Requirements
- PTR-001: Before enabling new runtime behaviour, there MUST be a design document
  and at least one governance test scenario. Source: docs/10-governance/GOVERNANCE_TESTS_PLAN.md,
  docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md, docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md,
  docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md.
- PTR-002: Pilots MUST run with enhanced logging and MUST remain reversible.
  Source: docs/GLOSSARY_PILOT_REPORT.md, docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md.
- PTR-003: Changes affecting cultural/historical interpretation MUST go through
  Glossary + Research + Human Gate before being considered stable.
  Source: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md, docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md.

## 8. Traceability to Source Docs
- FR-001 → docs/WORKFLOW.md, docs/total_project.md
- FR-003, GR-002, ASR-002 → docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md
- GR-003, ASR-004 → docs/WORKFLOW.md, docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md
- NFR-001, NFR-002 → docs/CODEX_META_PROMPT.md, docs/CODEX_SESSION_LOG.md
- PTR-001 → docs/10-governance/GOVERNANCE_TESTS_PLAN.md, docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md,
  docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md

## 9. Open Questions & Gaps
- Is er een maximale batch‑grootte voor pilots en tests?
- Welke performance‑ en cost‑eisen gelden in praktijk (lokale hardware)?
- Wanneer wordt een pilot formeel “gepromoveerd” tot standaardgedrag?

## 10. Change & Versioning
- Requirements‑wijzigingen MUST worden gelogd in docs/CODEX_SESSION_LOG.md.
- Requirements‑wijzigingen SHOULD gekoppeld worden aan een expliciet SYSTEM_* of toekomstig
  PHASE3_* item in docs/CODEX_TODO.md.
- Elke wijziging MUST herleidbaar zijn naar een menselijke beslissing (Human Gate of redactie).
