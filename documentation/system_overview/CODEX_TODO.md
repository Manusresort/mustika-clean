# CODEX_TODO — Capability-Driven Index

This file is a governance-aware capability index. It is non-operational and preparatory only.

Note: capabilities are the organizing principle; agents are support-only and non-authoritative; execution order is intentionally unspecified.

## Phase-4 — Preparatory (backlog)

- ID: PHASE4_CAPABILITY_MATURITY_BASELINE
  Status: COMPLETED
  Type: Analysis / Documentary (no execution)
  Description:
    Establish a capability-wide baseline by analysing all editorial
    capabilities as defined in docs/EDITORIAL_CAPABILITIES.md, including:
    - intended redactional behaviour (human reference model),
    - current maturity level (M1–M4),
    - system requirements needed to support the capability as intended,
    - indicative agent-support needs (signal-only, no authority).
  Explicitly out of scope:
    - agent design or implementation,
    - capability prioritisation,
    - runtime changes,
    - editorial or glossary decisions.
  Output:
    - documented maturity assessment per capability,
    - consolidated input for subsequent Phase-4 steps (gap analysis).
  Completion note: All editorial capabilities have been analysed to M4 level and consolidated
  in docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md. Placeholder sections deprecated.
  Phase-4 capability baseline is complete.
  Reference note: Cross-capability structural patterns identified in
  docs/PHASE4_CROSS_CAPABILITY_STRUCTURAL_LEVERS.md inform subsequent Phase-4.1 agent-gap derivation.

- ID: PHASE4_CROSS_CAPABILITY_STRUCTURAL_LEVERS
  Status: COMPLETED
  Type: Analysis / Documentary
  Description:
    Analyse cross-capability structural patterns and solution levers
    derived from the completed Phase-4 capability maturity analyses.
    This step consolidates recurring system-level gaps (e.g. proposal models,
    governance enforcement, signal handling) prior to any agent-gap derivation.
  Constraint note (explicit):
    Agent-gap derivation (Phase-4.1) MUST NOT start until this item is completed.
  Reference:
    docs/PHASE4_CROSS_CAPABILITY_STRUCTURAL_LEVERS.md
  Completion note:
    Cross-capability structural levers have been fully analysed and documented.
    This Phase-4 step is complete. Subsequent work may enter implementation
    mode only under an explicitly new phase or step.

- ID: PHASE4_IMPLEMENTATION_SCOPE_AND_SEQUENCE
  Status: PAUSED
  Type: Analysis / Planning (documentary only)
  Description:
    Determine the scope, order, and loci of implementation for the
    completed cross-capability structural levers.
    This step explicitly decides:
      - which levers are implemented first,
      - in which system layers (governance, workflow, agent derivation, tooling),
      - and which levers are intentionally deferred.
  Explicitly out of scope:
    - implementing any lever
    - designing agents or workflows
    - modifying runtime behavior or tooling
  Output:
    - documented implementation scope and sequencing rationale
    - explicit prerequisites for entering implementation mode
  Constraint note:
    No implementation work may start until this item is completed
    and explicitly marked as such.

  Status note:
    Cross-capability structural levers have been identified and
    described (documentary). One capability (Safety-Aware Editorial
    Judgement) has been normatively specified toward M4, but no
    structural lever has been systemically enforced.
    Further work on lever enforcement or testing is intentionally paused.

## Structural Levers — Enforcement & Testing

- ID: STRUCTURAL_LEVERS_ENFORCEMENT
  Status: PAUSED
  Type: Deferred (requires explicit restart)
  Description:
    Any work related to enforcing, testing, piloting, or system-level
    integration of cross-capability structural levers.
  Note:
    This item is intentionally paused. Restart requires an explicit
    decision and a clearly defined scope (capability, lever, and layer).

  Agreed implementation order (cross-capability structural levers):
    1. Canonical Proposal Model
    2. Signal → Gate → Closure
    3. Capability-agnostic Diff & Impact Representation
    4. Capability-specific Risk Taxonomies
    5. Agents as Sensors / Proposal Producers

  Execution rule:
    Structural levers are implemented strictly one at a time.
    Progression to the next lever is contingent on the previous
    lever proving tractable without unintended system coupling.

  PHASE-4.0 Capability Maturity Baseline — Analytical Breakdown
  - Type: Analysis / Documentary
    Status: IN PROGRESS
    Capability: Meaning Preservation & Semantic Integrity
    Reference: Extended M4-gap analysis documented in docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md
  - Type: Analysis / Documentary
    Status: IN PROGRESS
    Capability: Terminology & Glossary Stewardship
    Reference: Extended M4-gap analysis documented in docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md
  - Type: Analysis / Documentary
    Status: IN PROGRESS
    Capability: Readability Without Meaning Loss
    Reference: Extended M4-gap analysis documented in docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md
  - Type: Analysis / Documentary
    Status: IN PROGRESS
    Capability: Safety-Aware Editorial Judgement (Health & Risk Claims)
    Reference: Extended M4-gap analysis documented in docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md
  - Type: Analysis / Documentary
    Status: IN PROGRESS
    Capability: Document Integrity & Provenance Awareness
    Reference: Extended M4-gap analysis documented in docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md
  - Type: Analysis / Documentary
    Status: IN PROGRESS
    Capability: Cultural-Historical Interpretation
    Reference: Extended M4-gap analysis documented in docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md
  - Type: Analysis / Documentary
    Status: IN PROGRESS
    Capability: Annotation & Contextualisation
    Reference: Extended M4-gap analysis documented in docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md
  - Type: Analysis / Documentary
    Status: IN PROGRESS
    Capability: Error Recognition & Scholarly Commentary
    Reference: Extended M4-gap analysis documented in docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md
  Deprecated Phase-4 Capability Drafts (Superseded)
  - These entries represent early exploratory or pre-Phase-4 drafts.
  - They have been fully superseded by the completed Phase-4 capability maturity analyses.
  - The authoritative analysis is documented in docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md.
  - No additional Phase-4 capability assessment remains open.
  - Note: agent-support needs will be derived in a later Phase-4 step.

## Meaning Preservation & Semantic Control

Preserve meaning and semantic integrity across translations and edits.

Authority & System Support Envelope
- Authority owner: Human (editorial/historical).
- System support allowed: suggestion, detection, verification, logging, format checking only.
- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification.

### [PLACEHOLDER — NO TASKS]

- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]
- [FUTURE] [CAPABILITY] [NOT_AUTHORIZED_YET]

## Terminology Stewardship

Maintain consistent terminology and glossary discipline with provenance.

Authority & System Support Envelope
- Authority owner: Human (editorial/historical).
- System support allowed: suggestion, detection, verification, logging, format checking only.
- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification.

### [PLACEHOLDER — NO TASKS]

- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]
- [FUTURE] [CAPABILITY] [NOT_AUTHORIZED_YET]

## Cultural-Historical Interpretation

Provide cultural and historical interpretation without altering source integrity.

