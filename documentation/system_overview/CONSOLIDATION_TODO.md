# Consolidation TODO — Derived from Audit 01

## Scope
Deze lijst is uitsluitend afgeleid van `docs/CONSOLIDATION_AUDIT_01.md`.
Geen nieuwe analyses of interpretaties toegevoegd.

## Tasks
- ID: CONSOL_TOTAL_PROJECT_DOCS_LIST
  Source: "`docs/total_project.md` noemt in de “Docs-map (actuele lijst)” niet: `docs/WORKFLOW.md`, `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`, `docs/10-governance/GOVERNANCE_TESTS_PLAN.md`, `docs/CHAPTER_BATCH_WORKFLOW.md`, `docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md`, `docs/GLOSSARY_PILOT_REPORT.md`, `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`, `docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md`."
  Description: docs/total_project.md bevat een onvolledige lijst van actuele docs.
  ExpectedFixType: doc-edit
  RiskIfIgnored: drift tussen “actuele lijst” en feitelijke repo-documentatie.
  Notes: clarified and applied in docs/total_project.md (docs list updated).
  Status: done

- ID: CONSOL_TOTAL_PROJECT_PROMPTS_LIST
  Source: "`docs/total_project.md` noemt in de “Prompts-map (actuele lijst)” niet `prompts/handover_agent.md`, terwijl `prompts/handover_agent.md` bestaat en wordt genoemd in `docs/AGENTS.md` en `docs/WORKFLOW.md`."
  Description: docs/total_project.md bevat een onvolledige lijst van prompts.
  ExpectedFixType: doc-edit
  RiskIfIgnored: onvolledig overzicht van beschikbare prompts.
  Notes: handover_agent opgenomen in prompts-lijst in docs/total_project.md.
  Status: done

- ID: CONSOL_TOTAL_PROJECT_TODO_STATUS
  Source: "`docs/total_project.md` sectie 8.2 noemt TODO-items die in `docs/CODEX_TODO.md` inmiddels anders zijn gemarkeerd (bijv. workflow-documentatie staat daar op [x])."
  Description: docs/total_project.md en docs/CODEX_TODO.md geven niet dezelfde status voor TODO-items.
  ExpectedFixType: clarify
  RiskIfIgnored: statusdrift tussen overzicht en daadwerkelijke TODO-status.
  Notes: TODO/fase-beschrijvingen in total_project.md gesynchroniseerd met docs/CODEX_TODO.md.
  Status: done

- ID: CONSOL_PHASE2_HEADER_STATE
  Source: "`docs/CODEX_TODO.md` bevat de heading “PHASE-2 Roadmap (governed backlog — not started yet)” terwijl alle PHASE2-items eronder op [x] staan."
  Description: PHASE-2 heading zegt “not started yet” terwijl items als afgerond staan.
  ExpectedFixType: clarify
  RiskIfIgnored: inconsistente interpretatie van PHASE-2 status.
  Notes: PHASE-2 heading text in CODEX_TODO.md updated to reflect mixed completed/open backlog.
  Status: done

- ID: CONSOL_GOV_TEST_RUN_FILENAME
  Source: "`docs/CODEX_TODO.md` vermeldt bij **PHASE2_GOVERNANCE_TEST_SCENARIO_1** als output `docs/GOVERNANCE_TEST_RUN_01.md`, terwijl het aanwezige document `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md` heet."
  Description: verwijzing naar niet-bestaand test-run document in TODO.
  ExpectedFixType: link-fix
  RiskIfIgnored: broken reference in governance test output.
  Notes: Reference in CODEX_TODO.md updated to GOVERNANCE_TEST_SCENARIO_1.md.
  Status: done

- ID: CONSOL_AGENT_NAMING_CONTINUITY_COHESION
  Source: "In `docs/AGENTS.md` staat in de status-tabel “Continuity/Cohesion Agent” als gecombineerd item, terwijl er afzonderlijke secties en prompts bestaan: `prompts/continuity_agent.md` en `prompts/cohesion_agent.md`."
  Description: agentnaam in status-tabel is gecombineerd terwijl er aparte agents bestaan.
  ExpectedFixType: clarify
  RiskIfIgnored: verwarring over status/implementatie per agent.
  Notes: AGENTS.md genormaliseerd naar Cohesion als canonieke naam met Continuity als historische verwijzing.
  Status: done

- ID: CONSOL_AGENT_NAMING_DESIGN_LAYOUT
  Source: "In `docs/AGENTS.md` staat in de status-tabel “Design/Layout Advisor”, terwijl de agentsectie en prompt de naam “Design Agent” gebruiken (`prompts/design_agent.md`)."
  Description: agentnaam in status-tabel komt niet overeen met agentsectie/prompt.
  ExpectedFixType: rename
  RiskIfIgnored: inconsistent agent-naming in governance-documentatie.
  Notes: AGENTS.md genormaliseerd naar Design als canonieke naam met Layout als historische verwijzing.
  Status: done

- ID: CONSOL_GOV_TRIGGERS_GLOSSARY_RESEARCH
  Source: "`docs/WORKFLOW.md` noemt in “Governance Triggers” alleen Methodology/Technical/Troubleshooting, terwijl Glossary/Research triggers elders wel expliciet staan (stop-model tabel in `docs/WORKFLOW.md` en de lifecycle in `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`)."
  Description: governance-triggerlijst in WORKFLOW.md mist Glossary/Research.
  ExpectedFixType: clarify
  RiskIfIgnored: onvolledig beeld van governance-triggers in workflow-overzicht.
  Notes: Glossary & Research triggers nu expliciet in WORKFLOW.md.
  Status: done

- ID: CONSOL_AUTONOMY_STYLE_VARIANCE
  Source: "Autonomy-secties in prompts zijn niet uniform van stijl: Translation/Readability/Fidelity gebruiken een andere (Nederlandse) structuur dan de redactionele prompts met een Engelstalige “You MAY”/“You MUST” structuur."
  Description: autonomie/stop-model presentatie verschilt per promptgroep.
  ExpectedFixType: clarify
  RiskIfIgnored: inconsistenties in interpretatie van stop-model tussen prompts.
  Notes: requires clarification
  Status: pending

- ID: CONSOL_CODEX_META_PROMPT_BACKUP_REF
  Source: "`docs/CODEX_META_PROMPT.backup.1767359806` wordt genoemd in `docs/total_project.md`, maar wordt in de overige gelezen docs/prompts niet verder gerefereerd."
  Description: backup-bestand wordt alleen in total_project genoemd.
  ExpectedFixType: clarify
  RiskIfIgnored: onduidelijkheid over status/gebruik van backup-document.
  Notes: requires clarification
  Status: pending

- ID: CONSOL_ORPHAN_DOC_REFERENCE
  Source: "`docs/GOVERNANCE_TEST_RUN_01.md` wordt genoemd in `docs/CODEX_TODO.md` maar is niet aanwezig in de lijst van documenten in `docs/` (wel bestaat `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`)."
  Description: verwijzing naar een doc die niet voorkomt in huidige docs-lijst.
  ExpectedFixType: link-fix
  RiskIfIgnored: verwijzing naar niet-bestaand document in governance-docs.
  Notes: requires clarification
  Status: pending

## Non-Goals
- geen runtime-wijzigingen
- geen glossary-beslissingen
- geen nieuwe agents
- geen architectuurwijzigingen
- alleen consolidatie van documentatie

## Next Step (after this document)
Volgende stap is gecontroleerde uitvoering van deze items,
één voor één via Codex CLI, met review per stap.