Authority & System Support Envelope
- Authority owner: Human (editorial/historical).
- System support allowed: suggestion, detection, verification, logging, format checking only.
- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification.

### [PLACEHOLDER — NO TASKS]

- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]
- [FUTURE] [CAPABILITY] [NOT_AUTHORIZED_YET]

## Error Recognition & Scholarly Commentary

Identify errors and add scholarly commentary without silent correction.

Authority & System Support Envelope
- Authority owner: Human (editorial/historical).
- System support allowed: suggestion, detection, verification, logging, format checking only.
- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification.

### [PLACEHOLDER — NO TASKS]

- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]
- [FUTURE] [CAPABILITY] [NOT_AUTHORIZED_YET]

## Safety-Aware Editorial Judgement

Handle safety-sensitive content with explicit caution and context.

Authority & System Support Envelope
- Authority owner: Human (editorial/historical).
- System support allowed: suggestion, detection, verification, logging, format checking only.
- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification.

### [PLACEHOLDER — NO TASKS]

- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]
- [FUTURE] [CAPABILITY] [NOT_AUTHORIZED_YET]

## Culinary Validation

Assess culinary coherence while preserving source intent.

Authority & System Support Envelope
- Authority owner: Human (editorial/historical).
- System support allowed: suggestion, detection, verification, logging, format checking only.
- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification.

### [PLACEHOLDER — NO TASKS]

- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]
- [FUTURE] [CAPABILITY] [NOT_AUTHORIZED_YET]

## Balanced Readability Craft

Improve readability without changing meaning or authority.

Authority & System Support Envelope
- Authority owner: Human (editorial/historical).
- System support allowed: suggestion, detection, verification, logging, format checking only.
- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification.

### [PLACEHOLDER — NO TASKS]

- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]
- [FUTURE] [CAPABILITY] [NOT_AUTHORIZED_YET]

## Interpretation Guidance

Guide reader interpretation without asserting authority or canon.

Authority & System Support Envelope
- Authority owner: Human (editorial/historical).
- System support allowed: suggestion, detection, verification, logging, format checking only.
- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification.

### [PLACEHOLDER — NO TASKS]

- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]
- [FUTURE] [CAPABILITY] [NOT_AUTHORIZED_YET]

## Contextual Annotation

Add contextual notes without modifying canonical text.

Authority & System Support Envelope
- Authority owner: Human (editorial/historical).
- System support allowed: suggestion, detection, verification, logging, format checking only.
- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification.

### [PLACEHOLDER — NO TASKS]

- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]
- [FUTURE] [CAPABILITY] [NOT_AUTHORIZED_YET]

## Document Integrity Awareness

Maintain integrity of the historical object and its traceability.

Authority & System Support Envelope
- Authority owner: Human (editorial/historical).
- System support allowed: suggestion, detection, verification, logging, format checking only.
- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification.

### [PLACEHOLDER — NO TASKS]

- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]
- [FUTURE] [CAPABILITY] [NOT_AUTHORIZED_YET]

- Repository-wide Governance Relabeling (GOV-A / GOV-B / BRIDGE)  
  [GOV-A] [FUTURE] [NON-BLOCKING] [STRUCTURAL]  
  Based on the completed governance audit (Pass 1) and the formal classification rules (Pass 2),\n  the repository requires a careful relabeling of documents to make governance layers explicit (GOV-A, GOV-B, BRIDGE).\n  This task explicitly defers execution to a later phase to avoid premature or bulk refactoring. Relabeling must be done incrementally, cluster-by-cluster,\n  under explicit human review.\n  Notes:\n  - Prerequisites completed:\n      • GOV_LABEL_AUDIT.md\n      • GOV_A_B_CLASSIFICATION.md\n  - This is a Project Governance (GOV-A) action.\n  - No automatic or bulk relabeling is authorized.\n  - This task does not block current phases.

## Completed / Historical (verbatim)

# Codex TODO – Mustikarasa

Legend:
[ DONE — P4 ]  completed and documented
[ ACTIVE — P4 ]  small, bounded, learning only
[ PARKED — Phase-5 ] intentionally deferred (not a bug, just timing)

---

Deze lijst wordt door Codex CLI beheerd.
Taken worden afgevinkt met [x] zodra ze voltooid zijn.
## Kern

- [ ] Basis chapter-/batch-workflow ontwerpen (JSON + subcommand) → zie PHASE2_CHAPTER_BATCH_WORKFLOW_DESIGN
- [x] Documentatie voor workflow in docs/WORKFLOW.md (documentatie aanwezig in docs/WORKFLOW.md)

### PHASE-1 Foundations (completed / historic)

- [x] Stabiele recipe-CLI via mustikarasa_codex_cli.py (gecontroleerd en werkt)
- [x] Prompts per agent in prompts/*.md externaliseren (alle agents gebruiken nu externe promptbestanden)
- [x] Documentatie voor agents in docs/AGENTS.md (overzicht compleet en up-to-date)
- [x] Nieuwe meta-agents geïntroduceerd en geregistreerd  
      (Methodology Archivist, Technical Advisor, Troubleshooting Agent — prompts + AGENTS.md)

#### System Governance & Architecture

- [x] SYSTEM_ORCHESTRATOR_MANDATE  
  Formeel mandaat en grenzen van de Orchestrator definiëren in documentatie:
  - wat de Orchestrator WEL mag,
  - wat de Orchestrator NIET mag,
  - welke acties altijd via een mens of meta-agent moeten lopen.
  Output zal o.a. terechtkomen in prompts/orchestrator.md en (optioneel) docs/WORKFLOW.md.

- [x] SYSTEM_GLOSSARY_DECISION_LIFECYCLE  
  Volledige beslis-lifecycle voor terminologie vastleggen:
  - voorstel → context → risico-review → menselijke beslissing → versiebeheer/rollback.
  Output in een nieuw document: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md.

- [x] SYSTEM_GOVERNANCE_TRIGGERS  
  Documenteren wanneer Methodology Archivist, Technical Advisor en Troubleshooting Agent
  automatisch moeten worden aangeroepen (trigger-criteria vanuit de Orchestrator).
  Output o.a. in prompts/orchestrator.md en docs/AGENTS.md.

- [x] SYSTEM_AGENT_STOP_CRITERIA  
  Per agent expliciete STOP- en ESCALATE-criteria documenteren
  (wanneer een agent moet stoppen en opschalen i.p.v. blijven improviseren).
  Output in een nieuw of bestaand document, bijv. docs/AGENTS.md of docs/WORKFLOW.md.

- [x] SYSTEM_GOVERNANCE_TESTS  
  Ontwerp van een kleine test-suite die governance zelf test:
  - fout formaat → wordt correct afgehandeld?
  - ongeautoriseerde actie → STOP?
  - templateversie-wijziging → Methodology-log?
  Output als nieuw document, bijv. docs/10-governance/GOVERNANCE_TESTS_PLAN.md.

### PHASE-2 Roadmap (governed backlog — in progress)

- [x] **PHASE2_AGENT_AUTONOMY_COMPLETION** (autonomy model applied across all editorial agents)  
  Alle actieve redactionele agents krijgen dezelfde “Autonomy / Soft-Stop / Governance-Stop / Human-Gate”
  beschrijving en gedragsregels als de kernpipeline-agents.  
  Scope: Cultural-Historical, Book Structure, Annotation, Recipe, Table, Image, Cohesion, Challenger,
  Design, Continuity.  
  Output: bijgewerkte prompts + aangevulde bullets in docs/AGENTS.md.

- [x] **PHASE2_TODO_REALITY_SYNC** (completed — aligned TODO with repo; see session PHASE2_TODO_REALITY_SYNC)  
  CODEX_TODO en feitelijke repo-status volledig gelijk trekken.  
  Beslissen per oud item: afvinken, herformuleren of vervangen.  
  Output: bijgewerkte TODO + sessielog.

- [x] **PHASE2_CHAPTER_BATCH_WORKFLOW_DESIGN** (design documented in CHAPTER_BATCH_WORKFLOW.md)  
  Ontwerpdocument voor hoofdstuk/batch-workflow (zonder code).  
  Beschrijft input/output per batch, governance-touchpoints en escalatie op batch-niveau.  
  Output: docs/CHAPTER_BATCH_WORKFLOW.md (+ korte samenvatting in WORKFLOW.md).

- [x] **PHASE2_GOVERNANCE_AGENT_RUNTIME_INTEGRATION_DESIGN** (design documented in GOVERNANCE_INTEGRATION_DESIGN.md)  
  Ontwerp hoe governance-agents in de Python-runtime worden aangeroepen  
  (events, inputs, outputs, logging).  
  Output: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md.

- [x] **PHASE2_GLOSSARY_RESEARCH_PILOT** (pilot documented — proposals only, no final decisions)  
  Kleine, gecontroleerde pilot Glossary + Research volgens de lifecycle,  
  met alleen beslisdocumenten (geen definitieve glossary-wijzigingen).  
  Output: docs/GLOSSARY_PILOT_REPORT.md.

- [x] **PHASE2_GOVERNANCE_TEST_SCENARIO_1** (scenario executed — documentary test)  
  Eerste concrete uitvoering van een scenario uit GOVERNANCE_TESTS_PLAN.md  
  (bijv. template-compliance of lifecycle-enforcement).  
  Output: docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md.

### PHASE-3 Documentation Reorganisation (planned)

- [ PARKED — Phase-5 ] **PHASE3_DOCS_REORG_PLAN_APPROVED**  
  Op basis van docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md: design expliciet reviewen en goedkeuren.

- [ PARKED — Phase-5 ] **PHASE3_DOCS_REORG_MOVE_PILOTS**  
  Fysiek verplaatsen/herstructureren van PILOT_* docs + runs volgens design.

- [ DONE — P4 ] **PHASE3_DOCS_REORG_MOVE_GOVERNANCE** (governance docs moved according to DOCS_INFORMATION_ARCHITECTURE — pilot scope only)  
  Fysiek verplaatsen van governance-/workflowdocs naar 10-governance/ en 30-workflow/.

- [ PARKED — Phase-5 ] **PHASE3_DOCS_REORG_UPDATE_REFERENCES**  
  Updaten van verwijzingen in docs/prompts na reorg.

- [PHASE3] Review whether “verify against stored artefacts” should become a requirement (later, via governance lifecycle).
- [PHASE3] Design a sampling pilot to analyze how “²” is used across the corpus (evidence-building, no text edits).
- [PHASE3] LEGACY_IMPORT_PATTERN: All future imports from legacy repo must use the same governed process (small batches, role-separated, provenance headers, read-only).
- [PHASE3] Proposal: design a follow-up pilot that only detects and flags ambiguous “²” cases (no auto-fix), to test governance-aligned review workflows.
- [PHASE3] Prototype a review-handoff workflow where flagged items are routed to a human reviewer (no edits — decision logging only).
- [PHASE3] Consider a follow-up pilot simulating disagreement between reviewers and escalation to Human Gate (no edits — governance only).
- [PHASE3] Consider a future governance pilot with multiple conflicting reviewers and explicit evidence links (scan images / research docs) before any decision moves beyond provisional.
- [PHASE3] Proposal: explore annotation-vs-translation patterns for context-dependent food terms (no decisions — pilot only).
- [PHASE3] Proposal: design a small readability-pressure pilot testing when annotations become excessive (no rules — documentary only).
- [PHASE3] Proposal: future pilot comparing reader feedback on minimally vs heavily annotated excerpts (controlled test).
- [PHASE3] Proposal: design a micro-pilot exploring when cultural notes belong in annotations vs separate historical commentary.
- [PHASE4] Evaluate whether observed workflow gaps merit design changes (based on pilots and synthesis docs).
- [PHASE4] Consider formal diagramming once governance architecture stabilizes (policy-track, not Phase-3).
- [PHASE4] Design incident templates (INCIDENT_REPORT + REVIEW_LOG) —
  policy-track, not Phase-3.
- [PHASE3] Consider a lifecycle walk-through pilot using ubi/ketela
  (documentary only, no decision).
- [PHASE3] Design a second lifecycle rehearsal using a different term
  (contrast case), still proposal-only.
- [PHASE3] Consider a “flag-only OCR scanner” proposal pilot
  (documentary only — no implementation).
- [PHASE3] If useful, design a *governance review simulation* for the
  flag-scanner proposal (no code, documentary only).
- [PHASE3] Optional follow-up: design a *reader study proposal*
  (documentary only — no guidance, no UX policy).

## PHASE4_AGENT_BRIDGE_DESIGN

**Phase Tag:** PHASE-4.1 (Preparation — documentary only)  
**Category:** Governance / Design  
**Status:** PROPOSAL — NOT IMPLEMENTED  

**User Story**  
As a governance architect, I want a safe bridge between CrewAI outputs and
governed artifacts, so that agents can contribute analysis without ever
modifying source texts or making decisions.

**Context & Intent**  
CrewAI agents will soon produce runtime outputs (translations, flags,
glossary ideas, annotations). We must define where those outputs live,
how they are marked as proposals, how governance reviews them, and how
STOP and rollback behave. This design does not enable runtime; it defines
how runtime must behave.

**Out of Scope / Must NOT Happen**  
- agents modifying canonical text  
- agents writing inside docs/ or book content  
- automatic glossary promotion  
- silent decisions  
- automation without lifecycle review  

**Governance Alignment**  
- Nature: design proposal only  
- Lifecycle: requires governance review before any implementation  
- Human Gate: only if design implies irreversible behavior  
- Publication impact: none

**Acceptance Criteria (summary)**  
- All agent outputs land only under sandbox proposal paths  
- Glossary outputs are marked lifecycle_stage: proposal with provenance  
- Any attempt to write outside sandbox triggers STOP + log  
- Deleting a run folder removes all effects

**Definition of Ready (summary)**  
- runtime remains sandbox-only  
- reviewers identified  
- rollback philosophy understood

**Definition of Done (summary)**  
- docs/AGENT_RUNTIME_SAFETY_BRIDGE.md created  
- STOP triggers and flows documented  
- no text-modifying paths defined  
- session log entry written  
- no runtime implemented

---

## PHASE4_AGENT_HARNESS_SPEC

**Phase Tag:** PHASE-4.1 (Preparation — documentary / scaffolding)  
**Category:** Runtime / Governance / Engineering  
**Status:** PROPOSAL — NOT IMPLEMENTED  

**User Story**  
As a meta-orchestrator / runtime maintainer, I want a standard harness for
running CrewAI agent pipelines in sandbox mode, so that every agent run is
logged, reversible, governance-aware, and cannot touch canonical texts
directly.

**Context & Intent**  
The harness defines how an agent run is wrapped: sandbox directory, input/
output locations, logging, STOP behavior, and rollback. It does not change
what agents do; it constrains how and where they do it.

**Out of Scope / Must NOT Happen**  
- harness writing into docs/ or canonical text  
- harness promoting glossary entries  
- harness enabling text-editing automation  
- runs outside sandbox

**Governance Alignment**  
- Nature: design + scaffolding; outputs remain proposals  
- Lifecycle: governance review before implementation  
- Human Gate: only if non-sandbox use is proposed  
- Publication impact: none

**Acceptance Criteria (summary)**  
- Runs create unique sandbox/agent_runs/<run_id>/ directories  
- All outputs are written only inside the run sandbox and marked PROPOSAL  
- Every run is logged in docs/CODEX_SESSION_LOG.md with run ID and summary  
- Any attempt to write outside sandbox triggers STOP + log  
- Deleting the run directory removes all effects

**Definition of Ready (summary)**  
- bridge design exists or in review  
- sandbox conventions agreed  
- governance reviewers identified

**Definition of Done (summary)**  
- docs/AGENT_RUNTIME_HARNESS.md created  
- sandbox + logging + STOP + rollback behavior described  
- no runtime implementation performed  
- session log entry written

---

## PHASE4_AGENT_HARNESS_SPEC (detailed backlog entry)

**ID:** PHASE4_AGENT_HARNESS_SPEC  
**Phase Tag:** PHASE-4.1 — Preparation (documentary / scaffolding)  
**Category:** Runtime / Governance / Engineering  
**Status:** PROPOSAL — NOT IMPLEMENTED  

### User Story

As a runtime maintainer / orchestrator,  
I want a standard harness for running CrewAI agent pipelines in sandbox mode,  
so that every run is logged, reversible, traceable, and cannot modify
canonical texts.

### Context & Intent

Agents will soon begin running pipelines (translation analysis, OCR
ambiguity scans, glossary suggestions, etc.). We currently lack a shared
execution wrapper that enforces:

- sandbox isolation
- where outputs go
- STOP triggers
- provenance logging
- rollback by deletion

The harness does not change agent intelligence; it defines how agents are
allowed to operate inside governed space. This is scaffolding only —
no runtime implementation yet.

### Out of Scope / Must NOT Happen

- harness writing into docs/, data/, or book source folders  
- harness promoting glossary entries  
- harness enabling text-editing automation  
- runs happening outside sandbox/  
- silent runs without logging

### Governance Alignment

- Nature: design + execution scaffolding (documentary first)  
- Lifecycle: proposal → governance review → possible pilot later  
- Human Gate: only if harness is proposed for canonical editing or
  publication-facing use  
- Publication impact: none

### Risk & STOP Triggers

Soft-stop if:  
- metadata from agent outputs lacks provenance or run ID

Governance-stop if:  
- the harness design allows writing outside sandbox  
- the harness includes any auto-apply or promotion logic

Human Gate if:  
- the harness is proposed for use on non-sandbox / canonical corpora

### Acceptance Criteria (behavioral summary)

- Runs create unique sandbox/agent_runs/<run_id>/ directories  
- All outputs are written only inside the run sandbox and marked PROPOSAL
  / EXPERIMENTAL  
- Every run is logged in docs/CODEX_SESSION_LOG.md with run ID and summary  
- Any attempt to write outside sandbox triggers STOP + log  
- Deleting the run directory removes all effects

### Non-Functional Considerations

- reversibility: everything undoable by deleting the run folder  
- traceability: unique run IDs and timestamps  
- safety: read-only access to canonical docs only  
- clarity: logs must be human-readable

### Definition of Ready

This item may not start until:

- bridge design (AGENT_RUNTIME_SAFETY_BRIDGE) exists or is in review  
- sandbox conventions are agreed (e.g., sandbox/agent_runs/…)  
- governance reviewers are identified  
- risks have been reviewed at least once in governance

### Definition of Done

This item is complete when:

- docs/AGENT_RUNTIME_HARNESS.md is created  
- sandbox layout, logging, STOP behavior, and rollback are described  
- no executable runtime code is introduced by this item  
- a session log entry is written documenting the spec  
- all changes are reversible by deleting the spec file

### Rollback Plan

Delete docs/AGENT_RUNTIME_HARNESS.md and the associated session log entry.  
No runtime artifacts or behavior are affected.

### Artefacts Touched

- new: docs/AGENT_RUNTIME_HARNESS.md (spec only)  
- referenced-only: docs/WORKFLOW.md, docs/PHASE4_READINESS_NOTES.md  
- unchanged: all canonical texts and runtime code

### Related Documents

- docs/AGENT_RUNTIME_SAFETY_BRIDGE.md  
- docs/WORKFLOW.md  
- docs/PHASE4_READINESS_NOTES.md  
- glossary lifecycle docs  
- governance stop model

### Methodology Log

[METHODOLOGY_LOG]  
Harness backlog entry expanded using the standard template.  
No implementation implied. Reversible by deletion.  
[/METHODOLOGY_LOG]

---

## PHASE4_AGENT_BRIDGE_DESIGN (detailed backlog entry)

ID: PHASE4_AGENT_BRIDGE_DESIGN
Phase Tag: PHASE-4.1 — Preparation (documentary only)
Category: Governance / Runtime Safety
Status: PROPOSAL — NOT IMPLEMENTED

## User Story
As a governance architect, I want a safe bridge between CrewAI outputs and governed artifacts,
so that agents can contribute analysis without ever modifying canonical texts or creating policy accidentally.

## Context & Intent
CrewAI agents will soon produce outputs (analysis, glossary ideas, OCR notes, flags, annotations).
There is currently no governed pathway for those outputs to move from “agent scratch work”
into “reviewable proposals”. The bridge defines where outputs live, how they are labeled,
and how governance reviews and rolls back mistakes — without enabling runtime behavior.

## Out of Scope / Must NOT Happen
- agents writing into docs/ or book text
- automatic glossary promotion
- default automation or implicit editing
- irreversible writes
- silent decisions

## Governance Alignment
- Nature: design proposal only
- Lifecycle: requires governance review before implementation
- Human Gate: only if behavior could affect publication
- Publication impact: none

## Risk & STOP Triggers
Soft-stop if design mixes proposal + implementation.
Governance-stop if canonical writes become possible.
Human Gate if design touches publication paths.

## Acceptance Criteria
Given agent outputs exist, when saved, they live only in sandbox proposal paths with provenance.
Given governance reviews them, glossary state does not change.
Given a mistake occurs, deleting the proposal removes all effects.

## Non-Functional
reversible by deletion; fully traceable; proposal labels visible; safe by default.

## Definition of Ready
- sandbox conventions confirmed
- reviewers identified
- scope explicitly documentary

## Definition of Done
- docs/AGENT_RUNTIME_SAFETY_BRIDGE.md created
- proposal + provenance rules defined
- STOP + rollback documented
- session log entry added
- no runtime exists

## Rollback
Delete this spec + session log.

## Artefacts
- new doc: AGENT_RUNTIME_SAFETY_BRIDGE.md
- references: governance docs, lifecycle docs

## Related
- docs/WORKFLOW.md
- docs/PHASE4_READINESS_NOTES.md

## Methodology Log
Bridge backlog formalized. No execution implied. Reversible by deletion.

[BACKLOG_ITEM]
id: P4_SAYUR_MISTRAL_SHAKEDOWN_001
phase: 4.1
title: Sayur Mistral shakedown – config, prompt & eerste runrecept
status: DONE — P4
owner: Codex + Orchestrator (sandbox)
related:
  - docs/crew/CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL.md
  - sandbox/crew/shakedown_sayur_mistral.yaml
  - sandbox/crew/prompts/shakedown_sayur_mistral_system.md
  - docs/ANNOTATION_STYLECARD_P4.md
  - docs/10-governance/AGENT_AUTONOMY_ENVELOPE.md
  - docs/PILOT_TO_PRACTICE_GUIDE.md

description:
  Phase-4.1 shakedown om een enkele Mistral-annotatieagent (via Crew + Ollama)
  veilig te laten draaien op een mini-excerpt uit SAJUR-A, met:
  - geen file-writes
  - geen tool-calls
  - JSON-only output (labels)
  - expliciete logging en rollback-pad.

preconditions:
  - GO-status voor RUN-P4-SAYUR-A-0001 bevestigd in HUMAN_GATE_LOG.md
  - sandbox readiness: docs/10-governance/SANDBOX_READINESS_CHECKLIST_P4_V1.md ≈ [x]
  - incident- & rollback-docs bekend bij facilitator:
    - INCIDENT_PLAYBOOK_P4_SANDBOX.md
    - ROLLBACK_TESTPLAN_P4_SANDBOX.md

steps:
  1. Scope & GO-herbevestiging
     - Lees GO_REQUEST_RUN_P4_SAYUR_A.md, GO_EVALUATION_FORM_P4_SANDBOX.md
       en HUMAN_GATE_LOG.md voor RUN-P4-SAYUR-A-0001.
     - Noteer eventuele aanvullende voorwaarden (max stappen, manual gating).

  2. Shakedown-config sanity-check
     - Review sandbox/crew/shakedown_sayur_mistral.yaml tegen:
       - AGENT_AUTONOMY_ENVELOPE.md
       - GOVERNANCE_INTEGRATION_DESIGN.md
     - Bevestig:
       - precies één agent (annotator)
       - geen tools, geen file-writes, alleen stdout JSON
       - expliciete verwijzing naar sandbox-scope.

  3. Systemprompt aanscherpen
     - Review sandbox/crew/prompts/shakedown_sayur_mistral_system.md tegen:
       - ANNOTATION_STYLECARD_P4.md (labels HISTORICAL/GLOSSARY/SAFETY/OCR/NONE)
       - PILOT_TO_PRACTICE_GUIDE.md (bridging lessons)
     - Maak expliciet:
       - GEEN vertaling / geen normalisatie
       - JSON-schema (velden, verplicht/optioneel)
       - gedrag bij twijfel: soft-stop → markeren & toelichten, geen beslissen.

  4. JSON-schema & mini-excerpt vastleggen
     - Definieer een minimaal JSON-schema in CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL.md
       (bijv. list van { line_id, text, label, notes }).
     - Kies 3–5 regels uit SAJUR-A (EXCERPT_MAP / sayur_groente_excerpt_v1.txt)
       en noteer de exacte bronreferenties (EvidenceRef).

  5. Codex-runrecept voor shakedown
     - Specificeer in CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL.md:
       - welke CLI-stap de crew start (bijv. test_mistral_agent / crew runner)
       - modelconfig (Ollama mistral, temperature 0.0–0.3)
       - waar stdout JSON wordt gevangen (terminal / logbestand).

  6. Observability & logging checklist
     - Definieer in CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL.md:
       - wat we loggen (prompt, config-hash, excerpt, JSON output, runtime errors)
       - hoe we RUN-ID en EvidenceRefs koppelen aan CODEX_SESSION_LOG.md.

  7. Eerste shakedown-run (sandbox, single-shot)
     - Voer één run met de mini-excerpt uit, met manual gating actief.
     - Geen reruns totdat output is beoordeeld en gelogd.

  8. Evaluatie + rollback-rehearsal
     - Toets output aan:
       - valid JSON?
       - labelgebruik (geen vertaling, geen gloss-besluiten)?
       - stop-model-respect (twijfel → markeren, niet oplossen)?
     - Vul een korte evaluatienoot in CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL.md
       en update CODEX_SESSION_LOG.md met een P4_SAYUR_MISTRAL_SHAKEDOWN sessie.
     - Oefen rollback: beschrijf concreet hoe deze ene run ongedaan gemaakt
       wordt (logs, planupdates, eventuele artefacts).

done_when:
  - backlog-item heeft een verwijzing naar een P4_SAYUR_MISTRAL_SHAKEDOWN_* sessie
    in CODEX_SESSION_LOG.md
  - CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL.md bevat:
    - JSON-schema
    - mini-excerpt beschrijving
    - runrecept
    - observability checklist
    - korte evaluatienoot
  - EEN succesvolle sandbox-run is uitgevoerd of bewust gestopt
    met een gedocumenteerde reden (soft-stop / governance-stop).

rollback:
  - Verwijder het P4_SAYUR_MISTRAL_SHAKEDOWN_* sessieblok uit docs/CODEX_SESSION_LOG.md.
  - Verwijder of markeer shakedown-secties in CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL.md
    als “invalidated”.
  - Markeer dit BACKLOG_ITEM als cancelled, met korte rationale.
Result: PASS — JSON stable, glossary behaviour consistent.  
Known limitation: definition sentences occasionally labelled as full-line HISTORICAL.  
Mitigation: flagged for later human review (Phase-5), not a blocker.
[/BACKLOG_ITEM]

[BACKLOG_ITEM]
id: P4_LOBAK_MISTRAL_SHAKEDOWN_001
status: DONE — P4
summary: Annotation-only shakedown focused on glossary ambiguity for lobak.
scope: 3–5 lines, JSON stdout only, manual runs, fully reversible.
risk: low (signal-only, no glossary decisions).
next_step: confirm excerpt + run first shakedown.
Result: PASS — glossary detection reliable, JSON stable.  
Known limitation: reasons sometimes reference cultural context instead of purely textual evidence.  
Mitigation: flagged for later human review (annotation consolidation).
[/BACKLOG_ITEM]

[BACKLOG_ITEM]
id: P4_SAYUR_MISTRAL_MULTAGENT_MICROPILOT_001
status: DONE — P4
summary: Multi-agent micro-pilot on SAJUR-A (annotator + challenger, JSON-only).
scope: 1 locked excerpt, annotator produces JSON annotations, challenger reviews them for overreach.
risk: low (signal-only, no glossary/safety decisions).
next_step: implement and test multi-agent runner.
[/BACKLOG_ITEM]

## PHASE-5 — Prompt Pattern

[TODO] REVIEW_AGENT_PROMPT_PATTERN_P5
status: proposed
scope: documentation only
desc: Evaluate new Agent Prompt Pattern (AGENT_PROMPT_PATTERN_P5.md) across key agents (annotator, challenger) and record gaps.
notes:
- no runtime or prompt rewrites without Human Gate review
- use labels: compliant / needs-clarification / defer-to-governance

## PRACTICE — Archivist alignment rhythm

[TODO] PERIODIC_ARCHIVIST_ALIGNMENT
status: ongoing
scope: documentation hygiene
desc: Bij nieuwe pilots/consolidaties een korte archivist-check uitvoeren
      (rapport in docs/archivist_reports/) om structurele drift te voorkomen.
notes:
- geen herstructurering zonder Human Gate
- rapporten blijven signalerend, niet beslissend

### PHASE-6 Workflow & Repo Architecture (planning)

- [x] PHASE6_RUNNER_OUTPUT_LAYOUT (layout validated & READY_FOR_IMPLEMENTATION in P6_RUNNER_OUTPUT_LAYOUT.md)  
    Design the standard output/artefact layout for excerpt-aware runs
    (logs, annotator JSON, challenger JSON, crew provisional JSON),
    including naming rules, per-case directories, and rollback expectations.  
    Goal: when the excerpt-aware runner is implemented, all outputs
    already have a governed home — without new governance rules.

- [x] PHASE6_RUNNER_PAYLOAD_REFINEMENT  
    Implemented refined payload structure (excerpt + run + raw_output + payload)
    in run_excerpt_workflow.py for new runs only (no retro-edit of existing outputs).

- [x] PHASE6_SAYUR_MINI_WORKFLOW_DESIGN (docs/P6_WORKFLOW_SAYUR_MINI.md)  
      Ontwerpdocument voor een kleine, reproduceerbare workflow:
      SAYUR mini-excerpt → annotator → challenger → crew-synthese
      met decision_status (CANDIDATE/CREW_PROVISIONAL/READY_FOR_HUMAN_REVIEW),
      duidelijke logging en mapping naar sandbox-paden
      (sandbox/workflows/p6_sayur_mini/*).  
      Output: docs/P6_WORKFLOW_SAYUR_MINI.md (documentair, geen runtime-wijzigingen).

- [x] PHASE6_SAYUR_MINI_WORKFLOW_PILOT (docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT.md)  
      Eerste uitgevoerde pilot volgens P6_WORKFLOW_SAYUR_MINI:
      mens runt bestaande shakedown/micropilot runners,
      verzamelt annotator/challenger JSON, vult crew_decisions_provisional.json
      en logt resultaten. Geen publicatie-impact, sandbox-only.
      Output: pilot-log + korte evaluatie in docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT.md.

- [x] PHASE6_SAYUR_MINI_WORKFLOW_PILOT02 (docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT02_EVALUATION.md)  
      Plan and execute Pilot 02 using a more complex SAYUR excerpt (~6–10 items).
      Objective: observe lifecycle behavior at scale, escalation selectivity,
      and challenger bias patterns. Outputs follow the same workflow as Pilot 01.

- [x] PHASE6_SAYUR_MINI_WORKFLOW_SYNTHESIS (docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT_SYNTHESIS.md)  
      Synthesis van Pilot 01–02 voor lifecycle, bias-signalen en traceability.

- [x] PHASE6_SAYUR_MINI_WORKFLOW_PILOT03
      Pilot executed on definitional excerpt; outcome = INCONCLUSIVE (DESIGN-TRIGGER).
      Evaluation and artefacts:
      → docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT03_EVALUATION.md
      → docs/P6_EXCERPT_BINDING_SPEC.md

- [x] PHASE6_EXCERPT_BINDING_SPEC
  Design change: workflows must accept an explicit `excerpt_id` / `excerpt_path`
  and record it in run logs so excerpt → run → decision is traceable.
  Scope: specification only (no runtime changes yet).
  Context: Pilot 03 marked INCONCLUSIVE due to runner reusing earlier SAYUR excerpt.

- [x] PHASE6_EXCERPT_BINDING_INTEGRATION_PLAN
  Plan how excerpt binding (metadata fields) will propagate consistently into
  pilots, scholarly pipelines, and crew artefacts. Scope remains documentary;
  no runtime enforcement yet.

- [x] PHASE6_EXCERPT_METADATA_INTEGRATION_DOCS
  Added excerpt_id / excerpt_source / excerpt_version to pilot plans,
  evaluation templates, and workflow JSON examples so excerpt usage becomes
  explicitly documented and traceable (documentary only).

- [x] PHASE6_REPOSITORY_ARCHIVIST_INTEGRATION (integration rules documented in P6_REPOSITORY_ARCHIVIST_INTEGRATION.md)  
      Define how and when the Repository Archivist agent participates in Phase-6 workflows:  
    - routine checks for navigation consistency and documentation sprawl,  
    - proposals for cleanup rather than direct file moves,  
    - integration with docs/navigation/EDITORIAL_INDEX.md and DOCS_INFORMATION_ARCHITECTURE.md,  
    - clear handoff pattern to humans / Codex-backed tasks (no autonomous actions).  

- [x] PHASE6_INDEX_EXPANSION_PASS  
      Editorial Index expanded with Phase-6 documents.

- [x] PHASE6_NAV_GROUPING_CANDIDATES_REPORT  
      Read-only report listing navigation-grouping candidates.

- [x] LOW_RISK_MOVE_P6_MIGRATION_CANDIDATE_LIST  
      Single low-risk navigation move, fully logged with rollback.

- [x] CASEFILE_PLACEMENT_DECISION_LOG  
      Decision recorded: case files remain in docs/ for traceability.

- [x] EDITORIAL_INDEX_CASEFILE_UPDATE  
      Case files added to Editorial Index with decision reference.

- [x] PHASE6_EXCERPT_BINDING_IN_RUNTIME_DESIGN (design frozen in P6_EXCERPT_BINDING_RUNTIME_DESIGN.md)
    Design-only: define how excerpt_id/source/version propagate into runner logs
    (aligning with P6_EXCERPT_AWARE_RUNNER_DESIGN.md; no code deployment).

- [x] PHASE6_CASE01_READINESS_PLAN (readiness checklist defined in P6_CASE01_READINESS_PLAN.md; Case-01 is validation-ready: readiness, execution, validation docs exist)
      Document what is required to un-pend Case-01 once excerpt-aware logging exists
    (artefacts, log alignment, triage path, rollback).

- [ ] PHASE6_NAV_GROUPING_LOW_RISK_MOVE_PLAN
    For each navigation candidate, create per-file migration plans (proposal-only).

- [ ] PHASE6_NAV_LINK_CONSISTENCY_PASS
    Check and correct stale links created by earlier migrations (documentation only).

- [ ] PHASE6_IMPLEMENT_EXCERPT_AWARE_RUNNER  
    Implement an excerpt-aware runner and logging path matching P6_EXCERPT_AWARE_RUNNER_DESIGN.md for Case-01/Case-02, without changing governance rules.  
    - Create a real script (e.g. sandbox/crew/run_excerpt_workflow.py or equivalent),  
    - Wire CLI flags for excerpt_id/source/version,  
    - Ensure logs and JSON artefacts carry the metadata as designed.

- [x] PHASE6_CASE02_EXCERPT_SELECTION (excerpt lobak_034_048 locked, 2026-01-12)  
      Choose and lock a LOBAK excerpt for Case-02, update P6_LOBAK_INTERNAL_WORK_CASE02.md
      and replace the placeholders in P6_CASE02_READINESS_PLAN.md and
      P6_CASE02_REAL_RUN_EXECUTION_PLAN.md with real excerpt_id/source/version.

---

## Phase-6 — Clarity & Canon Governance (lightweight)

- [ ] PHASE6_CANONICAL_CRITERIA_OVERVIEW  
      Create docs/CANONICAL_CRITERIA_OVERVIEW.md.  
      Purpose: summarize — in one place — what “CANONICAL” means, who approves it,  
      and how it relates to the lifecycle (CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL).  
      Keep it documentary; reference existing governance docs rather than inventing new rules.

- [ ] PHASE6_CONFLICT_HANDLING_GUIDE  
      Create docs/CONFLICT_HANDLING_GUIDE.md.  
      Describe: when to leave disagreements in PROVISIONAL, when to escalate to Human Gate,  
      and how conflicts are logged and traced.  
      Goal: clarity without automated arbitration.

- [ ] PHASE6_ANNOTATION_QUALITY_NOTE  
      Create docs/ANNOTATION_QUALITY_ASSURANCE_NOTE.md.  
      Explain how quality is ensured in practice (annotator + challenger, bias checks, pilots, Human Gate).  
      Clarify that agents produce provisional outputs only; humans decide.

- [ ] PHASE6_CANON_EVOLUTION_POLICY_NOTE  
      Create docs/CANONICAL_EVOLUTION_NOTE.md.  
      Document — at a high level — how canonical material may change over time  
      (supersede instead of overwrite, keep history, explicit rationale, rollback expectations).  
      Keep scope small; no new governance, just transparency.

---

### PHASE6_CASE02_RUNNER_MAPPING — PENDING

Goal:
Design and later implement a mapping from the LOBAK config

- sandbox/crew/configs/lobak_case02.yaml

to a concrete runner/pipeline, mirroring the pattern used for
Case-01 (SAYUR), so that:

- annotator_primary and challenger_primary can run,
- excerpt-aware JSON artefacts are produced,
- logs and outputs follow the Phase-6 layout.

Notes:
- Two shakedown runs confirmed excerpt-binding works,
  but there is currently **no runner script mapped** to this config.
- This item is documentary until governance explicitly approves
  implementation work. No silent fixes; no untracked code changes.

Status: PENDING

### Phase-7 — Canonical Decision Trails

- [x] Rehearsal trail (LOBAK Case-02)
      status: DONE — rehearsal-only, non-canonical
      refs:
        - docs/pilots/P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md
        - docs/decisions/rehearsal/
        - docs/CODEX_SESSION_LOG.md

- [x] Real pilot: glossary lemma itemisation (“lobak”)
      status: DONE — first real canonical decision (lemma only, non-semantic)
      refs:
        - docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSARY_LOBAK_001.md
        - docs/CANONICAL_INDEX.md
        - docs/CODEX_SESSION_LOG.md

- [x] Reflection + decision types tuning (optional, after pilot)
      status: DONE — no decision-type changes required
      refs:
        - docs/pilots/P7_CANONICAL_PILOT_REFLECTION.md

### Phase-8 — Meaning Preservation (status note)

Voorbereidend: handmatige redactionele oefening — geen agent-run,
geen capability-evaluatie; telt niet als Phase-8 pilot.
Status: PHASE-8 — COMPLETED — REWORK ACCEPTED (PASS-run niet vereist; FAIL-signalen betekenisvol).
Note: Phase-9 micro-pilot P9_FORMAT_DISCIPLINE_PILOT_001 COMPLETED (validator PASS); refs: P9_FORMAT_DISCIPLINE_PILOT_001, P9_OUTPUT_CONTRACT_VALIDATOR_BUGFIX_001.

- [x] PHASE8_FIRST_REAL_AGENT_PILOT
      Beschrijving:
      Eerste Phase-8 pilot uitvoeren met:
      - echte CLI/Python agent-run (sandbox)
      - Translation → Readability → Fidelity (runnerbaar via bestaande entrypoints)
      - vastgelegde runner-context (command, logs, prompts)
      - expliciete evaluatie tegen EDITORIAL_CAPABILITIES (DoD)
      Scope: één klein, afgebakend fragment.
      Annotation stap is momenteel niet runnerbaar via bestaande entrypoints;
      wordt gelogd als runtime-gap en apart opgepakt.
      Uitgevoerd via echte agent-run (P8_RUN_20260108_112252).
      Volledige capability-evaluatie uitgevoerd.
      Uitkomst: REWORK (provisional).
      Leerpunten doorgezet naar vervolg-TODO’s.

- [x] PHASE8_ANNOTATION_RUNNER_GAP_TRIAGE
      Beschrijving:
      Repo-feitelijk vaststellen wat nodig is om Annotation Agent
      reproduceerbaar te kunnen draaien (sandbox-only),
      of expliciet besluiten dat Annotation in Phase-8 apart blijft.
      afronding:
      - gap_classification: GAP_B
      - besluit: Annotation expliciet buiten Phase-8 scope
      - verwijzing: ANNOTATION_RUNNER_GAP_REPORT

- [ ] FUTURE_ANNOTATION_PHASE_INTEGRATION
    Beschrijving:
    Evalueren of en hoe Annotation als volwaardige pipeline-stap
    geïntegreerd moet worden in een latere fase (bijv. Phase-9),
    inclusief:
    - CLI-entrypoint
    - output-contract
    - validator-uitbreiding
    Voorwaarde:
    Alleen na afronding van Phase-8 output-contract enforcement.

- [ ] FUTURE_ANNOTATION_OUTPUT_CONTRACT_DEFINITION
    Beschrijving:
    Vaststellen van een expliciet output-contract voor Annotation
    (scheiding hoofdtekst / annotaties / meta),
    los van Phase-8 runs.
    Dit voorkomt vermenging wanneer Annotation later wordt geïntegreerd.

- [x] PHASE8_OUTPUT_CONTRACT_AND_ROLE_ENFORCEMENT
    Beschrijving:
    Vaststellen en afdwingen van een expliciet output-contract
    voor Phase-8 agent-runs, zodat:
    - hoofdtekst, meta-commentaar en fidelity-signalen
      niet vermengd worden;
    - agents geen governance-onjuist taalgebruik introduceren
      (zoals “definitief”);
    - rolafbakening (Translation / Fidelity / Annotation)
      aantoonbaar gehandhaafd wordt op runner-niveau.

    Scope:
    - Analyse op basis van bestaande runner en logs
    - Sandbox-only
    - Geen canonieke wijzigingen
    - contract v2 (EN/NL allowed) adopted
    afronding:
    - gate enforced (procedural + technical)
    - no PASS-run reached; Phase-8 inhoudelijk open
    - closeout: COMPLETED — REWORK ACCEPTED (PASS-run niet vereist)

    [x] PHASE8_OUTPUT_CONTRACT_VALIDATOR_SCRIPT (sandbox-only)
        Beschrijving:
        Maak een minimale post-run validator (shell of python) die de
        verificatie-checklist draait (rg-commands) en PASS/FAIL rapporteert.
        Geen wijzigingen aan runner of agent prompts; alleen meten.

        Acceptatie:
        - kan draaien op een run_dir
        - geeft per check een duidelijke PASS/FAIL
        - schrijft report naar sandbox/phase8_runs/<run_id>/eval/output_contract_checks.txt
        Artefacten:
        - script: sandbox/tools/phase8_output_contract_validator.sh
        - first_run_id: P8_RUN_20260108_112252
        - result: FAIL (exit 1) — expected for this run

    [x] PHASE8_OUTPUT_CONTRACT_ENFORCEMENT_GATE
        Beschrijving:
        Verplicht de output-contract validator als harde gate na iedere Phase-8 CLI-run
        (Translation → Readability → Fidelity), met FAIL-status als blokkade voor verdere
        evaluatie/export.

        Acceptatiecriteria:
        - Validator wordt standaard uitgevoerd na elke Phase-8 run.
        - Een FAIL produceert expliciete gate-melding in eval/ (geen automatische correcties).
        - Geen wijzigingen aan pipeline-stappen of agents; enkel enforcement via gate.
        afronding:
        - enforcement_type: procedural
        - gate: mandatory validator run
        - automation: none (by design)

    [x] PHASE8_OUTPUT_CONTRACT_TECHNICAL_GATE_WRAPPER
        afronding:
        - artefact: sandbox/tools/phase8_run_with_gate.sh
        - verified: wrapper exercised on FAIL cases; gate messaging present
        - evidence: eval/output_contract_checks.txt updated on FAIL runs
        - date: 2026-01-08
        - note: no PASS-run reached (output contract violations remain)

    [x] PHASE8_VALIDATOR_DEPENDENCY_RIPGREP
        Beschrijving:
        Validator gebruikt rg (ripgrep). Borg dat Phase-8 runs niet onbetrouwbaar
        worden door ontbrekende rg:
        - documenteer prereq (brew install ripgrep)
        - (optioneel later) voeg deps-check toe in scripts
        Scope: sandbox-only; geen pipeline wijziging

- [ ] PHASE8_FIRST_PASS_RUN
    Beschrijving:
    Realiseer de eerste PASS-run onder output-contract v2 met gate.
    Acceptatie: validator overall_status: PASS (exit 0) + report aanwezig.
    Nota: PASS-run is niet vereist voor Phase-8 afronding (optioneel backlog).

- [ ] Phase-8: Fidelity volgt Opmerkingen-separator niet consistent — format strictness
      BACKLOG / LOW-RISK / NON-BLOCKING
    Beschrijving:
    Kleine aanscherping van Fidelity OUTPUT-FORMAT instructies om
    remarks-separator naleving te verbeteren, zonder blokkade voor Phase-8.

### Phase-9 — Format Discipline (status note)

- [ ] Phase-9: Gate/validator should always emit eval/output_contract_checks.txt even on FAIL (Run03 produced PHASE8_GATE_FAIL but eval/ was empty). Evidence: sandbox/phase9_runs/P9_RUN_20260108T_RUN03/logs/run.log and empty eval/ directory. BACKLOG / LOW-RISK / NON-BLOCKING.

### Capability Mapping Follow-Ups (documentation only)

- [ ] MAP_CLARIFY_PRIMARY_OWNERSHIP
      (per capability expliciet benoemen wie primair accountable is — later)
- [ ] MAP_ADD_CONTRIBUTOR_COLUMN
      (contributors zichtbaar maken — geen gedrag wijzigen)
- [ ] MAP_REVIEW_PHASE3_IMPACT
      (check of pilots geen beslissingen nemen in GAP-gebieden)

Note: do not execute automatically — governance review first.
## Capability M4 Enablement — Safety-Aware Editorial Judgement

- ID: SAFETY_M4_SIGNAL_DEFINITION
  Status: NOT STARTED
  Type: Analysis / Design
  Description:
    Define what constitutes a safety-relevant signal within the
    Safety-Aware Editorial Judgement capability.
    This includes identifying qualifying content patterns and
    explicit non-qualifying cases.
  Explicitly out of scope:
    - implementation
    - automation
    - agent behavior

- ID: SAFETY_M4_PROPOSAL_REQUIREMENT
  Status: NOT STARTED
  Type: Analysis / Design
  Description:
    Specify when a Canonical Proposal Record is mandatory for
    safety-related observations, including cases of intentional
    non-action or deferral.
  Explicitly out of scope:
    - deciding outcomes
    - governance enforcement

- ID: SAFETY_M4_GATE_AND_CLOSURE_RULES
  Status: NOT STARTED
  Type: Analysis / Design
  Description:
    Define the minimum gate and closure requirements for safety
    signals, including acceptable closure states and documentation
    expectations.
  Explicitly out of scope:
    - workflow orchestration
    - authority assignment

- ID: SAFETY_M4_STOP_CONDITIONS
  Status: NOT STARTED
  Type: Analysis / Design
  Description:
    Identify explicit STOP conditions where continuation without
    documented safety handling is not permitted.
  Explicitly out of scope:
    - runtime enforcement
    - tooling

- ID: SAFETY_M4_EVIDENCE_IN_RUNS
  Status: NOT STARTED
  Type: Validation Criteria
  Description:
    Define what constitutes sufficient evidence in runs/logs to
    justify upgrading Safety-Aware Editorial Judgement to M4.
  Explicitly out of scope:
    - executing runs
    - changing validators
