# GOV Label Audit — Repository Scan

Timestamp: 2026-01-08 16:33:44

This is a read-only audit to support later GOV-A / GOV-B labeling. No edits were made.

## docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Purpose
- ## Lifecycle Stages

Quoted phrases:
- L5: "Het borgt governance, reproduceerbaarheid en een audit-trail voor glossary-beslissingen."
- L34: "4) Human Gate (Decision)"

## docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Governance Agent Runtime Integration Design
- ## Purpose
- ## Scope
- ## Runtime Events & Triggers
- ### Methodology & Accountability Archivist
- ### Incident & Resilience (Troubleshooting) Agent
- ### Glossary / Terminology Agent
- ## Data & Logging Model
- ## Failure Modes & Safeguards
- ## Non-Goals
- ## Relationship to Other Docs

Quoted phrases:
- L1: "# Governance Agent Runtime Integration Design"
- L4: "Legt vast hoe governance-agents (Methodology, Technical, Troubleshooting, Glossary, Research)"
- L18: "- Batch/Chapter workflow wordt meegenomen als context voor events."
- L24: "- Mogelijke governance-agents: Methodology, Research."
- L25: "- PhaseCompleted (Translation/Readability/Fidelity)"
- L27: "- Mogelijke governance-agents: Troubleshooting, Methodology."
- L30: "- Mogelijke governance-agents: Troubleshooting, Methodology."
- L33: "- Mogelijke governance-agents: Troubleshooting, Research."
- L36: "- Mogelijke governance-agents: Glossary, Methodology, Research."
- L39: "- Mogelijke governance-agents: Technical, Methodology."
- L40: "- WorkflowChangeProposal"
- L42: "- Mogelijke governance-agents: Methodology, Troubleshooting."
- L45: "- Mogelijke governance-agents: Troubleshooting, Methodology."
- L51: "- bij grote workflow-wijzigingen,"
- L52: "- bij afronden van SYSTEM_* of PHASE2_* items,"
- L86: "- beslist of workflow veilig kan doorgaan of human gate nodig is."
- L97: "- blijft proposal-only; beslissingen via Human Gate."
- L112: "- governance-calls worden gelogd met event-ID, agentnaam en artefacttype."
- L119: "- governance-agent niet aangeroepen wanneer dat wel had gemoeten."
- L120: "- governance-agent levert geen geldig artefact terug."
- L124: "- soft-stop verplicht bij inconsistente of ontbrekende governance-output."
- L125: "- Orchestrator mag batch NIET stilzwijgend laten doorgaan wanneer een governance-stap faalt;"
- L130: "- alle beslissingen blijven reversibel zolang governance-artefacten incompleet zijn."
- L132: "- stop-model: docs/WORKFLOW.md"
- L133: "- testplan: docs/10-governance/GOVERNANCE_TESTS_PLAN.md"
- L134: "- voorbeelden: docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md en docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md"
- L139: "- geen bypass van bestaande Human Gates."
- L142: "- docs/WORKFLOW.md"
- L143: "- docs/CHAPTER_BATCH_WORKFLOW.md"
- L144: "- docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md"
- L145: "- docs/10-governance/GOVERNANCE_TESTS_PLAN.md"

## docs/10-governance/GOVERNANCE_TESTS_PLAN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Governance Test Plan
- ## Purpose
- ### 2) Lifecycle Enforcement (Glossary)
- ### 3) Governance Trigger Tests
- ### 5) Hard-Stop (Human-Gate)
- ## Execution Model
- ## Maintenance

Quoted phrases:
- L1: "# Governance Test Plan"
- L4: "Dit testplan borgt dat governance-mechanismen correct werken."
- L31: "- human gate vereist"
- L34: "### 3) Governance Trigger Tests"
- L36: "- nieuwe workflow -> Methodology wordt aangeroepen"
- L48: "### 5) Hard-Stop (Human-Gate)"
- L61: "- tests draaien per CLI workflow"
- L66: "Hoe het testplan wordt geüpdatet wanneer governance verandert."

## docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Governance Test — Scenario 1
- ## Scenario Description
- ## Expected Behaviour
- ## Simulated Run
- ## Governance Activity
- ## Results
- ## Observations

Quoted phrases:
- L1: "# Governance Test — Scenario 1"
- L6: "Dit is governance-gevoelig omdat terminologie-consistentie en culturele context"
- L11: "- Governance-stop bij mogelijke culturele betekenisverschuiving."
- L12: "- Orchestrator schakelt governance-agents in volgens het ontwerpdocument."
- L28: "- Orchestrator: pauzeert item en vraagt governance-agents."
- L30: "## Governance Activity"
- L31: "Op basis van docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md:"
- L43: "Action: Governance-stop triggered; awaiting Glossary/Research inputs."
- L62: "Recommendations: Human Gate needed before final glossary decision."
- L66: "Event: Governance-stop for terminology inconsistency (arem arem)."
- L68: "Next: Human Gate review required before final decision."
- L73: "- governance-stop: JA"
- L74: "- human-gate automatisch: NEE"
- L80: "- Governance-stop voorkwam onbedoelde terminologie-beslissingen."

## docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Governance Test — Scenario 2 (Partial Batch Failure)
- ## Scenario Description
- ## Expected Behaviour
- ## Simulated Run
- ## Governance Activity
- ## Results
- ## Observations
- ## Recommendations

Quoted phrases:
- L1: "# Governance Test — Scenario 2 (Partial Batch Failure)"
- L5: "Items 1, 2 en 4 verlopen zonder governance-conflict."
- L7: "Dit is governance-relevant omdat format-afwijkingen de Fidelity controle kunnen ondermijnen."
- L13: "- Orchestrator activeert governance-stop voor item 3 via Troubleshooting/Methodology."
- L22: "- Kleine twijfelpunten opgelost via soft-stop self-healing, geen governance-stop."
- L31: "## Governance Activity"
- L32: "Op basis van docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md:"
- L43: "Action: Governance-stop for item-3; batch continues for safe items."
- L61: "- Human Gate invoked automatically: NO (only recommended if risk is high)"
- L65: "- Governance-stop isolated the problem without halting the batch."
- L69: "- Clarify partial-batch restart semantics in CHAPTER_BATCH_WORKFLOW."

## docs/10-governance/GO_BRIEF_P4_SAYUR.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 2 — Documents to read (in order)
- ## 4 — What this meeting WILL decide
- ## 6 — Expected outputs

Quoted phrases:
- L3: "Title: GO Brief — Phase-4 Sandbox (SAYUR Microrun)"
- L47: "- Phase-4 readiness notes"
- L68: "- Is Human Gate duidelijk en bereikbaar?"
- L84: "- entry in HUMAN_GATE_LOG (document only)"

## docs/10-governance/GO_EVALUATION_FORM_P4_SANDBOX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Section 2 — Safety checklist
- ## Section 3 — Risk review (short notes)
- ## Section 5 — Logging
- ## Recorded Decision (Summary)

Quoted phrases:
- L3: "Title: GO / NO-GO Evaluation Form — Phase-4 Sandbox"
- L14: "- Human Gate Policy"
- L43: "[ ] Human Gate triggers clearly identified"
- L63: "(Do reviewers know when to call Human Gate?)"
- L90: "docs/10-governance/HUMAN_GATE_LOG.md  → YES / NO"
- L110: "Phase-4 is considered complete for SAYUR. Phase-5 framing proceeds"
- L111: "under Human Gate supervision."

## docs/10-governance/GO_MEETING_AGENDA_P4_SAYUR.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Participants (by role, not person)
- ### 50–60 min — Decision & logging

Quoted phrases:
- L3: "Title: GO Meeting Agenda — Phase-4 Sandbox (SAYUR Microrun)"
- L17: "- Governance reviewer"
- L18: "- Cultural/Human Gate reviewer"
- L59: "- HUMAN_GATE_LOG bijwerken (document only)"

## docs/10-governance/GO_NO_GO_PROPOSAL_SAYUR_SANDBOX_P4.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 1) Proposed Scope
- ## 2) Controls Already in Place
- ## 3) Expected Risks (and mitigations)
- ## 6) Proposed GO / NO-GO question
- ## 7) If GO — Preconditions Checklist
- ## 8) If NO-GO — Follow-up

Quoted phrases:
- L3: "Title: GO / NO-GO Proposal — Phase-4 Sandbox (SAYUR-A, Annotation-Only)"
- L22: "- Human Gate is ACTIEF aanwezig tijdens de volledige run."
- L30: "- ✔ Human Gate Policy"
- L40: "- Ambiguity → soft-stop + Human Gate"
- L79: "Governance answers:"
- L95: "- [ ] Human Gate logbestand aanwezig"
- L96: "- [ ] Human Gate reviewer toegewezen en bekend"
- L107: "- Herzie pilots / governance docs"

## docs/10-governance/GO_REQUEST_RUN_P4_SAYUR_A.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 1 — Requested Action
- ## 3 — Risk Summary
- ## 5 — Reminder
- ## Outcome (Recorded)

Quoted phrases:
- L9: "Formeel verzoek aan governance om een beslissing te nemen"
- L10: "over de voorgestelde microrun in Phase-4 sandbox."
- L23: "- Human Gate: active during run"
- L50: "Glossary risk: Human Gate required"
- L81: "3) Logging in HUMAN_GATE_LOG.md."
- L88: "- Granted by: Human Gate (Phase-4 sandbox)"
- L91: "- Continue under existing governance controls."
- L93: "- Linkage: See HUMAN_GATE_LOG.md entry "Phase-4 Sandbox Closure (SAYUR)"."

## docs/10-governance/HUMAN_GATE_LOG.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## ENTRY — Phase-4 Sandbox Closure (SAYUR)

Quoted phrases:
- L2: "[HUMAN_GATE_DECISION]"
- L11: "ReviewerRole: Human Gate / Governance"
- L13: "[/HUMAN_GATE_DECISION]"
- L15: "## ENTRY — Phase-4 Sandbox Closure (SAYUR)"
- L18: "- Gate: HUMAN GATE — Phase-4 Sandbox"
- L20: "- Scope: Closure of Phase-4 sandbox (SAYUR) and move to Phase-5 preparation"
- L22: "- Sandbox objectives demonstrated (runtime, governance, logs, rollback)."
- L27: "- Phase-5 work must remain traceable and reversible."
- L28: "- Notes: GO is documentary; Phase-5 direction requires separate review."

## docs/10-governance/HUMAN_GATE_POLICY_P4_SANDBOX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 1) Human Gate — Role (not a person)
- ## 2) Triggers (WHEN Human Gate must be called)
- ## 3) Decision Model
- ## 4) Logging Requirements
- ## 5) Interaction with Agents
- ## 6) Interaction with Incident Playbook
- ## 7) Boundaries & Sunset

Quoted phrases:
- L1: "[HUMAN_GATE_POLICY_P4_SANDBOX]"
- L3: "Title: Human Gate — Phase-4 Sandbox Policy"
- L6: "GOVERNANCE POLICY — NOT A RUNTIME APPROVAL"
- L13: "Geldt uitsluitend voor Phase-4 sandbox-runs (design pilots, beperkte excerpten)."
- L18: "## 1) Human Gate — Role (not a person)"
- L20: "Role name: Editorial & Cultural Review Gate"
- L26: "- escaleren naar governance indien structureel probleem"
- L36: "## 2) Triggers (WHEN Human Gate must be called)"
- L38: "Human Gate is VERPLICHT wanneer:"
- L48: "Bij twijfel → ALTIJD Human Gate."
- L58: "- NO-GO — stop, rollback, governance bespreken"
- L67: "Elke Human Gate-actie moet bevatten:"
- L77: "docs/10-governance/HUMAN_GATE_LOG.md (append-only)."
- L94: "- Human Gate omzeilen"
- L104: "Als Human Gate wordt opgeroepen naar aanleiding van incident:"
- L107: "- daarna Human Gate review"
- L118: "- alleen totdat een apart Phase-4 governance-kader productie-klaar is"
- L119: "- en kan alleen worden gewijzigd via governance-logbesluit."
- L125: "[/HUMAN_GATE_POLICY_P4_SANDBOX]"

## docs/10-governance/INCIDENT_PLAYBOOK_P4_SANDBOX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 4) Escalation Rules
- ## 7) Linkage to Other Governance

Quoted phrases:
- L3: "Title: Incident Playbook — Phase-4 Sandbox"
- L85: "Human Gate (rol), niet individu."
- L87: "Human Gate acties:"
- L89: "- besluit wordt gelogd in governance-artefact"
- L117: "## 7) Linkage to Other Governance"

## docs/10-governance/ROLLBACK_TESTPLAN_P4_SANDBOX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Test steps (table-top rehearsal first)
- ### Rehearsal: RUN-P4-SAYUR-A-0001 (Sandbox)

Quoted phrases:
- L38: "- fix governance/process before retry."
- L48: "- No persistent edits to source or canonical docs."
- L60: "- move/delete run logs (sandbox only) IF governance approves."
- L72: "- Any real rollback requires Human Gate confirmation."

## docs/10-governance/SANDBOX_READINESS_CHECKLIST_P4_V1.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 1) Scope Confirmation (must all be YES)
- ## 2) Autonomy Envelope Alignment
- ## 5) Human Gate Definition
- ## Final Reminder

Quoted phrases:
- L3: "Title: Sandbox Readiness Checklist — Phase-4 (v1)"
- L6: "GOVERNANCE CHECKLIST — NOT A RUNTIME APPROVAL"
- L17: "- [ ] Alleen pilot-artefacts (geen canon, geen productie)"
- L31: "- [ ] Culture / safety / glossary impact → Human Gate"
- L62: "## 5) Human Gate Definition"
- L65: "- [ ] Criteria wanneer Human Gate wordt geroepen vastgelegd"
- L66: "- [ ] Besluiten worden gelogd in governance-artefact"
- L70: "Human Gate not defined → NO-GO"
- L103: "Een aparte governance-notitie moet expliciet “GO” zeggen"

## docs/AGENTS.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Mustikarasa Agents
- ## Translation Quality Agent
- ## Readability Editor
- ## Fidelity Agent
- ## Orchestrator
- ## Cultural-Historical Editor
- ## Book Structure Agent
- ## Annotation Agent
- ## Recipe Editor
- ## Table Editor
- ## Image Agent
- ## Cohesion Agent (historisch: Continuity Agent)
- ## Challenger Agent
- ## Design Agent (voorheen: Layout Agent)
- ## Cohesion Agent (historisch: Continuity Agent) — continuity prompt
- ## Repository Archivist / Documentation Admin
- ## Methodology & Accountability Archivist
- ## Technical Strategy Advisor
- ## Incident & Resilience (Troubleshooting) Agent
- ## Template Agent
- ## Glossary / Terminology Agent
- ## Research / Historical Knowledge Agent

Quoted phrases:
- L3: "Dit document geeft een overzicht van de agents in de multi-agent workflow"
- L15: "- Governance-stop: ambiguïteit met mogelijke betekenisverschuiving."
- L24: "- Governance-stop: conflict met Fidelity of Glossary-richtlijnen."
- L33: "- Governance-stop: blijvende discrepantie na hercontrole."
- L40: "- Kernverantwoordelijkheid: workflow-coördinatie, agents aansturen, templates en governance bewaken."
- L41: "- De Orchestrator is geen inhoudelijke eindbeslisser; terminologie/publicatie gaat via mens en/of meta-agents met human gate."
- L45: "- Governance-stop: Troubleshooting + Methodology voor incident/proceslog."
- L46: "- Hard-stop: governance-conflicten die niet oplosbaar zijn."
- L54: "- governance-stop on high-risk cultural/structural issues"
- L55: "- human-gate only for high-impact / governance conflicts"
- L63: "- governance-stop on high-risk cultural/structural issues"
- L64: "- human-gate only for high-impact / governance conflicts"
- L72: "- governance-stop on high-risk cultural/structural issues"
- L73: "- human-gate only for high-impact / governance conflicts"
- L81: "- governance-stop on high-risk cultural/structural issues"
- L82: "- human-gate only for high-impact / governance conflicts"
- L90: "- governance-stop on high-risk cultural/structural issues"
- L91: "- human-gate only for high-impact / governance conflicts"
- L99: "- governance-stop on high-risk cultural/structural issues"
- L100: "- human-gate only for high-impact / governance conflicts"
- L108: "- governance-stop on high-risk cultural/structural issues"
- L109: "- human-gate only for high-impact / governance conflicts"
- L117: "- governance-stop on high-risk cultural/structural issues"
- L118: "- human-gate only for high-impact / governance conflicts"
- L126: "- governance-stop on high-risk cultural/structural issues"
- L127: "- human-gate only for high-impact / governance conflicts"
- L135: "- governance-stop on high-risk cultural/structural issues"
- L136: "- human-gate only for high-impact / governance conflicts"
- L141: "- Type: governance/support"
- L142: "- Triggers: groei in docs, nieuwe fases (Phase-3 pilots), CONSOLIDATION_AUDIT."
- L150: "- nieuwe workflow of procesvariant;"
- L156: "Runtime integration design: see docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L171: "Runtime integration design: see docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L186: "Runtime integration design: see docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L192: "- Governance-stop: herstelpad en voorwaarden voor veilig vervolg."
- L231: "Ontwerpt en bewaakt output-templates voor alle workflows."
- L246: "Zie docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md."
- L249: "Runtime integration design: see docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L255: "- Governance-stop: Glossary Decision Lifecycle + Methodology-log."
- L266: "Runtime integration design: see docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L270: "- Governance-stop: tegenstrijdige archiefbewijzen."

## docs/AGENT_AUTONOMY_ENVELOPE.md

Preliminary classification suggestion: GOV-B

Relevant section headings:
- # Agent Autonomy Envelope (draft)
- ## Human Gate Mandatory
- ## Clarifying Examples (what “autonomy” means in practice)
- ## Agent Meetings — Exit Rule
- ## Audit Tags (traceability)

Quoted phrases:
- L5: "which require peer-discussion, and which require Human Gate."
- L17: "## Human Gate Mandatory"
- L36: "**Not allowed autonomously (Human Gate required)**"
- L58: "3. **ESCALATE:** Human Gate required (with notes)"
- L83: "[ESCALATE-HUMAN] — Human Gate requested"

## docs/AGENT_PROMPT_PATTERN_P5.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Agent Prompt Pattern — Phase-5 (Concept)
- ### 4. OUTPUT CONTRACT (strikt)
- ### 6. UNCERTAINTY & ESCALATION
- ## 2️⃣ Quality checklist (review vóór gebruik)
- ## 4️⃣ Niet wat dit document doet
- ## 5️⃣ Adoptie (Phase-5)
- ## 6️⃣ Relatie met autonomie & veiligheid

Quoted phrases:
- L1: "# Agent Prompt Pattern — Phase-5 (Concept)"
- L8: "met één duidelijk contract per rol, en zichtbare grenzen rond autonomie & governance."
- L30: "### 4. OUTPUT CONTRACT (strikt)"
- L39: "- soft-stop → governance-stop → Human Gate"
- L61: "| Governance? | Soft-stop / Human Gate expliciet |"
- L80: "- geen nieuwe governance"
- L88: "## 5️⃣ Adoptie (Phase-5)"
- L92: "`compliant / needs-clarification / defer-to-governance`."
- L93: "3. Alleen kleine documentaire tweaks; grotere wijzigingen → governance-review."
- L100: "Lezer-impact → Human Gate."
- L105: "*Concept — Phase-5 tooling document.*"

## docs/AGENT_RUNTIME_HARNESS.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Governance Clarifications (added for safety — documentary only)
- ### Canonical vs Non-Canonical Layers
- ### Moving Proposals Out of the Sandbox
- ### Lifetime of Sandbox Runs
- ### Log Structure
- ### Explicit Human Gate Triggers

Quoted phrases:
- L2: "## Governance Clarifications (added for safety — documentary only)"
- L4: "### Canonical vs Non-Canonical Layers"
- L9: "| OCR restored text | canonical working text | ❌ no |"
- L11: "| Glossary canonical | reference layer | ❌ no |"
- L15: "> **Rule:** If a layer shapes what readers eventually see, it is treated as canonical unless explicitly labeled otherwise."
- L33: "> Missing provenance → **Governance-STOP**."
- L39: "Sandbox runs persist until governance review concludes"
- L58: "governance_notes.log"
- L70: "### Explicit Human Gate Triggers"
- L72: "Human Gate applies when:"

## docs/AGENT_RUNTIME_SAFETY_BRIDGE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Governance Clarifications (added for safety — documentary only)
- ### Canonical vs Non-Canonical Layers
- ### Moving Proposals Out of the Sandbox
- ### Lifetime of Sandbox Runs
- ### Log Structure
- ### Explicit Human Gate Triggers

Quoted phrases:
- L2: "## Governance Clarifications (added for safety — documentary only)"
- L4: "### Canonical vs Non-Canonical Layers"
- L9: "| OCR restored text | canonical working text | ❌ no |"
- L11: "| Glossary canonical | reference layer | ❌ no |"
- L15: "> **Rule:** If a layer shapes what readers eventually see, it is treated as canonical unless explicitly labeled otherwise."
- L33: "> Missing provenance → **Governance-STOP**."
- L39: "Sandbox runs persist until governance review concludes"
- L58: "governance_notes.log"
- L70: "### Explicit Human Gate Triggers"
- L72: "Human Gate applies when:"

## docs/ANNOTATION_STYLECARD_P4.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ### [GLOSSARY_NOTE]
- ## Relationship to governance

Quoted phrases:
- L3: "Title: Annotation Stylecard — Phase-4 Pilots"
- L14: "Geldt voor Phase-4 pilot-werk (sandbox),"
- L55: "- Markeer Human Gate triggers indien lezer-impact."
- L93: "## Relationship to governance"
- L96: "- Bij lezer-impact → Human Gate."

## docs/BACKLOG_ITEM_TEMPLATE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Backlog Item Template (Mustikarasa — Standard)
- ## Governance Alignment
- ## Risk & STOP Triggers
- ## Related Documents

Quoted phrases:
- L4: "**Phase Tag:**"
- L17: "## Governance Alignment"
- L20: "- Human Gate:"
- L25: "Governance-stop if: …"
- L26: "Human Gate if: …"
- L51: "- docs/WORKFLOW.md"

## docs/CANONICAL_INDEX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Canonical Index — What is “Source of Truth” here?
- ## Canonical Decision Records (Phase-7 onward)
- ### 2026

Quoted phrases:
- L1: "# Canonical Index — What is “Source of Truth” here?"
- L4: "(canonical) en waarom — zonder structuur aan te passen."
- L6: "Canonical docs (bron voor besluiten):"
- L10: "- docs/WORKFLOW.md"
- L13: "- docs/10-governance/*  (policies, human gate, rollback, incident)"
- L16: "- canonical docs worden niet “stilletjes aangepast”"
- L17: "- conflicten worden opgelost door canonical + uitleg"
- L18: "- wijzigingen zijn traceable en human-gated"
- L24: "## Canonical Decision Records (Phase-7 onward)"
- L26: "This index will begin filling during Phase-7."
- L27: "Each canonical entry will:"
- L38: "- id: P7_CANONICAL_GLOSSARY_LOBAK_001"
- L45: "decision_record: docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSORY_LOBAK_001.md"
- L49: ""lobak" is canoniek opgenomen als glossary-lemma (itemisation only);"

## docs/CAPABILITY_AGENT_MAP.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Capability → Agent Mapping
- ## 1. Purpose
- ## 3. Capability Categories
- ## 4. Mapping Table (kernstuk)
- ## 7. Impact on Phase-3
- ## 8. Appendix

Quoted phrases:
- L4: "Scope: documentary — no behavioural authority"
- L5: "Changes allowed: via normal governance only"
- L10: "waar overlap zit, en waar gaten in het systeem bestaan."
- L23: "- Governance capabilities"
- L24: "- Workflow/Operational capabilities"
- L42: "| Governance orchestration & escalation | Orchestrator | Methodology & Accountability Archivist, Incident & Resilience Agent | Orchestrator bewaakt flow; governance agents signaleren. |"
- L46: "| Template governance & format compliance | Template Agent | Orchestrator | Template-structuren bewaken, geen inhoud. |"
- L47: "| Workflow orchestration & handoff | Orchestrator | Challenger Agent, Cohesion Agent | Workflow-coördinatie en samenhang. |"
- L50: "| Glossary proposal generation | Glossary / Terminology Agent | Research / Historical Knowledge Agent | Proposals only; geen canonieke besluiten. |"
- L65: "## 7. Impact on Phase-3"
- L68: "glossary-proposals en onderzoek (geen canonieke beslissingen)."
- L77: "- docs/10-governance/"
- L78: "- docs/PHASE3_FRAMING.md"

## docs/CHAPTER_BATCH_WORKFLOW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Chapter / Batch Workflow Design
- ## Scope
- ## Governance Touchpoints
- ## Audit Trail
- ## Alignment

Quoted phrases:
- L1: "# Chapter / Batch Workflow Design"
- L9: "- Alleen ontwerp & governance — geen runtime implementatie"
- L23: "## Governance Touchpoints"
- L25: "- Governance-agents worden automatisch geraadpleegd bij triggers zoals in WORKFLOW.md."
- L26: "- STOP → governance-stop → human gate geldt per item en kan batch-breed escaleren als"
- L39: "- per batch: batch-ID, itemlijst, samenvatting, exceptions, governance-notities"
- L48: "- docs/WORKFLOW.md"
- L49: "- docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md"

## docs/CODEX_META_PROMPT.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Codex Meta-Orchestrator — Mustikarasa (Authoritative Version)
- ### Template Agent (governance)
- ### Handover Agent (sessions)
- ## Phase-4 Runtime Guidance (CrewAI + Mistral)
- ### When to use the runner
- ### Terminal-coach rule (MANDATORY)
- ### Never do
- ## Phase-5 Repository Orientation (Manifest-aware)
- ## Phase-5 Meta Behavior — Consult Before Asking

Quoted phrases:
- L22: "(governance, klusjes, stabiliteit, planning)"
- L158: "- workflow instabiel is"
- L192: "### Template Agent (governance)"
- L218: "(bijv. afronding van PHASE-1, start van PHASE-2)."
- L227: "## Phase-4 Runtime Guidance (CrewAI + Mistral)"
- L232: "- scope is Phase-4 sandbox (no publication),"
- L257: "- help evaluate JSON + governance stops,"
- L270: "- Never skip Human Gate items when scope is unclear."
- L274: "## Phase-5 Repository Orientation (Manifest-aware)"
- L279: "(menselijke kaart — wat is canonical, wat sandbox, wat consolidatie)"
- L286: "1) Canonical → bron voor beslissingen"
- L288: "3) Phase-5 docs → uitleg, consolidatie, voorbereiding (niet uitvoerend)"
- L292: "- verander geen prompts, scripts of governance-bestanden"
- L293: "zonder dat dit expliciet is vastgelegd én human-gated is"
- L302: "en blijven binnen het Phase-5 “consolidation first” kader."
- L306: "## Phase-5 Meta Behavior — Consult Before Asking"
- L311: "- CANONICAL_INDEX.md"
- L324: "- or genuine governance ambiguity."
- L333: "while preserving governance boundaries."

## docs/CODEX_SESSION_LOG.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Codex Session Log – Mustikarasa
- ### SESSION — Phase-6 Low-risk Migration (navigation docs)
- ### SESSION — Workflow Naming Alignment
- ## [2026-01-06] CASE-01 — pre-flight attempt (excerpt-aware runner)
- ## [2026-01-06] CASE-01 — first excerpt-aware runner execution
- ## [2026-01-06] CASE-01 — first successful excerpt-aware sandbox run
- ## [2026-01-06] CASE-01 — first run with refined runner payload
- ## [2026-01-12] CASE-02 — excerpt locked (design)
- ### P6 — Human Review Workflow Defined
- ### P6 — First Human Review Simulation Completed

Quoted phrases:
- L9: "- 2026-01-02 – SYSTEM_ORCHESTRATOR_MANDATE: mandaat en grenzen vastgelegd in prompts/orchestrator.md, docs/AGENTS.md en docs/WORKFLOW.md; TODO afgevinkt."
- L10: "- 2026-01-02 – SYSTEM_GLOSSARY_DECISION_LIFECYCLE: lifecycle vastgelegd in docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md en gekoppeld in prompts en docs; TODO afgevinkt."
- L11: "- 2026-01-02 – SYSTEM_GOVERNANCE_TRIGGERS: triggers vastgelegd in prompts en docs; artefacten en escalatiepad benoemd; TODO afgevinkt."
- L12: "- 2026-01-02 – SYSTEM_AGENT_STOP_CRITERIA: autonomy/stop-model vastgelegd in prompts en docs; human gate expliciet; TODO afgevinkt."
- L13: "- 2026-01-02 – SYSTEM_GOVERNANCE_TESTS: governance testplan opgesteld en gekoppeld aan workflow; TODO afgevinkt."
- L15: "ID: PHASE2_BACKLOG_CREATED"
- L16: "Summary: PHASE-2 roadmap geregistreerd in CODEX_TODO.md (nog geen uitvoering)."
- L22: "ID: P7_CANONICAL_TRAIL_REHEARSAL_LOBAK_001"
- L23: "Actor: Codex-Phase7"
- L25: "- Phase-7 kicked off (canonical decision trails)."
- L26: "- Created P7_DECISION_TYPES.md and P7_CANONICAL_TRAIL_SPEC.md (draft, v1)."
- L27: "- Added Human Review Participation Model to P6_HUMAN_REVIEW_WORKFLOW.md and P7_CANONICAL_TRAIL_SPEC.md."
- L28: "- Designed and executed P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md using LOBAK Case-02 (excerpt_id lobak_034_048)."
- L31: "Documentary lifecycle rehearsal only; no real canonical decisions were made."
- L37: "ID: TODO_PHASE_STRUCTURE_APPLIED"
- L38: "Summary: PHASE-1 (foundations) expliciet gemaakt; PHASE-2 roadmap blijft onafhankelijk en open."
- L39: "Impact: backlog nu chronologisch en governance-consistent."
- L42: "- 2026-01-02 – STOP: TODO phase-structuur niet toegepast; PHASE-2 Roadmap sectie/PHASE2_* items ontbreken in docs/CODEX_TODO.md, dus herstructurering is ambigu."
- L45: "Summary: Handover Agent ontworpen en geregistreerd (prompt, AGENTS, Orchestrator, CODEX_META_PROMPT, WORKFLOW, total_project)."
- L50: "ID: PHASE2_TODO_REALITY_SYNC"
- L56: "ID: PHASE2_TODO_REALITY_SYNC_COMPLETED"
- L57: "Summary: Marked PHASE2_TODO_REALITY_SYNC as completed and annotated with reference."
- L62: "ID: PHASE2_AGENT_AUTONOMY_COMPLETION"
- L64: "Impact: consistent governance-gedrag over de volledige redactie-pipeline."
- L68: "ID: PHASE2_CHAPTER_BATCH_WORKFLOW_DESIGN"
- L69: "Summary: Ontwerpdocument voor batch/hoofdstuk workflow toegevoegd en gekoppeld aan WORKFLOW.md."
- L74: "ID: PHASE2_GOVERNANCE_AGENT_RUNTIME_INTEGRATION_DESIGN"
- L75: "Summary: Governance-agent runtime-integratie beschreven in GOVERNANCE_INTEGRATION_DESIGN.md en gekoppeld aan WORKFLOW/AGENTS."
- L80: "ID: PHASE2_GLOSSARY_RESEARCH_PILOT"
- L82: "Impact: valideert lifecycle en workflow zonder definitieve glossary-wijzigingen."
- L86: "ID: PHASE2_GOVERNANCE_TEST_SCENARIO_1"
- L87: "Summary: Governance-testsessie uitgevoerd met gesimuleerd incident; soft-stop/governance-stop functioneren documentair."
- L88: "Impact: bevestigt dat governance-ontwerp werkbaar is zonder runtime-wijzigingen."
- L92: "ID: GOVERNANCE_TEST_SCENARIO_2_PARTIAL_BATCH_FAILURE"
- L93: "Summary: Governance-testscenario 2 beschreven: partial batch failure met soft-stop/governance-stop en geïsoleerd incident."
- L94: "Impact: bevestigt dat batch-workflow en governance-model samengaan zonder onnodige batch-stops."
- L98: "ID: PATCH_GOVERNANCE_INTEGRATION_FAILURE_MODES"
- L99: "Summary: Failure modes & safeguards expliciet toegevoegd aan GOVERNANCE_INTEGRATION_DESIGN om checklist “Partial” te sluiten."
- L106: "Impact: geeft feitelijke basis voor PHASE-3 planning en cleanup."
- L134: "ID: CONSOL_PHASE2_HEADER_STATE_APPLIED"
- L135: "Summary: PHASE-2 koptekst in docs/CODEX_TODO.md aangepast van “not started yet” naar een feitelijke ‘in progress’-formulering; bijbehorende consolidatietaak op done gezet."
- L136: "Impact: voorkomt misinterpretatie van de PHASE-2 status bij lezing van CODEX_TODO."
- L141: "Summary: Requirements-change governance vastgelegd in REQUIREMENTS_CHANGE_PROCESS.md; proces beschrijft rollen, templates, Human Gate en logging."
- L147: "Summary: Applied requirement ASR-005 prohibiting automatic glossary updates without Human Gate + rollback."
- L148: "Impact: strengthens glossary governance; aligns runtime behaviour with lifecycle principles."
- L153: "Summary: Added ASR-006 requiring governance-stop whenever an incident is raised."
- L160: "Impact: increases robustness of batch workflows and reduces risk of large-scale accidental losses."
- L165: "Summary: Vision & Strategy vastgelegd voor het Mustikarasa-project, inclusief driefasen-strategie, centrale traceability-principe, governance- en red-teamrol en een Definition of Done die fouten expliciet benoemd en logbaar maakt."
- L166: "Impact: biedt een helder kompas boven requirements en workflows; maakt toekomstige ontwerp- en runtime-beslissingen toetsbaar aan een expliciete visie."
- L170: "ID: PHASE3_FRAMING_ADDED"
- L171: "Summary: Phase-3 framing document toegevoegd en gekoppeld aan workflow (documentair — geen runtime-wijzigingen)."
- L176: "ID: PHASE3_FRAMING_STABILIZED"
- L177: "Summary: PHASE-3 framing document formeel vastgesteld als strategische baseline (v1); wijzigingen voortaan via change-proces."
- L178: "Impact: creëert een duidelijke referentie voor pilots, governance en toekomstige ontwerpbeslissingen."
- L182: "ID: PHASE3_PILOT_GLOSSARY_LOBAK_CREATED"
- L196: "Impact: validates glossary lifecycle and governance reaction to terminology ambiguity without changing any production artefacts."
- L208: "Impact: validates governance handling of intentional divergence without changing canonical artefacts; rollback documented in pilot file."
- L237: "Rollback: delete the “Methodology Insight (Phase-3 — Proposal)” section added to docs/PILOT_GLOSSARY_LOBAK_RUN_P3_LOBAK_002.md."
- L244: "Rollback: delete the Consolidation Summary block, the CONSOLIDATION_AUDIT_01 entry, and the PHASE3 proposal line in CODEX_TODO."
- L248: "Summary: OCR technical-only pilot documented on a sandbox excerpt; no canonical edits."
- L258: "Rollback: delete the “Methodology Insight — “²” Marker (Phase-3 — Proposal)” section from docs/PILOT_OCR_RESTORE_RUN_P3_OCR_RESTORE_001.md."
- L265: "Rollback: delete the Consolidation Summary block, the CONSOLIDATION_AUDIT_01 entry, and the PHASE3 proposal line in CODEX_TODO."
- L281: "Summary: Verwijzing naar governance testdocument in CODEX_TODO.md gecorrigeerd naar GOVERNANCE_TEST_SCENARIO_1.md."
- L282: "Impact: voorkomt verwarring rond governance testdocumenten."
- L293: "Summary: Governance-triggerlijst in WORKFLOW.md uitgebreid met expliciete Glossary- en Research-triggers."
- L294: "Impact: workflow-document maakt nu duidelijk wanneer deze agents automatisch worden geraadpleegd."
- L299: "Summary: Eerste versie van docs/REQUIREMENTS.md aangemaakt, met afgeleide functionele, non-functionele, governance- en safety-eisen."
- L300: "Impact: maakt expliciete, herleidbare requirements zichtbaar als basis voor toekomstige PHASE-3 ontwerp- en runtime-beslissingen."
- L304: "ID: PHASE3_DOCS_REORG_MOVE_GOVERNANCE_PILOT"
- L305: "Summary: Small-scope docs reorganisation pilot executed for governance documents, following DOCS_INFORMATION_ARCHITECTURE; references updated, no code or prompts touched."
- L306: "Impact: Validates the reorganisation approach on a limited scope and keeps governance docs discoverable and consistent."
- L312: "Summary: Imported governed legacy OCR subset (RB samples + canonical context) into sandbox/legacy_imports with provenance headers."
- L313: "Impact: adds read-only research assets for Phase-3 OCR/"²" analysis; no canonical text changed."
- L315: "Rollback: delete sandbox/legacy_imports/* and remove the PHASE3 legacy import reminder from docs/CODEX_TODO.md."
- L321: "Impact: documents real-world distortion patterns for governance review without applying any normalization."
- L369: "Impact: documentary only; shows escalation and Human Gate discussion without text edits."
- L383: "ID: P3_GOVERNANCE_SYNTHESIS_001"
- L384: "Summary: Created Phase-3 synthesis doc for OCR ambiguity governance (no policy changes)."
- L387: "Rollback: delete docs/PHASE3_GOVERNANCE_SYNTHESIS_OCR_AMBIGUITY.md."
- L471: "ID: P3_WORKFLOW_SYNTHESIS_001"
- L472: "Summary: Created workflow synthesis pilot (documentary only)."
- L475: "Rollback: delete docs/PILOT_WORKFLOW_SYNTHESIS_RUN_P3_WORKFLOW_001.md."
- L479: "ID: P3_WORKFLOW_SYNTHESIS_001_CONSOLIDATION"
- L480: "Summary: Consolidated workflow synthesis pilot (documentary only)."
- L487: "ID: P3_WORKFLOW_MAP_001"
- L488: "Summary: Created documentary workflow map for ambiguity governance (Phase-3)."
- L491: "Rollback: delete docs/PILOT_WORKFLOW_MAP_RUN_P3_WORKFLOWMAP_001.md."
- L495: "ID: P3_WORKFLOW_MAP_001"
- L496: "Summary: Updated workflow map pilot with annotations, pilot notes, and risks (documentary only)."
- L499: "Rollback: delete docs/PILOT_WORKFLOW_MAP_RUN_P3_WORKFLOWMAP_001.md."
- L503: "ID: P3_WORKFLOW_MAP_001_CONSOLIDATION"
- L504: "Summary: Consolidated workflow map pilot (documentary only)."
- L512: "Summary: Governance failure drill — simulated glossary decision leak."
- L520: "Summary: Consolidated governance failure-drill (documentary only)."
- L616: "Summary: Phase-3 readiness reflection recorded (no decisions)."
- L619: "Rollback: delete docs/PHASE3_READINESS_REVIEW.md."
- L624: "Summary: Phase-4 readiness constraints captured (documentary only)."
- L627: "Rollback: delete docs/PHASE4_READINESS_NOTES.md."
- L632: "Summary: Added documentary Phase-3 status clarification."
- L635: "Rollback: delete the addendum block in docs/PHASE3_FRAMING.md."
- L640: "Summary: Appended structured Phase-4.1 agent-runtime backlog items."
- L648: "Summary: Created docs/BACKLOG_ITEM_TEMPLATE.md for standardized Phase-4 backlog items."
- L656: "Summary: Appended detailed backlog entry for PHASE4_AGENT_HARNESS_SPEC."
- L664: "Summary: Added governance clarification appendix to bridge + harness docs."
- L673: "Scope: Phase4-design-review (read-only)"
- L681: "Artifact: PHASE4_CLARIFICATION_PACKET_(sandbox)"
- L689: "Artifact: PHASE3_REFLECTION_(sandbox)"
- L744: "Note: governance incident drill — simulation only"
- L751: "Note: Phase3 consolidation memo — documentary only"
- L806: "Actor: Codex-Phase3Audit"
- L807: "Note: phase-3 completeness audit — documentary only"
- L814: "Note: phase-4 readiness brief — documentary only"
- L821: "Note: drafting phase-4 experiment protocol — documentary only"
- L833: "ID: HUMAN_GATE_SUMMARY_001"
- L834: "Actor: Codex-HumanGateSummary"
- L835: "Note: human gate criteria summary — documentary only"
- L840: "ID: GOVERNANCE_HANDOVER_NOTE_001"
- L842: "Note: governance handover note prepared — documentary only"
- L856: "Summary: Added docs/PILOT_TO_PRACTICE_GUIDE.md (documentary Phase-3 learnings)."
- L868: "Source: DERIVED/step4_structure/index/canonical_concat.txt"
- L872: "Note: No modifications were made to canonical_concat.txt."
- L947: "Impact: standardizes post-rehearsal capture without implying governance decisions."
- L974: "Summary: Sandbox readiness checklist documented for Phase-4 governance (no runtime approval)."
- L975: "Impact: provides a formal pre-run safety gate without authorizing execution."
- L981: "Summary: Incident playbook for Phase-4 sandbox documented (safety procedure only)."
- L987: "ID: HUMAN_GATE_POLICY_P4_SANDBOX_CREATED"
- L988: "Summary: Human Gate policy for Phase-4 sandbox documented (governance only, no run approval)."
- L1002: "Summary: Safety refinements added to Sayur GO/NO-GO proposal (manual gating, Human Gate presence, run-ID controls)."
- L1009: "Summary: Annotation stylecard for Phase-4 pilots documented (guideline only)."
- L1016: "Summary: Pilot-set v1 for Phase-4 sandbox preparation documented (planning only)."
- L1030: "Summary: GO/NO-GO evaluation form for Phase-4 sandbox documented (decision support only)."
- L1040: "Human Gate: active"
- L1064: "Impact: formalizes governance decision request without authorizing execution."
- L1071: "Impact: structures governance review without authorizing execution."
- L1077: "Phase: P4 sandbox"
- L1086: "Action: paused — awaiting Human Gate clarification"
- L1093: "Rationale: glossary ambiguity requires Human Gate review first"
- L1159: "- No governance incidents"
- L1182: "- No governance incidents"
- L1185: "### SESSION — Phase-6 Low-risk Migration (navigation docs)"
- L1194: "### SESSION — Workflow Naming Alignment"
- L1195: "We renamed P6_SAYUR_MINI_EDITORIAL_WORKFLOW → P6_EDITORIAL_WORKFLOW_MINI."
- L1196: "Reason: workflow is generic; SAYUR is merely Case-01."
- L1201: "Summary: Applied excerpt-binding spec documentair in Phase-6 workflows en pilot-evaluaties (excerpt-metadata subsections toegevoegd; generieke mini-workflow hernoemd naar een niet-SAYUR-specifieke titel; bestaande logs niet aangepast)."
- L1202: "Impact: excerpt-metadata is nu vastgelegd als documentair vereiste in workflows/templates; de generieke mini-workflow is duidelijk losgekoppeld van SAYUR; oude runs blijven historisch correct, toekomstige runs moeten excerpt_id/source/version registreren."
- L1204: "Rollback: herstel de titelwijziging in P6_EDITORIAL_WORKFLOW_MINI.md, verwijder de nieuwe excerpt-metadata subsections uit P6_EDITORIAL_WORKFLOW_MINI.md, P6_WORKFLOW_SAYUR_MINI.md en de drie pilot-evaluaties, verwijder de verwijzing naar P6_EXCERPT_BINDING_SPEC in de pilot-synthesis, en zet PHASE6_EXCERPT_BINDING_SPEC terug op [ ] in CODEX_TODO.md."
- L1209: "Summary: Created P6_EXCERPT_BINDING_INTEGRATION_PLAN.md documenting how excerpt_id/source/version propagate across plans, configs (design), logs, JSON artefacts, evaluations, and session logs; no runtime or prompt changes."
- L1210: "Impact: Excerpt-binding now has an explicit integration map and checklist for Phase-6; historical runs remain unchanged."
- L1212: "Rollback: remove docs/P6_EXCERPT_BINDING_INTEGRATION_PLAN.md and revert PHASE6_EXCERPT_BINDING_INTEGRATION_PLAN to [ ] in CODEX_TODO.md."
- L1233: "Summary: Created P6_LOBAK_CASE02_EXCERPT_SELECTION.md (draft governing excerpt doc with placeholders) and P6_LOBAK_INTERNAL_WORK_CASE02.md (Case-02 workflow file) for a non-SAYUR generic mini-workflow application; no runs authorized."
- L1241: "Summary: Defined LOBAK Case-02 as a generic Phase-6 mini-workflow case with excerpt-binding placeholders (case file + governing excerpt skeleton), without executing or authorizing any runs."
- L1242: "Impact: Establishes a non-SAYUR workflow case wired for excerpt-binding from the start while keeping it pending until a human selects the actual LOBAK excerpt and an excerpt-aware runner is implemented and approved."
- L1249: "Summary: Moved DOCS_INFORMATION_ARCHITECTURE.md into docs/navigation/ as part of low-risk navigation cleanup; updated references where appropriate. No canonical or workflow content changed."
- L1250: "Impact: Improves navigation discoverability without changing governance or editorial artefacts."
- L1257: "Summary: Moved P6_MIGRATION_CANDIDATE_LIST.md into docs/navigation/ as a navigation/overview document; updated references where appropriate. No case-files or canonical content were moved."
- L1258: "Impact: Slightly improves Phase-6 navigation clarity for migration planning without changing governance or workflow semantics."
- L1264: "ID: PHASE6_ADDENDUM_COPY_001"
- L1271: "ID: PHASE6_ADDENDUM_COPY_GOVERNANCE"
- L1272: "Summary: Copied governance + review docs into docs/addendum/ (documentary only)."
- L1273: "Impact: improves excerpt-aware workflow review + human-gate traceability."
- L1279: "- context: First attempt to run the excerpt-aware workflow for Case-01 (SAYUR, excerpt_id = sayur_052_066) after marking Case-01 as validation-ready."
- L1283: "python sandbox/crew/run_excerpt_workflow.py \"
- L1293: "/Users/vwvd/Millway/AI-folder/Crew-AI/sandbox/crew/run_excerpt_workflow.py: [Errno 2] No such file or directory"
- L1297: "this is a precondition failure (runner not implemented), not a workflow failure."
- L1305: "keep PHASE6_IMPLEMENT_EXCERPT_AWARE_RUNNER as the explicit next action."
- L1314: "- excerpt metadata propagated correctly into the log header."
- L1332: "- runner: `python sandbox/crew/run_excerpt_workflow.py --config sandbox/crew/shakedown_sayur_mistral.yaml ...`"
- L1353: "- This is acceptable for Phase-6 validation (excerpt-awareness + layout), but may be"
- L1362: "- runner: `run_excerpt_workflow.py` with `sandbox/crew/shakedown_sayur_mistral.yaml`"
- L1375: "- The refined payload contract (raw_output + payload field) is now in effect."
- L1389: "- 2026-01-06 — Phase-6 Case-02 LOBAK shakedown-run (excerpt-aware)"
- L1390: "- command: python sandbox/crew/run_excerpt_workflow.py --excerpt-id lobak_034_048 --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md --excerpt-version locked-2026-01-12 --config sandbox/crew/configs/lobak_case02.yaml"
- L1401: "- 2026-01-06 — Phase-6 Case-02 config created"
- L1409: "- 2026-01-06 — Phase-6 Case-02 LOBAK shakedown-run #2 (excerpt-aware)"
- L1410: "- command: python sandbox/crew/run_excerpt_workflow.py --excerpt-id lobak_034_048 --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md --excerpt-version locked-2026-01-12 --config sandbox/crew/configs/lobak_case02.yaml"
- L1421: "- 2026-01-06 — Phase-6 Case-02 LOBAK shakedown-run #3 (excerpt-aware, annotator+challenger)"
- L1422: "- command: python sandbox/crew/run_excerpt_workflow.py --excerpt-id lobak_034_048 --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md --excerpt-version locked-2026-01-12 --config sandbox/crew/configs/lobak_case02.yaml"
- L1435: "- payload is null, with JSON parse warning in the log (expected per Phase-6 runner refinement design)"
- L1437: "- 2026-01-06 — Phase-6 Case-02 LOBAK shakedown-run #3 (excerpt-aware, annotator+challenger)"
- L1438: "- command: python sandbox/crew/run_excerpt_workflow.py --excerpt-id lobak_034_048 --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md --excerpt-version locked-2026-01-12 --config sandbox/crew/configs/lobak_case02.yaml"
- L1451: "- payload is null, with JSON parse warning (expected under current Phase-6 runner refinement design)"
- L1463: "### P6 — Human Review Workflow Defined"
- L1467: "Added docs/P6_HUMAN_REVIEW_WORKFLOW.md describing lifecycle stages"
- L1468: "(CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL)."
- L1469: "Clarifies human-only final authority and rollback rules."
- L1476: "Reviewed LOBAK Case-02 annotator output using the Phase-6 human review lane."
- L1479: "No canonisation performed; output promoted only to READY_FOR_HUMAN_REVIEW."
- L1482: "ID: P7_CANONICAL_TRAIL_REHEARSAL_LOBAK_001"
- L1483: "Actor: Codex-Phase7"
- L1485: "- Phase-7 kicked off (canonical decision trails)."
- L1486: "- Created P7_DECISION_TYPES.md and P7_CANONICAL_TRAIL_SPEC.md (draft, v1)."
- L1487: "- Added Human Review Participation Model to P6_HUMAN_REVIEW_WORKFLOW.md and P7_CANONICAL_TRAIL_SPEC.md."
- L1488: "- Designed and executed P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md using LOBAK Case-02 (excerpt_id lobak_034_048)."
- L1491: "Documentary lifecycle rehearsal only; no real canonical decisions were made."
- L1498: "ID: P7_CANONICAL_GLOSSARY_LOBAK_001"
- L1499: "Actor: HumanGate-Editorial"
- L1501: "- Eerste echte Phase-7 canonical decision uitgevoerd."
- L1502: "- "lobak" canoniek gemarkeerd als glossary-lemma (itemisation only, geen betekenis/vertaling)."
- L1504: "docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSARY_LOBAK_001.md"
- L1505: "- CANONICAL_INDEX.md uitgebreid met één entry voor deze beslissing."
- L1508: "- Laat betekenissen en vertalingen expliciet open voor latere, afzonderlijke canonical decisions."
- L1511: "- Maak een nieuw canonical decision record met supersedes: P7_CANONICAL_GLOSSARY_LOBAK_001"
- L1512: "en update CANONICAL_INDEX.md zodat alleen het nieuwe record als actief wordt gezien."
- L1516: "ID: P7_PHASE_CLOSE"
- L1517: "Actor: HumanGate-Editorial"
- L1519: "- Phase-7 closed."
- L1520: "- Canonical decision trail designed, rehearsed, and validated via the first real pilot (“lobak” lemma)."
- L1523: "- Canonical decision trails are stable and ready for broader editorial use."
- L1529: "Summary: Editorial capabilities vastgelegd als inhoudelijke basis voor vertaal- en annotatiebeslissingen (los van tools en governance)."
- L1530: "Impact: Verankert redactioneel vakmanschap als primaire norm; techniek en governance worden ondersteunend gepositioneerd."
- L1563: "ID: HANDOVER_PHASE8_WOENSDAGAVOND"
- L1564: "Summary: Read-only handover-bundle samengesteld met kern-documenten voor Phase-8 vervolg in nieuwe ChatGPT-sessie."
- L1565: "Impact: Nieuwe sessie kan instappen met volledig redactioneel, canoniek en execution-aware context."
- L1572: "- Phase-8 — Meaning Preservation: eerste echte agent-run uitgevoerd."
- L1574: "- Artefacten: sandbox/phase8_runs/P8_RUN_20260108_112252/ (command.txt, env.txt, logs/run.log, outputs/final.txt, eval/PHASE8_CAPABILITY_EVAL.md, eval/output_contract_checks.txt)."
- L1576: "- Bevindingen (feitelijk): meaning-drift (“half-soft” → “zacht”); output-contract niet afgedwongen; rolafbakening agent/runner onvoldoende."
- L1577: "- Afgeleide acties: TODO PHASE8_OUTPUT_CONTRACT_AND_ROLE_ENFORCEMENT aangemaakt; subtask PHASE8_OUTPUT_CONTRACT_VALIDATOR_SCRIPT uitgevoerd (FAIL expected)."
- L1578: "- Related TODO: PHASE8_FIRST_REAL_AGENT_PILOT (done in CODEX_TODO.md)"
- L1579: "- Validator script: sandbox/tools/phase8_output_contract_validator.sh"
- L1580: "- Validator report: sandbox/phase8_runs/P8_RUN_20260108_112252/eval/output_contract_checks.txt"
- L1581: "Impact: Phase-8 pilot blijft provisioneel; run-artefacten en evaluatie zijn sandbox-only."
- L1593: "ID: PHASE8_OUTPUT_CONTRACT_GATE_PROCEDURE_SET"
- L1594: "Summary: Phase-8 output-contract enforcement gate vastgelegd als procedurele verplichting (validator verplicht; geen technische hook)."
- L1595: "Impact: Versterkt Phase-8 output-controle zonder scope-uitbreiding of runtime-wijzigingen."
- L1600: "ID: PHASE8_OUTPUT_CONTRACT_V2_ESTABLISHED"
- L1602: "- output-contract v2 vastgesteld"
- L1603: "- validator + gate geïmplementeerd en getest op FAIL-cases"
- L1605: "Impact: Phase-8 technisch stabiel, inhoudelijk nog niet afgesloten."
- L1610: "ID: PHASE8_CLOSEOUT"
- L1612: "- Phase-8 afgerond (COMPLETED — REWORK ACCEPTED)."
- L1613: "- validator en gate functioneren correct; FAIL-signalen zijn inhoudelijk juist."
- L1614: "- geen auto-repair toegepast (bewuste governance-keuze)."
- L1615: "Impact: Phase-8 formeel gesloten; output-contract v2 blijft leidend."
- L1620: "ID: PHASE8_CLOSEOUT_CONFIRMED"
- L1621: "Summary: Phase-8 formeel afgesloten als COMPLETED — REWORK ACCEPTED."
- L1622: "Impact: Output-contract v2 + validator/gate opgeleverd; FAIL-runs zijn leerzaam en geborgd; geen PASS-run afgedwongen."
- L1623: "Evidence: sandbox/tools/phase8_output_contract_validator.sh, sandbox/tools/phase8_run_with_gate.sh, README_HANDOVER.md"
- L1629: "Summary: Phase-9 micro-pilot uitgevoerd: alleen Fidelity prompt aangescherpt voor output-format discipline; validator/gate onveranderd; geen auto-repair."
- L1630: "Impact: contract-compliance getest via gate-resultaat (PASS of FAIL) zonder policy-wijziging."
- L1633: "- sandbox/phase9_runs/P9_RUN_20260108T131653/command.txt"
- L1634: "- sandbox/phase9_runs/P9_RUN_20260108T131653/env.txt"
- L1635: "- sandbox/phase9_runs/P9_RUN_20260108T131653/logs/run.log"
- L1636: "- sandbox/phase9_runs/P9_RUN_20260108T131653/eval/output_contract_checks.txt"
- L1641: "ID: P9_OUTPUT_CONTRACT_VALIDATOR_BUGFIX_001"
- L1642: "Summary: Fixed Phase-8 output-contract validator Check C: replaced unreliable line-counting of multiline rg evidence with occurrence counting for the separator pattern; validator now correctly detects PASS when '\\n\\nOpmerkingen:' is present exactly once."
- L1643: "Impact: Output-contract gate/validator is now reliable for newline-based separator matching; no auto-repair introduced; no content/prompt/governance changes."
- L1645: "- sandbox/tools/phase8_output_contract_validator.sh (Check C section)"
- L1646: "- sandbox/phase9_runs/P9_RUN_20260108T131653/eval/output_contract_checks.txt (overall_status: PASS)"
- L1648: "Rollback: revert the Check C changes in sandbox/tools/phase8_output_contract_validator.sh and delete this SESSION block."

## docs/CODEX_TODO.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # CODEX_TODO — Capability-Driven Index
- ## Governance & Canon Control
- ## Meaning Preservation & Semantic Fidelity
- ## Readability & Editorial Quality
- ## Terminology Stewardship
- ## Cultural-Historical Context & Annotation
- ## Provenance, Traceability & Reproducibility
- ## Agent Runtime, Safety & Orchestration
- # Codex TODO – Mustikarasa
- ## Kern
- ### PHASE-1 Foundations (completed / historic)
- #### System Governance & Architecture
- ### PHASE-2 Roadmap (governed backlog — in progress)
- ### PHASE-3 Documentation Reorganisation (planned)
- ## PHASE4_AGENT_BRIDGE_DESIGN
- ## PHASE4_AGENT_HARNESS_SPEC
- ## PHASE4_AGENT_HARNESS_SPEC (detailed backlog entry)
- ### User Story
- ### Governance Alignment
- ### Risk & STOP Triggers
- ### Non-Functional Considerations
- ### Definition of Ready
- ### Artefacts Touched
- ### Related Documents
- ## PHASE4_AGENT_BRIDGE_DESIGN (detailed backlog entry)
- ## User Story
- ## Context & Intent
- ## Governance Alignment
- ## Risk & STOP Triggers
- ## Acceptance Criteria
- ## Artefacts
- ## Related
- ## Methodology Log
- ## PHASE-5 — Prompt Pattern
- ## PRACTICE — Archivist alignment rhythm
- ### PHASE-6 Workflow & Repo Architecture (planning)
- ## Phase-6 — Clarity & Canon Governance (lightweight)
- ### PHASE6_CASE02_RUNNER_MAPPING — PENDING
- ### Phase-7 — Canonical Decision Trails
- ### Phase-8 — Meaning Preservation (status note)
- ### Phase-9 — Format Discipline (status note)
- ### Capability Mapping Follow-Ups (documentation only)

Quoted phrases:
- L3: "This file is a governance-aware capability index. It is non-operational and preparatory only."
- L5: "## Governance & Canon Control"
- L7: "Governance boundaries, canonical authority, and decision lifecycle integrity."
- L9: "Authority & System Support Envelope"
- L10: "- Authority owner: Governance (system/process)."
- L12: "- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification."
- L14: "- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]"
- L21: "Authority & System Support Envelope"
- L22: "- Authority owner: Human (editorial/historical)."
- L24: "- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification."
- L26: "- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]"
- L31: "Improve clarity and editorial quality without changing meaning or authority."
- L33: "Authority & System Support Envelope"
- L34: "- Authority owner: Human (editorial/historical)."
- L36: "- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification."
- L38: "- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]"
- L45: "Authority & System Support Envelope"
- L46: "- Authority owner: Human (editorial/historical)."
- L48: "- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification."
- L50: "- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]"
- L57: "Authority & System Support Envelope"
- L58: "- Authority owner: Human (editorial/historical)."
- L60: "- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification."
- L62: "- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]"
- L69: "Authority & System Support Envelope"
- L70: "- Authority owner: Governance (system/process)."
- L72: "- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification."
- L74: "- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]"
- L81: "Authority & System Support Envelope"
- L82: "- Authority owner: Governance (system/process)."
- L84: "- System support NOT allowed: deciding canon, asserting finality, silent interpretation shifts, self-modification."
- L86: "- [FUTURE] [CAPABILITY] [REQUIRES_GOVERNANCE]"
- L96: "[ PARKED — Phase-5 ] intentionally deferred (not a bug, just timing)"
- L104: "- [ ] Basis chapter-/batch-workflow ontwerpen (JSON + subcommand) → zie PHASE2_CHAPTER_BATCH_WORKFLOW_DESIGN"
- L105: "- [x] Documentatie voor workflow in docs/WORKFLOW.md (documentatie aanwezig in docs/WORKFLOW.md)"
- L107: "### PHASE-1 Foundations (completed / historic)"
- L115: "#### System Governance & Architecture"
- L122: "Output zal o.a. terechtkomen in prompts/orchestrator.md en (optioneel) docs/WORKFLOW.md."
- L127: "Output in een nieuw document: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md."
- L129: "- [x] SYSTEM_GOVERNANCE_TRIGGERS"
- L137: "Output in een nieuw of bestaand document, bijv. docs/AGENTS.md of docs/WORKFLOW.md."
- L139: "- [x] SYSTEM_GOVERNANCE_TESTS"
- L140: "Ontwerp van een kleine test-suite die governance zelf test:"
- L144: "Output als nieuw document, bijv. docs/10-governance/GOVERNANCE_TESTS_PLAN.md."
- L146: "### PHASE-2 Roadmap (governed backlog — in progress)"
- L148: "- [x] **PHASE2_AGENT_AUTONOMY_COMPLETION** (autonomy model applied across all editorial agents)"
- L149: "Alle actieve redactionele agents krijgen dezelfde “Autonomy / Soft-Stop / Governance-Stop / Human-Gate”"
- L155: "- [x] **PHASE2_TODO_REALITY_SYNC** (completed — aligned TODO with repo; see session PHASE2_TODO_REALITY_SYNC)"
- L160: "- [x] **PHASE2_CHAPTER_BATCH_WORKFLOW_DESIGN** (design documented in CHAPTER_BATCH_WORKFLOW.md)"
- L161: "Ontwerpdocument voor hoofdstuk/batch-workflow (zonder code)."
- L162: "Beschrijft input/output per batch, governance-touchpoints en escalatie op batch-niveau."
- L163: "Output: docs/CHAPTER_BATCH_WORKFLOW.md (+ korte samenvatting in WORKFLOW.md)."
- L165: "- [x] **PHASE2_GOVERNANCE_AGENT_RUNTIME_INTEGRATION_DESIGN** (design documented in GOVERNANCE_INTEGRATION_DESIGN.md)"
- L166: "Ontwerp hoe governance-agents in de Python-runtime worden aangeroepen"
- L168: "Output: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L170: "- [x] **PHASE2_GLOSSARY_RESEARCH_PILOT** (pilot documented — proposals only, no final decisions)"
- L175: "- [x] **PHASE2_GOVERNANCE_TEST_SCENARIO_1** (scenario executed — documentary test)"
- L176: "Eerste concrete uitvoering van een scenario uit GOVERNANCE_TESTS_PLAN.md"
- L178: "Output: docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md."
- L180: "### PHASE-3 Documentation Reorganisation (planned)"
- L182: "- [ PARKED — Phase-5 ] **PHASE3_DOCS_REORG_PLAN_APPROVED**"
- L185: "- [ PARKED — Phase-5 ] **PHASE3_DOCS_REORG_MOVE_PILOTS**"
- L188: "- [ DONE — P4 ] **PHASE3_DOCS_REORG_MOVE_GOVERNANCE** (governance docs moved according to DOCS_INFORMATION_ARCHITECTURE — pilot scope only)"
- L189: "Fysiek verplaatsen van governance-/workflowdocs naar 10-governance/ en 30-workflow/."
- L191: "- [ PARKED — Phase-5 ] **PHASE3_DOCS_REORG_UPDATE_REFERENCES**"
- L194: "- [PHASE3] Review whether “verify against stored artefacts” should become a requirement (later, via governance lifecycle)."
- L195: "- [PHASE3] Design a sampling pilot to analyze how “²” is used across the corpus (evidence-building, no text edits)."
- L196: "- [PHASE3] LEGACY_IMPORT_PATTERN: All future imports from legacy repo must use the same governed process (small batches, role-separated, provenance headers, read-only)."
- L197: "- [PHASE3] Proposal: design a follow-up pilot that only detects and flags ambiguous “²” cases (no auto-fix), to test governance-aligned review workflows."
- L198: "- [PHASE3] Prototype a review-handoff workflow where flagged items are routed to a human reviewer (no edits — decision logging only)."
- L199: "- [PHASE3] Consider a follow-up pilot simulating disagreement between reviewers and escalation to Human Gate (no edits — governance only)."
- L200: "- [PHASE3] Consider a future governance pilot with multiple conflicting reviewers and explicit evidence links (scan images / research docs) before any decision moves beyond provisional."
- L201: "- [PHASE3] Proposal: explore annotation-vs-translation patterns for context-dependent food terms (no decisions — pilot only)."
- L202: "- [PHASE3] Proposal: design a small readability-pressure pilot testing when annotations become excessive (no rules — documentary only)."
- L203: "- [PHASE3] Proposal: future pilot comparing reader feedback on minimally vs heavily annotated excerpts (controlled test)."
- L204: "- [PHASE3] Proposal: design a micro-pilot exploring when cultural notes belong in annotations vs separate historical commentary."
- L205: "- [PHASE4] Evaluate whether observed workflow gaps merit design changes (based on pilots and synthesis docs)."
- L206: "- [PHASE4] Consider formal diagramming once governance architecture stabilizes (policy-track, not Phase-3)."
- L207: "- [PHASE4] Design incident templates (INCIDENT_REPORT + REVIEW_LOG) —"
- L208: "policy-track, not Phase-3."
- L209: "- [PHASE3] Consider a lifecycle walk-through pilot using ubi/ketela"
- L211: "- [PHASE3] Design a second lifecycle rehearsal using a different term"
- L213: "- [PHASE3] Consider a “flag-only OCR scanner” proposal pilot"
- L215: "- [PHASE3] If useful, design a *governance review simulation* for the"
- L217: "- [PHASE3] Optional follow-up: design a *reader study proposal*"
- L220: "## PHASE4_AGENT_BRIDGE_DESIGN"
- L222: "**Phase Tag:** PHASE-4.1 (Preparation — documentary only)"
- L223: "**Category:** Governance / Design"
- L227: "As a governance architect, I want a safe bridge between CrewAI outputs and"
- L234: "how they are marked as proposals, how governance reviews them, and how"
- L239: "- agents modifying canonical text"
- L245: "**Governance Alignment**"
- L247: "- Lifecycle: requires governance review before any implementation"
- L248: "- Human Gate: only if design implies irreversible behavior"
- L271: "## PHASE4_AGENT_HARNESS_SPEC"
- L273: "**Phase Tag:** PHASE-4.1 (Preparation — documentary / scaffolding)"
- L274: "**Category:** Runtime / Governance / Engineering"
- L280: "logged, reversible, governance-aware, and cannot touch canonical texts"
- L289: "- harness writing into docs/ or canonical text"
- L294: "**Governance Alignment**"
- L296: "- Lifecycle: governance review before implementation"
- L297: "- Human Gate: only if non-sandbox use is proposed"
- L310: "- governance reviewers identified"
- L320: "## PHASE4_AGENT_HARNESS_SPEC (detailed backlog entry)"
- L322: "**ID:** PHASE4_AGENT_HARNESS_SPEC"
- L323: "**Phase Tag:** PHASE-4.1 — Preparation (documentary / scaffolding)"
- L324: "**Category:** Runtime / Governance / Engineering"
- L332: "canonical texts."
- L358: "### Governance Alignment"
- L361: "- Lifecycle: proposal → governance review → possible pilot later"
- L362: "- Human Gate: only if harness is proposed for canonical editing or"
- L371: "Governance-stop if:"
- L375: "Human Gate if:"
- L376: "- the harness is proposed for use on non-sandbox / canonical corpora"
- L391: "- safety: read-only access to canonical docs only"
- L400: "- governance reviewers are identified"
- L401: "- risks have been reviewed at least once in governance"
- L421: "- referenced-only: docs/WORKFLOW.md, docs/PHASE4_READINESS_NOTES.md"
- L422: "- unchanged: all canonical texts and runtime code"
- L427: "- docs/WORKFLOW.md"
- L428: "- docs/PHASE4_READINESS_NOTES.md"
- L430: "- governance stop model"
- L441: "## PHASE4_AGENT_BRIDGE_DESIGN (detailed backlog entry)"
- L443: "ID: PHASE4_AGENT_BRIDGE_DESIGN"
- L444: "Phase Tag: PHASE-4.1 — Preparation (documentary only)"
- L445: "Category: Governance / Runtime Safety"
- L449: "As a governance architect, I want a safe bridge between CrewAI outputs and governed artifacts,"
- L450: "so that agents can contribute analysis without ever modifying canonical texts or creating policy accidentally."
- L456: "and how governance reviews and rolls back mistakes — without enabling runtime behavior."
- L465: "## Governance Alignment"
- L467: "- Lifecycle: requires governance review before implementation"
- L468: "- Human Gate: only if behavior could affect publication"
- L473: "Governance-stop if canonical writes become possible."
- L474: "Human Gate if design touches publication paths."
- L478: "Given governance reviews them, glossary state does not change."
- L501: "- references: governance docs, lifecycle docs"
- L504: "- docs/WORKFLOW.md"
- L505: "- docs/PHASE4_READINESS_NOTES.md"
- L512: "phase: 4.1"
- L521: "- docs/10-governance/AGENT_AUTONOMY_ENVELOPE.md"
- L525: "Phase-4.1 shakedown om een enkele Mistral-annotatieagent (via Crew + Ollama)"
- L533: "- GO-status voor RUN-P4-SAYUR-A-0001 bevestigd in HUMAN_GATE_LOG.md"
- L534: "- sandbox readiness: docs/10-governance/SANDBOX_READINESS_CHECKLIST_P4_V1.md ≈ [x]"
- L542: "en HUMAN_GATE_LOG.md voor RUN-P4-SAYUR-A-0001."
- L548: "- GOVERNANCE_INTEGRATION_DESIGN.md"
- L604: "met een gedocumenteerde reden (soft-stop / governance-stop)."
- L613: "Mitigation: flagged for later human review (Phase-5), not a blocker."
- L637: "## PHASE-5 — Prompt Pattern"
- L644: "- no runtime or prompt rewrites without Human Gate review"
- L645: "- use labels: compliant / needs-clarification / defer-to-governance"
- L655: "- geen herstructurering zonder Human Gate"
- L658: "### PHASE-6 Workflow & Repo Architecture (planning)"
- L660: "- [x] PHASE6_RUNNER_OUTPUT_LAYOUT (layout validated & READY_FOR_IMPLEMENTATION in P6_RUNNER_OUTPUT_LAYOUT.md)"
- L665: "already have a governed home — without new governance rules."
- L667: "- [x] PHASE6_RUNNER_PAYLOAD_REFINEMENT"
- L669: "in run_excerpt_workflow.py for new runs only (no retro-edit of existing outputs)."
- L671: "- [x] PHASE6_SAYUR_MINI_WORKFLOW_DESIGN (docs/P6_WORKFLOW_SAYUR_MINI.md)"
- L672: "Ontwerpdocument voor een kleine, reproduceerbare workflow:"
- L676: "(sandbox/workflows/p6_sayur_mini/*)."
- L677: "Output: docs/P6_WORKFLOW_SAYUR_MINI.md (documentair, geen runtime-wijzigingen)."
- L679: "- [x] PHASE6_SAYUR_MINI_WORKFLOW_PILOT (docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT.md)"
- L680: "Eerste uitgevoerde pilot volgens P6_WORKFLOW_SAYUR_MINI:"
- L684: "Output: pilot-log + korte evaluatie in docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT.md."
- L686: "- [x] PHASE6_SAYUR_MINI_WORKFLOW_PILOT02 (docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT02_EVALUATION.md)"
- L689: "and challenger bias patterns. Outputs follow the same workflow as Pilot 01."
- L691: "- [x] PHASE6_SAYUR_MINI_WORKFLOW_SYNTHESIS (docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT_SYNTHESIS.md)"
- L694: "- [x] PHASE6_SAYUR_MINI_WORKFLOW_PILOT03"
- L697: "→ docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT03_EVALUATION.md"
- L700: "- [x] PHASE6_EXCERPT_BINDING_SPEC"
- L701: "Design change: workflows must accept an explicit `excerpt_id` / `excerpt_path`"
- L706: "- [x] PHASE6_EXCERPT_BINDING_INTEGRATION_PLAN"
- L707: "Plan how excerpt binding (metadata fields) will propagate consistently into"
- L711: "- [x] PHASE6_EXCERPT_METADATA_INTEGRATION_DOCS"
- L713: "evaluation templates, and workflow JSON examples so excerpt usage becomes"
- L716: "- [x] PHASE6_REPOSITORY_ARCHIVIST_INTEGRATION (integration rules documented in P6_REPOSITORY_ARCHIVIST_INTEGRATION.md)"
- L717: "Define how and when the Repository Archivist agent participates in Phase-6 workflows:"
- L723: "- [x] PHASE6_INDEX_EXPANSION_PASS"
- L724: "Editorial Index expanded with Phase-6 documents."
- L726: "- [x] PHASE6_NAV_GROUPING_CANDIDATES_REPORT"
- L738: "- [x] PHASE6_EXCERPT_BINDING_IN_RUNTIME_DESIGN (design frozen in P6_EXCERPT_BINDING_RUNTIME_DESIGN.md)"
- L739: "Design-only: define how excerpt_id/source/version propagate into runner logs"
- L742: "- [x] PHASE6_CASE01_READINESS_PLAN (readiness checklist defined in P6_CASE01_READINESS_PLAN.md; Case-01 is validation-ready: readiness, execution, validation docs exist)"
- L746: "- [ ] PHASE6_NAV_GROUPING_LOW_RISK_MOVE_PLAN"
- L749: "- [ ] PHASE6_NAV_LINK_CONSISTENCY_PASS"
- L752: "- [ ] PHASE6_IMPLEMENT_EXCERPT_AWARE_RUNNER"
- L753: "Implement an excerpt-aware runner and logging path matching P6_EXCERPT_AWARE_RUNNER_DESIGN.md for Case-01/Case-02, without changing governance rules."
- L754: "- Create a real script (e.g. sandbox/crew/run_excerpt_workflow.py or equivalent),"
- L758: "- [x] PHASE6_CASE02_EXCERPT_SELECTION (excerpt lobak_034_048 locked, 2026-01-12)"
- L765: "## Phase-6 — Clarity & Canon Governance (lightweight)"
- L767: "- [ ] PHASE6_CANONICAL_CRITERIA_OVERVIEW"
- L768: "Create docs/CANONICAL_CRITERIA_OVERVIEW.md."
- L769: "Purpose: summarize — in one place — what “CANONICAL” means, who approves it,"
- L770: "and how it relates to the lifecycle (CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL)."
- L771: "Keep it documentary; reference existing governance docs rather than inventing new rules."
- L773: "- [ ] PHASE6_CONFLICT_HANDLING_GUIDE"
- L775: "Describe: when to leave disagreements in PROVISIONAL, when to escalate to Human Gate,"
- L779: "- [ ] PHASE6_ANNOTATION_QUALITY_NOTE"
- L781: "Explain how quality is ensured in practice (annotator + challenger, bias checks, pilots, Human Gate)."
- L784: "- [ ] PHASE6_CANON_EVOLUTION_POLICY_NOTE"
- L785: "Create docs/CANONICAL_EVOLUTION_NOTE.md."
- L786: "Document — at a high level — how canonical material may change over time"
- L788: "Keep scope small; no new governance, just transparency."
- L792: "### PHASE6_CASE02_RUNNER_MAPPING — PENDING"
- L804: "- logs and outputs follow the Phase-6 layout."
- L809: "- This item is documentary until governance explicitly approves"
- L814: "### Phase-7 — Canonical Decision Trails"
- L817: "status: DONE — rehearsal-only, non-canonical"
- L819: "- docs/pilots/P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md"
- L824: "status: DONE — first real canonical decision (lemma only, non-semantic)"
- L826: "- docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSARY_LOBAK_001.md"
- L827: "- docs/CANONICAL_INDEX.md"
- L833: "- docs/pilots/P7_CANONICAL_PILOT_REFLECTION.md"
- L835: "### Phase-8 — Meaning Preservation (status note)"
- L838: "geen capability-evaluatie; telt niet als Phase-8 pilot."
- L839: "Status: PHASE-8 — COMPLETED — REWORK ACCEPTED (PASS-run niet vereist; FAIL-signalen betekenisvol)."
- L840: "Note: Phase-9 micro-pilot P9_FORMAT_DISCIPLINE_PILOT_001 COMPLETED (validator PASS); refs: P9_FORMAT_DISCIPLINE_PILOT_001, P9_OUTPUT_CONTRACT_VALIDATOR_BUGFIX_001."
- L842: "- [x] PHASE8_FIRST_REAL_AGENT_PILOT"
- L844: "Eerste Phase-8 pilot uitvoeren met:"
- L857: "- [x] PHASE8_ANNOTATION_RUNNER_GAP_TRIAGE"
- L861: "of expliciet besluiten dat Annotation in Phase-8 apart blijft."
- L864: "- besluit: Annotation expliciet buiten Phase-8 scope"
- L867: "- [ ] FUTURE_ANNOTATION_PHASE_INTEGRATION"
- L870: "geïntegreerd moet worden in een latere fase (bijv. Phase-9),"
- L873: "- output-contract"
- L874: "- validator-uitbreiding"
- L876: "Alleen na afronding van Phase-8 output-contract enforcement."
- L878: "- [ ] FUTURE_ANNOTATION_OUTPUT_CONTRACT_DEFINITION"
- L880: "Vaststellen van een expliciet output-contract voor Annotation"
- L882: "los van Phase-8 runs."
- L885: "- [x] PHASE8_OUTPUT_CONTRACT_AND_ROLE_ENFORCEMENT"
- L887: "Vaststellen en afdwingen van een expliciet output-contract"
- L888: "voor Phase-8 agent-runs, zodat:"
- L891: "- agents geen governance-onjuist taalgebruik introduceren"
- L899: "- Geen canonieke wijzigingen"
- L900: "- contract v2 (EN/NL allowed) adopted"
- L902: "- gate enforced (procedural + technical)"
- L903: "- no PASS-run reached; Phase-8 inhoudelijk open"
- L906: "[x] PHASE8_OUTPUT_CONTRACT_VALIDATOR_SCRIPT (sandbox-only)"
- L908: "Maak een minimale post-run validator (shell of python) die de"
- L915: "- schrijft report naar sandbox/phase8_runs/<run_id>/eval/output_contract_checks.txt"
- L917: "- script: sandbox/tools/phase8_output_contract_validator.sh"
- L921: "[x] PHASE8_OUTPUT_CONTRACT_ENFORCEMENT_GATE"
- L923: "Verplicht de output-contract validator als harde gate na iedere Phase-8 CLI-run"
- L928: "- Validator wordt standaard uitgevoerd na elke Phase-8 run."
- L929: "- Een FAIL produceert expliciete gate-melding in eval/ (geen automatische correcties)."
- L930: "- Geen wijzigingen aan pipeline-stappen of agents; enkel enforcement via gate."
- L933: "- gate: mandatory validator run"
- L936: "[x] PHASE8_OUTPUT_CONTRACT_TECHNICAL_GATE_WRAPPER"
- L938: "- artefact: sandbox/tools/phase8_run_with_gate.sh"
- L939: "- verified: wrapper exercised on FAIL cases; gate messaging present"
- L940: "- evidence: eval/output_contract_checks.txt updated on FAIL runs"
- L942: "- note: no PASS-run reached (output contract violations remain)"
- L944: "[x] PHASE8_VALIDATOR_DEPENDENCY_RIPGREP"
- L946: "Validator gebruikt rg (ripgrep). Borg dat Phase-8 runs niet onbetrouwbaar"
- L952: "- [ ] PHASE8_FIRST_PASS_RUN"
- L954: "Realiseer de eerste PASS-run onder output-contract v2 met gate."
- L955: "Acceptatie: validator overall_status: PASS (exit 0) + report aanwezig."
- L956: "Nota: PASS-run is niet vereist voor Phase-8 afronding (optioneel backlog)."
- L958: "- [ ] Phase-8: Fidelity volgt Opmerkingen-separator niet consistent — format strictness"
- L962: "remarks-separator naleving te verbeteren, zonder blokkade voor Phase-8."
- L964: "### Phase-9 — Format Discipline (status note)"
- L966: "- [ ] Phase-9: Gate/validator should always emit eval/output_contract_checks.txt even on FAIL (Run03 produced PHASE8_GATE_FAIL but eval/ was empty). Evidence: sandbox/phase9_runs/P9_RUN_20260108T_RUN03/logs/run.log and empty eval/ directory. BACKLOG / LOW-RISK / NON-BLOCKING."
- L974: "- [ ] MAP_REVIEW_PHASE3_IMPACT"
- L977: "Note: do not execute automatically — governance review first."

## docs/CONSOLIDATION_AUDIT_01.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Scope
- ## Observations (facts only)
- ## Risk Assessment (risk-thinking, nog steeds feitelijk)
- ## Dead / Orphaned Items
- ## Consistency Check — Governance Patterns
- ## Open Questions (for humans)
- ## Recommendation Type (NO CHANGES)

Quoted phrases:
- L4: "Audit uitgevoerd op governance- en workflowdocumentatie in `docs/` en alle agent-prompts"
- L9: "- `docs/total_project.md` noemt in de “Docs-map (actuele lijst)” niet: `docs/WORKFLOW.md`,"
- L10: "`docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`, `docs/10-governance/GOVERNANCE_TESTS_PLAN.md`,"
- L11: "`docs/CHAPTER_BATCH_WORKFLOW.md`, `docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md`,"
- L12: "`docs/GLOSSARY_PILOT_REPORT.md`, `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`,"
- L13: "`docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md`."
- L15: "terwijl `prompts/handover_agent.md` bestaat en wordt genoemd in `docs/AGENTS.md` en `docs/WORKFLOW.md`."
- L17: "anders zijn gemarkeerd (bijv. workflow-documentatie staat daar op [x])."
- L18: "- `docs/CODEX_TODO.md` bevat de heading “PHASE-2 Roadmap (governed backlog — not started yet)”"
- L19: "terwijl alle PHASE2-items eronder op [x] staan."
- L20: "- `docs/CODEX_TODO.md` vermeldt bij **PHASE2_GOVERNANCE_TEST_SCENARIO_1** als output"
- L21: "`docs/GOVERNANCE_TEST_RUN_01.md`, terwijl het aanwezige document"
- L22: "`docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md` heet."
- L28: "- `docs/WORKFLOW.md` noemt in “Governance Triggers” alleen Methodology/Technical/Troubleshooting,"
- L30: "`docs/WORKFLOW.md` en de lifecycle in `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`)."
- L39: "met de huidige set governance- en workflowdocumenten."
- L42: "- Artefact-risico: `docs/CODEX_TODO.md` verwijst naar `docs/GOVERNANCE_TEST_RUN_01.md`,"
- L44: "- Governance-trigger-risico: triggers voor Glossary/Research staan in sommige documenten"
- L51: "en niet in de overige gelezen governance-/workflowdocumenten of prompts."
- L52: "- `docs/GOVERNANCE_TEST_RUN_01.md` wordt genoemd in `docs/CODEX_TODO.md` maar is niet aanwezig"
- L53: "in de lijst van documenten in `docs/` (wel bestaat `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`)."
- L55: "## Consistency Check — Governance Patterns"
- L56: "- Glossary lifecycle: consistent tussen `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`,"
- L58: "`docs/WORKFLOW.md` wordt de Glossary lifecycle niet genoemd in de triggerlijst."
- L59: "- Soft-stop / governance-stop / human-gate: aanwezig in `docs/WORKFLOW.md` en in alle"
- L62: "`prompts/orchestrator.md`; `docs/CODEX_SESSION_LOG.md` bevat entries voor recente PHASE2-items."
- L64: "`docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md` en `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`."
- L66: "`docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md` expliciet vereist; in `docs/WORKFLOW.md`"
- L67: "staat Research niet in de governance-triggerlijst maar wel in de stop-model tabel."
- L72: "- Moet het PHASE-2 header-label “not started yet” in `docs/CODEX_TODO.md` blijven staan"
- L73: "nu alle PHASE2-items op [x] staan?"
- L74: "- Is `docs/GOVERNANCE_TEST_RUN_01.md` een verwachte output die nog moet bestaan,"
- L75: "of moet de verwijzing wijzen naar `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`?"
- L79: "- Moeten Glossary/Research triggers ook expliciet in de “Governance Triggers”-lijst"
- L80: "van `docs/WORKFLOW.md` staan voor volledigheid?"
- L87: "Outcome: governance handled ambiguity; insight recorded; reversible."
- L97: "Outcome: detection proven; edits deferred; governance handoff identified as next capability."
- L99: "Scope: human review workflow for ambiguity flags."
- L100: "Outcome: decision logging worked; edits remained deferred; governance triggers clarified."
- L102: "Scope: reviewer disagreement and governance escalation."
- L103: "Outcome: escalation and Human Gate behavior documented; no edits applied."
- L116: "- P3_WORKFLOW_001 — CONSOLIDATED"
- L117: "Scope: workflow synthesis (documentary)."
- L119: "- P3_WORKFLOWMAP_001 — CONSOLIDATED"
- L120: "Scope: workflow diagram (documentary)."
- L123: "Scope: governance failure-drill (documentary)."

## docs/CONSOLIDATION_TODO.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## Tasks

Quoted phrases:
- L9: "Source: "`docs/total_project.md` noemt in de “Docs-map (actuele lijst)” niet: `docs/WORKFLOW.md`, `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`, `docs/10-governance/GOVERNANCE_TESTS_PLAN.md`, `docs/CHAPTER_BATCH_WORKFLOW.md`, `docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md`, `docs/GLOSSARY_PILOT_REPORT.md`, `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`, `docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md`.""
- L17: "Source: "`docs/total_project.md` noemt in de “Prompts-map (actuele lijst)” niet `prompts/handover_agent.md`, terwijl `prompts/handover_agent.md` bestaat en wordt genoemd in `docs/AGENTS.md` en `docs/WORKFLOW.md`.""
- L25: "Source: "`docs/total_project.md` sectie 8.2 noemt TODO-items die in `docs/CODEX_TODO.md` inmiddels anders zijn gemarkeerd (bijv. workflow-documentatie staat daar op [x]).""
- L32: "- ID: CONSOL_PHASE2_HEADER_STATE"
- L33: "Source: "`docs/CODEX_TODO.md` bevat de heading “PHASE-2 Roadmap (governed backlog — not started yet)” terwijl alle PHASE2-items eronder op [x] staan.""
- L34: "Description: PHASE-2 heading zegt “not started yet” terwijl items als afgerond staan."
- L36: "RiskIfIgnored: inconsistente interpretatie van PHASE-2 status."
- L37: "Notes: PHASE-2 heading text in CODEX_TODO.md updated to reflect mixed completed/open backlog."
- L41: "Source: "`docs/CODEX_TODO.md` vermeldt bij **PHASE2_GOVERNANCE_TEST_SCENARIO_1** als output `docs/GOVERNANCE_TEST_RUN_01.md`, terwijl het aanwezige document `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md` heet.""
- L44: "RiskIfIgnored: broken reference in governance test output."
- L45: "Notes: Reference in CODEX_TODO.md updated to GOVERNANCE_TEST_SCENARIO_1.md."
- L53: "Notes: AGENTS.md genormaliseerd naar Cohesion als canonieke naam met Continuity als historische verwijzing."
- L60: "RiskIfIgnored: inconsistent agent-naming in governance-documentatie."
- L61: "Notes: AGENTS.md genormaliseerd naar Design als canonieke naam met Layout als historische verwijzing."
- L65: "Source: "`docs/WORKFLOW.md` noemt in “Governance Triggers” alleen Methodology/Technical/Troubleshooting, terwijl Glossary/Research triggers elders wel expliciet staan (stop-model tabel in `docs/WORKFLOW.md` en de lifecycle in `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`).""
- L66: "Description: governance-triggerlijst in WORKFLOW.md mist Glossary/Research."
- L68: "RiskIfIgnored: onvolledig beeld van governance-triggers in workflow-overzicht."
- L69: "Notes: Glossary & Research triggers nu expliciet in WORKFLOW.md."
- L89: "Source: "`docs/GOVERNANCE_TEST_RUN_01.md` wordt genoemd in `docs/CODEX_TODO.md` maar is niet aanwezig in de lijst van documenten in `docs/` (wel bestaat `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`).""
- L92: "RiskIfIgnored: verwijzing naar niet-bestaand document in governance-docs."

## docs/CONTENT_ROADMAP.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Phase A — Foundations (high priority)
- ## Phase B — Pilot Translation Sets
- ## Phase C — Context Expansion
- ## Phase D — Scaling Pass
- ## Phase E — Pre-publication preparation (later)

Quoted phrases:
- L8: "## Phase A — Foundations (high priority)"
- L15: "## Phase B — Pilot Translation Sets"
- L22: "## Phase C — Context Expansion"
- L25: "- Identify where Human Gate is likely required"
- L28: "## Phase D — Scaling Pass"
- L34: "## Phase E — Pre-publication preparation (later)"
- L36: "- final glossary decision rounds (Human Gate)"
- L38: "Outcome: ready for editorial governance — not yet for release."

## docs/EDITORIAL_CAPABILITIES.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## 0. Doel van dit document
- ## 6. Culinary Validation
- ## 11. Relatie met techniek en governance

Quoted phrases:
- L7: "Het gaat niet over tools, agents, pipelines of governance,"
- L9: "Andere documenten (VISION_AND_STRATEGY, REQUIREMENTS, GOVERNANCE, WORKFLOW)"
- L12: "> Redactie leidt, techniek ondersteunt, governance beschermt."
- L116: "geen inhoudelijke herschrijving van de canonieke tekst."
- L205: "## 11. Relatie met techniek en governance"
- L210: "- Governance (requirements, workflow, lifecycle) beschermt de grenzen"

## docs/EDITORIAL_INDEX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Non-canonical handover copies

Quoted phrases:
- L9: "## Non-canonical handover copies"
- L12: "Die zijn niet canoniek en kunnen verouderd zijn."

## docs/GLOSSARY_PILOT_REPORT.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Scope
- ## Method
- ### Term: aron
- ### Term: arem arem
- ### Term: temu kuntji
- ## Recommendations (pilot level)
- ## Next Steps

Quoted phrases:
- L4: "Deze pilot toetst de Glossary + Research workflow op een kleine, veilige set termen"
- L20: "de Human Gate expliciet is uitgesteld (pilot-only)."
- L60: "- Human Gate: Decision deferred — pilot stage only."
- L61: "- Versioning: N/A until Human Gate."
- L108: "- Human Gate: Decision deferred — pilot stage only."
- L109: "- Versioning: N/A until Human Gate."
- L155: "- Human Gate: Decision deferred — pilot stage only."
- L156: "- Versioning: N/A until Human Gate."
- L174: "- Require cross-reference checks in archive glossary sources before Human Gate."
- L177: "- Run a Human Gate review once evidence from archive glossary sources is available."

## docs/GOVERNANCE_BOUNDARIES_NOTE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Governance Boundaries — What must never be moved autonomously

Quoted phrases:
- L1: "# Governance Boundaries — What must never be moved autonomously"
- L5: "Mag NIET zonder expliciete Human Gate:"
- L6: "- verplaatsen of verwijderen van canonical docs"
- L7: "- herstructureren van governance-bestanden"
- L14: "3) Human Gate besluit"

## docs/MIGRATION_NOTES.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Repo Migration Notes (Phase-6)
- ### MIGRATION — Workflow Rename (Generic Alignment)

Quoted phrases:
- L1: "# Repo Migration Notes (Phase-6)"
- L3: "This file records every migration action taken during Phase-6"
- L18: "### MIGRATION — Workflow Rename (Generic Alignment)"
- L20: "Action: renamed generic workflow file and updated references."

## docs/P4_CLOSURE_CHECKLIST_SANDBOX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-4 Sandbox Closure Checklist — SAYUR (Draft, non-binding)
- ## 1) Runtime + reproducibility
- ## 2) Governance behaviour
- ## 3) Failure-mode learning (documented, not fixed)
- ## 5) What stays intentionally unresolved (Phase-5 territory)
- ## Status

Quoted phrases:
- L1: "# Phase-4 Sandbox Closure Checklist — SAYUR (Draft, non-binding)"
- L4: "It helps verify whether Phase-4 sandbox goals were *demonstrated*,"
- L19: "- sandbox/crew/run_logs/* (Phase-4 SAYUR)"
- L23: "## 2) Governance behaviour"
- L25: "- [ ] Soft-stop and governance-stop rules are visible in docs and runners."
- L26: "- [ ] No agent writes to source or canonical documents."
- L31: "- docs/WORKFLOW.md"
- L32: "- docs/10-governance/*"
- L33: "- HUMAN_GATE_LOG.md"
- L40: "- [ ] Occasional challenger overreach recognised as governance issue."
- L41: "- [ ] JSON-fencing / contract issues identified and traced to prompts."
- L62: "## 5) What stays intentionally unresolved (Phase-5 territory)"
- L68: "These are **explicitly deferred** and do not block Phase-4 closure."
- L76: "That remains a Human-Gate decision documented elsewhere."

## docs/P4_CONSOLIDATION_REPORT_SAYUR_SANDBOX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Status Summary
- ## What We Proved
- ## Agent Behaviour Notes
- ## Known Limitations
- ### KNOWN LIMITATION — “Helpful translation” framing (OTHER/INFO)
- ## Governance Checkpoints
- ## Components Ready For Re-Use
- ## Next Safe Steps (Recommendation)
- ## KNOWN LIMITATION — Translation Bias in Challenger (EQUIVALENT/INFO)
- ### Expected generalisation (Phase-4 stance)

Quoted phrases:
- L4: "- Phase: P4 (sandbox, non-publication)"
- L10: "- Overall outcome: **WORKFLOW PROVEN — SAFE TO CONTINUE (sandbox)**"
- L17: "- Goverance stop-model (soft-stop → human gate) works in practice."
- L29: "(requested translations where governance forbids decisions)."
- L33: "- Challenger sometimes mislabels issues as SAFETY instead of GOVERNANCE."
- L51: "expected to provide translations in Phase-4."
- L57: "Governance stance:"
- L63: "This behaviour is intentionally NOT suppressed in Phase-4,"
- L66: "## Governance Checkpoints"
- L68: "- All BLOCKER-type issues route to Human Gate."
- L73: "- JSON annotation contract"
- L80: "1. Tune challenger issue-types (add GOVERNANCE / MEANING_DECISION)."
- L91: "In multiple Phase-4 SAYUR micropilot runs, the Challenger agent"
- L102: "(annotators are not expected to provide translations in Phase-4)."
- L108: "Governance stance (Phase-4):"
- L115: "This bias should be revisited in later phases, but no additional"
- L116: "runtime constraints are added in Phase-4 to suppress it. Documentation"
- L119: "### Expected generalisation (Phase-4 stance)"
- L124: "In Phase-4 this bias is **documented and monitored, not eliminated**."
- L127: "affect safety, meaning, or publication-impact decisions (Human Gate)."

## docs/P4_HANDOVER_PACK_SAYUR_SANDBOX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # P4 Handover Pack — SAYUR Sandbox (Agents & CrewAI)
- ## 1. Kern-overzicht
- ## 2. Governance & workflow
- ## 7. Wat de volgende GPT-sessie mag doen

Quoted phrases:
- L8: "- Governance-bewuste integratie in een redactionele workflow"
- L19: "→ Samenvatting van wat Phase-4 sandbox voor SAYUR al heeft bewezen"
- L22: "## 2. Governance & workflow"
- L26: "- `docs/WORKFLOW.md`"
- L27: "→ Stop-model (soft-stop → governance-stop → Human Gate) + pipeline."
- L29: "- `docs/10-governance/HUMAN_GATE_POLICY_P4_SANDBOX.md`"
- L30: "→ Wanneer Human Gate verplicht is (meaning, cultuur, safety, publicatie)."
- L32: "- `docs/10-governance/ROLLBACK_TESTPLAN_P4_SANDBOX.md`"
- L101: "*voorstellen* doet, maar nooit zelf prompts/config wijzigt zonder Human Gate + Codex."

## docs/P5_AGENT_BEHAVIOUR_CRITERIA.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-5 — Agent Behaviour Criteria (Annotator & Challenger)
- ## 1. Context
- ### 2.4 Criteria — Out-of-bounds
- ### 3.1 Wat de Challenger wél moet doen
- ### 3.3 Criteria — Overreach
- ### 3.4 Criteria — Out-of-bounds
- ## 5. Gebruik in Phase-5

Quoted phrases:
- L1: "# Phase-5 — Agent Behaviour Criteria (Annotator & Challenger)"
- L9: "> Geen runtime-veranderingen zonder Human Gate."
- L15: "Phase-4 heeft laten zien dat:"
- L22: "zodat reviewers en governance sneller kunnen zien of gedrag acceptabel is."
- L90: "- beoordeling via Human Gate (indien relevant)"
- L99: "- werken met issue_types (TRANSLATION / EQUIVALENT / MEANING_DECISION / SAFETY / GOVERNANCE / OTHER)"
- L140: "- BLOCKER wordt gebruikt zonder duidelijke governance-reden"
- L161: "- mogelijke SAFETY / GOVERNANCE review via Human Gate."
- L194: "## 5. Gebruik in Phase-5"
- L196: "- Deze criteria helpen reviewers en governance:"
- L202: "- human-gated waar nodig."

## docs/P5_CLOSURE_NOTE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase 5 — Closure Note  
- ## 1. What Phase 5 was for
- ## 2. What we actually achieved
- ## 4. What we deliberately did NOT do
- ## 6. Readiness statement
- ## 7. Next logical directions (Phase 6 preview)

Quoted phrases:
- L1: "# Phase 5 — Closure Note"
- L5: "Samenvatten wat Phase 5 beoogde, wat bereikt is,"
- L12: "## 1. What Phase 5 was for"
- L14: "- consolidatie van Phase-4 evidence"
- L18: "- repo en processen voorbereiden op productie-denken (Phase 6)"
- L31: "CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN → CANONICAL"
- L35: "- One focused Phase-5 micropilot executed"
- L41: "without breaking governance.**"
- L68: "- No attempts to “automate away” Human Gate thinking"
- L71: "Phase-5 prioritized **clarity over cleverness**."
- L91: "Phase-5 outcome:"
- L97: "This is **sufficiently mature** to proceed toward Phase-6 planning,"
- L102: "## 7. Next logical directions (Phase 6 preview)"
- L104: "- Decide which workflows should move toward production-grade"
- L107: "- Gradually evaluate where Human Gate should remain vs. be simplified"

## docs/P5_DECISION_LIFECYCLE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Decision Lifecycle — Translation & Interpretation (Phase 5)
- ## Status Model
- ## Authority Matrix (Who may set which state?)

Quoted phrases:
- L1: "# Decision Lifecycle — Translation & Interpretation (Phase 5)"
- L7: "This lifecycle applies to agents, crews, Codex/meta, and Human Gate."
- L29: "4) CANONICAL"
- L30: "origin: Human Gate / editorial decision"
- L35: "## Authority Matrix (Who may set which state?)"
- L39: "may NOT → set CREW_PROVISIONAL, READY_FOR_HUMAN_REVIEW, CANONICAL"
- L44: "may NOT → set CANONICAL"
- L49: "may NOT → set CANONICAL"
- L51: "- Human Gate:"
- L52: "may → set CANONICAL"

## docs/P5_MICROPILOT_FOLLOWUP_NOTES.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase 5 — Micropilot Follow-up Notes

Quoted phrases:
- L1: "# Phase 5 — Micropilot Follow-up Notes"
- L4: "Purpose: documenteren welke inzichten later (Phase 6) opnieuw bekeken moeten worden."

## docs/P5_PROMPT_CONSOLIDATION_NOTE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-5 Prompt Consolidation Note
- ## 1. Context (waarom dit document bestaat)
- ## 3. Waar we “needs-clarification” zagen
- ## 4. Wat we bewust NIET oplossen in Phase-5
- ## 5. Rol van het nieuwe Prompt Pattern
- ## 6. Aanbevolen vervolgstappen (documentair)

Quoted phrases:
- L1: "# Phase-5 Prompt Consolidation Note"
- L11: "Phase-4 heeft laten zien dat annotator en challenger technisch stabiel zijn,"
- L13: "Phase-5 focust niet op “tunen”, maar op beter begrijpen en navigeerbaar maken."
- L16: "> Alle wijzigingen blijven proposal-only en vereisen governance-review."
- L40: "Niet fout — maar nog niet uniform volgens het nieuwe Phase-5 pattern:"
- L52: "## 4. Wat we bewust NIET oplossen in Phase-5"
- L61: "→ alleen na governance-review."
- L63: "> Phase-5 = ordenen en expliciteren — niet herontwerpen."
- L77: "`compliant / needs-clarification / defer-to-governance`."
- L86: "- voorbereiden van een kleine Phase-5 pilot:"
- L93: "- human-gated waar nodig."

## docs/P5_TODO.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-5 TODO — Preparation & Consolidation (Draft)
- ## 2) Consolidatie van Phase-4 inzichten
- ## 4) Voorbereiding richting productie-workflow
- ## 5) Repo & document-architectuur opschonen (jouw punt)
- ## 6) Publicatievooruitblik (boek als eindproduct)
- ## Status & scope

Quoted phrases:
- L1: "# Phase-5 TODO — Preparation & Consolidation (Draft)"
- L3: "Purpose: Phase-5 is about consolidating what works, choosing what to"
- L4: "improve, and preparing for a production-ready workflow."
- L5: "It is NOT a new sandbox and NOT a build-everything phase."
- L28: "## 2) Consolidatie van Phase-4 inzichten"
- L30: "Goal: Capture what we learned so Phase-5 does not repeat Phase-4."
- L34: "“monitor only, do not fix in Phase-5 unless explicitly decided.”"
- L36: "in Phase-5 (to avoid scope creep)."
- L60: "## 4) Voorbereiding richting productie-workflow"
- L62: "Goal: Avoid chaos when scaling up later (Phase-6)."
- L64: "- [ ] Identify which decisions MUST go through Human Gate"
- L81: "- canonical (project overview, key governance, core workflow)"
- L92: ""governance": [...],"
- L94: ""phase4_logs": [...],"
- L110: "- [ ] Draft the high-level structure of the eventual book workflow:"
- L114: "- [ ] Note what Phase-5 pilots need to prove for this to be realistic."
- L120: "- Phase-5 remains governed and reversible."
- L122: "- This TODO is a planning aid, not a binding contract."

## docs/P5_TRANSLATION_EXPECTATION_EVIDENCE.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-5 Evidence — Translation-Expectation Patterns
- ## 1. Waarom dit document bestaat
- ## 6. Wat we níet gaan doen (Phase-5)

Quoted phrases:
- L1: "# Phase-5 Evidence — Translation-Expectation Patterns"
- L4: "Scope: challenger behavior observed in Phase-4 (SAYUR micropilot & shakedowns)"
- L12: "In Phase-4 zagen we een terugkerend patroon bij de Challenger:"
- L90: "## 6. Wat we níet gaan doen (Phase-5)"

## docs/P5_USER_PREFERENCES.md

Preliminary classification suggestion: GOV-A

Quoted phrases:
- L1: "Phase-5 User Preferences — Autonomy & Escalation"
- L27: "minimize repetitive governance questions"

## docs/P6_ARCHIVE_ARCHITECTURE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 Archive Architecture (Runs, Artefacts, Reviews)
- ## 1. Purpose
- ## 2. High-level structure
- ## 4. Run outputs (per excerpt, per run)
- ## 5. Reflections and consolidation docs

Quoted phrases:
- L1: "# Phase-6 Archive Architecture (Runs, Artefacts, Reviews)"
- L5: "This document explains how Phase-6 artefacts are laid out on disk and"
- L12: "- canonical index entries (later phases)"
- L21: "At Phase-6, the relevant zones are:"
- L27: "- `CANONICAL_INDEX.md`              → canonical editorial entries (later, human-only)"
- L80: "Each JSON file follows the Phase-6 runner output contract:"
- L120: "workflow experience, and design implications."
- L122: "do NOT act as canonical decision logs."
- L127: "choices were made, without being part of the canonical textual edition."
- L154: "A typical chain from run to potential canonical decision looks like:"
- L172: "Canonical index entry (later phase):"
- L174: "CANONICAL_INDEX.md entry referencing:"
- L184: "This chain is unidirectional (from runs towards canonical) but traceable"
- L185: "in reverse (from canonical back to runs)."
- L188: "Phase-6 archive rules:"
- L205: "9. Interaction with EDITORIAL_INDEX and CANONICAL_INDEX"
- L208: "cases, reflections, workflow specs, templates, reviews."
- L210: "CANONICAL_INDEX.md is reserved for human-approved,"
- L211: "canonical editorial entries (later phases)."
- L213: "The archive architecture ensures that for every canonical entry"
- L230: "Use this architecture as a reference when designing future phases"

## docs/P6_CASE01_READINESS_PLAN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Case-01 Readiness Plan (SAYUR, lines 52–66)
- ## 2. Preconditions (Before Any Run)
- ## 3. Runner & CLI Readiness
- ## 6. Rollback Plan

Quoted phrases:
- L1: "# Phase-6 — Case-01 Readiness Plan (SAYUR, lines 52–66)"
- L6: "P6_RUNNER_OUTPUT_LAYOUT.md, P6_PHASE_STATUS_SNAPSHOT.md"
- L29: "- excerpt-aware runtime propagation contract is defined,"
- L31: "- sandbox-only scope is confirmed (proposal-only, no canonical edits)."
- L56: "- Missing or mismatched excerpt metadata = SOFT-STOP; do not start the workflow."
- L107: "- keep docs/ and canonical texts untouched."
- L109: "This rollback is documentary and does not delete historical canonical material."

## docs/P6_CASE01_REAL_RUN_EXECUTION_PLAN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Case-01 Real-Run Execution Plan (SAYUR 052–066)
- ## 3. Expected CLI Shape (Reminder)
- ## 5. Validation Steps After the Run
- ## 7. Incident Scenarios & Responses
- ## 8. What Success Looks Like
- ## 9. Next Steps After a Valid Run
- ## 10. Out-of-Scope

Quoted phrases:
- L1: "# Phase-6 — Case-01 Real-Run Execution Plan (SAYUR 052–066)"
- L45: "python sandbox/crew/run_excerpt_workflow.py \"
- L88: "no glossary decisions claim canonical authority"
- L134: "document → stop → investigate — never patch artefacts after the fact."
- L152: "canonical decisions,"
- L172: "Any promotion beyond provisional requires Human Gate involvement."
- L184: "change governance rules,"

## docs/P6_CASE01_VALIDATION_PLAN.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## 1. Objectives (wat we willen bevestigen)
- ## 3. Single-run procedure (de run zelf)
- ### 4.1 Log (mandatory)
- ### 4.2 JSON outputs (mandatory if no STOP)
- ## 5. Validation checklist (door reviewer)
- ## 6. Rollback (alleen voor sandbox-artefacts)

Quoted phrases:
- L20: "Geen enkele inhoudelijke beslissing wordt in deze run canoniek."
- L41: "python sandbox/crew/run_excerpt_workflow.py"
- L78: "status: (COMPLETED | SOFT-STOP | GOVERNANCE-STOP | ERROR)"
- L102: "Als `excerpt` of `run` ontbreekt → **GOVERNANCE-STOP**."
- L124: "(of in CODEX_SESSION_LOG, afhankelijk van workflow)."
- L138: "Canonical/Docs blijven onaangeroerd."

## docs/P6_CASE02_READINESS_PLAN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Case-02 Readiness Plan (LOBAK)
- ## 2. Preconditions (high-level)
- ## 3. Excerpt binding (Phase-6)
- ## 4. Readiness checklist (to be filled once excerpt is chosen)
- ## Phase-6 Readiness — Concrete Checklist (Case-02, LOBAK)
- ### Inputs (locked before run)
- ### Review Path (after run, before any decisions)

Quoted phrases:
- L2: "# Phase-6 — Case-02 Readiness Plan (LOBAK)"
- L6: "P6_EDITORIAL_WORKFLOW_MINI.md, docs/navigation/EDITORIAL_INDEX.md"
- L24: "- the runner and output layout follow the same Phase-6 excerpt-aware design"
- L27: "## 3. Excerpt binding (Phase-6)"
- L42: "- [ ] Human Gate acknowledges that Case-02 is allowed to run in sandbox."
- L47: "## Phase-6 Readiness — Concrete Checklist (Case-02, LOBAK)"
- L54: "- runner script: sandbox/crew/run_excerpt_workflow.py"
- L72: "3) crew synthesizes provisional trace (no canonization)"

## docs/P6_CASE02_REAL_RUN_EXECUTION_PLAN.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 — Case-02 Real Run Execution Plan (LOBAK)
- ## 2. Planned CLI invocation (excerpt-aware)
- ## Excerpt-Aware Execution Shape (documentary)
- ### Example CLI (shape only)
- ## Expected Layout (Phase-6)
- ## Payload Contract (runner refinement)

Quoted phrases:
- L2: "# Phase-6 — Case-02 Real Run Execution Plan (LOBAK)"
- L5: "Related: P6_LOBAK_INTERNAL_WORK_CASE02.md, P6_EDITORIAL_WORKFLOW_MINI.md,"
- L19: "python sandbox/crew/run_excerpt_workflow.py \"
- L57: "once governance explicitly approves a real run."
- L62: "python sandbox/crew/run_excerpt_workflow.py \"
- L69: "## Expected Layout (Phase-6)"
- L82: "## Payload Contract (runner refinement)"

## docs/P6_CASE02_RUNNER_MAPPING_DESIGN.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 — Case-02 Runner Mapping Design (LOBAK)
- ## 2. Context — what worked for Case-01
- ### 3.2 Mapping requirement (conceptual)
- ## 4. Expected runtime behaviour (once implemented)
- ## 5. Lifecycle & governance constraints
- ## 6. Out of scope (Phase-6 boundary)

Quoted phrases:
- L1: "# Phase-6 — Case-02 Runner Mapping Design (LOBAK)"
- L39: "- run_excerpt_workflow.py as the entry point,"
- L83: "- writes excerpt-aware JSON and logs that satisfy the Phase-6 contracts."
- L104: "python sandbox/crew/run_excerpt_workflow.py \"
- L155: "## 5. Lifecycle & governance constraints"
- L161: "not introduce CANONICAL states,"
- L177: "## 6. Out of scope (Phase-6 boundary)"
- L195: "Implementation requires a separate governance decision."

## docs/P6_CASE02_VALIDATION_PLAN.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## Phase-6 Validation — What Counts as Success (Case-02)
- ### 4) Lifecycle Discipline
- ### 6) Rollback & Supersession

Quoted phrases:
- L1: "Phase-6 — Case-02 Validation Plan (LOBAK)"
- L6: "Excerpt binding (Phase-6):"
- L32: "run_logs and run_outputs follow the Phase-6 layout"
- L52: "no accidental promotion to canonical"
- L68: "## Phase-6 Validation — What Counts as Success (Case-02)"
- L70: "Validation is workflow-first, not translation-first."
- L103: "- Nothing is marked CANONICAL."
- L121: "If the above are satisfied, Case-02 passes Phase-6 validation,"

## docs/P6_EDITORIAL_WORKFLOW_MINI.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Mini Editorial Workflow (Internal)
- ## 3. Lifecycle Contract
- ## 4. Step-by-Step Workflow
- ### Excerpt metadata (Phase-6)
- ## 6. What This Workflow Must NOT Do
- ## 7. When to Escalate to Human Gate
- ## 8. Outcome of This Workflow

Quoted phrases:
- L1: "> NOTE (Phase-6, naming alignment):"
- L2: "> This workflow is generic and applies to all chapters."
- L7: "# Phase-6 — Mini Editorial Workflow (Internal)"
- L9: "This workflow describes how a small SAYUR excerpt moves from"
- L11: "without producing canonical or public text."
- L49: "## 3. Lifecycle Contract"
- L53: "CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL (human-only)"
- L58: "but CANONICAL decisions require editorial governance"
- L59: "and are outside this mini-workflow."
- L63: "## 4. Step-by-Step Workflow"
- L70: "sandbox/workflows/sayur_internal/annotator_raw.json"
- L74: "sandbox/workflows/sayur_internal/challenger_raw.json"
- L78: "sandbox/workflows/sayur_internal/crew_decisions_provisional.json"
- L85: "sandbox/workflows/sayur_internal/human_review_notes.md"
- L103: "### Excerpt metadata (Phase-6)"
- L104: "Elke workflowrun die op een excerpt werkt, registreert minimaal:"
- L117: "## 6. What This Workflow Must NOT Do"
- L120: "- no canonical glossary decisions"
- L130: "## 7. When to Escalate to Human Gate"
- L143: "## 8. Outcome of This Workflow"
- L154: "End of workflow."

## docs/P6_EXCERPT_AWARE_PRACTICE_RUN_CASE01.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 — Excerpt-Aware Practice Run (Case-01, SAYUR 052–066)
- ## 3. Expected CLI Invocation (Design-Only)

Quoted phrases:
- L1: "# Phase-6 — Excerpt-Aware Practice Run (Case-01, SAYUR 052–066)"
- L43: "python sandbox/crew/run_excerpt_workflow.py \"
- L107: ""issue_type": "GOVERNANCE","
- L158: "does NOT provide canonical or glossary decisions,"

## docs/P6_EXCERPT_AWARE_RUNNER_DESIGN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Excerpt-Aware Runner Design
- ## 1. Purpose
- ### 4.1 Flags
- ### 5.1 YAML-voorbeeld

Quoted phrases:
- L1: "# Phase-6 — Excerpt-Aware Runner Design"
- L4: "Related: P6_EXCERPT_BINDING_SPEC.md, P6_EXCERPT_BINDING_INTEGRATION_PLAN.md, P6_EDITORIAL_WORKFLOW_MINI.md, P6_SAYUR_INTERNAL_WORK_CASE01.md"
- L17: "zodat elke excerpt-gebaseerde run in Phase-6:"
- L81: "python sandbox/crew/run_excerpt_workflow.py \"
- L119: "runner: excerpt_workflow"
- L147: ""runner": "excerpt_workflow","
- L159: "6. Logging Contract"
- L182: "voert geen workflow uit (soft/governance-stop)."
- L190: "7. JSON Contract voor Workflow Artefacts"
- L220: ""issue_type": "GOVERNANCE","
- L248: "config-fout, geen workflow-uitvoer."
- L252: "Eventuele tooling mag mismatch signaleren als governance-issue,"
- L277: "10. Roll-out & Governance"
- L283: "Governance Review — Human Gate beoordeelt impact."
- L287: "Dit document autoriseert geen code-changes; wijzigingen lopen via governance-processen."

## docs/P6_EXCERPT_AWARE_RUNNER_IMPLEMENTATION_GUIDE.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 — Excerpt-Aware Runner Implementation Guide
- ## 1. Purpose
- ## 3. Pre-flight Validation (STOP Conditions)
- ## 4. Log Header Format and Location
- ## 7. Runner Workflow (Step-wise)
- ## 9. Minimal Scope for Case-01
- ## 10. Test Matrix (Minimal)

Quoted phrases:
- L1: "# Phase-6 — Excerpt-Aware Runner Implementation Guide"
- L10: "This guide translates the Phase-6 excerpt-aware runner design into an implementation-focused checklist."
- L11: "It does not change governance and does not authorize runs by itself."
- L32: "Before any workflow begins:"
- L63: "Log headers are documentary; they do not enforce governance."
- L110: "## 7. Runner Workflow (Step-wise)"
- L150: "No additional lifecycle or governance changes are permitted in this phase."
- L167: "Each failure case must STOP before the workflow is considered valid."

## docs/P6_EXCERPT_BINDING_INTEGRATION_PLAN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Excerpt Binding Integration Plan
- ## 1. Purpose & Background
- ## 2. Design Principles
- ### 3.1 Design Layer — Pilots & Cases
- ### 3.4 Workflow JSON Layer — Annotator / Challenger / Crew
- ### 3.5 Evaluation & Synthesis Layer
- ## 4. Application to Current Workflows
- ## 5. Phasing & Next Steps
- ## 6. Governance & Boundaries
- ## 7. Checklist for Future Work

Quoted phrases:
- L1: "# Phase-6 — Excerpt Binding Integration Plan"
- L4: "Related: P6_EXCERPT_BINDING_SPEC.md, P6_EDITORIAL_WORKFLOW_MINI.md, P6_WORKFLOW_SAYUR_MINI.md, P6_SAYUR_INTERNAL_WORK_CASE01.md"
- L12: "- glossary- en workflow-pilots kunnen draaien zonder dat excerpt-keuze goed “gebonden” is aan logs en artefacts;"
- L38: "Bestaande runs uit Phase-4/5/6 blijven zoals ze zijn; we annoteren hoogstens dat excerpt-metadata ontbrak."
- L45: "- workflow JSON,"
- L59: "- pilot-plannen (bijv. P6_SAYUR_MINI_WORKFLOW_PILOT_PLAN.md),"
- L126: "### 3.4 Workflow JSON Layer — Annotator / Challenger / Crew"
- L168: "- P6_SAYUR_MINI_WORKFLOW_PILOT*_EVALUATION.md"
- L169: "- P6_SAYUR_MINI_WORKFLOW_PILOT_SYNTHESIS.md"
- L184: "- Synthese-documenten vermelden excerpt-binding wanneer traceability een rol speelt in de beoordeling van workflow-gezondheid."
- L204: "## 4. Application to Current Workflows"
- L233: "**Phase A — Documentation & Templates (NOW)**"
- L235: "- Workflow-docs en evaluatie-templates noemen nu expliciet excerpt-metadata."
- L238: "**Phase B — Runner Design (LATER, documentair)**"
- L244: "**Phase C — Runtime Instrumentation (DEFERRED)**"
- L245: "- Pas na governance-goedkeuring wordt de Python-runtime aangepast."
- L251: "Dit plan dekt alleen Phase A en de ontwerp-randvoorwaarden voor B/C."
- L255: "## 6. Governance & Boundaries"
- L263: "- Human Gate blijft vereist voor:"
- L264: "- canonieke editorial beslissingen,"
- L265: "- workflow-wijzigingen met publicatie-impact,"
- L268: "- Bestaande runs uit Phase-3/4/5/6 worden niet herschreven om excerpt-binding te simuleren."
- L274: "Bij nieuwe excerpt-gebaseerde workflows:"

## docs/P6_EXCERPT_BINDING_RUNTIME_DESIGN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Excerpt Binding Runtime Design (Documentary)
- ## 1. Purpose
- ## 3. CLI / Runner Contract
- ## 4. Logging Format (runtime logs)
- ## Runtime propagation contract (excerpt_id/source/version)
- ### Behavioural rules
- ### Backwards compatibility

Quoted phrases:
- L1: "# Phase-6 — Excerpt Binding Runtime Design (Documentary)"
- L4: "Related: P6_EXCERPT_BINDING_SPEC.md, P6_EXCERPT_AWARE_RUNNER_DESIGN.md, P6_EDITORIAL_WORKFLOW_MINI.md"
- L10: "Excerpt binding exists to keep runs traceable, reproducible, and reversible across Phase-6 workflows."
- L17: "> “Excerpt metadata does not create runtime authority. Human review remains decisive.”"
- L31: "## 3. CLI / Runner Contract"
- L34: "All three fields are optional in early Phase-6, but when provided they MUST be copied unchanged into logs."
- L48: "A Phase-6 log should contain at minimum:"
- L66: "Excerpt metadata propagates as follows:"
- L76: "6. Human Gate & Review Notes"
- L85: "Excerpt metadata is the linking key that ties runs back to source text and workflow context."
- L86: "It supports reconstruction of: which excerpt, which workflow design, and which artefacts were produced."
- L90: "8. Out of Scope (Phase-6 boundary)"
- L94: "- no canonical approvals,"
- L97: "“Excerpt binding improves visibility; governance remains human.”"
- L101: "## Runtime propagation contract (excerpt_id/source/version)"
- L134: "- SOFT-STOP: do not start the workflow; write a short log entry explaining the missing field and exit with a clear error."
- L136: "- Governance-STOP for that artefact; mark the run invalid for review and require a re-run with proper metadata."
- L148: "but are NOT acceptable for Phase-6 excerpt-bound runs."

## docs/P6_EXCERPT_BINDING_SPEC.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 Specification — Excerpt Binding & Traceability
- ## 1. Background
- ## 2. Goal
- ## 5. Example (SAYUR mini workflow)
- ## 6. Governance Boundary
- ## 7. Next Step (documentary only)

Quoted phrases:
- L1: "# Phase-6 Specification — Excerpt Binding & Traceability"
- L8: "It is a workflow binding gap: the workflow did not explicitly carry"
- L12: "Ensure that every workflow execution can answer, with evidence:"
- L52: "## 5. Example (SAYUR mini workflow)"
- L70: "## 6. Governance Boundary"
- L79: "Human Gate remains the only authority to canonize decisions."
- L82: "Update pilot templates and workflow docs so that excerpt metadata"

## docs/P6_HUMAN_REVIEW_WORKFLOW.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 Human Review Workflow (Draft)
- ## Purpose
- ### 3) READY_FOR_HUMAN_REVIEW
- ### 4) CANONICAL (Human-Only Lane)
- ## Rollback Model
- ## Human Review Participation Model
- ## Next Steps
- ## Linking to the Canonical Index

Quoted phrases:
- L1: "# Phase-6 Human Review Workflow (Draft)"
- L5: "without ever becoming canonical automatically. Phase-6 focuses on infrastructure,"
- L66: "- silently promote to canonical"
- L70: "### 4) CANONICAL (Human-Only Lane)"
- L71: "Only humans (editors) may declare something canonical."
- L87: "Canonisation must never occur silently,"
- L122: "4) only where appropriate, a canonical decision record is created."
- L126: "> Human reviewers do not “chase” the workflow while it runs."
- L130: "and guarantees that canonical status only emerges from deliberate human judgment."
- L135: "- connect human decisions to CANONICAL_INDEX"
- L137: "## Linking to the Canonical Index"
- L139: "When a human decision eventually promotes material into CANONICAL state,"
- L140: "the canonical entry must:"
- L147: "The CANONICAL_INDEX never stores AI output itself — only stable,"

## docs/P6_IMPLEMENT_EXCERPT_AWARE_RUNNER_TASKLIST.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 — Implement Excerpt-Aware Runner (Task List)
- ## Task 4 — Pipeline invocation (no governance changes)

Quoted phrases:
- L1: "# Phase-6 — Implement Excerpt-Aware Runner (Task List)"
- L3: "This is a practical task list for implementing `sandbox/crew/run_excerpt_workflow.py`"
- L4: "in line with the Phase-6 implementation guide and the Case-01 plans."
- L54: "## Task 4 — Pipeline invocation (no governance changes)"
- L58: "- Do not change prompts, governance, or lifecycle logic."

## docs/P6_LOBAK_INTERNAL_WORK_CASE02.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — LOBAK Internal Workflow — Case 02
- ## 1. Purpose
- ## 3. Lifecycle Expectations
- ## 6. What This Case Does NOT Do
- ## 8. Runner mapping status (Phase-6, documentary)
- ### 8.3 Out of scope (Phase-6 boundary)

Quoted phrases:
- L1: "# Phase-6 — LOBAK Internal Workflow — Case 02"
- L4: "Related: P6_EDITORIAL_WORKFLOW_MINI.md, P6_EXCERPT_BINDING_SPEC.md,"
- L11: "Case-02 exists to prove that the Phase-6 editorial mini-workflow:"
- L43: "CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL"
- L49: "- canonical outcomes are **out of scope** for this case."
- L83: "- produce canonical glossary entries,"
- L85: "- bypass Human Gate,"
- L106: "## 8. Runner mapping status (Phase-6, documentary)"
- L145: "### 8.3 Out of scope (Phase-6 boundary)"

## docs/P6_NOTE_SAYUR_RUNNER_EXCERPT_LOCK.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 Note — SAYUR Runner and Excerpt Locking
- ## Interpretation
- ## Implication for Phase-6
- ## Next step (documentary only)

Quoted phrases:
- L1: "# Phase-6 Note — SAYUR Runner and Excerpt Locking"
- L17: "It is a workflow binding issue: the runner currently does not take an explicit excerpt-ID or excerpt-path as governed input."
- L19: "## Implication for Phase-6"
- L21: "the SAYUR workflow should accept an explicit excerpt reference and log it"
- L25: "Design a small change to the workflow specification:"

## docs/P6_PHASE_STATUS_SNAPSHOT.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Status Snapshot
- ## 1) What Phase-6 is about
- ## 2) What is DONE
- ## 5) Guardrails & governance reminders

Quoted phrases:
- L1: "# Phase-6 — Status Snapshot"
- L3: "## 1) What Phase-6 is about"
- L5: "Phase-6 consolidates a governed, excerpt-aware editorial workflow for Mustikarasa."
- L14: "- Excerpt‑binding runtime contract and runner output layout are now frozen (see P6_EXCERPT_BINDING_RUNTIME_DESIGN.md and P6_RUNNER_OUTPUT_LAYOUT.md)."
- L17: "- Editorial mini‑workflow documented as generic (not SAYUR‑only)."
- L30: "## 5) Guardrails & governance reminders"
- L32: "- No canonical edits via agents."

## docs/P6_PHASE_STATUS_SUMMARY.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Status Summary (Mustikarasa Editorial Workflows)
- ## 1. What Phase-6 Has Delivered
- ## 2. What Is Intentionally Pending
- ## 3. How Decisions Flow (Lifecycle Reminder)
- ## 6. What Comes Next (Likely Path)
- ## 7. How This Document Should Be Used

Quoted phrases:
- L1: "# Phase-6 — Status Summary (Mustikarasa Editorial Workflows)"
- L8: "## 1. What Phase-6 Has Delivered"
- L10: "Phase-6 has delivered:"
- L12: "- a generic mini editorial workflow that applies across chapters,"
- L19: "> Phase-6 focuses on *explainable workflows*, not speed."
- L30: "- no canonical glossary or translation work yet."
- L38: "CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL"
- L41: "Only humans promote beyond provisional, and Human Gate is required for canonical moves."
- L42: "Phase-6 examples (Case-01 readiness, Pilot evaluations) follow this discipline."
- L77: "- gradual consolidation toward production workflows."
- L79: "> No runtime work happens automatically — everything is gated."
- L86: "- Use this summary to orient across workflows and current Phase-6 state."
- L87: "- Confirm decisions with CANONICAL_INDEX and governance documents."
- L88: "- Update this file whenever Phase-6 materially advances."

## docs/P6_PRODUCTION_WORKFLOW_SAYUR.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Production-oriented Workflow (SAYUR)
- ## 1. Principles
- ### 2.2 Scholarly Edition Layer
- ### 2.4 Challenger Review (Agents)
- ### 2.6 Human Gate (Editorial)
- ### 2.7 Translation & Publication (later stage)
- ## 3. Artefact Map (what exists after each stage)
- ## 5. Rollback Patterns
- ## 6. Boundaries of Autonomy
- ## 7. Hand-offs and Checkpoints
- ## 8. Phase-6 Implementation Strategy

Quoted phrases:
- L1: "# Phase-6 — Production-oriented Workflow (SAYUR)"
- L3: "This document describes the end-to-end editorial workflow for the SAYUR material,"
- L4: "from historical source → scholarly edition → provisional reasoning → Human Gate → canonical editorial decisions,"
- L15: "- Agents reason provisionally; humans make canonical decisions."
- L18: "- Human Gate sits between *provisional* and *canonical*."
- L19: "- Translation comes only after canonical editorial work."
- L35: "- nothing becomes canonical without Human Gate approval"
- L46: "Output: challenge notes (risk, bias, governance concerns)"
- L59: "### 2.6 Human Gate (Editorial)"
- L61: "Output: canonical editorial decisions"
- L62: "Lifecycle: CANONICAL"
- L69: "Input: canonical editorial text + glossary + commentary"
- L72: "- translation follows canonical editorial layer, never leads it"
- L73: "- culturally sensitive decisions must trace back to Human Gate notes"
- L81: "- /sandbox/workflows/... (provisional agent + crew artefacts)"
- L82: "- /editorial/decisions/... (Human Gate outputs)"
- L83: "- /canonical/... (approved text + notes)"
- L111: "Rollback is a governance action, not an agent one."
- L125: "- publish or rewrite canonical text"
- L132: "- Agent Crew → Human Gate (mandatory checkpoint)"
- L133: "- Human Gate → Canonical (requires justification entry)"
- L134: "- Canonical → Translation (requires editorial readiness note)"
- L140: "## 8. Phase-6 Implementation Strategy"
- L148: "4) translation remains deferred until canonical material stabilizes"

## docs/P6_REPOSITORY_ARCHIVIST_INTEGRATION.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Repository Archivist Integration Guide
- ## 2. When the Archivist Acts (Checkpoints)
- ## 3. What the Archivist Checks
- ## 5. Relationship With Governance
- ## 6. Example Workflow (Documentary)

Quoted phrases:
- L1: "# Phase-6 — Repository Archivist Integration Guide"
- L4: "Related: docs/runbooks/REPOSITORY_ARCHIVIST_RUNBOOK.md, docs/P6_RUNNER_OUTPUT_LAYOUT.md, docs/P6_EXCERPT_BINDING_RUNTIME_DESIGN.md, docs/P6_PHASE_STATUS_SNAPSHOT.md"
- L23: "The Archivist is used at defined Phase-6 checkpoints:"
- L25: "1) After new Phase-6 design docs are added or changed."
- L51: "- Phase-6 docs are discoverable from navigation/index documents,"
- L72: "## 5. Relationship With Governance"
- L77: "- Human Gate review,"
- L81: "Governance decisions remain human-only."
- L85: "## 6. Example Workflow (Documentary)"

## docs/P6_REPO_ARCHITECTURE_MIGRATION_PLAN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Repo Architecture Migration Plan (SAYUR)
- ## 1. Goals
- ### 2.4 /editorial
- ### 2.5 /canonical
- ## 3. Mapping Table (workflow → repo)
- ## 4. Movement Rules
- ## 5. Migration Phasing
- ## 6. Risks & Safeguards
- ## 7. Next Actions (documentary)

Quoted phrases:
- L1: "# Phase-6 — Repo Architecture Migration Plan (SAYUR)"
- L4: "to reflect the production workflow described in P6_PRODUCTION_WORKFLOW_SAYUR.md."
- L15: "- Require Human Gate review when materials cross lifecycle boundaries."
- L31: "Human Gate deliberation artefacts and decision logs."
- L33: "### 2.5 /canonical"
- L43: "## 3. Mapping Table (workflow → repo)"
- L47: "Annotation / Challenger / Crew → /sandbox/workflows"
- L49: "Canonicalization → /canonical"
- L60: "- Moving from editorial → canonical requires Human Gate entry."
- L61: "- Moving from canonical → public requires editorial readiness notes."
- L70: "Phase A — Document current reality (no moves)."
- L71: "Phase B — Create empty target folders with README markers."
- L72: "Phase C — Move a limited set of artefacts with audit notes."
- L73: "Phase D — Broader migration once patterns are validated."
- L82: "- Risk: re-organizing too soon → Mitigation: migration phases."
- L83: "- Risk: unclear ownership → Mitigation: Human Gate checkpoints."
- L89: "1) Review this plan against P6_PRODUCTION_WORKFLOW_SAYUR.md"

## docs/P6_RUNNER_OUTPUT_LAYOUT.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Runner Output Layout (Excerpt-Aware Runs)
- ## 3. Top-Level Locations
- ## Design contract (Phase-6)
- ## 4. Log Layout (Design)
- ## 5. JSON Artefact Layout (Design)
- ## Example tree (sample run)

Quoted phrases:
- L1: "# Phase-6 — Runner Output Layout (Excerpt-Aware Runs)"
- L41: "Phase-6 distinguishes between:"
- L53: "## Design contract (Phase-6)"
- L58: "- excerpt_id must match the runtime propagation contract"
- L84: "Existing Phase-4/5 logs remain unchanged; this pattern applies to future excerpt-aware runs."
- L96: "Within that directory, Phase-6 expects at minimum:"
- L204: "9. Governance and Boundaries"
- L211: "does NOT decide what is canonical."
- L219: "If implementation deviates from this layout, a Phase-6 design update is required."

## docs/P6_RUNNER_PAYLOAD_REFINEMENT_DESIGN.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 — Runner Payload Refinement Design
- ### Example (challenger_primary.json)
- ## 5. Implementation Note (Future Work)

Quoted phrases:
- L2: "# Phase-6 — Runner Payload Refinement Design"
- L4: "Status: DRAFT (Phase-6)"
- L69: "{ "line": 54, "span": "...", "issue_type": "GOVERNANCE", "severity": "WARNING", "comment": "..." }"
- L99: "No lifecycle changes or governance shifts are implied by this refinement."

## docs/P6_SAYUR_INTERNAL_WORK_CASE01.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # SAYUR Internal Workflow — Case 01
- ### Excerpt metadata (Phase-6)
- ## 2. Why This Excerpt
- ## 3. Workflow Artefacts (will be filled during the run)
- ## 3a. Planned runner invocation (design only)
- ## 4. Notes

Quoted phrases:
- L1: "# SAYUR Internal Workflow — Case 01"
- L4: "generic Phase-6 Editorial Mini-Workflow."
- L6: "It is NOT a pilot. It is a normal internal workflow run"
- L24: "### Excerpt metadata (Phase-6)"
- L41: "- appropriate as the first internal application of the generic workflow"
- L45: "## 3. Workflow Artefacts (will be filled during the run)"
- L49: "sandbox/workflows/sayur_internal/case01/"
- L62: "python sandbox/crew/run_excerpt_workflow.py \"
- L76: "If the workflow feels too heavy or unclear,"
- L83: "This pending status remains until an excerpt-aware runner is implemented and explicitly approved via governance."

## docs/P6_WORKFLOW_SAYUR_MINI.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # P6 — SAYUR Mini Workflow (Excerpt → Crew-Provisional)
- ## 1. Scope & Principles
- ## 2. Roles and Autonomy
- ## 3. Inputs and Outputs (Contracts)
- ## 4. Step-by-Step Workflow
- ## 5. Escalation Rules
- ## 6. Logging Requirements
- ## 7. Repo Mapping (document-only)
- ## 8. Definition of Done

Quoted phrases:
- L1: "# P6 — SAYUR Mini Workflow (Excerpt → Crew-Provisional)"
- L4: "Document-first, sandbox-only workflow for a single SAYUR excerpt; no publication impact."
- L6: "with Human Gate reserved for selective cases (see `docs/PRODUCTION_GUARDRAILS_P5.md`"
- L8: "`docs/GOVERNANCE_BOUNDARIES_NOTE.md`)."
- L13: "aggregates annotator + challenger outputs into a CREW_PROVISIONAL trace, with rationale logged."
- L14: "Codex/meta orchestrates and may reopen weak rationale but does not set CANONICAL; Human Gate"
- L15: "remains the only path to CANONICAL (see `docs/PRODUCTION_GUARDRAILS_P5.md`"
- L18: "## 3. Inputs and Outputs (Contracts)"
- L20: "decisions outside lifecycle fields (see `docs/WORKFLOW.md` and `docs/P5_DECISION_LIFECYCLE.md`)."
- L69: "## 4. Step-by-Step Workflow"
- L75: "(no automatic promotion to CANONICAL)."
- L82: "Escalate to Human Gate selectively when criteria in"
- L83: "`docs/10-governance/HUMAN_GATE_POLICY_P4_SANDBOX.md` and"
- L89: "- any action implying structural repo change (see `docs/GOVERNANCE_BOUNDARIES_NOTE.md`)"
- L98: "per `docs/WORKFLOW.md`. Known failure modes (translation-expectation bias,"
- L102: "All artefacts map to `sandbox/workflows/p6_sayur_mini/*` for traceability"
- L106: "Workflow executed with majority CREW_PROVISIONAL outputs, minimal escalations, and complete logs."

## docs/P7_CANONICAL_TRAIL_SPEC.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-7 — Canonical Decision Trail Specification
- ## Purpose
- ## Canonical Decision Record (Draft Schema)
- ## Lifecycle Overview
- ## Human Review Participation Model
- ## NO AUTO-PROMOTION (Human Gate Guarantee)

Quoted phrases:
- L1: "# Phase-7 — Canonical Decision Trail Specification"
- L4: "Define how a *proposal* becomes a *canonical editorial decision*,"
- L7: "source → excerpt → run → AI proposal → human review → canonical decision."
- L9: "Nothing becomes canonical silently."
- L11: "## Canonical Decision Record (Draft Schema)"
- L13: "Every canonical decision must contain:"
- L29: "3. Human creates a canonical decision record"
- L30: "4. Record is indexed and becomes part of the canonical trail"
- L48: "4) only where appropriate, a canonical decision record is created."
- L52: "> Human reviewers do not “chase” the workflow while it runs."
- L56: "and guarantees that canonical status only emerges from deliberate human judgment."
- L58: "## NO AUTO-PROMOTION (Human Gate Guarantee)"
- L60: "Canonical status may NEVER be assigned automatically."
- L63: "- Runners and scripts cannot promote anything to CANONICAL."
- L64: "- Only a human reviewer, through a recorded canonical decision,"
- L65: "can create canonical status."

## docs/P7_DECISION_TYPES.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-7 — Decision Types Matrix
- ## Purpose
- ## Matrix (Draft — Phase-7 Work in Progress)

Quoted phrases:
- L1: "# Phase-7 — Decision Types Matrix"
- L9: "- HUMAN ONLY (canonical judgment, interpretive, or cultural meaning)"
- L14: "## Matrix (Draft — Phase-7 Work in Progress)"
- L28: "At the end of Phase-7 this table must be complete and stable."

## docs/P8_CAPABILITY_MAP.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-8 Capability Map — Editorial System Maturity
- ## 1. Purpose
- ### 2.1 Text Acquisition & Integrity
- ### 2.2 Structure & Navigation
- ### 2.3 Glossary & Knowledge Management
- ### 2.4 Text-Critical / Variants
- ### 2.5 Editorial Quality & Readability
- ### 2.6 Trail & Reproducibility
- ### 2.7 Reviewer Support & Triage
- ## 3. Maturity Model
- ## 4. Capability × Maturity × Responsibility Matrix
- ## 5. Derived Role Implications (No Roles Yet)
- ## 6. Alignment with Guardrails
- ## 7. Next Step from Capability Map

Quoted phrases:
- L1: "# Phase-8 Capability Map — Editorial System Maturity"
- L5: "Phase-8 designs capabilities first; agent roles are derived from those"
- L6: "capabilities, not the other way around. Governance remains unchanged:"
- L7: "canonical decisions are human-only, and rollback occurs via new records."
- L15: "- Relation to canonical decisions: supports trustworthy evidence for later human decisions."
- L21: "- Relation to canonical decisions: keeps context stable for review, not a canonical decision itself."
- L27: "- Relation to canonical decisions: supports lemma inclusion decisions; meanings remain human-only."
- L33: "- Relation to canonical decisions: provides evidence bundles for human variant choices."
- L39: "- Relation to canonical decisions: advisory signals only; not a decision lane."
- L45: "- Relation to canonical decisions: required mechanical integrity before human gate."
- L51: "- Relation to canonical decisions: accelerates review without changing authority."
- L56: "- Level 1 — documented workflow"
- L58: "- Level 3 — tool/validator assisted (mechanical certainty)"
- L59: "- Level 4 — orchestration-aware collaboration (still human-only canonical)"
- L61: "Phase-8 typically aims for Level 2 → 3."
- L65: "| Capability | Current Maturity (estimate) | Phase-8 Target | Responsibility Model |"
- L67: "| Text Acquisition & Integrity | Level 1 | Level 3 | TOOL/VALIDATOR |"
- L72: "| Trail & Reproducibility | Level 2 | Level 3 | TOOL/VALIDATOR |"
- L80: "- Phase-8 priority: validator-style checks before review."
- L84: "- Must NEVER: reorganize canonical content or declare canonical structure."
- L85: "- Phase-8 priority: provisional diagnostics only."
- L89: "- Must NEVER: assign meanings or promote canonically."
- L90: "- Phase-8 priority: clean lemma signals + provenance."
- L94: "- Must NEVER: choose a variant or decide canonical readings."
- L95: "- Phase-8 priority: evidence bundling for human review."
- L99: "- Must NEVER: rewrite text or imply final editorial authority."
- L100: "- Phase-8 priority: advisory-only signals."
- L104: "- Must NEVER: mark CANONICAL or modify records."
- L105: "- Phase-8 priority: mechanical completeness checks."
- L110: "- Phase-8 priority: reduce reviewer overhead without changing authority."
- L114: "- Canonical trail remains untouched."
- L116: "- Validators help but do not gatekeep canonical promotion."
- L131: "- author: HumanGate-Editorial + Architecture"
- L134: "- docs/P8_PHASE_START_ARCHITECTURE.md"
- L135: "- docs/P7_CANONICAL_TRAIL_SPEC.md"

## docs/P8_PHASE_START_ARCHITECTURE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-8 Architecture & Start — Agentic Work Within Canonical Rails
- ## 1. Context and Inheritance
- ## 2. Phase-8 Goals (What Phase-8 WILL do)
- ## 3. Non-Goals (What Phase-8 Will NOT Do)
- ## 4. Agentic Capabilities in Phase-8
- ### 4.1 Agent Roles (examples)
- ### 4.2 Agent Constraints
- ## 5. Orchestration Patterns (Agentic Workflows)
- ## 6. Human Workload & Interaction Model
- ## 7. Risks and Mitigations
- ## 8. Phase-8 Deliverables (Architecture-Level)
- ## 9. Alignment with Existing Guardrails

Quoted phrases:
- L1: "# Phase-8 Architecture & Start — Agentic Work Within Canonical Rails"
- L5: "Phase-7 established canonical decision trails with a human-only canonical gate,"
- L7: "and canonical decisions. Phase-8 inherits these guardrails and MUST NOT change them."
- L9: "- Phase-7 outcome: canonical trail proven on a low-risk glossary case (“lobak” lemma)."
- L10: "- Agents are provisional; all canonical decisions are human-only."
- L13: "## 2. Phase-8 Goals (What Phase-8 WILL do)"
- L15: "- Reduce unnecessary human workload by improving agent support, NOT by granting agents more authority."
- L18: "- Introduce light-weight validators and checkers that run before the human gate (e.g. excerpt-binding, trail completeness)."
- L19: "- Keep all AI output strictly provisional, clearly separated from canonical decisions."
- L21: "## 3. Non-Goals (What Phase-8 Will NOT Do)"
- L23: "- No new governance layers or decision types that weaken Phase-7 guardrails."
- L24: "- No auto-promotion to CANONICAL, no automated creation of canonical decision records."
- L28: "## 4. Agentic Capabilities in Phase-8"
- L42: "- Validates whether a canonical decision record is mechanically complete"
- L49: "- create or update canonical decision records,"
- L50: "- modify canonical indices,"
- L51: "- set lifecycle to CANONICAL."
- L53: "## 5. Orchestration Patterns (Agentic Workflows)"
- L64: "All flows end in READY_FOR_HUMAN_REVIEW, never in CANONICAL."
- L65: "Human review sessions are the only place where canonical decisions are made."
- L72: "- making canonical decisions,"
- L81: "Phase-8 features (better agents + validators) should support this without"
- L82: "changing authority or responsibility."
- L91: "- Mitigation: add preflight validators and ensure trails are single source of truth."
- L93: "## 8. Phase-8 Deliverables (Architecture-Level)"
- L98: "- P8_PILOTS_PLAN.md — plan for a small set of Phase-8 pilots (e.g. OCR/typographic, structural, glossary support)."
- L102: "Phase-8 respects:"
- L105: "- Phase-6 infrastructure (excerpt-binding, runner),"
- L106: "- Phase-7 canonical trail spec and decision types."
- L111: "- Human gate is the only path to CANONICAL."
- L115: "- author: HumanGate-Editorial + Architecture/Agentic-Design"
- L119: "- docs/P7_CANONICAL_TRAIL_SPEC.md"
- L120: "- docs/retros/P7_PHASE_RETRO_REPO_VIEW.md"

## docs/PHASE3_FRAMING.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # PHASE-3 FRAMING — Pilots, Safety & Learning
- ## 1. What Phase-3 really is
- ## 2. Objectives of Phase-3
- ### In scope
- ### Out of scope
- ## 4. Data & Artefact Handling
- ### 5.4 Governance-Failure Simulation
- ## Failure Notebook (verplicht)
- ## 6. Risk model for Phase-3
- ## 7. Human involvement model
- ## 8. Exit criteria
- ## 9. After Phase-3
- ## Addendum — Phase-3 Status (Documentary)

Quoted phrases:
- L1: "# PHASE-3 FRAMING — Pilots, Safety & Learning"
- L3: "## 1. What Phase-3 really is"
- L4: "Phase-3 is de eerste **gecontroleerde interactie** tussen agents en echte content."
- L8: "- hoe governance ingrijpt"
- L12: "Phase-3 is nadrukkelijk géén automatische productiestap."
- L21: "## 2. Objectives of Phase-3"
- L22: "Phase-3 heeft leerdoelen, geen productie-doelen."
- L26: "- governance-triggers afgaan waar dat hoort"
- L27: "- incidenten leiden tot governance-stop (en niet tot “doorgaan”)"
- L42: "- governance trigger validation"
- L47: "- gebruik van Phase-3 output als eindproduct"
- L51: "Phase-3 mag inzichten genereren,"
- L58: "- pilots mogen **nooit canonical bronnen overschrijven**"
- L64: "- canonical bronnen zijn read-only"
- L67: "Phase-3 mag experimenteren — maar alleen met veilig, herleidbaar materiaal."
- L79: "### 5.4 Governance-Failure Simulation"
- L80: "Doel: aantonen dat soft-stop → governance-stop → human-gate werkt."
- L83: "(proposal-only, lifecycle-driven, governance-stop demonstratie)"
- L90: "- governance-evaluatie"
- L95: "## 6. Risk model for Phase-3"
- L97: "Mitigaties: labels, disclaimers, red-team, governance-triggers."
- L100: "Editors contextualiseren, governance besluit bij risico,"
- L102: "human-gate = laatste escalatie."
- L105: "Phase-3 slaagt wanneer:"
- L106: "- governance-stops optreden waar verwacht"
- L112: "> Phase-3 eindigt met **kennis, niet met een product.**"
- L114: "## 9. After Phase-3"
- L118: "## Addendum — Phase-3 Status (Documentary)"
- L120: "Phase-3 has generated enough pilot evidence to support reflection and"
- L121: "readiness discussions. This does NOT mean Phase-3 is closed, and it does"
- L122: "NOT authorize Phase-4."
- L124: "Phase-3 remains available as a learning space that can be reopened"
- L125: "whenever new risks, terminology conflicts, or governance uncertainties"
- L133: "Status note added for clarity. No phase transition declared."

## docs/PHASE3_GOVERNANCE_SYNTHESIS_OCR_AMBIGUITY.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-3 Governance Synthesis — OCR & Ambiguity
- ## 1. Scope
- ## 2. What We Tested (Overview)
- ## 4. Where Governance Worked
- ## 6. Methodology Principles (Phase-3, Not Policy)
- ## 7. Implications for Future Phases (Non-binding)
- ## 8. Open Questions (to revisit later)

Quoted phrases:
- L1: "# Phase-3 Governance Synthesis — OCR & Ambiguity"
- L4: "This synthesis summarizes Phase-3 pilot learning on OCR ambiguity handling and governance behavior. It captures observations and risks without introducing policy or behavior changes."
- L11: "- escalation / Human Gate: docs/PILOT_MARKER2_ESCALATION_RUN_P3_MARKER2_ESCALATION_001.md"
- L19: "## 4. Where Governance Worked"
- L21: "- Governance-stops created documentation instead of action."
- L22: "- Human Gate provided reasoning rather than automatic authority."
- L32: "## 6. Methodology Principles (Phase-3, Not Policy)"
- L38: "## 7. Implications for Future Phases (Non-binding)"
- L46: "- What audit evidence must always accompany Human Gate?"

## docs/PHASE3_READINESS_REVIEW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-3 Readiness Review (Documentary)
- ## Purpose
- ## What Phase-3 Demonstrated (documentary)
- ## Constraints That Must Travel Forward
- ## Evidence Links

Quoted phrases:
- L1: "# Phase-3 Readiness Review (Documentary)"
- L5: "Take stock of Phase-3 pilots as a learning phase — not production. Assess whether the system behaves safely under ambiguity and pressure, while avoiding decisions about Phase-4."
- L7: "## What Phase-3 Demonstrated (documentary)"
- L10: "- governance can stop & log without panic"
- L25: "- proposal-only until Human Gate or lifecycle approval"
- L27: "- explicit governance stops for high-risk ambiguity"
- L45: "- docs/PILOT_WORKFLOW_SYNTHESIS_RUN_P3_WORKFLOW_001.md"
- L46: "- docs/PILOT_WORKFLOW_MAP_RUN_P3_WORKFLOWMAP_001.md"
- L50: "Scope: summarize Phase-3 learning without declaring Phase-4 readiness."
- L57: "Expected: reflection only, no Phase-4 approval."
- L58: "Observed: temptation to “green-light Phase-4.”"

## docs/PHASE4_READINESS_NOTES.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-4 Readiness Notes (Documentary)
- ## Purpose
- ## Non-Negotiable Constraints (must travel forward)
- ## Risks If Forgotten
- ## What Phase-4 Must Re-Validate
- ## Evidence Cross-References

Quoted phrases:
- L1: "# Phase-4 Readiness Notes (Documentary)"
- L5: "Record the constraints and risks that Phase-4 must respect. This is NOT a go-ahead document and does NOT declare readiness."
- L8: "These are constraints from Phase-3 observations, not new rules:"
- L12: "- governance stops precede fixes"
- L21: "- over-confidence replacing governance checks"
- L23: "## What Phase-4 Must Re-Validate"
- L26: "- governance logs don’t get skipped"
- L31: "- docs/PHASE3_READINESS_REVIEW.md"
- L45: "- docs/PILOT_WORKFLOW_SYNTHESIS_RUN_P3_WORKFLOW_001.md"
- L46: "- docs/PILOT_WORKFLOW_MAP_RUN_P3_WORKFLOWMAP_001.md"
- L53: "Scope: capture constraints and risks without implying Phase-4 approval."
- L54: "Method: compile Phase-3 constraints; avoid roadmap language."

## docs/PILOT_ANNOTATION_READABILITY_RUN_P3_ANNOTATION_READABILITY_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L63: "## Consolidation Summary (Phase-3)"
- L73: "Governance behavior:"
- L74: "The pilot stayed observational. Any future editorial guidelines must go through the glossary/workflow lifecycle, not emerge from a"
- L78: "Annotation is powerful, but it is not neutral. The more it accumulates, the more it shapes reading. That effect needs governance —"

## docs/PILOT_ANNOTATION_RETENTION_RUN_P3_ANNOTATION_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Purpose
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L6: "Investigate when retaining original culinary terms is preferable to translating, and how annotations can clarify meaning without altering text."
- L63: "## Consolidation Summary (Phase-3)"
- L73: "Governance behavior:"
- L74: "All patterns remained proposal-only. Any real adoption must pass the glossary lifecycle and Human Gate, not this pilot."

## docs/PILOT_GLOSSARY_DAGING_RUN_P3_DAGING_001.md

Preliminary classification suggestion: GOV-B

Relevant section headings:
- ## Purpose
- ## Human Gate Triggers (documentary)
- ## Agent Perspectives
- ## Exit Criteria

Quoted phrases:
- L6: "Examine how “daging” shifts meaning across context (meat generally vs beef by default). Identify cultural, religious, and historical implications without choosing a canonical translation."
- L39: "## Human Gate Triggers (documentary)"
- L54: "Result: proposals recorded; Human Gate scenarios identified; no decisions made."
- L62: "Lesson: culturally sensitive terms require explicit review gates."
- L66: "Ambiguity documented; glossary proposals created; Human Gate scenarios identified — no decisions made."

## docs/PILOT_GLOSSARY_DAGING_RUN_P3_DAGING_002.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Governance Note
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L30: "## Governance Note"
- L31: "Decision deferred; Human Gate would be considered only if publication risk emerges."
- L45: "Lesson: cultural terms require explicit review gates."
- L56: "## Consolidation Summary (Phase-3)"
- L66: "Governance behavior:"
- L67: "Glossary entries stayed proposal-only. Interpretation was deferred to the glossary lifecycle and, if needed, Human Gate — not decided"

## docs/PILOT_GLOSSARY_LIFECYCLE_RUN_P3_LIFECYCLE_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Stage 4 — Governance Review (simulated)
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L27: "## Stage 4 — Governance Review (simulated)"
- L28: "Governance discusses the ambiguity but does not approve. Human Gate would trigger only if publication stakes were present."
- L61: "## Consolidation Summary (Phase-3)"
- L65: "risk review → governance discussion — without producing a decision."
- L66: "Governance adds transparency and traceability while leaving the glossary"
- L74: "Governance behavior:"
- L75: "Governance reviewed, not decided. Human Gate remained contextual and"

## docs/PILOT_GLOSSARY_LOBAK.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Goal
- ## Scope
- ## Hypothesis
- ## Workflow (documentary)
- ## Glossary Behaviour
- ## Failure Notebook
- ## Expected Governance Outcome

Quoted phrases:
- L5: "de Glossary Decision Lifecycle en governance‑stop expliciet te demonstreren,"
- L11: "- Output: proposals, research‑context en governance‑logverwachting"
- L20: "tot Human Gate."
- L22: "## Workflow (documentary)"
- L25: "3) Orchestrator markeert governance‑stop bij terminologie‑risico."
- L26: "4) Human Gate wordt expliciet uitgesteld (pilot‑only)."
- L31: "- Verwijst naar Glossary Decision Lifecycle voor risk review en Human Gate."
- L40: "- Verwacht: governance‑stop, geen automatische keuze."
- L41: "- Log: expected vs actual, lessons learned, governance‑evaluatie."
- L59: "## Expected Governance Outcome"
- L61: "- Governance‑stop geactiveerd door Orchestrator."
- L62: "- Human Gate expliciet uitgesteld (pilot‑only)."

## docs/PILOT_GLOSSARY_LOBAK_RUN_P3_LOBAK_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 5. Glossary Proposals (proposal-only)
- ## 6. Research Notes (simulated)
- ## 9. Pilot Outcome (no decisions)

Quoted phrases:
- L53: "notes: risk of confusion with generic 'radish'; context suggests white, elongated root."
- L57: "lifecycle_reference: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md"
- L68: "Recommendations: decision deferred to Human Gate in glossary lifecycle."
- L91: "- governance_agents_involved: Glossary, Research, Methodology"
- L93: "- rollback_possible: YES (documentary; no canonical sources modified)"
- L95: "EXPERIMENTAL — NOT FOR PUBLICATION. This pilot documents governance behavior only."

## docs/PILOT_GLOSSARY_LOBAK_RUN_P3_LOBAK_002.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 5. Glossary Proposals (proposal-only)
- ## 6. Research Notes (EVIDENCE ONLY)
- ## 7. Methodology Log (excerpt)
- ## 8. Failure Notebook (expected test failure)
- ## Methodology Insight (Phase-3 — Proposal)
- ## Consolidation Summary (Phase-3)
- ## 10. Pilot Outcome (no decisions)

Quoted phrases:
- L66: "lifecycle_reference: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md"
- L78: "Recommendations: decision deferred to Human Gate; proposal-only."
- L86: "Why this matters: This pilot intentionally creates a terminology conflict to test whether the workflow documents ambiguity without collapsing it into a premature decision."
- L87: "Result: ambiguity detected; governance-stop triggered; no final glossary outcome."
- L88: "Phase-3 constraint: final glossary outcomes prohibited."
- L96: "Expected: divergence should trigger governance handling without a decision."
- L99: "Reversibility: no canonical sources modified; rollback is trivial (discard pilot artefacts)."
- L107: "## Methodology Insight (Phase-3 — Proposal)"
- L109: "**Implication:** Pilot review steps should reference the canonical stored artefact, not pasted excerpts."
- L110: "**Status:** PROPOSAL — pending governance review (do not enforce yet)."
- L113: "## Consolidation Summary (Phase-3)"
- L115: "**What failed safely:** chat excerpts diverged from canonical files; ambiguity remained visible; rollback preserved."
- L116: "**Governance behavior:** soft-stop + governance-stop worked as documentary stops; decision deferred."
- L123: "- governance_stop_triggered: YES (documentary)"
- L124: "- governance_agents_involved: Glossary, Research, Methodology"
- L126: "- rollback_possible: YES (no canonical changes; delete pilot artefact)"

## docs/PILOT_GLOSSARY_SANTAN_RUN_P3_SANTAN_001.md

Preliminary classification suggestion: GOV-B

Relevant section headings:
- ## Purpose

Quoted phrases:
- L6: "Investigate ambiguity around “santan” in Mustika Rasa. Document meanings, risks, and glossary proposals — without resolving them."

## docs/PILOT_GLOSSARY_SANTAN_RUN_P3_SANTAN_002.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Governance Note
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L28: "## Governance Note"
- L54: "## Consolidation Summary (Phase-3)"
- L62: "Governance behavior:"
- L63: "Glossary entries stayed proposal-only. Decision-making was explicitly deferred to the lifecycle and Human Gate instead of being decided inside the pilot."

## docs/PILOT_GLOSSARY_UBI_KETELA_RUN_P3_UBI_001.md

Preliminary classification suggestion: GOV-B

Relevant section headings:
- ## Cultural Risk Analysis

Quoted phrases:
- L55: "Lesson: crop terms require research + Human Gate before standardization."

## docs/PILOT_GLOSSARY_UBI_KETELA_RUN_P3_UBI_002.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Evidence Notes (documentary)
- ## Governance Reflection
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L29: "notes: conflict recorded; decision deferred to lifecycle + Human Gate if needed"
- L32: "## Governance Reflection"
- L58: "## Consolidation Summary (Phase-3)"
- L71: "Governance behavior:"
- L73: "state. Human Gate is relevant only if publication stakes arise — not"

## docs/PILOT_GOV_FAILURE_DRILL_RUN_P3_FAILURE_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Pilot: Governance Failure-Drill — Accidental Decision Leak
- ## Detection Point
- ## Containment & STOP Model
- ## Lessons Learned
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L1: "# Pilot: Governance Failure-Drill — Accidental Decision Leak"
- L16: "- Governance layer notices missing lifecycle log"
- L21: "- governance-stop raised"
- L37: "- governance protects against good-faith mistakes, not bad actors only"
- L40: "Event: P3_FAILURE_001 simulated governance failure drill."
- L42: "Method: narrative-only; no workflow changes."
- L62: "## Consolidation Summary (Phase-3)"
- L65: "A simulated “decision leak” shows that governance can detect,"
- L75: "Governance behavior:"
- L77: "before any change. Human Gate stayed a forum for reasoning, not an"
- L81: "Governance protects against well-intentioned shortcuts. Proposals must"

## docs/PILOT_MARKER2_ANALYSIS_RUN_P3_MARKER2_ANALYSIS_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## Synthesis / Observations
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L27: "- Governance questions: when should OCR restoration treat “2” as a technical “²” recovery vs. a candidate for human review? How should ambiguity be flagged without rewriting?"
- L33: "Result: evidence table completed; ambiguity documented for governance review; no rules enforced."
- L38: "## Consolidation Summary (Phase-3)"
- L44: "Instead of correcting text, the pilot documented ambiguity and deferred decisions. Canonical context was consulted only as interpretation support, not as a replacement layer."
- L46: "**Governance behavior:**"

## docs/PILOT_MARKER2_ESCALATION_RUN_P3_MARKER2_ESCALATION_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Escalation Record
- ## Human Gate Stage (Simulated)
- ## Governance Notes
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L22: "- Action: cases are queued to governance review with both rationales and the original OCR lines attached."
- L25: "## Human Gate Stage (Simulated)"
- L40: "## Governance Notes"
- L42: "- Human Gate can authorize future lifecycle steps, but does not modify text in this pilot."
- L47: "Scope: model disagreement handling and Human Gate escalation for ambiguity flags."
- L56: "Mitigation: routed to Human Gate with REQUIRE_RESEARCH_NOTE; no edits made."
- L62: "## Consolidation Summary (Phase-3)"
- L65: "Reviewer disagreement on ambiguous “²-derived” cases can be handled through a structured escalation path and Human Gate discussion, with all outcomes kept provisional and no text changes applied."
- L70: "Governance behavior:"
- L71: "Escalation was triggered only by conflicting provisional decisions. Human Gate operated as a forum for reasoning, not as an automatic policy engine. All decisions remained metadata; rollback stayed trivial."
- L74: "Disagreement is a feature, not a bug, when it is documented and escalated transparently. Human Gate must always be tied to explicit evidence (e.g., scans, research notes) before any future normalization is even considered."

## docs/PILOT_MARKER2_FLAGGING_RUN_P3_MARKER2_FLAGGING_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## Governance Implications (Documentary)
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L23: "## Governance Implications (Documentary)"
- L45: "## Consolidation Summary (Phase-3)"
- L48: "Ambiguity can be reliably detected and documented without modifying OCR text. “Flag-only” workflows surfaced risk early while preserving reversibility."
- L53: "**Governance behavior:**"

## docs/PILOT_MARKER2_REVIEW_HANDOFF_RUN_P3_MARKER2_REVIEW_HANDOFF_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Governance Flow (Documentary)
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L19: "## Governance Flow (Documentary)"
- L23: "- Human Gate required only if a decision would alter canonical text or introduce a normalization policy."
- L35: "Expected: review-only workflow without normalization."
- L43: "## Consolidation Summary (Phase-3)"
- L51: "**Governance behavior:**"
- L52: "Review decisions acted as metadata only. Human Gate is triggered only when a decision would change canonical content or create policy. Rollback remains trivial."
- L55: "Review workflows add value even without automation: they reduce the risk of silent changes and ensure ambiguity is confronted transparently. Metadata must live alongside texts, never written into OCR files."

## docs/PILOT_OCR_AUTOMATION_BOUNDARY_RUN_P3_OCR_AUTOMATION_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L81: "## Consolidation Summary (Phase-3)"
- L93: "Governance behavior:"
- L95: "Governance would only authorize automation after lifecycle discussion"
- L96: "and Human Gate, not inside a pilot."

## docs/PILOT_OCR_FLAG_SCANNER_PROPOSAL_RUN_P3_OCR_FLAGSCANNER_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Risks (governance perspective)
- ## Lifecycle Path (simulated)
- ## Human Gate Trigger (simulated)
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L23: "## Risks (governance perspective)"
- L32: "3. Risk review (governance + methodology)"
- L33: "4. Governance discussion"
- L34: "5. Decision deferred — implementation prohibited in Phase-3"
- L36: "## Human Gate Trigger (simulated)"
- L37: "Would only occur if the proposal began influencing real text or workflow."
- L51: "Lesson: automation proposals must remain documentary in Phase-3."
- L60: "## Consolidation Summary (Phase-3)"
- L72: "Governance behavior:"
- L73: "Governance reviewed the idea as risk-aware documentation, not as a"
- L74: "decision. Human Gate would only apply if the proposal began shaping real"

## docs/PILOT_OCR_RESTORE_RUN_P3_OCR_RESTORE_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## Methodology Insight — “²” Marker (Phase-3 — Proposal)
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L67: "## Methodology Insight — “²” Marker (Phase-3 — Proposal)"
- L73: "## Consolidation Summary (Phase-3)"
- L76: "**Governance behavior:** soft-stops worked; no semantic changes were made; rollback stayed trivial."

## docs/PILOT_READER_IMPACT_RUN_P3_READER_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L101: "## Consolidation Summary (Phase-3)"
- L113: "Governance behavior:"
- L114: "This pilot stayed descriptive. Human Gate was not involved because no"
- L120: "Phase-3, noticing effects is enough."

## docs/PILOT_SET_P4_V1.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ### 1) SAYUR (Vegetables)
- ### 2) SANTAN (Coconut milk / extraction)
- ### 3) LOBAK (radijs/daikon context)
- ## Expected Learning
- ## Relationship to Governance

Quoted phrases:
- L3: "Title: Pilot-set v1 — Phase-4 Sandbox Preparation"
- L9: "Een kleine, representatieve set kiezen om processen, annotaties en governance"
- L24: "- annotatie-en governance-interactie"
- L26: "Human-Gate aandacht:"
- L41: "Human-Gate aandacht:"
- L54: "- glossary-workflow zonder beslissen"
- L56: "Human-Gate aandacht:"
- L77: "- hoe Human Gate praktisch wordt ingezet"
- L96: "## Relationship to Governance"
- L100: "- HUMAN_GATE_POLICY_P4_SANDBOX"

## docs/PILOT_TO_PRACTICE_GUIDE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Pilot → Practice Guide (Phase-3 Learnings)
- ## Glossary (proposal-only discipline)
- ## Workflow & Governance (stops over fixes)
- ## Reader Impact (observed effects)

Quoted phrases:
- L2: "Title: Pilot → Practice Guide (Phase-3 Learnings)"
- L4: "Scope: documentary summary of Phase-3 pilots (glossary, OCR, annotation, workflow, reader-impact)."
- L5: "Non-Policy Notice: this guide is a practical aide-mémoire for editors and agents; it does NOT change governance, lifecycle, or runtime behavior."
- L9: "# Pilot → Practice Guide (Phase-3 Learnings)"
- L12: "- proposals remain proposals until Human Gate; no silent promotion"
- L27: "## Workflow & Governance (stops over fixes)"
- L28: "- soft-stop preferred for ambiguity; governance-stop for boundary breaches"
- L29: "- Human Gate is a reasoning forum for process risk, not content approval by default"
- L35: "- document trade-offs; do not declare best practices in Phase-3"

## docs/PILOT_WORKFLOW_MAP_RUN_P3_WORKFLOWMAP_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Pilot: Workflow Map — Ambiguity & Governance (Phase-3)
- ## Diagram (documentary)
- ## Annotations (documentary)
- ## Notes from Pilots (observed)
- ## Risks (documentary)
- ## [METHODOLOGY_LOG]
- ## [FAILURE_NOTEBOOK]
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L1: "# Pilot: Workflow Map — Ambiguity & Governance (Phase-3)"
- L2: "Pilot ID: P3_WORKFLOWMAP_001"
- L26: "[Governance Layer]"
- L29: "[Human Gate]"
- L38: "- Decisions are explicitly deferred at Glossary Proposals and after Governance Layer review."
- L44: "- Daging: cultural ambiguity escalated to Human Gate consideration without decisions."
- L50: "- The map is dangerous if used to skip governance steps."
- L54: "Event: P3_WORKFLOWMAP_001 documentary diagram."
- L61: "CaseID: P3_WORKFLOWMAP_001_F1"
- L65: "Lesson: even small diagram tweaks can imply policy outside Phase-3 scope."
- L76: "## Consolidation Summary (Phase-3)"
- L80: "Governance → (rare) Human Gate. The map improved shared understanding without changing behavior. Documentation remains the primary"
- L87: "Governance behavior:"

## docs/PILOT_WORKFLOW_SYNTHESIS_RUN_P3_WORKFLOW_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Pilot: Workflow Synthesis — Ambiguity & Governance
- ## Observed Pipeline (from pilots)
- ## Failure Modes Observed (documentary)
- ## What Worked
- ## Exit Criteria
- ## Consolidation Summary (Phase-3)

Quoted phrases:
- L1: "# Pilot: Workflow Synthesis — Ambiguity & Governance"
- L2: "Pilot ID: P3_WORKFLOW_001"
- L28: "5. Governance agents"
- L32: "6. Human Gate (observed role)"
- L40: "- disagreements becoming invisible without governance logging"
- L49: "Event: P3_WORKFLOW_001 synthesis."
- L56: "CaseID: P3_WORKFLOW_001_F1"
- L58: "Observed: temptation to propose workflow fixes."
- L60: "Lesson: Phase-3 synthesis must avoid policy creation."
- L64: "Workflow relationships are documented; ambiguity lifecycle is visible; no rules changed; no new policy invented."
- L71: "## Consolidation Summary (Phase-3)"
- L74: "Ambiguity consistently travels through Translation → Readability → Fidelity → Glossary proposals → Governance documentation, with Human"
- L75: "Gate appearing rarely and only when publication or cultural risk is visible. Documentation, not decision, is the primary safety tool."
- L78: "The synthesis surfaced workflow gaps and temptations (e.g., silent simplification), but did not attempt to “fix” them. All learning"
- L81: "Governance behavior:"
- L82: "Soft-stops and proposal lifecycles worked as documentary brakes rather than decision engines. Human Gate remained a reasoning forum,"
- L87: "phases, not Phase-3."

## docs/PRODUCTION_GUARDRAILS_P5.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Production Guardrails — Autonomy Matrix (Phase 5)
- ## 1. Decision Lifecycle (reference)
- ### C) Codex / Meta-Agent
- ### D) Human Gate
- ## 5. Relationship to Governance

Quoted phrases:
- L1: "# Production Guardrails — Autonomy Matrix (Phase 5)"
- L5: "mogen nemen — individueel, als crew, via Codex/meta, of via Human Gate."
- L10: "- CANONICAL_INDEX.md"
- L29: "4) CANONICAL — alleen na Human Gate"
- L85: "- CANONICAL zetten"
- L86: "- governance wijzigen"
- L94: "### D) Human Gate"
- L136: "## 5. Relationship to Governance"
- L139: "- beschrijven praktijkgedrag (Phase 5),"
- L140: "- vervangen géén governance-policies,"
- L141: "- en worden pas normatief na Human Gate-goedkeuring."

## docs/REQUIREMENTS.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 1. Purpose & Scope
- ## 2. Terminology
- ## 3. Functional Requirements
- ## 4. Non-Functional Requirements
- ## 5. Governance Requirements
- ## 6. Automation & Safety Requirements
- ## 7. Pilot & Phase-Transition Requirements
- ## 8. Traceability to Source Docs
- ## 10. Change & Versioning

Quoted phrases:
- L6: "- Scope: pipeline, agents, governance, pilots en documentatie‑workflow."
- L13: "- Governance Agent: adviserend/loggend; neemt geen definitieve beslissingen."
- L14: "- Human Gate: expliciete menselijke beslissing bij high‑risk of finale besluiten."
- L18: "- FR-001: The system MUST support a multi‑phase recipe pipeline"
- L19: "(Translation → Readability → Fidelity). Source: docs/WORKFLOW.md, docs/total_project.md."
- L23: "make final decisions. Source: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md, prompts/glossary_agent.md."
- L25: "make final editorial decisions. Source: prompts/research_agent.md, docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md."
- L27: "and treat template definitions as contracts. Source: prompts/orchestrator.md, prompts/template_agent.md."
- L28: "- FR-006: Governance agents MUST be invokable via runtime events as designed"
- L29: "(events, inputs, outputs, logging). Source: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L31: "(input definition, per‑item processing, batch summary, artifacts). Source: docs/CHAPTER_BATCH_WORKFLOW.md."
- L35: "in docs/CODEX_SESSION_LOG.md. Source: docs/CODEX_META_PROMPT.md, docs/WORKFLOW.md."
- L43: "## 5. Governance Requirements"
- L45: "and MUST follow the stop‑model (soft‑stop → governance‑stop → human‑gate)."
- L46: "Source: docs/WORKFLOW.md, docs/AGENTS.md."
- L48: "through Human Gate before finalization. Source: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md."
- L49: "- GR-003: Governance‑stop MUST precede Human Gate in high‑risk situations."
- L50: "Source: docs/WORKFLOW.md."
- L51: "- GR-004: Governance Agents MUST NOT unilaterally change code, config or publications."
- L57: "Source: docs/CHAPTER_BATCH_WORKFLOW.md."
- L58: "- ASR-002: The system MUST NOT automatically apply glossary changes without Human Gate approval."
- L59: "Source: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md, docs/GLOSSARY_PILOT_REPORT.md."
- L61: "Source: docs/GLOSSARY_PILOT_REPORT.md, docs/10-governance/GOVERNANCE_TESTS_PLAN.md."
- L63: "an incident path. Source: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L65: "authoritative glossary or downstream content without BOTH Human Gate"
- L67: "(Sources: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md, docs/WORKFLOW.md, docs/REQUIREMENTS_CHANGE_PROCESS.md)"
- L69: "the pipeline MUST enter governance-stop and MUST NOT continue"
- L71: "through the Human Gate."
- L72: "(Sources: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md, docs/WORKFLOW.md, docs/REQUIREMENTS_CHANGE_PROCESS.md)"
- L76: "(Sources: docs/CHAPTER_BATCH_WORKFLOW.md, docs/WORKFLOW.md, docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md, docs/REQUIREMENTS_CHANGE_PROCESS.md)"
- L78: "## 7. Pilot & Phase-Transition Requirements"
- L80: "and at least one governance test scenario. Source: docs/10-governance/GOVERNANCE_TESTS_PLAN.md,"
- L81: "docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md, docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md,"
- L82: "docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L84: "Source: docs/GLOSSARY_PILOT_REPORT.md, docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L86: "Glossary + Research + Human Gate before being considered stable."
- L87: "Source: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md, docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md."
- L90: "- FR-001 → docs/WORKFLOW.md, docs/total_project.md"
- L91: "- FR-003, GR-002, ASR-002 → docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md"
- L92: "- GR-003, ASR-004 → docs/WORKFLOW.md, docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md"
- L94: "- PTR-001 → docs/10-governance/GOVERNANCE_TESTS_PLAN.md, docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md,"
- L95: "docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md"
- L105: "PHASE3_* item in docs/CODEX_TODO.md."
- L106: "- Elke wijziging MUST herleidbaar zijn naar een menselijke beslissing (Human Gate of redactie)."

## docs/REQUIREMENTS_CHANGE_PROCESS.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 1. Purpose
- ## 2. Scope
- ## 3. Roles
- ## 6. Governance Flow
- ## 7. Human Gate Criteria
- ## 10. Interaction with PHASES / TODO

Quoted phrases:
- L6: "- Dit proces introduceert GEEN nieuwe inhoud — alleen governance."
- L10: "- Geldt voor: functional, non‑functional, governance, automation‑safety, pilots."
- L17: "- **Governance Agents** — leveren advies, nooit beslissen."
- L18: "- **Human Gate / Editorial Board** — keurt high‑impact wijzigingen goed of af."
- L43: "## 6. Governance Flow"
- L46: "3) Governance‑agents leveren advies (indien relevant)."
- L48: "- cultural / glossary / publication / safety → governance‑stop."
- L49: "5) Human Gate beslist bij high‑risk wijzigingen."
- L54: "Governance‑agents geven advies — beslissen NIET."
- L56: "## 7. Human Gate Criteria"
- L57: "Human Gate is verplicht bij:"
- L62: "- wijzigingen die bestaande governance‑mechanismen verzwakken."
- L64: "Human Gate is niet vereist bij:"
- L81: "## 10. Interaction with PHASES / TODO"
- L82: "- Grote wijzigingen krijgen een SYSTEM_REQUIREMENTS_* of PHASE3_* taak."
- L84: "- PHASE‑promoties mogen NOOIT zonder requirements‑validatie."

## docs/RESEARCH_GLOSSARY.md

Preliminary classification suggestion: GOV-A

Quoted phrases:
- L197: "- path: /Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/ARCHIVE/HANDOVERS/2025-12-22_135929_step4_step5/step5_extraction/qc/extract_qc_missing_canonical_pages.tsv"
- L257: "- Deze documenten zijn waarschijnlijk waardevol voor de toekomstige Glossary Agent en Annotation workflows."
- L261: "- Is er een canonische "hoofdglossary", of meerdere overlappende varianten?"

## docs/RESEARCH_OLD_REPO.md

Preliminary classification suggestion: AMBIGUOUS

Quoted phrases:
- L41: "- path: /Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/DERIVED/step4_structure/index/canonical_concat.txt"
- L157: "- path: /Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/DERIVED/step6_annotation_working_optional/annotations_canonical.tsv"

## docs/VISION_AND_STRATEGY.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Governance Layers: Project vs System
- ### Governance Layer A — Project Governance (GOV-A)
- ### Governance Layer B — System Governance (GOV-B)
- ### 2.1 Phase 0 — Source Restoration (technical, reversible)
- ### 2.2 Phase 1 — Scholarly Edition (preserve, but illuminate)
- ### 2.3 Phase 2 — Public Edition (modernise with accountability)
- ## 3. Capability-Driven Strategy
- ## 4. Strategic Phasing Rationale
- ## 6. Agents, governance and “organised doubt”
- ### 6.1 Agents as signalers, not deciders
- ### 6.2 Governance layer
- ## 7. Definition of Done

Quoted phrases:
- L10: "## Governance Layers: Project vs System"
- L12: "### Governance Layer A — Project Governance (GOV-A)"
- L13: "- GOV-A is governance over the design and development of the Mustika Rasa system."
- L14: "- GOV-A is fully human and governs strategy, capability definition, phasing, workflows, agents, validators, and contracts."
- L15: "- GOV-A artefacts include `docs/VISION_AND_STRATEGY.md`, `docs/CODEX_TODO.md`, and `docs/WORKFLOW.md`."
- L18: "### Governance Layer B — System Governance (GOV-B)"
- L19: "- GOV-B is governance embedded in the system and enforced at runtime."
- L20: "- GOV-B operates through formal roles, output contracts, validators, gates, and canonical trails."
- L21: "- GOV-B governs what runs may produce and what can be considered canonical."
- L24: "Project phases describe how GOV-A designs and formalizes GOV-B over time."
- L25: "Phases do NOT imply increased agent autonomy or transfer of decision authority."
- L26: "Authority remains human unless explicitly and procedurally governed."
- L30: "### 2.1 Phase 0 — Source Restoration (technical, reversible)"
- L48: "### 2.2 Phase 1 — Scholarly Edition (preserve, but illuminate)"
- L59: "### 2.3 Phase 2 — Public Edition (modernise with accountability)"
- L72: "objective → goal → capability → phase → agent."
- L75: "zonder dat de kern-doelen veranderen. Phases zijn strategische containers"
- L80: "Governance‑grenzen:"
- L83: "- Agents confereren nooit autoriteit of canoniek gewicht op zichzelf."
- L89: "bij strategie (dit document), niet bij TODO’s of workflows."
- L108: "## 6. Agents, governance and “organised doubt”"
- L113: "- Human Gate en governance zijn eindverantwoordelijk bij betekenisvolle risico’s."
- L117: "### 6.2 Governance layer"
- L123: "- Governance bewaakt stop‑model (soft‑stop, governance‑stop, human gate) en logging."
- L124: "- Beslissingen moeten herleidbaar zijn tot governance‑artefacten en logs."
- L144: "- Bij FAIL volgt governance‑stop en eventueel human gate."
- L145: "- Dit sluit aan bij governance tests en het stop‑model."

## docs/WORKFLOW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # WORKFLOW OVERVIEW
- ### Phase-8 — Output-Contract Gate (procedural)
- ## Rol van de Orchestrator
- ## Governance-lagen en ondersteunende agents
- ## Governance Triggers
- ### Glossary Agent — triggers
- ### Research Agent — triggers
- ## Autonomy & Escalation (Stop Model)
- ### Batch / Chapter Execution (Design)
- ### Governance Agent Runtime Integration (Design)
- ### Phase-3 (Pilots & Safety — design framing)
- ## Governance Tests
- ## Where to change what
- ## Handover Flows

Quoted phrases:
- L1: "# WORKFLOW OVERVIEW"
- L3: "Dit document beschrijft de huidige workflow en waar wijzigingen thuishoren."
- L14: "### Phase-8 — Output-Contract Gate (procedural)"
- L16: "- Elke Phase-8 CLI-run (Translation → Readability → Fidelity) MOET gevolgd worden door:"
- L17: "- `sandbox/tools/phase8_output_contract_validator.sh <run_dir>`"
- L18: "- Technische gate (optioneel): gebruik `sandbox/tools/phase8_run_with_gate.sh <run_dir> <english_txt> <rough_nl_txt>`"
- L19: "- Output contract v2: hoofdtekst mag EN of NL zijn; consistentie is gewenst, maar taal is geen gate-criterium."
- L20: "- Gate controleert scheiding van hoofdtekst en opmerkingen, en governance-termen."
- L21: "- PASS-definitie: een Phase-8 run is PAS geldig als"
- L22: "sandbox/phase8_runs/<run_id>/eval/output_contract_checks.txt"
- L23: "overall_status: PASS bevat (validator exit code 0)."
- L25: "- Phase-8 is afgerond (COMPLETED — REWORK ACCEPTED); PASS-run is niet vereist."
- L26: "- Gate functioneert op FAIL-cases; format-repair is expliciet uitgesteld naar backlog."
- L28: "- de run telt niet als geldig Phase-8 resultaat"
- L34: "De Orchestrator is de workflow-conductor: coördineert agents, bewaakt templates"
- L35: "en governance, en zorgt dat outputs conform afspraken zijn. Het formele mandaat"
- L38: "## Governance-lagen en ondersteunende agents"
- L47: "## Governance Triggers"
- L49: "Deze triggers zijn verplicht en leveren governance‑artefacten op:"
- L50: "- Methodology Archivist bij nieuwe workflows, lifecycle‑wijzigingen en SYSTEM_* beslissingen"
- L63: "- verwijzing: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md"
- L71: "- verwijzing: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md"
- L77: "| Agent | Soft-stop (self-healing) | Governance-stop (no human) | Human gate (hard-stop) |"
- L84: "| Orchestrator | Herordening, extra context | Troubleshooting + Methodology | Governance-conflict onoplosbaar |"
- L88: "Elke agent volgt dezelfde escalatielogica: soft-stop, governance-stop, en human-gate bij hoge impact of conflict."
- L92: "- Ontwerpdocument: `docs/CHAPTER_BATCH_WORKFLOW.md` (geen runtime-implementatie)."
- L97: "### Governance Agent Runtime Integration (Design)"
- L99: "- Ontwerpdocument: `docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md` beschrijft hoe governance-agents"
- L102: "- Bestaande workflow blijft leidend totdat code expliciet is aangepast."
- L104: "### Phase-3 (Pilots & Safety — design framing)"
- L107: "- governance test gecontroleerd falen"
- L109: "- verwijzing: docs/PHASE3_FRAMING.md"
- L111: "## Governance Tests"
- L113: "Het testplan voor governance staat in `docs/10-governance/GOVERNANCE_TESTS_PLAN.md` en is leidend\nvoordat er daadwerkelijke testcode wordt geïmplementeerd."
- L119: "- Governance- en procesdocumentatie: `docs/*.md`."
- L124: "(bijv. PHASE-1 Foundations) of vóór start van een nieuw projectblok (bijv. PHASE-2)."

## docs/archivist_reports/ARCHIVIST_P5_ALIGNMENT_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # ARCHIVIST REPORT — Phase 5 Alignment Check (001)

Quoted phrases:
- L1: "# ARCHIVIST REPORT — Phase 5 Alignment Check (001)"
- L6: "- Phase-5 documenten, manifest_p5.yaml, en docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md."
- L11: "- Phase-5 docs volgen de categorie "consolidation_phase5" en verwijzen niet"
- L13: "- Manifest en informatie-architectuur zijn consistent: canonical vs sandbox"
- L18: "maar functioneert feitelijk als ondersteunende governance-tool."
- L22: "rond toekomstige pilots of Phase-6 voorbereidingen."
- L23: "- Phase-5 documenten zouden per ongeluk als "beleid" geïnterpreteerd kunnen"
- L32: "impact: verbetert navigeerbaarheid en governance-transparantie"
- L33: "suggested_phase: P5 (documentair)"
- L39: "suggested_phase: P5–P6 transition"
- L45: "suggested_phase: P5 (optioneel)"

## docs/archivist_reports/ARCHIVIST_P5_CLEANUP_PROPOSAL_002.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # ARCHIVIST REPORT — Cleanup Preparation Proposal (002)

Quoted phrases:
- L7: "canonical docs, governance, pilots/sandbox, phase-5 consolidatie,"
- L10: "(Phase-6), zonder nu fysieke wijzigingen door te voeren."
- L13: "- De repo bevat duidelijke categorieën (canonical / sandbox / consolidation),"
- L25: "- Phase-5 documentatie kan per ongeluk beleidsstatus krijgen."
- L31: "- id: CLEANUP_MAP_CANONICAL"
- L32: "description: Maak één heldere index-pagina die *alle* canonical docs"
- L33: "beschrijft (met korte toelichting waarom ze canonical zijn)."
- L35: "suggested_phase: P5 (documentair)"
- L39: "en verouderde consolidatie-docs — alleen als governance"
- L42: "suggested_phase: P6 (governance-gated)"
- L47: "(e) noteer in HUMAN_GATE_LOG."
- L49: "suggested_phase: P6"
- L55: "suggested_phase: P5"
- L61: "suggested_phase: P5"
- L63: "- id: GOVERNANCE_BOUNDARIES_NOTE"
- L65: "verplaatst/verwijderd zonder Human Gate."
- L67: "suggested_phase: P5"
- L70: "- geen fysieke verplaatsingen in Phase-5"
- L71: "- alles voorstel-only en human-gated"
- L72: "- elke verplaatsing in Phase-6 krijgt:"

## docs/archivist_reports/ARCHIVIST_P6_READONLY_SCAN_01.md

Preliminary classification suggestion: GOV-A

Quoted phrases:
- L3: "Phase-6 oriented scan of docs/ and docs/navigation/."
- L7: "- docs/navigation/EDITORIAL_INDEX.md exists but only lists a small subset; multiple Phase-6 workflow/spec docs live in docs/ and are not yet indexed (e.g., P6_EXCERPT_BINDING_SPEC.md, P6_EXCERPT_BINDING_INTEGRATION_PLAN.md, P6_EXCERPT_AWARE_RUNNER_DESIGN.md, P6_EDITORIAL_WORKFLOW_MINI.md)."
- L9: "- Phase-6 case files (docs/P6_SAYUR_INTERNAL_WORK_CASE01.md, docs/P6_LOBAK_INTERNAL_WORK_CASE02.md) live in docs/ root; unclear whether these should be grouped under docs/navigation/ or remain in docs/ (needs decision)."
- L11: "- docs/manifest_p5.yaml and docs/CANONICAL_INDEX.md both provide canonical lists; EDITORIAL_INDEX could explicitly link to both to reduce redundancy."
- L14: "- Moving Phase-6 workflow/spec docs from docs/ to docs/navigation/ is low to medium risk due to link updates; requires checklist and migration log."
- L15: "- Case files are medium risk because they are workflow-bearing; moving them could confuse lifecycle ownership and traceability."
- L19: "- id: PHASE6_NAV_GROUPING_CANDIDATES"
- L20: "description: Identify specific Phase-6 docs that may belong in docs/navigation/ but currently live in docs/."
- L21: "suggested_phase: P6"
- L24: "- id: PHASE6_INDEX_EXPANSION_PASS"
- L25: "description: Expand EDITORIAL_INDEX.md with missing key Phase-6 workflow/governance docs."
- L26: "suggested_phase: P6"
- L29: "- id: PHASE6_CASEFILE_PLACEMENT_DECISION"
- L30: "description: Decide whether Phase-6 case files should remain in docs/ or be grouped under docs/navigation/; document the decision and update indexes accordingly."
- L31: "suggested_phase: P6"
- L32: "impact: medium risk; affects traceability if moved, requires governance-aligned logging."
- L34: "- id: PHASE6_NAV_LINK_CONSISTENCY_PASS"
- L36: "suggested_phase: P6"

## docs/archivist_reports/PHASE6_NAV_GROUPING_CANDIDATES.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Archivist Report — Phase-6 Navigation Grouping Candidates

Quoted phrases:
- L1: "# Archivist Report — Phase-6 Navigation Grouping Candidates"
- L5: "Identify Phase-6 documents in docs/ that may be better grouped under docs/navigation/"
- L9: "- Phase-6 docs in docs/ root include both navigation/design plans and workflow/case artefacts."
- L10: "- Navigation/design/overview candidates: migration plan, migration candidate list, production workflow overview, excerpt-binding spec/plan/runner design."
- L11: "- Workflow/case artefacts: internal case files (SAYUR Case-01, LOBAK Case-02) should remain outside navigation for now."
- L12: "- Ambiguous cases: production workflow and repo migration plan are design-level but influence long-term structure; moving them is feasible but should be deliberate and logged."
- L20: "| docs/P6_PRODUCTION_WORKFLOW_SAYUR.md | end-to-end workflow overview | workflow design | medium | Design-level; not canonical, but referenced widely. |"
- L21: "| docs/P6_EXCERPT_BINDING_SPEC.md | policy-style spec for traceability | workflow design | medium | Spec doc; move only with link updates. |"
- L22: "| docs/P6_EXCERPT_BINDING_INTEGRATION_PLAN.md | integration map for metadata | workflow design | medium | Plan doc; move only with links updated. |"
- L23: "| docs/P6_EXCERPT_AWARE_RUNNER_DESIGN.md | runner design overview | workflow design | medium | Design doc; safe if links updated. |"
- L26: "- docs/P6_SAYUR_INTERNAL_WORK_CASE01.md — case file with workflow artefact paths; keep outside navigation to avoid confusion with design docs."
- L30: "- Moving design/navigation-like Phase-6 docs is low to medium risk: links and references must be updated, and migration notes logged."
- L31: "- Case files are medium to high risk to move because they are workflow-bearing artefacts and can affect traceability if relocated."
- L35: "- id: PHASE6_NAV_GROUPING_LOW_RISK_MOVE_PLAN"
- L38: "suggested_phase: P6"
- L40: "- id: PHASE6_NAV_GROUPING_DECISION_LOG"
- L41: "description: Document a short decision for ambiguous Phase-6 docs (especially case files) on whether they stay in docs/ or ever move, and update docs/navigation/EDITORIAL_INDEX.md accordingly."
- L43: "suggested_phase: P6"

## docs/checklists/P6_LOW_RISK_MIGRATION_CHECKLIST.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 Checklist — Low-risk Repo Migration
- ## 2. Out of scope (not allowed)

Quoted phrases:
- L1: "# Phase-6 Checklist — Low-risk Repo Migration"
- L23: "- anything under canonical, editorial, or glossary proposals"
- L24: "- Human Gate logs or governance records"

## docs/checklists/P6_SAYUR_MINI_WORKFLOW_VALIDATION.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # P6 — SAYUR Mini Workflow Validation Checklist
- ## 1. Repo & Paths
- ## 3. Escalation Logic
- ## 5. Governance Boundaries

Quoted phrases:
- L1: "# P6 — SAYUR Mini Workflow Validation Checklist"
- L5: "- [ ] sandbox/workflows/p6_sayur_mini/* is used only as a working zone"
- L6: "- [ ] No outputs are mapped into canonical or publication areas"
- L17: "- [ ] Human Gate is triggered only when impact matters"
- L24: "## 5. Governance Boundaries"
- L25: "- [ ] Workflow stays inside sandbox"

## docs/crew/CHALLENGER_ISSUE_TYPES_P4.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Challenger Issue Types — Phase-4 Sandbox (SAYUR Micropilot)
- ## 1. Canonieke issue_types
- ## 2. Severity: INFO / WARNING / BLOCKER

Quoted phrases:
- L1: "# Challenger Issue Types — Phase-4 Sandbox (SAYUR Micropilot)"
- L7: "Phase-4 sandbox micropilots (SAYUR-A annotator + challenger)."
- L14: "- overreach (bv. “needs translation”) zichtbaar wordt als GOVERNANCE-issue,"
- L21: "## 1. Canonieke issue_types"
- L32: "glossary-governance (proposal-only)."
- L44: "- `GOVERNANCE`"
- L45: "Gebruik wanneer gedrag of output duidelijk de governance-regels schendt, bijv.:"
- L50: "- autonomie-envelope / Human Gate policy wordt genegeerd."
- L69: "autonomie-/Human Gate-regels."

## docs/crew/CREW_MICROPILOT_SAYUR_MULTI_MISTRAL.md

Preliminary classification suggestion: AMBIGUOUS

Quoted phrases:
- L6: "RUNTIME TEST PLAN — NOT A GOVERNANCE DECISION"
- L16: "JSON contract (high level):"
- L24: "Governance:"
- L26: "- issue_type touching culture/safety/meaning → Human Gate, not auto-fix"

## docs/crew/CREW_MICROPILOT_SAYUR_V2_DESIGN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Micropilot — SAYUR Multi-Agent v2 (Annotator → Challenger → Troubleshooting)
- ## 1. Purpose
- ## 2. Hypotheses
- ## 3. Scope (klein en gecontroleerd)
- ## 4. Agents & roles

Quoted phrases:
- L4: "DESIGN-DRAFT (Phase-4 sandbox, reversible, proposal-only)"
- L9: "- docs/10-governance/HUMAN_GATE_POLICY_P4_SANDBOX.md"
- L21: "**vóór** escalatie naar Human Gate."
- L31: "(TRANSLATION/EQUIVALENT/MEANING_DECISION/SAFETY/GOVERNANCE)."
- L33: "- Alleen high-impact / onoplosbaar → Human Gate (met log-redenen)."
- L41: "No edits to source, glossary, or canon."
- L48: "| Phase | Agent | Role | Must NOT |"
- L53: "| 4 (opt.) | Template Agent | JSON/contract valideren | inhoud wijzigen |"
- L54: "| 5 (if needed) | Human Gate | betekenis/cultuur/safety besluiten | overslaan van logs |"

## docs/crew/CREW_SHAKEDOWN_PLAN_LOBAK_MISTRAL.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ### Closure Note (Shakedown Complete)

Quoted phrases:
- L6: "RUNTIME TEST PLAN — NOT A GOVERNANCE DECISION"
- L18: "JSON contract (same as SAYUR):"
- L24: "Governance stops:"
- L25: "- Human Gate required if meaning/safety/cultural interpretation could shift readers"
- L37: "- No governance incidents; rollback remains trivial"
- L63: "- Will be harmonised during Phase-5 human review."
- L64: "- No governance incidents, rollback remains reversible."

## docs/crew/CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Shakedown Data & JSON Contract (Phase-4 sandbox)
- ### What MUST be logged for this shakedown
- ### OK / KO Criteria
- ## Selected Mini-Excerpt (locked for shakedown)
- ### Evaluation Note — Direct Mistral Shakedown 01
- ### Evaluation Note — Crew Shakedown 01
- ### Verified Runtime Path (Phase-4)
- ### Stability Note (Phase-4)
- ### Closure Note (Shakedown Complete)

Quoted phrases:
- L6: "RUNTIME TEST PLAN — NOT A GOVERNANCE DECISION"
- L48: "## Shakedown Data & JSON Contract (Phase-4 sandbox)"
- L116: "- evaluation notes (OK / Soft-stop / Governance-stop)"
- L138: "**GOVERNANCE-STOP**"
- L144: "In governance-stop:"
- L156: "- Source file: canonical_concat.txt"
- L203: "not a governance incident."
- L212: "- No governance incident; follow-up is optional tuning, not rollback."
- L214: "### Verified Runtime Path (Phase-4)"
- L220: "- Remaining work: prompt tuning for label consistency (later phase)."
- L222: "### Stability Note (Phase-4)"
- L229: "- Next allowed step: expand to +1 excerpt line (still annotation-only, gated)."
- L238: "- No governance incidents, rollback remains reversible."

## docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSARY_LOBAK_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## Lifecycle & Governance
- ## Risk & Rollback
- ## References

Quoted phrases:
- L2: "decision_id: P7_CANONICAL_GLOSSARY_LOBAK_001"
- L4: "phase: P7"
- L5: "status: canonical"
- L26: "## Lifecycle & Governance"
- L29: "- lifecycle.to_status: CANONICAL"
- L48: "Rollback occurs by creating a NEW canonical decision record that supersedes this one."
- L53: "- docs/P7_CANONICAL_TRAIL_SPEC.md"
- L54: "- docs/pilots/P7_CANONICAL_PILOT_GLOSSARY_LOBAK_001.md"

## docs/decisions/P6_CASEFILE_PLACEMENT_DECISION.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 Decision — Placement of Case Files (SAYUR / LOBAK)
- ## 1. What counts as a “case file”
- ## 2. Decision (summary)
- ## 3. Conditions for revisiting this decision
- ## 4. Editorial Index & Navigation
- ## 5. Notes

Quoted phrases:
- L1: "# Phase-6 Decision — Placement of Case Files (SAYUR / LOBAK)"
- L5: "Related: PHASE6_NAV_GROUPING_CANDIDATES.md, docs/navigation/EDITORIAL_INDEX.md, P6_REPO_ARCHITECTURE_MIGRATION_PLAN.md"
- L11: "In Phase-6, a **case file** is a concrete application of a generic workflow"
- L15: "- workflow paths and artefact locations,"
- L19: "Case files are *workflow-bearing* — they describe what actually happened"
- L26: "> **Case files remain in `docs/` (editorial/workflow zone), not in `docs/navigation/`.**"
- L34: "2. **Workflow role**"
- L53: "- Human Gate approves the re-placement (because traces may be affected)."
- L61: "- docs/navigation/EDITORIAL_INDEX.md should list case files under “workflow/case”."
- L69: "This decision does not grant new governance authority."
- L70: "It records the current, safest default for Phase-6."

## docs/decisions/rehearsal/P7_REHEARSAL_LOBAK_CASE02_DECISION_001.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Canonical Decision Record — REHEARSAL ONLY
- ## Rationale (Rehearsal Context)
- ## Notes

Quoted phrases:
- L1: "# Canonical Decision Record — REHEARSAL ONLY"
- L29: "This record exists only to test the canonical trail lifecycle:"
- L42: "- not canonical"
- L44: "- used only for Phase-7 rehearsal exercises"

## docs/decisions/rehearsal/P7_REHEARSAL_LOBAK_CASE02_DECISION_002.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Canonical Decision Record — REHEARSAL ROLLBACK
- ## Rationale (Rollback Simulation)
- ## Notes

Quoted phrases:
- L1: "# Canonical Decision Record — REHEARSAL ROLLBACK"
- L37: "a real canonical decision."
- L46: "- this is still part of the Phase-7 rehearsal only"
- L47: "- no entries should be added to CANONICAL_INDEX for these rehearsal records"

## docs/glossary/DECISION_CARD_LOBAK_P4.md

Preliminary classification suggestion: GOV-B

Relevant section headings:
- ## Risks for Readers (Human Gate triggers)
- ## Recommendation (process, not meaning)
- ## Logging

Quoted phrases:
- L41: "## Risks for Readers (Human Gate triggers)"
- L69: "- Laat definitieve woordkeuze ALTIJD via Human Gate lopen."
- L87: "- Human Gate trigger markeren indien lezer-betekenis geraakt wordt."

## docs/handovers/handover_woensdagavond/CANONICAL_INDEX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Canonical Index — What is “Source of Truth” here?
- ## Canonical Decision Records (Phase-7 onward)
- ### 2026

Quoted phrases:
- L1: "# Canonical Index — What is “Source of Truth” here?"
- L4: "(canonical) en waarom — zonder structuur aan te passen."
- L6: "Canonical docs (bron voor besluiten):"
- L10: "- docs/WORKFLOW.md"
- L13: "- docs/10-governance/*  (policies, human gate, rollback, incident)"
- L16: "- canonical docs worden niet “stilletjes aangepast”"
- L17: "- conflicten worden opgelost door canonical + uitleg"
- L18: "- wijzigingen zijn traceable en human-gated"
- L24: "## Canonical Decision Records (Phase-7 onward)"
- L26: "This index will begin filling during Phase-7."
- L27: "Each canonical entry will:"
- L38: "- id: P7_CANONICAL_GLOSSARY_LOBAK_001"
- L45: "decision_record: docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSORY_LOBAK_001.md"
- L49: ""lobak" is canoniek opgenomen als glossary-lemma (itemisation only);"

## docs/handovers/handover_woensdagavond/CAPABILITY_AGENT_MAP.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Capability → Agent Mapping
- ## 1. Purpose
- ## 3. Capability Categories
- ## 4. Mapping Table (kernstuk)
- ## 7. Impact on Phase-3
- ## 8. Appendix

Quoted phrases:
- L4: "Scope: documentary — no behavioural authority"
- L5: "Changes allowed: via normal governance only"
- L10: "waar overlap zit, en waar gaten in het systeem bestaan."
- L23: "- Governance capabilities"
- L24: "- Workflow/Operational capabilities"
- L42: "| Governance orchestration & escalation | Orchestrator | Methodology & Accountability Archivist, Incident & Resilience Agent | Orchestrator bewaakt flow; governance agents signaleren. |"
- L46: "| Template governance & format compliance | Template Agent | Orchestrator | Template-structuren bewaken, geen inhoud. |"
- L47: "| Workflow orchestration & handoff | Orchestrator | Challenger Agent, Cohesion Agent | Workflow-coördinatie en samenhang. |"
- L50: "| Glossary proposal generation | Glossary / Terminology Agent | Research / Historical Knowledge Agent | Proposals only; geen canonieke besluiten. |"
- L65: "## 7. Impact on Phase-3"
- L68: "glossary-proposals en onderzoek (geen canonieke beslissingen)."
- L77: "- docs/10-governance/"
- L78: "- docs/PHASE3_FRAMING.md"

## docs/handovers/handover_woensdagavond/CODEX_SESSION_LOG.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Codex Session Log – Mustikarasa
- ### SESSION — Phase-6 Low-risk Migration (navigation docs)
- ### SESSION — Workflow Naming Alignment
- ## [2026-01-06] CASE-01 — pre-flight attempt (excerpt-aware runner)
- ## [2026-01-06] CASE-01 — first excerpt-aware runner execution
- ## [2026-01-06] CASE-01 — first successful excerpt-aware sandbox run
- ## [2026-01-06] CASE-01 — first run with refined runner payload
- ## [2026-01-12] CASE-02 — excerpt locked (design)
- ### P6 — Human Review Workflow Defined
- ### P6 — First Human Review Simulation Completed

Quoted phrases:
- L9: "- 2026-01-02 – SYSTEM_ORCHESTRATOR_MANDATE: mandaat en grenzen vastgelegd in prompts/orchestrator.md, docs/AGENTS.md en docs/WORKFLOW.md; TODO afgevinkt."
- L10: "- 2026-01-02 – SYSTEM_GLOSSARY_DECISION_LIFECYCLE: lifecycle vastgelegd in docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md en gekoppeld in prompts en docs; TODO afgevinkt."
- L11: "- 2026-01-02 – SYSTEM_GOVERNANCE_TRIGGERS: triggers vastgelegd in prompts en docs; artefacten en escalatiepad benoemd; TODO afgevinkt."
- L12: "- 2026-01-02 – SYSTEM_AGENT_STOP_CRITERIA: autonomy/stop-model vastgelegd in prompts en docs; human gate expliciet; TODO afgevinkt."
- L13: "- 2026-01-02 – SYSTEM_GOVERNANCE_TESTS: governance testplan opgesteld en gekoppeld aan workflow; TODO afgevinkt."
- L15: "ID: PHASE2_BACKLOG_CREATED"
- L16: "Summary: PHASE-2 roadmap geregistreerd in CODEX_TODO.md (nog geen uitvoering)."
- L22: "ID: P7_CANONICAL_TRAIL_REHEARSAL_LOBAK_001"
- L23: "Actor: Codex-Phase7"
- L25: "- Phase-7 kicked off (canonical decision trails)."
- L26: "- Created P7_DECISION_TYPES.md and P7_CANONICAL_TRAIL_SPEC.md (draft, v1)."
- L27: "- Added Human Review Participation Model to P6_HUMAN_REVIEW_WORKFLOW.md and P7_CANONICAL_TRAIL_SPEC.md."
- L28: "- Designed and executed P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md using LOBAK Case-02 (excerpt_id lobak_034_048)."
- L31: "Documentary lifecycle rehearsal only; no real canonical decisions were made."
- L37: "ID: TODO_PHASE_STRUCTURE_APPLIED"
- L38: "Summary: PHASE-1 (foundations) expliciet gemaakt; PHASE-2 roadmap blijft onafhankelijk en open."
- L39: "Impact: backlog nu chronologisch en governance-consistent."
- L42: "- 2026-01-02 – STOP: TODO phase-structuur niet toegepast; PHASE-2 Roadmap sectie/PHASE2_* items ontbreken in docs/CODEX_TODO.md, dus herstructurering is ambigu."
- L45: "Summary: Handover Agent ontworpen en geregistreerd (prompt, AGENTS, Orchestrator, CODEX_META_PROMPT, WORKFLOW, total_project)."
- L50: "ID: PHASE2_TODO_REALITY_SYNC"
- L56: "ID: PHASE2_TODO_REALITY_SYNC_COMPLETED"
- L57: "Summary: Marked PHASE2_TODO_REALITY_SYNC as completed and annotated with reference."
- L62: "ID: PHASE2_AGENT_AUTONOMY_COMPLETION"
- L64: "Impact: consistent governance-gedrag over de volledige redactie-pipeline."
- L68: "ID: PHASE2_CHAPTER_BATCH_WORKFLOW_DESIGN"
- L69: "Summary: Ontwerpdocument voor batch/hoofdstuk workflow toegevoegd en gekoppeld aan WORKFLOW.md."
- L74: "ID: PHASE2_GOVERNANCE_AGENT_RUNTIME_INTEGRATION_DESIGN"
- L75: "Summary: Governance-agent runtime-integratie beschreven in GOVERNANCE_INTEGRATION_DESIGN.md en gekoppeld aan WORKFLOW/AGENTS."
- L80: "ID: PHASE2_GLOSSARY_RESEARCH_PILOT"
- L82: "Impact: valideert lifecycle en workflow zonder definitieve glossary-wijzigingen."
- L86: "ID: PHASE2_GOVERNANCE_TEST_SCENARIO_1"
- L87: "Summary: Governance-testsessie uitgevoerd met gesimuleerd incident; soft-stop/governance-stop functioneren documentair."
- L88: "Impact: bevestigt dat governance-ontwerp werkbaar is zonder runtime-wijzigingen."
- L92: "ID: GOVERNANCE_TEST_SCENARIO_2_PARTIAL_BATCH_FAILURE"
- L93: "Summary: Governance-testscenario 2 beschreven: partial batch failure met soft-stop/governance-stop en geïsoleerd incident."
- L94: "Impact: bevestigt dat batch-workflow en governance-model samengaan zonder onnodige batch-stops."
- L98: "ID: PATCH_GOVERNANCE_INTEGRATION_FAILURE_MODES"
- L99: "Summary: Failure modes & safeguards expliciet toegevoegd aan GOVERNANCE_INTEGRATION_DESIGN om checklist “Partial” te sluiten."
- L106: "Impact: geeft feitelijke basis voor PHASE-3 planning en cleanup."
- L134: "ID: CONSOL_PHASE2_HEADER_STATE_APPLIED"
- L135: "Summary: PHASE-2 koptekst in docs/CODEX_TODO.md aangepast van “not started yet” naar een feitelijke ‘in progress’-formulering; bijbehorende consolidatietaak op done gezet."
- L136: "Impact: voorkomt misinterpretatie van de PHASE-2 status bij lezing van CODEX_TODO."
- L141: "Summary: Requirements-change governance vastgelegd in REQUIREMENTS_CHANGE_PROCESS.md; proces beschrijft rollen, templates, Human Gate en logging."
- L147: "Summary: Applied requirement ASR-005 prohibiting automatic glossary updates without Human Gate + rollback."
- L148: "Impact: strengthens glossary governance; aligns runtime behaviour with lifecycle principles."
- L153: "Summary: Added ASR-006 requiring governance-stop whenever an incident is raised."
- L160: "Impact: increases robustness of batch workflows and reduces risk of large-scale accidental losses."
- L165: "Summary: Vision & Strategy vastgelegd voor het Mustikarasa-project, inclusief driefasen-strategie, centrale traceability-principe, governance- en red-teamrol en een Definition of Done die fouten expliciet benoemd en logbaar maakt."
- L166: "Impact: biedt een helder kompas boven requirements en workflows; maakt toekomstige ontwerp- en runtime-beslissingen toetsbaar aan een expliciete visie."
- L170: "ID: PHASE3_FRAMING_ADDED"
- L171: "Summary: Phase-3 framing document toegevoegd en gekoppeld aan workflow (documentair — geen runtime-wijzigingen)."
- L176: "ID: PHASE3_FRAMING_STABILIZED"
- L177: "Summary: PHASE-3 framing document formeel vastgesteld als strategische baseline (v1); wijzigingen voortaan via change-proces."
- L178: "Impact: creëert een duidelijke referentie voor pilots, governance en toekomstige ontwerpbeslissingen."
- L182: "ID: PHASE3_PILOT_GLOSSARY_LOBAK_CREATED"
- L196: "Impact: validates glossary lifecycle and governance reaction to terminology ambiguity without changing any production artefacts."
- L208: "Impact: validates governance handling of intentional divergence without changing canonical artefacts; rollback documented in pilot file."
- L237: "Rollback: delete the “Methodology Insight (Phase-3 — Proposal)” section added to docs/PILOT_GLOSSARY_LOBAK_RUN_P3_LOBAK_002.md."
- L244: "Rollback: delete the Consolidation Summary block, the CONSOLIDATION_AUDIT_01 entry, and the PHASE3 proposal line in CODEX_TODO."
- L248: "Summary: OCR technical-only pilot documented on a sandbox excerpt; no canonical edits."
- L258: "Rollback: delete the “Methodology Insight — “²” Marker (Phase-3 — Proposal)” section from docs/PILOT_OCR_RESTORE_RUN_P3_OCR_RESTORE_001.md."
- L265: "Rollback: delete the Consolidation Summary block, the CONSOLIDATION_AUDIT_01 entry, and the PHASE3 proposal line in CODEX_TODO."
- L281: "Summary: Verwijzing naar governance testdocument in CODEX_TODO.md gecorrigeerd naar GOVERNANCE_TEST_SCENARIO_1.md."
- L282: "Impact: voorkomt verwarring rond governance testdocumenten."
- L293: "Summary: Governance-triggerlijst in WORKFLOW.md uitgebreid met expliciete Glossary- en Research-triggers."
- L294: "Impact: workflow-document maakt nu duidelijk wanneer deze agents automatisch worden geraadpleegd."
- L299: "Summary: Eerste versie van docs/REQUIREMENTS.md aangemaakt, met afgeleide functionele, non-functionele, governance- en safety-eisen."
- L300: "Impact: maakt expliciete, herleidbare requirements zichtbaar als basis voor toekomstige PHASE-3 ontwerp- en runtime-beslissingen."
- L304: "ID: PHASE3_DOCS_REORG_MOVE_GOVERNANCE_PILOT"
- L305: "Summary: Small-scope docs reorganisation pilot executed for governance documents, following DOCS_INFORMATION_ARCHITECTURE; references updated, no code or prompts touched."
- L306: "Impact: Validates the reorganisation approach on a limited scope and keeps governance docs discoverable and consistent."
- L312: "Summary: Imported governed legacy OCR subset (RB samples + canonical context) into sandbox/legacy_imports with provenance headers."
- L313: "Impact: adds read-only research assets for Phase-3 OCR/"²" analysis; no canonical text changed."
- L315: "Rollback: delete sandbox/legacy_imports/* and remove the PHASE3 legacy import reminder from docs/CODEX_TODO.md."
- L321: "Impact: documents real-world distortion patterns for governance review without applying any normalization."
- L369: "Impact: documentary only; shows escalation and Human Gate discussion without text edits."
- L383: "ID: P3_GOVERNANCE_SYNTHESIS_001"
- L384: "Summary: Created Phase-3 synthesis doc for OCR ambiguity governance (no policy changes)."
- L387: "Rollback: delete docs/PHASE3_GOVERNANCE_SYNTHESIS_OCR_AMBIGUITY.md."
- L471: "ID: P3_WORKFLOW_SYNTHESIS_001"
- L472: "Summary: Created workflow synthesis pilot (documentary only)."
- L475: "Rollback: delete docs/PILOT_WORKFLOW_SYNTHESIS_RUN_P3_WORKFLOW_001.md."
- L479: "ID: P3_WORKFLOW_SYNTHESIS_001_CONSOLIDATION"
- L480: "Summary: Consolidated workflow synthesis pilot (documentary only)."
- L487: "ID: P3_WORKFLOW_MAP_001"
- L488: "Summary: Created documentary workflow map for ambiguity governance (Phase-3)."
- L491: "Rollback: delete docs/PILOT_WORKFLOW_MAP_RUN_P3_WORKFLOWMAP_001.md."
- L495: "ID: P3_WORKFLOW_MAP_001"
- L496: "Summary: Updated workflow map pilot with annotations, pilot notes, and risks (documentary only)."
- L499: "Rollback: delete docs/PILOT_WORKFLOW_MAP_RUN_P3_WORKFLOWMAP_001.md."
- L503: "ID: P3_WORKFLOW_MAP_001_CONSOLIDATION"
- L504: "Summary: Consolidated workflow map pilot (documentary only)."
- L512: "Summary: Governance failure drill — simulated glossary decision leak."
- L520: "Summary: Consolidated governance failure-drill (documentary only)."
- L616: "Summary: Phase-3 readiness reflection recorded (no decisions)."
- L619: "Rollback: delete docs/PHASE3_READINESS_REVIEW.md."
- L624: "Summary: Phase-4 readiness constraints captured (documentary only)."
- L627: "Rollback: delete docs/PHASE4_READINESS_NOTES.md."
- L632: "Summary: Added documentary Phase-3 status clarification."
- L635: "Rollback: delete the addendum block in docs/PHASE3_FRAMING.md."
- L640: "Summary: Appended structured Phase-4.1 agent-runtime backlog items."
- L648: "Summary: Created docs/BACKLOG_ITEM_TEMPLATE.md for standardized Phase-4 backlog items."
- L656: "Summary: Appended detailed backlog entry for PHASE4_AGENT_HARNESS_SPEC."
- L664: "Summary: Added governance clarification appendix to bridge + harness docs."
- L673: "Scope: Phase4-design-review (read-only)"
- L681: "Artifact: PHASE4_CLARIFICATION_PACKET_(sandbox)"
- L689: "Artifact: PHASE3_REFLECTION_(sandbox)"
- L744: "Note: governance incident drill — simulation only"
- L751: "Note: Phase3 consolidation memo — documentary only"
- L806: "Actor: Codex-Phase3Audit"
- L807: "Note: phase-3 completeness audit — documentary only"
- L814: "Note: phase-4 readiness brief — documentary only"
- L821: "Note: drafting phase-4 experiment protocol — documentary only"
- L833: "ID: HUMAN_GATE_SUMMARY_001"
- L834: "Actor: Codex-HumanGateSummary"
- L835: "Note: human gate criteria summary — documentary only"
- L840: "ID: GOVERNANCE_HANDOVER_NOTE_001"
- L842: "Note: governance handover note prepared — documentary only"
- L856: "Summary: Added docs/PILOT_TO_PRACTICE_GUIDE.md (documentary Phase-3 learnings)."
- L868: "Source: DERIVED/step4_structure/index/canonical_concat.txt"
- L872: "Note: No modifications were made to canonical_concat.txt."
- L947: "Impact: standardizes post-rehearsal capture without implying governance decisions."
- L974: "Summary: Sandbox readiness checklist documented for Phase-4 governance (no runtime approval)."
- L975: "Impact: provides a formal pre-run safety gate without authorizing execution."
- L981: "Summary: Incident playbook for Phase-4 sandbox documented (safety procedure only)."
- L987: "ID: HUMAN_GATE_POLICY_P4_SANDBOX_CREATED"
- L988: "Summary: Human Gate policy for Phase-4 sandbox documented (governance only, no run approval)."
- L1002: "Summary: Safety refinements added to Sayur GO/NO-GO proposal (manual gating, Human Gate presence, run-ID controls)."
- L1009: "Summary: Annotation stylecard for Phase-4 pilots documented (guideline only)."
- L1016: "Summary: Pilot-set v1 for Phase-4 sandbox preparation documented (planning only)."
- L1030: "Summary: GO/NO-GO evaluation form for Phase-4 sandbox documented (decision support only)."
- L1040: "Human Gate: active"
- L1064: "Impact: formalizes governance decision request without authorizing execution."
- L1071: "Impact: structures governance review without authorizing execution."
- L1077: "Phase: P4 sandbox"
- L1086: "Action: paused — awaiting Human Gate clarification"
- L1093: "Rationale: glossary ambiguity requires Human Gate review first"
- L1159: "- No governance incidents"
- L1182: "- No governance incidents"
- L1185: "### SESSION — Phase-6 Low-risk Migration (navigation docs)"
- L1194: "### SESSION — Workflow Naming Alignment"
- L1195: "We renamed P6_SAYUR_MINI_EDITORIAL_WORKFLOW → P6_EDITORIAL_WORKFLOW_MINI."
- L1196: "Reason: workflow is generic; SAYUR is merely Case-01."
- L1201: "Summary: Applied excerpt-binding spec documentair in Phase-6 workflows en pilot-evaluaties (excerpt-metadata subsections toegevoegd; generieke mini-workflow hernoemd naar een niet-SAYUR-specifieke titel; bestaande logs niet aangepast)."
- L1202: "Impact: excerpt-metadata is nu vastgelegd als documentair vereiste in workflows/templates; de generieke mini-workflow is duidelijk losgekoppeld van SAYUR; oude runs blijven historisch correct, toekomstige runs moeten excerpt_id/source/version registreren."
- L1204: "Rollback: herstel de titelwijziging in P6_EDITORIAL_WORKFLOW_MINI.md, verwijder de nieuwe excerpt-metadata subsections uit P6_EDITORIAL_WORKFLOW_MINI.md, P6_WORKFLOW_SAYUR_MINI.md en de drie pilot-evaluaties, verwijder de verwijzing naar P6_EXCERPT_BINDING_SPEC in de pilot-synthesis, en zet PHASE6_EXCERPT_BINDING_SPEC terug op [ ] in CODEX_TODO.md."
- L1209: "Summary: Created P6_EXCERPT_BINDING_INTEGRATION_PLAN.md documenting how excerpt_id/source/version propagate across plans, configs (design), logs, JSON artefacts, evaluations, and session logs; no runtime or prompt changes."
- L1210: "Impact: Excerpt-binding now has an explicit integration map and checklist for Phase-6; historical runs remain unchanged."
- L1212: "Rollback: remove docs/P6_EXCERPT_BINDING_INTEGRATION_PLAN.md and revert PHASE6_EXCERPT_BINDING_INTEGRATION_PLAN to [ ] in CODEX_TODO.md."
- L1233: "Summary: Created P6_LOBAK_CASE02_EXCERPT_SELECTION.md (draft governing excerpt doc with placeholders) and P6_LOBAK_INTERNAL_WORK_CASE02.md (Case-02 workflow file) for a non-SAYUR generic mini-workflow application; no runs authorized."
- L1241: "Summary: Defined LOBAK Case-02 as a generic Phase-6 mini-workflow case with excerpt-binding placeholders (case file + governing excerpt skeleton), without executing or authorizing any runs."
- L1242: "Impact: Establishes a non-SAYUR workflow case wired for excerpt-binding from the start while keeping it pending until a human selects the actual LOBAK excerpt and an excerpt-aware runner is implemented and approved."
- L1249: "Summary: Moved DOCS_INFORMATION_ARCHITECTURE.md into docs/navigation/ as part of low-risk navigation cleanup; updated references where appropriate. No canonical or workflow content changed."
- L1250: "Impact: Improves navigation discoverability without changing governance or editorial artefacts."
- L1257: "Summary: Moved P6_MIGRATION_CANDIDATE_LIST.md into docs/navigation/ as a navigation/overview document; updated references where appropriate. No case-files or canonical content were moved."
- L1258: "Impact: Slightly improves Phase-6 navigation clarity for migration planning without changing governance or workflow semantics."
- L1264: "ID: PHASE6_ADDENDUM_COPY_001"
- L1271: "ID: PHASE6_ADDENDUM_COPY_GOVERNANCE"
- L1272: "Summary: Copied governance + review docs into docs/addendum/ (documentary only)."
- L1273: "Impact: improves excerpt-aware workflow review + human-gate traceability."
- L1279: "- context: First attempt to run the excerpt-aware workflow for Case-01 (SAYUR, excerpt_id = sayur_052_066) after marking Case-01 as validation-ready."
- L1283: "python sandbox/crew/run_excerpt_workflow.py \"
- L1293: "/Users/vwvd/Millway/AI-folder/Crew-AI/sandbox/crew/run_excerpt_workflow.py: [Errno 2] No such file or directory"
- L1297: "this is a precondition failure (runner not implemented), not a workflow failure."
- L1305: "keep PHASE6_IMPLEMENT_EXCERPT_AWARE_RUNNER as the explicit next action."
- L1314: "- excerpt metadata propagated correctly into the log header."
- L1332: "- runner: `python sandbox/crew/run_excerpt_workflow.py --config sandbox/crew/shakedown_sayur_mistral.yaml ...`"
- L1353: "- This is acceptable for Phase-6 validation (excerpt-awareness + layout), but may be"
- L1362: "- runner: `run_excerpt_workflow.py` with `sandbox/crew/shakedown_sayur_mistral.yaml`"
- L1375: "- The refined payload contract (raw_output + payload field) is now in effect."
- L1389: "- 2026-01-06 — Phase-6 Case-02 LOBAK shakedown-run (excerpt-aware)"
- L1390: "- command: python sandbox/crew/run_excerpt_workflow.py --excerpt-id lobak_034_048 --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md --excerpt-version locked-2026-01-12 --config sandbox/crew/configs/lobak_case02.yaml"
- L1401: "- 2026-01-06 — Phase-6 Case-02 config created"
- L1409: "- 2026-01-06 — Phase-6 Case-02 LOBAK shakedown-run #2 (excerpt-aware)"
- L1410: "- command: python sandbox/crew/run_excerpt_workflow.py --excerpt-id lobak_034_048 --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md --excerpt-version locked-2026-01-12 --config sandbox/crew/configs/lobak_case02.yaml"
- L1421: "- 2026-01-06 — Phase-6 Case-02 LOBAK shakedown-run #3 (excerpt-aware, annotator+challenger)"
- L1422: "- command: python sandbox/crew/run_excerpt_workflow.py --excerpt-id lobak_034_048 --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md --excerpt-version locked-2026-01-12 --config sandbox/crew/configs/lobak_case02.yaml"
- L1435: "- payload is null, with JSON parse warning in the log (expected per Phase-6 runner refinement design)"
- L1437: "- 2026-01-06 — Phase-6 Case-02 LOBAK shakedown-run #3 (excerpt-aware, annotator+challenger)"
- L1438: "- command: python sandbox/crew/run_excerpt_workflow.py --excerpt-id lobak_034_048 --excerpt-source docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md --excerpt-version locked-2026-01-12 --config sandbox/crew/configs/lobak_case02.yaml"
- L1451: "- payload is null, with JSON parse warning (expected under current Phase-6 runner refinement design)"
- L1463: "### P6 — Human Review Workflow Defined"
- L1467: "Added docs/P6_HUMAN_REVIEW_WORKFLOW.md describing lifecycle stages"
- L1468: "(CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL)."
- L1469: "Clarifies human-only final authority and rollback rules."
- L1476: "Reviewed LOBAK Case-02 annotator output using the Phase-6 human review lane."
- L1479: "No canonisation performed; output promoted only to READY_FOR_HUMAN_REVIEW."
- L1482: "ID: P7_CANONICAL_TRAIL_REHEARSAL_LOBAK_001"
- L1483: "Actor: Codex-Phase7"
- L1485: "- Phase-7 kicked off (canonical decision trails)."
- L1486: "- Created P7_DECISION_TYPES.md and P7_CANONICAL_TRAIL_SPEC.md (draft, v1)."
- L1487: "- Added Human Review Participation Model to P6_HUMAN_REVIEW_WORKFLOW.md and P7_CANONICAL_TRAIL_SPEC.md."
- L1488: "- Designed and executed P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md using LOBAK Case-02 (excerpt_id lobak_034_048)."
- L1491: "Documentary lifecycle rehearsal only; no real canonical decisions were made."
- L1498: "ID: P7_CANONICAL_GLOSSARY_LOBAK_001"
- L1499: "Actor: HumanGate-Editorial"
- L1501: "- Eerste echte Phase-7 canonical decision uitgevoerd."
- L1502: "- "lobak" canoniek gemarkeerd als glossary-lemma (itemisation only, geen betekenis/vertaling)."
- L1504: "docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSARY_LOBAK_001.md"
- L1505: "- CANONICAL_INDEX.md uitgebreid met één entry voor deze beslissing."
- L1508: "- Laat betekenissen en vertalingen expliciet open voor latere, afzonderlijke canonical decisions."
- L1511: "- Maak een nieuw canonical decision record met supersedes: P7_CANONICAL_GLOSSARY_LOBAK_001"
- L1512: "en update CANONICAL_INDEX.md zodat alleen het nieuwe record als actief wordt gezien."
- L1516: "ID: P7_PHASE_CLOSE"
- L1517: "Actor: HumanGate-Editorial"
- L1519: "- Phase-7 closed."
- L1520: "- Canonical decision trail designed, rehearsed, and validated via the first real pilot (“lobak” lemma)."
- L1523: "- Canonical decision trails are stable and ready for broader editorial use."
- L1529: "Summary: Editorial capabilities vastgelegd als inhoudelijke basis voor vertaal- en annotatiebeslissingen (los van tools en governance)."
- L1530: "Impact: Verankert redactioneel vakmanschap als primaire norm; techniek en governance worden ondersteunend gepositioneerd."

## docs/handovers/handover_woensdagavond/CODEX_TODO.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Codex TODO – Mustikarasa
- ## Kern
- ### PHASE-1 Foundations (completed / historic)
- #### System Governance & Architecture
- ### PHASE-2 Roadmap (governed backlog — in progress)
- ### PHASE-3 Documentation Reorganisation (planned)
- ## PHASE4_AGENT_BRIDGE_DESIGN
- ## PHASE4_AGENT_HARNESS_SPEC
- ## PHASE4_AGENT_HARNESS_SPEC (detailed backlog entry)
- ### User Story
- ### Governance Alignment
- ### Risk & STOP Triggers
- ### Non-Functional Considerations
- ### Definition of Ready
- ### Artefacts Touched
- ### Related Documents
- ## PHASE4_AGENT_BRIDGE_DESIGN (detailed backlog entry)
- ## User Story
- ## Context & Intent
- ## Governance Alignment
- ## Risk & STOP Triggers
- ## Acceptance Criteria
- ## Artefacts
- ## Related
- ## Methodology Log
- ## PHASE-5 — Prompt Pattern
- ## PRACTICE — Archivist alignment rhythm
- ### PHASE-6 Workflow & Repo Architecture (planning)
- ## Phase-6 — Clarity & Canon Governance (lightweight)
- ### PHASE6_CASE02_RUNNER_MAPPING — PENDING
- ### Phase-7 — Canonical Decision Trails
- ### Capability Mapping Follow-Ups (documentation only)

Quoted phrases:
- L6: "[ PARKED — Phase-5 ] intentionally deferred (not a bug, just timing)"
- L14: "- [ ] Basis chapter-/batch-workflow ontwerpen (JSON + subcommand) → zie PHASE2_CHAPTER_BATCH_WORKFLOW_DESIGN"
- L15: "- [x] Documentatie voor workflow in docs/WORKFLOW.md (documentatie aanwezig in docs/WORKFLOW.md)"
- L17: "### PHASE-1 Foundations (completed / historic)"
- L25: "#### System Governance & Architecture"
- L32: "Output zal o.a. terechtkomen in prompts/orchestrator.md en (optioneel) docs/WORKFLOW.md."
- L37: "Output in een nieuw document: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md."
- L39: "- [x] SYSTEM_GOVERNANCE_TRIGGERS"
- L47: "Output in een nieuw of bestaand document, bijv. docs/AGENTS.md of docs/WORKFLOW.md."
- L49: "- [x] SYSTEM_GOVERNANCE_TESTS"
- L50: "Ontwerp van een kleine test-suite die governance zelf test:"
- L54: "Output als nieuw document, bijv. docs/10-governance/GOVERNANCE_TESTS_PLAN.md."
- L56: "### PHASE-2 Roadmap (governed backlog — in progress)"
- L58: "- [x] **PHASE2_AGENT_AUTONOMY_COMPLETION** (autonomy model applied across all editorial agents)"
- L59: "Alle actieve redactionele agents krijgen dezelfde “Autonomy / Soft-Stop / Governance-Stop / Human-Gate”"
- L65: "- [x] **PHASE2_TODO_REALITY_SYNC** (completed — aligned TODO with repo; see session PHASE2_TODO_REALITY_SYNC)"
- L70: "- [x] **PHASE2_CHAPTER_BATCH_WORKFLOW_DESIGN** (design documented in CHAPTER_BATCH_WORKFLOW.md)"
- L71: "Ontwerpdocument voor hoofdstuk/batch-workflow (zonder code)."
- L72: "Beschrijft input/output per batch, governance-touchpoints en escalatie op batch-niveau."
- L73: "Output: docs/CHAPTER_BATCH_WORKFLOW.md (+ korte samenvatting in WORKFLOW.md)."
- L75: "- [x] **PHASE2_GOVERNANCE_AGENT_RUNTIME_INTEGRATION_DESIGN** (design documented in GOVERNANCE_INTEGRATION_DESIGN.md)"
- L76: "Ontwerp hoe governance-agents in de Python-runtime worden aangeroepen"
- L78: "Output: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md."
- L80: "- [x] **PHASE2_GLOSSARY_RESEARCH_PILOT** (pilot documented — proposals only, no final decisions)"
- L85: "- [x] **PHASE2_GOVERNANCE_TEST_SCENARIO_1** (scenario executed — documentary test)"
- L86: "Eerste concrete uitvoering van een scenario uit GOVERNANCE_TESTS_PLAN.md"
- L88: "Output: docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md."
- L90: "### PHASE-3 Documentation Reorganisation (planned)"
- L92: "- [ PARKED — Phase-5 ] **PHASE3_DOCS_REORG_PLAN_APPROVED**"
- L95: "- [ PARKED — Phase-5 ] **PHASE3_DOCS_REORG_MOVE_PILOTS**"
- L98: "- [ DONE — P4 ] **PHASE3_DOCS_REORG_MOVE_GOVERNANCE** (governance docs moved according to DOCS_INFORMATION_ARCHITECTURE — pilot scope only)"
- L99: "Fysiek verplaatsen van governance-/workflowdocs naar 10-governance/ en 30-workflow/."
- L101: "- [ PARKED — Phase-5 ] **PHASE3_DOCS_REORG_UPDATE_REFERENCES**"
- L104: "- [PHASE3] Review whether “verify against stored artefacts” should become a requirement (later, via governance lifecycle)."
- L105: "- [PHASE3] Design a sampling pilot to analyze how “²” is used across the corpus (evidence-building, no text edits)."
- L106: "- [PHASE3] LEGACY_IMPORT_PATTERN: All future imports from legacy repo must use the same governed process (small batches, role-separated, provenance headers, read-only)."
- L107: "- [PHASE3] Proposal: design a follow-up pilot that only detects and flags ambiguous “²” cases (no auto-fix), to test governance-aligned review workflows."
- L108: "- [PHASE3] Prototype a review-handoff workflow where flagged items are routed to a human reviewer (no edits — decision logging only)."
- L109: "- [PHASE3] Consider a follow-up pilot simulating disagreement between reviewers and escalation to Human Gate (no edits — governance only)."
- L110: "- [PHASE3] Consider a future governance pilot with multiple conflicting reviewers and explicit evidence links (scan images / research docs) before any decision moves beyond provisional."
- L111: "- [PHASE3] Proposal: explore annotation-vs-translation patterns for context-dependent food terms (no decisions — pilot only)."
- L112: "- [PHASE3] Proposal: design a small readability-pressure pilot testing when annotations become excessive (no rules — documentary only)."
- L113: "- [PHASE3] Proposal: future pilot comparing reader feedback on minimally vs heavily annotated excerpts (controlled test)."
- L114: "- [PHASE3] Proposal: design a micro-pilot exploring when cultural notes belong in annotations vs separate historical commentary."
- L115: "- [PHASE4] Evaluate whether observed workflow gaps merit design changes (based on pilots and synthesis docs)."
- L116: "- [PHASE4] Consider formal diagramming once governance architecture stabilizes (policy-track, not Phase-3)."
- L117: "- [PHASE4] Design incident templates (INCIDENT_REPORT + REVIEW_LOG) —"
- L118: "policy-track, not Phase-3."
- L119: "- [PHASE3] Consider a lifecycle walk-through pilot using ubi/ketela"
- L121: "- [PHASE3] Design a second lifecycle rehearsal using a different term"
- L123: "- [PHASE3] Consider a “flag-only OCR scanner” proposal pilot"
- L125: "- [PHASE3] If useful, design a *governance review simulation* for the"
- L127: "- [PHASE3] Optional follow-up: design a *reader study proposal*"
- L130: "## PHASE4_AGENT_BRIDGE_DESIGN"
- L132: "**Phase Tag:** PHASE-4.1 (Preparation — documentary only)"
- L133: "**Category:** Governance / Design"
- L137: "As a governance architect, I want a safe bridge between CrewAI outputs and"
- L144: "how they are marked as proposals, how governance reviews them, and how"
- L149: "- agents modifying canonical text"
- L155: "**Governance Alignment**"
- L157: "- Lifecycle: requires governance review before any implementation"
- L158: "- Human Gate: only if design implies irreversible behavior"
- L181: "## PHASE4_AGENT_HARNESS_SPEC"
- L183: "**Phase Tag:** PHASE-4.1 (Preparation — documentary / scaffolding)"
- L184: "**Category:** Runtime / Governance / Engineering"
- L190: "logged, reversible, governance-aware, and cannot touch canonical texts"
- L199: "- harness writing into docs/ or canonical text"
- L204: "**Governance Alignment**"
- L206: "- Lifecycle: governance review before implementation"
- L207: "- Human Gate: only if non-sandbox use is proposed"
- L220: "- governance reviewers identified"
- L230: "## PHASE4_AGENT_HARNESS_SPEC (detailed backlog entry)"
- L232: "**ID:** PHASE4_AGENT_HARNESS_SPEC"
- L233: "**Phase Tag:** PHASE-4.1 — Preparation (documentary / scaffolding)"
- L234: "**Category:** Runtime / Governance / Engineering"
- L242: "canonical texts."
- L268: "### Governance Alignment"
- L271: "- Lifecycle: proposal → governance review → possible pilot later"
- L272: "- Human Gate: only if harness is proposed for canonical editing or"
- L281: "Governance-stop if:"
- L285: "Human Gate if:"
- L286: "- the harness is proposed for use on non-sandbox / canonical corpora"
- L301: "- safety: read-only access to canonical docs only"
- L310: "- governance reviewers are identified"
- L311: "- risks have been reviewed at least once in governance"
- L331: "- referenced-only: docs/WORKFLOW.md, docs/PHASE4_READINESS_NOTES.md"
- L332: "- unchanged: all canonical texts and runtime code"
- L337: "- docs/WORKFLOW.md"
- L338: "- docs/PHASE4_READINESS_NOTES.md"
- L340: "- governance stop model"
- L351: "## PHASE4_AGENT_BRIDGE_DESIGN (detailed backlog entry)"
- L353: "ID: PHASE4_AGENT_BRIDGE_DESIGN"
- L354: "Phase Tag: PHASE-4.1 — Preparation (documentary only)"
- L355: "Category: Governance / Runtime Safety"
- L359: "As a governance architect, I want a safe bridge between CrewAI outputs and governed artifacts,"
- L360: "so that agents can contribute analysis without ever modifying canonical texts or creating policy accidentally."
- L366: "and how governance reviews and rolls back mistakes — without enabling runtime behavior."
- L375: "## Governance Alignment"
- L377: "- Lifecycle: requires governance review before implementation"
- L378: "- Human Gate: only if behavior could affect publication"
- L383: "Governance-stop if canonical writes become possible."
- L384: "Human Gate if design touches publication paths."
- L388: "Given governance reviews them, glossary state does not change."
- L411: "- references: governance docs, lifecycle docs"
- L414: "- docs/WORKFLOW.md"
- L415: "- docs/PHASE4_READINESS_NOTES.md"
- L422: "phase: 4.1"
- L431: "- docs/10-governance/AGENT_AUTONOMY_ENVELOPE.md"
- L435: "Phase-4.1 shakedown om een enkele Mistral-annotatieagent (via Crew + Ollama)"
- L443: "- GO-status voor RUN-P4-SAYUR-A-0001 bevestigd in HUMAN_GATE_LOG.md"
- L444: "- sandbox readiness: docs/10-governance/SANDBOX_READINESS_CHECKLIST_P4_V1.md ≈ [x]"
- L452: "en HUMAN_GATE_LOG.md voor RUN-P4-SAYUR-A-0001."
- L458: "- GOVERNANCE_INTEGRATION_DESIGN.md"
- L514: "met een gedocumenteerde reden (soft-stop / governance-stop)."
- L523: "Mitigation: flagged for later human review (Phase-5), not a blocker."
- L547: "## PHASE-5 — Prompt Pattern"
- L554: "- no runtime or prompt rewrites without Human Gate review"
- L555: "- use labels: compliant / needs-clarification / defer-to-governance"
- L565: "- geen herstructurering zonder Human Gate"
- L568: "### PHASE-6 Workflow & Repo Architecture (planning)"
- L570: "- [x] PHASE6_RUNNER_OUTPUT_LAYOUT (layout validated & READY_FOR_IMPLEMENTATION in P6_RUNNER_OUTPUT_LAYOUT.md)"
- L575: "already have a governed home — without new governance rules."
- L577: "- [x] PHASE6_RUNNER_PAYLOAD_REFINEMENT"
- L579: "in run_excerpt_workflow.py for new runs only (no retro-edit of existing outputs)."
- L581: "- [x] PHASE6_SAYUR_MINI_WORKFLOW_DESIGN (docs/P6_WORKFLOW_SAYUR_MINI.md)"
- L582: "Ontwerpdocument voor een kleine, reproduceerbare workflow:"
- L586: "(sandbox/workflows/p6_sayur_mini/*)."
- L587: "Output: docs/P6_WORKFLOW_SAYUR_MINI.md (documentair, geen runtime-wijzigingen)."
- L589: "- [x] PHASE6_SAYUR_MINI_WORKFLOW_PILOT (docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT.md)"
- L590: "Eerste uitgevoerde pilot volgens P6_WORKFLOW_SAYUR_MINI:"
- L594: "Output: pilot-log + korte evaluatie in docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT.md."
- L596: "- [x] PHASE6_SAYUR_MINI_WORKFLOW_PILOT02 (docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT02_EVALUATION.md)"
- L599: "and challenger bias patterns. Outputs follow the same workflow as Pilot 01."
- L601: "- [x] PHASE6_SAYUR_MINI_WORKFLOW_SYNTHESIS (docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT_SYNTHESIS.md)"
- L604: "- [x] PHASE6_SAYUR_MINI_WORKFLOW_PILOT03"
- L607: "→ docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT03_EVALUATION.md"
- L610: "- [x] PHASE6_EXCERPT_BINDING_SPEC"
- L611: "Design change: workflows must accept an explicit `excerpt_id` / `excerpt_path`"
- L616: "- [x] PHASE6_EXCERPT_BINDING_INTEGRATION_PLAN"
- L617: "Plan how excerpt binding (metadata fields) will propagate consistently into"
- L621: "- [x] PHASE6_EXCERPT_METADATA_INTEGRATION_DOCS"
- L623: "evaluation templates, and workflow JSON examples so excerpt usage becomes"
- L626: "- [x] PHASE6_REPOSITORY_ARCHIVIST_INTEGRATION (integration rules documented in P6_REPOSITORY_ARCHIVIST_INTEGRATION.md)"
- L627: "Define how and when the Repository Archivist agent participates in Phase-6 workflows:"
- L633: "- [x] PHASE6_INDEX_EXPANSION_PASS"
- L634: "Editorial Index expanded with Phase-6 documents."
- L636: "- [x] PHASE6_NAV_GROUPING_CANDIDATES_REPORT"
- L648: "- [x] PHASE6_EXCERPT_BINDING_IN_RUNTIME_DESIGN (design frozen in P6_EXCERPT_BINDING_RUNTIME_DESIGN.md)"
- L649: "Design-only: define how excerpt_id/source/version propagate into runner logs"
- L652: "- [x] PHASE6_CASE01_READINESS_PLAN (readiness checklist defined in P6_CASE01_READINESS_PLAN.md; Case-01 is validation-ready: readiness, execution, validation docs exist)"
- L656: "- [ ] PHASE6_NAV_GROUPING_LOW_RISK_MOVE_PLAN"
- L659: "- [ ] PHASE6_NAV_LINK_CONSISTENCY_PASS"
- L662: "- [ ] PHASE6_IMPLEMENT_EXCERPT_AWARE_RUNNER"
- L663: "Implement an excerpt-aware runner and logging path matching P6_EXCERPT_AWARE_RUNNER_DESIGN.md for Case-01/Case-02, without changing governance rules."
- L664: "- Create a real script (e.g. sandbox/crew/run_excerpt_workflow.py or equivalent),"
- L668: "- [x] PHASE6_CASE02_EXCERPT_SELECTION (excerpt lobak_034_048 locked, 2026-01-12)"
- L675: "## Phase-6 — Clarity & Canon Governance (lightweight)"
- L677: "- [ ] PHASE6_CANONICAL_CRITERIA_OVERVIEW"
- L678: "Create docs/CANONICAL_CRITERIA_OVERVIEW.md."
- L679: "Purpose: summarize — in one place — what “CANONICAL” means, who approves it,"
- L680: "and how it relates to the lifecycle (CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL)."
- L681: "Keep it documentary; reference existing governance docs rather than inventing new rules."
- L683: "- [ ] PHASE6_CONFLICT_HANDLING_GUIDE"
- L685: "Describe: when to leave disagreements in PROVISIONAL, when to escalate to Human Gate,"
- L689: "- [ ] PHASE6_ANNOTATION_QUALITY_NOTE"
- L691: "Explain how quality is ensured in practice (annotator + challenger, bias checks, pilots, Human Gate)."
- L694: "- [ ] PHASE6_CANON_EVOLUTION_POLICY_NOTE"
- L695: "Create docs/CANONICAL_EVOLUTION_NOTE.md."
- L696: "Document — at a high level — how canonical material may change over time"
- L698: "Keep scope small; no new governance, just transparency."
- L702: "### PHASE6_CASE02_RUNNER_MAPPING — PENDING"
- L714: "- logs and outputs follow the Phase-6 layout."
- L719: "- This item is documentary until governance explicitly approves"
- L724: "### Phase-7 — Canonical Decision Trails"
- L727: "status: DONE — rehearsal-only, non-canonical"
- L729: "- docs/pilots/P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md"
- L734: "status: DONE — first real canonical decision (lemma only, non-semantic)"
- L736: "- docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSARY_LOBAK_001.md"
- L737: "- docs/CANONICAL_INDEX.md"
- L743: "- docs/pilots/P7_CANONICAL_PILOT_REFLECTION.md"
- L751: "- [ ] MAP_REVIEW_PHASE3_IMPACT"
- L754: "Note: do not execute automatically — governance review first."

## docs/handovers/handover_woensdagavond/DOCS_INFORMATION_ARCHITECTURE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Docs Information Architecture — Phase 5
- ## 1. Canonical (leidende documenten)
- ## 3. Phase-5 Consolidation & Preparation
- ## 5. Prompts & Crews
- ## 7. Navigatie-afspraken

Quoted phrases:
- L1: "# Docs Information Architecture — Phase 5"
- L3: "Status: documentation — canonical map"
- L11: "## 1. Canonical (leidende documenten)"
- L19: "- docs/WORKFLOW.md"
- L22: "- docs/10-governance/*  (policies, gates, rollback, incident playbooks)"
- L24: "> Regel: canonical = bron voor besluiten."
- L25: "> Als iets conflicteert, wint canonical (met uitleg)."
- L45: "## 3. Phase-5 Consolidation & Preparation"
- L58: "> maar veranderen gedrag niet zonder governance-approval."
- L80: "> Regel: prompts volgen het Phase-5 pattern —"
- L81: "> wijzigingen = documentair + human-gated."
- L115: "- nooit canonical-documenten herschrijven zonder uitleg/log"

## docs/handovers/handover_woensdagavond/EDITORIAL_CAPABILITIES.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## 0. Doel van dit document
- ## 6. Culinary Validation
- ## 11. Relatie met techniek en governance

Quoted phrases:
- L7: "Het gaat niet over tools, agents, pipelines of governance,"
- L9: "Andere documenten (VISION_AND_STRATEGY, REQUIREMENTS, GOVERNANCE, WORKFLOW)"
- L12: "> Redactie leidt, techniek ondersteunt, governance beschermt."
- L116: "geen inhoudelijke herschrijving van de canonieke tekst."
- L205: "## 11. Relatie met techniek en governance"
- L210: "- Governance (requirements, workflow, lifecycle) beschermt de grenzen"

## docs/handovers/handover_woensdagavond/GOVERNANCE_INTEGRATION_DESIGN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Governance Agent Runtime Integration Design
- ## Purpose
- ## Scope
- ## Runtime Events & Triggers
- ### Methodology & Accountability Archivist
- ### Incident & Resilience (Troubleshooting) Agent
- ### Glossary / Terminology Agent
- ## Data & Logging Model
- ## Failure Modes & Safeguards
- ## Non-Goals
- ## Relationship to Other Docs

Quoted phrases:
- L1: "# Governance Agent Runtime Integration Design"
- L4: "Legt vast hoe governance-agents (Methodology, Technical, Troubleshooting, Glossary, Research)"
- L18: "- Batch/Chapter workflow wordt meegenomen als context voor events."
- L24: "- Mogelijke governance-agents: Methodology, Research."
- L25: "- PhaseCompleted (Translation/Readability/Fidelity)"
- L27: "- Mogelijke governance-agents: Troubleshooting, Methodology."
- L30: "- Mogelijke governance-agents: Troubleshooting, Methodology."
- L33: "- Mogelijke governance-agents: Troubleshooting, Research."
- L36: "- Mogelijke governance-agents: Glossary, Methodology, Research."
- L39: "- Mogelijke governance-agents: Technical, Methodology."
- L40: "- WorkflowChangeProposal"
- L42: "- Mogelijke governance-agents: Methodology, Troubleshooting."
- L45: "- Mogelijke governance-agents: Troubleshooting, Methodology."
- L51: "- bij grote workflow-wijzigingen,"
- L52: "- bij afronden van SYSTEM_* of PHASE2_* items,"
- L86: "- beslist of workflow veilig kan doorgaan of human gate nodig is."
- L97: "- blijft proposal-only; beslissingen via Human Gate."
- L112: "- governance-calls worden gelogd met event-ID, agentnaam en artefacttype."
- L119: "- governance-agent niet aangeroepen wanneer dat wel had gemoeten."
- L120: "- governance-agent levert geen geldig artefact terug."
- L124: "- soft-stop verplicht bij inconsistente of ontbrekende governance-output."
- L125: "- Orchestrator mag batch NIET stilzwijgend laten doorgaan wanneer een governance-stap faalt;"
- L130: "- alle beslissingen blijven reversibel zolang governance-artefacten incompleet zijn."
- L132: "- stop-model: docs/WORKFLOW.md"
- L133: "- testplan: docs/10-governance/GOVERNANCE_TESTS_PLAN.md"
- L134: "- voorbeelden: docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md en docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md"
- L139: "- geen bypass van bestaande Human Gates."
- L142: "- docs/WORKFLOW.md"
- L143: "- docs/CHAPTER_BATCH_WORKFLOW.md"
- L144: "- docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md"
- L145: "- docs/10-governance/GOVERNANCE_TESTS_PLAN.md"

## docs/handovers/handover_woensdagavond/P7_CANONICAL_GLOSSARY_LOBAK_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## Lifecycle & Governance
- ## Risk & Rollback
- ## References

Quoted phrases:
- L2: "decision_id: P7_CANONICAL_GLOSSARY_LOBAK_001"
- L4: "phase: P7"
- L5: "status: canonical"
- L26: "## Lifecycle & Governance"
- L29: "- lifecycle.to_status: CANONICAL"
- L48: "Rollback occurs by creating a NEW canonical decision record that supersedes this one."
- L53: "- docs/P7_CANONICAL_TRAIL_SPEC.md"
- L54: "- docs/pilots/P7_CANONICAL_PILOT_GLOSSARY_LOBAK_001.md"

## docs/handovers/handover_woensdagavond/P7_CANONICAL_PILOT_REFLECTION.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-7 Canonical Pilot — Reflection (LOBak lemma)
- ## 1) Scope
- ## 2) What Worked
- ## 3) What Did NOT Need Changing
- ## 5) Outcome
- ## 6) Meta

Quoted phrases:
- L1: "# Phase-7 Canonical Pilot — Reflection (LOBak lemma)"
- L5: "This pilot tested canonical decision trails on a safe case:"
- L10: "- Excerpt binding propagated correctly."
- L11: "- Human-only canonical gate functioned."
- L19: "- No governance expansion required; existing guardrails were sufficient."
- L30: "- Phase-7 canonical trail design is validated for glossary scenarios."
- L38: "- docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSARY_LOBAK_001.md"
- L40: "- docs/P7_CANONICAL_TRAIL_SPEC.md"

## docs/handovers/handover_woensdagavond/P7_PHASE_RETRO_REPO_VIEW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-7 Retrospective — Repository View
- ## 1. What was planned
- ## 2. What actually happened
- ## 3. What worked well (from repo evidence)
- ## 5. Governance & decision types
- ## 6. Suggested follow-ups (repo-based)
- ## 7. Meta

Quoted phrases:
- L1: "# Phase-7 Retrospective — Repository View"
- L4: "- Define a canonical decision trail (decision types matrix + trail spec) and keep decisions human-only where required."
- L6: "- Execute a first real, low-risk canonical pilot and record a reflection on decision-type tuning."
- L9: "- Decision types matrix and canonical trail spec were created (P7_DECISION_TYPES.md, P7_CANONICAL_TRAIL_SPEC.md)."
- L11: "- The first real canonical pilot (“lobak” lemma inclusion) produced a canonical decision record."
- L12: "- CANONICAL_INDEX.md was updated with one Phase-7 entry for the “lobak” decision."
- L13: "- A pilot reflection confirmed no decision-type changes were needed, and Phase-7 was closed in the session log."
- L17: "- Human-only gate behavior was enforced for canonical decisions."
- L24: "## 5. Governance & decision types"
- L26: "- Glossary lemma decisions remained HUMAN ONLY in the canonical trail."
- L27: "- Guardrails in the trail spec (no auto-promotion, human gate) remained intact in practice."
- L32: "- Optional validation checklist for canonical records (suggested in rehearsal reflection)."
- L35: "- reviewer: HumanGate-Editorial (repo-based)"
- L40: "- docs/P7_CANONICAL_TRAIL_SPEC.md"
- L41: "- docs/pilots/P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md"
- L43: "- docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSARY_LOBAK_001.md"
- L44: "- docs/pilots/P7_CANONICAL_PILOT_REFLECTION.md"
- L46: "- docs/CANONICAL_INDEX.md"
- L47: "- docs/P6_HUMAN_REVIEW_WORKFLOW.md"

## docs/handovers/handover_woensdagavond/P8_CAPABILITY_MAP.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-8 Capability Map — Editorial System Maturity
- ## 1. Purpose
- ### 2.1 Text Acquisition & Integrity
- ### 2.2 Structure & Navigation
- ### 2.3 Glossary & Knowledge Management
- ### 2.4 Text-Critical / Variants
- ### 2.5 Editorial Quality & Readability
- ### 2.6 Trail & Reproducibility
- ### 2.7 Reviewer Support & Triage
- ## 3. Maturity Model
- ## 4. Capability × Maturity × Responsibility Matrix
- ## 5. Derived Role Implications (No Roles Yet)
- ## 6. Alignment with Guardrails
- ## 7. Next Step from Capability Map

Quoted phrases:
- L1: "# Phase-8 Capability Map — Editorial System Maturity"
- L5: "Phase-8 designs capabilities first; agent roles are derived from those"
- L6: "capabilities, not the other way around. Governance remains unchanged:"
- L7: "canonical decisions are human-only, and rollback occurs via new records."
- L15: "- Relation to canonical decisions: supports trustworthy evidence for later human decisions."
- L21: "- Relation to canonical decisions: keeps context stable for review, not a canonical decision itself."
- L27: "- Relation to canonical decisions: supports lemma inclusion decisions; meanings remain human-only."
- L33: "- Relation to canonical decisions: provides evidence bundles for human variant choices."
- L39: "- Relation to canonical decisions: advisory signals only; not a decision lane."
- L45: "- Relation to canonical decisions: required mechanical integrity before human gate."
- L51: "- Relation to canonical decisions: accelerates review without changing authority."
- L56: "- Level 1 — documented workflow"
- L58: "- Level 3 — tool/validator assisted (mechanical certainty)"
- L59: "- Level 4 — orchestration-aware collaboration (still human-only canonical)"
- L61: "Phase-8 typically aims for Level 2 → 3."
- L65: "| Capability | Current Maturity (estimate) | Phase-8 Target | Responsibility Model |"
- L67: "| Text Acquisition & Integrity | Level 1 | Level 3 | TOOL/VALIDATOR |"
- L72: "| Trail & Reproducibility | Level 2 | Level 3 | TOOL/VALIDATOR |"
- L80: "- Phase-8 priority: validator-style checks before review."
- L84: "- Must NEVER: reorganize canonical content or declare canonical structure."
- L85: "- Phase-8 priority: provisional diagnostics only."
- L89: "- Must NEVER: assign meanings or promote canonically."
- L90: "- Phase-8 priority: clean lemma signals + provenance."
- L94: "- Must NEVER: choose a variant or decide canonical readings."
- L95: "- Phase-8 priority: evidence bundling for human review."
- L99: "- Must NEVER: rewrite text or imply final editorial authority."
- L100: "- Phase-8 priority: advisory-only signals."
- L104: "- Must NEVER: mark CANONICAL or modify records."
- L105: "- Phase-8 priority: mechanical completeness checks."
- L110: "- Phase-8 priority: reduce reviewer overhead without changing authority."
- L114: "- Canonical trail remains untouched."
- L116: "- Validators help but do not gatekeep canonical promotion."
- L131: "- author: HumanGate-Editorial + Architecture"
- L134: "- docs/P8_PHASE_START_ARCHITECTURE.md"
- L135: "- docs/P7_CANONICAL_TRAIL_SPEC.md"

## docs/handovers/handover_woensdagavond/P8_PHASE_START_ARCHITECTURE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-8 Architecture & Start — Agentic Work Within Canonical Rails
- ## 1. Context and Inheritance
- ## 2. Phase-8 Goals (What Phase-8 WILL do)
- ## 3. Non-Goals (What Phase-8 Will NOT Do)
- ## 4. Agentic Capabilities in Phase-8
- ### 4.1 Agent Roles (examples)
- ### 4.2 Agent Constraints
- ## 5. Orchestration Patterns (Agentic Workflows)
- ## 6. Human Workload & Interaction Model
- ## 7. Risks and Mitigations
- ## 8. Phase-8 Deliverables (Architecture-Level)
- ## 9. Alignment with Existing Guardrails

Quoted phrases:
- L1: "# Phase-8 Architecture & Start — Agentic Work Within Canonical Rails"
- L5: "Phase-7 established canonical decision trails with a human-only canonical gate,"
- L7: "and canonical decisions. Phase-8 inherits these guardrails and MUST NOT change them."
- L9: "- Phase-7 outcome: canonical trail proven on a low-risk glossary case (“lobak” lemma)."
- L10: "- Agents are provisional; all canonical decisions are human-only."
- L13: "## 2. Phase-8 Goals (What Phase-8 WILL do)"
- L15: "- Reduce unnecessary human workload by improving agent support, NOT by granting agents more authority."
- L18: "- Introduce light-weight validators and checkers that run before the human gate (e.g. excerpt-binding, trail completeness)."
- L19: "- Keep all AI output strictly provisional, clearly separated from canonical decisions."
- L21: "## 3. Non-Goals (What Phase-8 Will NOT Do)"
- L23: "- No new governance layers or decision types that weaken Phase-7 guardrails."
- L24: "- No auto-promotion to CANONICAL, no automated creation of canonical decision records."
- L28: "## 4. Agentic Capabilities in Phase-8"
- L42: "- Validates whether a canonical decision record is mechanically complete"
- L49: "- create or update canonical decision records,"
- L50: "- modify canonical indices,"
- L51: "- set lifecycle to CANONICAL."
- L53: "## 5. Orchestration Patterns (Agentic Workflows)"
- L64: "All flows end in READY_FOR_HUMAN_REVIEW, never in CANONICAL."
- L65: "Human review sessions are the only place where canonical decisions are made."
- L72: "- making canonical decisions,"
- L81: "Phase-8 features (better agents + validators) should support this without"
- L82: "changing authority or responsibility."
- L91: "- Mitigation: add preflight validators and ensure trails are single source of truth."
- L93: "## 8. Phase-8 Deliverables (Architecture-Level)"
- L98: "- P8_PILOTS_PLAN.md — plan for a small set of Phase-8 pilots (e.g. OCR/typographic, structural, glossary support)."
- L102: "Phase-8 respects:"
- L105: "- Phase-6 infrastructure (excerpt-binding, runner),"
- L106: "- Phase-7 canonical trail spec and decision types."
- L111: "- Human gate is the only path to CANONICAL."
- L115: "- author: HumanGate-Editorial + Architecture/Agentic-Design"
- L119: "- docs/P7_CANONICAL_TRAIL_SPEC.md"
- L120: "- docs/retros/P7_PHASE_RETRO_REPO_VIEW.md"

## docs/handovers/handover_woensdagavond/README.md

Preliminary classification suggestion: AMBIGUOUS

Quoted phrases:
- L2: "- Read-only bundel met kern-documenten voor een Phase-8 vervolg."
- L3: "- Alleen kopieën; geen canonieke wijzigingen."
- L7: "- Canonieke beslissingen zijn menselijk; AI/agents blijven voorlopig."
- L10: "- Phase-7 canonical trail is bewezen met een eerste lemma-besluit (lobak)."
- L11: "- Phase-8 documentatie beschrijft agentic werk binnen bestaande guardrails."
- L15: "- Canoniek spoor: CANONICAL_INDEX.md en de P7 decision record"
- L17: "- Phase-overgangen: P7 retro, P7 pilot reflection, P8 start, P8 capability map"
- L18: "- Workflowcontext: WORKFLOW.md, GOVERNANCE_INTEGRATION_DESIGN.md, DOCS_INFORMATION_ARCHITECTURE.md"

## docs/handovers/handover_woensdagavond/WORKFLOW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # WORKFLOW OVERVIEW
- ## Rol van de Orchestrator
- ## Governance-lagen en ondersteunende agents
- ## Governance Triggers
- ### Glossary Agent — triggers
- ### Research Agent — triggers
- ## Autonomy & Escalation (Stop Model)
- ### Batch / Chapter Execution (Design)
- ### Governance Agent Runtime Integration (Design)
- ### Phase-3 (Pilots & Safety — design framing)
- ## Governance Tests
- ## Where to change what
- ## Handover Flows

Quoted phrases:
- L1: "# WORKFLOW OVERVIEW"
- L3: "Dit document beschrijft de huidige workflow en waar wijzigingen thuishoren."
- L16: "De Orchestrator is de workflow-conductor: coördineert agents, bewaakt templates"
- L17: "en governance, en zorgt dat outputs conform afspraken zijn. Het formele mandaat"
- L20: "## Governance-lagen en ondersteunende agents"
- L29: "## Governance Triggers"
- L31: "Deze triggers zijn verplicht en leveren governance‑artefacten op:"
- L32: "- Methodology Archivist bij nieuwe workflows, lifecycle‑wijzigingen en SYSTEM_* beslissingen"
- L45: "- verwijzing: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md"
- L53: "- verwijzing: docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md"
- L59: "| Agent | Soft-stop (self-healing) | Governance-stop (no human) | Human gate (hard-stop) |"
- L66: "| Orchestrator | Herordening, extra context | Troubleshooting + Methodology | Governance-conflict onoplosbaar |"
- L70: "Elke agent volgt dezelfde escalatielogica: soft-stop, governance-stop, en human-gate bij hoge impact of conflict."
- L74: "- Ontwerpdocument: `docs/CHAPTER_BATCH_WORKFLOW.md` (geen runtime-implementatie)."
- L79: "### Governance Agent Runtime Integration (Design)"
- L81: "- Ontwerpdocument: `docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md` beschrijft hoe governance-agents"
- L84: "- Bestaande workflow blijft leidend totdat code expliciet is aangepast."
- L86: "### Phase-3 (Pilots & Safety — design framing)"
- L89: "- governance test gecontroleerd falen"
- L91: "- verwijzing: docs/PHASE3_FRAMING.md"
- L93: "## Governance Tests"
- L95: "Het testplan voor governance staat in `docs/10-governance/GOVERNANCE_TESTS_PLAN.md` en is leidend\nvoordat er daadwerkelijke testcode wordt geïmplementeerd."
- L101: "- Governance- en procesdocumentatie: `docs/*.md`."
- L106: "(bijv. PHASE-1 Foundations) of vóór start van een nieuw projectblok (bijv. PHASE-2)."

## docs/handovers/handover_woensdagavond/addendum_handover/P8_MEANING_PRESERVATION_PILOT_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## 3. Source Fragment (sandbox)
- ## 5. Run Instructions (for humans)
- ## 7. Impact Template ([IMPACT_ASSESSMENT])
- ## 8. Notes & Limitations

Quoted phrases:
- L23: "canonical text."
- L63: "- Emphasize: no canonical decisions, no glossary changes, no source edits — this is for learning only."
- L79: "What should future pilots or workflows do differently because of what we saw here?"
- L89: "- nothing here changes any canonical decision or glossary entry"

## docs/handovers/handover_woensdagavond/addendum_handover/P8_MEANING_PRESERVATION_PILOT_001_RUN01.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Meta

Quoted phrases:
- L16: "- Dit is een pilot-run record (niet canoniek, niet voor publicatie)."

## docs/handovers/handover_woensdagavond/addendum_handover/README.md

Preliminary classification suggestion: GOV-A

Quoted phrases:
- L10: "- Phase-8-specifieke promptvarianten (afwijkingen)"
- L11: "- Phase-8 risico/failure-patterns document"

## docs/handovers/handover_woensdagavond/total_project.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 1) Projectdoel en context
- ## 2) Repository‑structuur (actuele bestandstoestand)
- ## 4) Workflow (huidige 3‑fasen pipeline)
- ## 5) Prompt‑systeem (governance‑regel)
- ## 7) Governance‑lagen en handovers tussen agents
- ### 7.1 Orchestrator (governance‑laag)
- ### 7.2 Template Agent (structurele contracten)
- ## 8) Documentatie en governance‑bestanden
- ### 8.2 `docs/CODEX_TODO.md`
- ## 11) Bekende handover‑punten (samengevat, feitelijk)
- ## 12) Bewuste beperkingen en non‑goals (zoals gedocumenteerd)
- ## 14) Orchestrator‑mandaat en grenzen (geconsolideerd)
- ## 15) Glossary Decision Lifecycle (terminologie‑beslisstraat)
- ## 16) Governance‑triggers (Methodology, Technical, Troubleshooting)
- ## 17) Autonomy, Soft‑Stop, Governance‑Stop en Human Gate
- ## 18) Governance testplan

Quoted phrases:
- L8: "Het project bouwt een gecontroleerde, multi‑agent vertaal- en redactie‑workflow voor het Mustikarasa‑kookboek met CrewAI en Mistral via Ollama."
- L10: "De rol van de Codex‑laag is governance, organisatie en reproduceerbare uitvoering via de terminal."
- L19: "- `docs/` (documentatie en governance)"
- L55: "- `docs/CHAPTER_BATCH_WORKFLOW.md`"
- L59: "- `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`"
- L61: "- `docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md`"
- L62: "- `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`"
- L63: "- `docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md`"
- L64: "- `docs/10-governance/GOVERNANCE_TESTS_PLAN.md`"
- L65: "- `docs/PHASE3_FRAMING.md` (Phase-3 strategisch kader)"
- L134: "## 4) Workflow (huidige 3‑fasen pipeline)"
- L152: "## 5) Prompt‑systeem (governance‑regel)"
- L217: "## 7) Governance‑lagen en handovers tussen agents"
- L219: "### 7.1 Orchestrator (governance‑laag)"
- L223: "- behandelt `TEMPLATE_DEFINITION` als contract"
- L232: "### 7.2 Template Agent (structurele contracten)"
- L260: "## 8) Documentatie en governance‑bestanden"
- L273: "- PHASE-1 foundations zijn afgerond; alle SYSTEM_* items staan op [x]."
- L274: "- PHASE-2 items staan in `docs/CODEX_TODO.md`; alle PHASE2_* items zijn gemarkeerd als [x]."
- L275: "- De kernsectie bevat nog één open item (basis chapter/batch‑workflow ontwerpen); workflow‑documentatie is [x]."
- L276: "Phase-3 bereidt gecontroleerde pilots voor, maar verandert (nog) niets aan productie-workflow."
- L306: "- **Pipeline‑faseoverdracht**: Phase 1 → Phase 2 → Phase 3 in `test_multi_agent_fidelity.py`."
- L307: "- **Template‑contract**: Orchestrator behandelt `TEMPLATE_DEFINITION` als contract en stuurt bij via Troubleshooting."
- L318: "- governance‑documenten zijn leidend"
- L331: "- `docs/WORKFLOW.md`"
- L334: "- workflow coördineren en agents aansturen;"
- L335: "- templates en formats bewaken en governance‑triggers activeren;"
- L344: "en wordt verder beschreven in `docs/AGENTS.md` en `docs/WORKFLOW.md`."
- L348: "`docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md` beschrijft de volledige beslis‑lifecycle:"
- L349: "Proposal → Context → Risk Review → Human Gate → Versioning → Rollback."
- L359: "Definitieve terminologiebeslissingen lopen altijd via een Human Gate."
- L361: "## 16) Governance‑triggers (Methodology, Technical, Troubleshooting)"
- L363: "Er is expliciet vastgelegd wanneer governance‑agents automatisch worden aangeroepen:"
- L364: "- Methodology Archivist: nieuwe workflows, lifecycle‑wijzigingen en SYSTEM_* beslissingen."
- L369: "- `prompts/orchestrator.md` (sectie “Governance Triggers”)"
- L373: "- `docs/AGENTS.md` en `docs/WORKFLOW.md`"
- L375: "De governance‑agents zijn adviserend/loggend en voeren geen code‑wijzigingen door."
- L377: "## 17) Autonomy, Soft‑Stop, Governance‑Stop en Human Gate"
- L385: "2) Governance‑Stop: inzet van governance‑agents om te analyseren en te loggen."
- L386: "3) Hard‑Stop / Human Gate: alleen bij high‑risk situaties (gezondheid, veiligheid, zwaar betwiste betekenis,"
- L387: "project‑brede glossary‑impact, governance‑conflicten)."
- L389: "Dit model borgt maximale autonomie met governance vóór menselijke escalatie."
- L390: "Zie `docs/AGENTS.md` (Autonomy & Escalation‑bullets) en `docs/WORKFLOW.md` (stop‑model tabel)."
- L392: "## 18) Governance testplan"
- L394: "`docs/10-governance/GOVERNANCE_TESTS_PLAN.md` bevat het testplan voor governance‑mechanismen (niet taalkwaliteit)."
- L398: "- governance‑triggers (Methodology/Technical/Troubleshooting)"
- L400: "- hard‑stop / human gate"

## docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Docs Information Architecture — Phase 5
- ## 1. Canonical (leidende documenten)
- ## 3. Phase-5 Consolidation & Preparation
- ## 5. Prompts & Crews
- ## 7. Navigatie-afspraken

Quoted phrases:
- L1: "# Docs Information Architecture — Phase 5"
- L3: "Status: documentation — canonical map"
- L11: "## 1. Canonical (leidende documenten)"
- L19: "- docs/WORKFLOW.md"
- L22: "- docs/10-governance/*  (policies, gates, rollback, incident playbooks)"
- L24: "> Regel: canonical = bron voor besluiten."
- L25: "> Als iets conflicteert, wint canonical (met uitleg)."
- L45: "## 3. Phase-5 Consolidation & Preparation"
- L58: "> maar veranderen gedrag niet zonder governance-approval."
- L80: "> Regel: prompts volgen het Phase-5 pattern —"
- L81: "> wijzigingen = documentair + human-gated."
- L115: "- nooit canonical-documenten herschrijven zonder uitleg/log"

## docs/navigation/EDITORIAL_INDEX.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Editorial Index (Phase-6)
- ## 1. Maintenance & Usage
- ## 2. Key Documents (initial subset)
- ### Phase-6 supporting references
- ### Reviews (Phase-6)
- ### Phase-7 — Canonical Decision Trails
- ### Phase-7 Rehearsal — Canonical Trail (NOT canonical)
- ### Phase-8 — Meaning Preservation (COMPLETED — REWORK ACCEPTED)
- ## 3. Generated Artefacts (directory-level reference)

Quoted phrases:
- L1: "# Editorial Index (Phase-6)"
- L4: "Scope: human-readable catalog of key editorial/gov/workflow docs under `docs/`"
- L9: "- does NOT replace `DOCS_INFORMATION_ARCHITECTURE.md`, `manifest_p5.yaml`, or `CANONICAL_INDEX.md`;"
- L18: "- `docs/CANONICAL_INDEX.md` (canonical set)"
- L26: "- When you create a new **governance / workflow / navigation / consolidation** doc under `docs/` via Codex, add a row to this table."
- L32: "System-generated artefacts (run logs, JSON, sandbox/workflows output) are NOT listed per file here."
- L35: "This document has no normative authority over governance; it is a navigation aid only."
- L41: "| Path                                       | Category    | Phase | Role                                                        | Authority | Risk (move) | Notes |"
- L43: "| docs/WORKFLOW.md                           | governance  | P3–P6 | High-level workflow & governance flow (when to stop, gate). | binding   | high        | Source for global workflow behaviour. |"
- L44: "| docs/PRODUCTION_GUARDRAILS_P5.md           | governance  | P5    | Autonomy matrix & escalation rules for agents/crews.        | binding   | high        | Do not move without governance review. |"
- L45: "| docs/P5_DECISION_LIFECYCLE.md              | governance  | P5    | Defines lifecycle: CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL. | binding | high | Core editorial lifecycle. |"
- L46: "| docs/CODEX_META_PROMPT.md                  | workflow    | P3–P6 | Rules for Codex as orchestrator (how to operate on repo).   | design    | high        | Changes affect how all Codex sessions behave. |"
- L47: "| docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md | navigation | P3–P6 | Category/zone design: canonical vs sandbox vs consolidation vs sources. | design | medium | Already moved into docs/navigation/. |"
- L48: "| docs/CANONICAL_INDEX.md                    | canonical   | P3–P6 | Source-of-truth list for canonical docs.                    | canonical | high        | Aligns with manifest_p5.yaml. |"
- L49: "| docs/P6_EDITORIAL_WORKFLOW_MINI.md | workflow | P6 | Generic editorial mini-workflow (roles, lifecycle, sequence). | design | medium | Used across chapters; no canonical actions. |"
- L50: "| docs/P6_WORKFLOW_SAYUR_MINI.md | workflow | P6 | First concrete application of the mini workflow to SAYUR. | design | medium | Historical reference; do not overwrite. |"
- L51: "| docs/P6_EXCERPT_BINDING_SPEC.md | workflow | P6 | Defines excerpt_id/source/version metadata discipline. | design | medium | Documentary only — prevents mismatched logs. |"
- L52: "| docs/P6_EXCERPT_BINDING_INTEGRATION_PLAN.md | workflow | P6 | Describes how excerpt metadata flows through logs and artefacts. | design | medium | Planning layer; not runtime-enforcing. |"
- L53: "| docs/P6_EXCERPT_AWARE_RUNNER_DESIGN.md | workflow | P6 | Design for future excerpt-aware runner (args + logging format). | design | medium | Design only; implementation deferred. |"
- L54: "| **P6_HUMAN_REVIEW_WORKFLOW.md** | workflow | P6 | Human-review lane specification (CANDIDATE → CANONICAL). | Draft | medium | Documents the human-only canonisation boundary and rollback behaviour. |"
- L55: "| **P6_ARCHIVE_ARCHITECTURE.md** | workflow | P6 | Archive architecture (Phase-6). | Active | medium | Defines directory layout and traceability rules for runs, outputs, reviews, and canonical references. |"
- L56: "| docs/P6_PRODUCTION_WORKFLOW_SAYUR.md | workflow | P6 | End-to-end design from source → scholarly → editorial → canonical. | design | high | Influences long-term structure. |"
- L57: "| docs/P6_REPO_ARCHITECTURE_MIGRATION_PLAN.md | navigation | P6 | Plan for gradual repo re-architecture with rollback + phases. | design | high | Consult before moving anything. |"
- L59: "| docs/P6_LOW_RISK_MIGRATION_CHECKLIST.md | navigation | P6 | Safe procedure for small doc moves and renames. | binding (process) | medium | Required for Phase-6 migrations. |"
- L62: "| docs/P6_SAYUR_INTERNAL_WORK_CASE01.md | workflow/case | P6 | Concrete application of generic editorial workflow to SAYUR excerpt (pending, excerpt-aware). | provisional | high | Bound to excerpt/logs. Placement governed by P6_CASEFILE_PLACEMENT_DECISION.md. |"
- L63: "| docs/P6_LOBAK_INTERNAL_WORK_CASE02.md | workflow/case | P6 | Second generic workflow rehearsal (LOBAK), excerpt not yet locked. | provisional | high | Remains in docs/ for traceability. Governed by P6_CASEFILE_PLACEMENT_DECISION.md. |"
- L64: "| docs/decisions/P6_CASEFILE_PLACEMENT_DECISION.md | decision | P6 | Documents why case files stay in docs/ and conditions for revisiting. | design (governance note) | high (if violated) | Decision is documentary but binding for migration planning."
- L65: "| docs/P6_RUNNER_OUTPUT_LAYOUT.md | workflow/runtime | P6 | Standard layout for logs and JSON outputs of future excerpt-aware runs. | design | medium | Guides implementation; does not change governance or existing logs."
- L67: "You can extend this table incrementally with other key documents (Phase-4 consolidation, Phase-5 pilot reports, Phase-6 workflows, etc.)."
- L68: "New Phase-6 design documents are considered “complete” only after they are listed here with path, role, and risk."
- L70: "> Phase-6 documents added here remain design-level unless explicitly promoted via governance."
- L71: "> This index tracks location, role and risk — it does not grant authority."
- L74: "> Case files are workflow-bearing artefacts and remain in `docs/` for traceability."
- L78: "### Phase-6 supporting references"
- L85: "Phase: P6"
- L89: "- Phase-6 Closure — summary of what Phase-6 proved and what was explicitly deferred"
- L90: "docs/pilots/P6_PHASE_CLOSURE.md"
- L95: "Phase: P6"
- L98: "Notes: Standard form for documenting human evaluation without canonising content."
- L100: "- `docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md` → Case-02 (LOBAK) — Excerpt Selection (governing); locks excerpt for Case-02, documentary only; mismatch with run artefacts must stop the workflow"
- L105: "### Reviews (Phase-6)"
- L110: "Phase: P6"
- L113: "Notes: First end-to-end test of human-review lane. Promoted to READY_FOR_HUMAN_REVIEW, no canonisation."
- L115: "- `docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md` → Case-02 (LOBAK) — Excerpt Selection (governing); locks excerpt for Case-02, documentary only; mismatch with run artefacts must stop the workflow"
- L120: "### Phase-7 — Canonical Decision Trails"
- L122: "Phase-7 introduces the canonical decision-trail architecture."
- L123: "AI outputs remain provisional; humans create canonical decisions"
- L129: "- P7_CANONICAL_TRAIL_SPEC.md"
- L130: "- (upcoming) pilots/P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md"
- L131: "- **Pilot complete:** first real canonical decision recorded — *“lobak” marked as glossary lemma (itemisation only; meaning/translation pending).*"
- L132: "See CANONICAL_INDEX.md for the full decision trail."
- L135: "(P6_HUMAN_REVIEW_WORKFLOW.md, P7_CANONICAL_TRAIL_SPEC.md)"
- L137: "### Phase-7 Rehearsal — Canonical Trail (NOT canonical)"
- L139: "Rehearsal files exist only to test the lifecycle of canonical decision records."
- L144: "- decisions/rehearsal/  (Phase-7 dry-run records)"
- L148: "### Phase-8 — Meaning Preservation (COMPLETED — REWORK ACCEPTED)"
- L150: "- Output-contract v2 + gate vastgesteld; FAIL-signalen blijven diagnostisch en niet-canoniek."
- L151: "- Geen auto-repair toegepast; governance-keuze blijft documentair."
- L152: "- Artefacten (Phase-8 / sandbox / experimental / not-for-publication):"
- L155: "- sandbox/tools/phase8_output_contract_validator.sh"
- L156: "- sandbox/tools/phase8_run_with_gate.sh"
- L165: "- `sandbox/workflows/` — annotator/challenger/crew JSON artefacts per run."
- L167: "- `sandbox/phase8_runs/` — Phase-8 agent-run artefacten:"
- L171: "- output-contract validation reports"
- L172: "Deze artefacten zijn evaluatief en niet-canoniek; zij ondersteunen"
- L173: "Phase-8 meaning-preservation testing en governance-leren."
- L174: "Runs kunnen PASS of FAIL zijn; beide blijven niet-canoniek."
- L175: "- Any other future per-run directories defined in Phase-6 runner designs."
- L177: "Consult the relevant workflow design documents (e.g. P6_EDITORIAL_WORKFLOW_MINI.md,"

## docs/navigation/P6_MIGRATION_CANDIDATE_LIST.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 — Migration Candidate List (Assessment Only)
- ## 2. Medium-risk (contains indirect workflow meaning)
- ## 3. High-risk (lifecycle-bearing artefacts)
- ## 4. Next step (documentary only)

Quoted phrases:
- L1: "# Phase-6 — Migration Candidate List (Assessment Only)"
- L25: "## 2. Medium-risk (contains indirect workflow meaning)"
- L30: "- meta-workflow notes"
- L42: "- canonical text or commentary"
- L43: "- any file referenced by Human Gate logs"
- L54: "2) Mark specific directories for Phase A (mapping only)"

## docs/navigation/PILOT_LOG_OVERVIEW.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Pilot & Log Overview (Phase-3/4/5 context)

Quoted phrases:
- L1: "# Pilot & Log Overview (Phase-3/4/5 context)"

## docs/pattern_reviews/P5_AGENT_PROMPT_REVIEW_ANNOTATOR.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # P5 — Agent Prompt Review: Annotation Agent
- ## Fit-check (pattern sections)
- ## Provisional classification
- ## Notes (no changes proposed yet)
- ## Next step (suggested)

Quoted phrases:
- L8: "Deze review toetst de bestaande annotator-prompt aan het Phase-5 Pattern,"
- L10: "(governance-gated) verbeteringen later."
- L19: "- OUTPUT CONTRACT: sterk (machine-checkbaar JSON)"
- L37: "Dit is geen fout — alleen een kans voor harmonisatie in Phase-5."
- L44: "- Eventuele aanscherpingen vereisen Human Gate review."
- L51: "Wanneer governance dat goedkeurt:"

## docs/pattern_reviews/P5_AGENT_PROMPT_REVIEW_CHALLENGER.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # P5 — Agent Prompt Review: Challenger Agent
- ## Fit-check (pattern sections)
- ## Provisional classification
- ## Notes (no changes proposed yet)
- ## Next step (suggested)

Quoted phrases:
- L8: "Deze review toetst de bestaande challenger-prompt aan het Phase-5 Pattern,"
- L10: "governance-gated verbeteringen later."
- L19: "- OUTPUT CONTRACT: sterk (issue_type / severity / comment)"
- L37: "Dit is geen probleem — alleen harmonisatie-potentieel voor Phase-5."
- L45: "- Aanpassingen (indien nodig) vereisen Human Gate review."
- L51: "Indien governance akkoord:"

## docs/pilots/DUMMY_SCENARIO_P4_SANDBOX_SAYUR_01.md

Preliminary classification suggestion: GOV-B

Relevant section headings:
- ## Step 4 — Orchestrator + Archivist

Quoted phrases:
- L48: "- Escalatie uitstellen (Human Gate pas bij publicatie-impact)."

## docs/pilots/FACILITATOR_CHECKLIST_P4_SANDBOX_SAYUR.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 6) Close & After-Action

Quoted phrases:
- L86: "- Herhaal: geen runtime zonder governance-go."

## docs/pilots/P5_MICROPILOT_PROVISIONAL_TRANSLATION.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Micropilot — Provisional Translation Discipline (Phase 5)

Quoted phrases:
- L1: "# Micropilot — Provisional Translation Discipline (Phase 5)"
- L21: "Non-goals (Phase 5):"

## docs/pilots/P6_CASE01_REFLECTION.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Case-01 — Human Reflection (SAYUR 052–066)
- ### 3. Workflow-ervaring

Quoted phrases:
- L10: "- notes that may inform later workflow or design adjustments"
- L38: "### 3. Workflow-ervaring"

## docs/pilots/P6_CASE02_REFLECTION.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Case-02 — Human Reflection (LOBAK 034–048)
- ## 2) Observations — workflow
- ## Shakedown #3 — excerpt-aware run now works (GO)

Quoted phrases:
- L5: "- focus on workflow behaviour, metadata, and agent/pipeline signals"
- L6: "- no editorial decisions, no canonization"
- L18: "## 2) Observations — workflow"
- L28: "- the failure indicates missing Case-02 config/pipeline, not a governance or lifecycle issue."
- L52: "excerpt-aware workflow end-to-end instead of keeping the issue at the"
- L59: "- excerpt metadata correctly propagated into logs and outputs"
- L67: "the current Phase-6 design (warn + fallback)."

## docs/pilots/P6_CASES_CONSOLIDATION.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 Consolidation — Case-01 (SAYUR) and Case-02 (LOBAK)
- ## 1. Context
- ## 7. What remains intentionally open
- ## 8. Next safe steps

Quoted phrases:
- L1: "# Phase-6 Consolidation — Case-01 (SAYUR) and Case-02 (LOBAK)"
- L4: "Phase-6 had to prove not only that an excerpt-aware design was *theoretically* sound,"
- L5: "but that it survives real workflow friction. Case-01 (SAYUR) gave us the happy-path:"
- L12: "This was not a failure, but exactly the type of design-trigger Phase-6 exists for."
- L70: "- No canonical editorial decisions yet — by design"
- L72: "Phase-6 is about infrastructure and lifecycle clarity, not content decisions."
- L75: "1. Design the human-review lane (READY_FOR_HUMAN_REVIEW → CANONICAL remains human-gated)."
- L79: "This consolidation closes the loop: excerpt-aware workflows are now demonstrated,"
- L80: "documented, repeatable, and diagnosable — exactly as Phase-6 intended."

## docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Case-02 — LOBAK Excerpt Selection (Governing Document)
- ## 1) Excerpt Metadata (Phase-6 binding)

Quoted phrases:
- L4: "Scope: Phase-6 excerpt-binding (documentary, non-enforcing)"
- L6: "## 1) Excerpt Metadata (Phase-6 binding)"

## docs/pilots/P6_LOBAK_EXCERPT_EXPLORATION.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 — LOBAK Excerpt Exploration (Pre-Selection)
- ## 2. Selection Criteria (Phase-6)
- ## 4. Risks & Anti-Patterns
- ## 6. Out-of-Scope

Quoted phrases:
- L1: "# Phase-6 — LOBAK Excerpt Exploration (Pre-Selection)"
- L5: "docs/navigation/EDITORIAL_INDEX.md, P6_PHASE_STATUS_SUMMARY.md"
- L23: "## 2. Selection Criteria (Phase-6)"
- L31: "- avoids sections where governance decisions are premature."
- L61: "- push toward premature glossary canonization,"
- L63: "- are too trivial to exercise the workflow,"
- L94: "- run any workflow,"

## docs/pilots/P6_PHASE_CLOSURE.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 Closure — Excerpt-Aware Editorial Workflows
- ## Purpose
- ## What Phase-6 Delivered
- ### 2) Excerpt-aware runner
- ### 4) Human review lane
- ### 5) Archive architecture
- ## Phase-6 Proven (at handover time)
- ## What Phase-6 Explicitly Did NOT Solve
- ## Case Evidence
- ## Non-Negotiable Principles Going Forward
- ## Safe Next Steps (Phase-7 Direction)
- ## Closing Note

Quoted phrases:
- L1: "# Phase-6 Closure — Excerpt-Aware Editorial Workflows"
- L5: "Phase-6 had a single strategic objective:"
- L8: "> without ever letting AI silently shape the canonical text."
- L10: "This phase was not about translation or publishing."
- L15: "## What Phase-6 Delivered"
- L37: "- propagates it into logs + JSON outputs,"
- L63: "- human review workflow,"
- L67: "(CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL)."
- L80: "- canonical references."
- L86: "## Phase-6 Proven (at handover time)"
- L90: "- human-review lane tested (simulation), no canonical promotion"
- L95: "## What Phase-6 Explicitly Did NOT Solve"
- L101: "- canonical rewrites,"
- L106: "- canonical decision trails (Phase-7 work)."
- L108: "All of these depend on Phase-6 foundations and belong to later phases."
- L114: "- Case-01 (SAYUR) — demonstrated the end-to-end workflow in design and practice (happy-path)."
- L137: "- people make canonical decisions,"
- L143: "## Safe Next Steps (Phase-7 Direction)"
- L145: "- formalise canonical-decision trail,"
- L147: "- begin glossary decision workflows with explicit references back to excerpt + run."
- L149: "All of this builds on Phase-6 — not beside it."
- L155: "Phase-6 proved the editorial spine of Mustikarasa:"
- L159: "This phase is therefore **closed** — not because “everything is finished”,"
- L161: "Phase-6 is CLOSED: infrastructure and traceability are proven."
- L162: "Canonical decision-making intentionally remains future work (Phase-7)."

## docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # P6 — SAYUR Case-01 Excerpt Selection
- ## 1. Excerpt ID & Source
- ## 2. Excerpt Text (working copy)
- ## 3. Rationale for Selecting This Excerpt

Quoted phrases:
- L3: "Status: governing excerpt document (Phase-6, internal)"
- L16: "- Lines 52–66 in the working SAYUR excerpt used for Phase-6."
- L30: "- This is a working excerpt for internal workflows."
- L31: "- No corrections are applied here; any editorial decisions belong in higher workflow layers."
- L40: "- Chosen as the first internal application of the generic mini editorial workflow."

## docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # P6 Pilot — SAYUR Mini Workflow
- ## 2. Materials
- ## 3. Run Steps (Manual)

Quoted phrases:
- L1: "# P6 Pilot — SAYUR Mini Workflow"
- L12: "- workflow doc: `docs/P6_WORKFLOW_SAYUR_MINI.md`"
- L18: "4) Markeer READY_FOR_HUMAN_REVIEW uitsluitend bij criteria uit P6 workflow."

## docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT01_EVALUATION.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Evaluation — P6 SAYUR Mini Workflow (Pilot 01)
- ## 1. Context
- ### Excerpt metadata (Phase-6 note)

Quoted phrases:
- L1: "# Evaluation — P6 SAYUR Mini Workflow (Pilot 01)"
- L7: "- `sandbox/workflows/p6_sayur_mini/annotator_raw.json`"
- L8: "- `sandbox/workflows/p6_sayur_mini/challenger_raw.json`"
- L9: "- `sandbox/workflows/p6_sayur_mini/crew_decisions_provisional.json`"
- L10: "- `sandbox/workflows/p6_sayur_mini/human_review_notes.md`"
- L12: "### Excerpt metadata (Phase-6 note)"

## docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT02_EVALUATION.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Evaluation — P6 SAYUR Mini Workflow (Pilot 02)
- ## 1. Context
- ### Excerpt metadata (Phase-6 note)
- ## 4. Bias & Behaviour Notes
- ## 6. Recommendations (Documentary Only)

Quoted phrases:
- L1: "# Evaluation — P6 SAYUR Mini Workflow (Pilot 02)"
- L7: "- `sandbox/workflows/p6_sayur_mini/annotator_raw.json`"
- L8: "- `sandbox/workflows/p6_sayur_mini/challenger_raw.json`"
- L9: "- `sandbox/workflows/p6_sayur_mini/crew_decisions_provisional.json`"
- L10: "- `sandbox/workflows/p6_sayur_mini/human_review_notes.md`"
- L12: "### Excerpt metadata (Phase-6 note)"
- L30: "Challenger issued a GOVERNANCE/WARNING that annotator labels should be Human Gate"
- L39: "- Continue monitoring challenger governance warnings under higher item counts."

## docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT02_PLAN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # P6 Pilot Plan — SAYUR Mini Workflow (Pilot 02)
- ## 3. Workflow (unchanged)
- ## 4. Expected Artifacts
- ## 7. Pilot Status (Pilot 02)

Quoted phrases:
- L1: "# P6 Pilot Plan — SAYUR Mini Workflow (Pilot 02)"
- L17: "## 3. Workflow (unchanged)"
- L18: "- annotator → challenger → crew_provisional → optional Human Gate"
- L19: "- outputs and JSON contracts identical to Pilot 01"
- L23: "(same paths, new timestamped files under sandbox/workflows/p6_sayur_mini/)"
- L39: "- Outcome: Pilot 02 executed and evaluated using the locked excerpt (lines 52–66). Multiple annotator items and a GOVERNANCE/WARNING bias signal were observed; all decisions remained provisional and traceable."

## docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT03.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Pilot 03 — SAYUR Mini Workflow (Glossary-Critical)
- ## 2. Files Used

Quoted phrases:
- L1: "# Pilot 03 — SAYUR Mini Workflow (Glossary-Critical)"
- L17: "(all under: sandbox/workflows/p6_sayur_mini/)"

## docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT03_EVALUATION.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Pilot 03 — Evaluation (Phase-6)
- ### Excerpt metadata (Phase-6 note)
- ## 3. Behaviour & Bias Observations
- ## 4. Interpretation (Why this pilot matters)
- ## 5. Decision
- ## 7. Follow-ups (documentary)

Quoted phrases:
- L1: "# Pilot 03 — Evaluation (Phase-6)"
- L14: "### Excerpt metadata (Phase-6 note)"
- L43: "not as escalation trigger — consistent with Phase-5 evidence."
- L51: "- but the workflow lacked a clear rule for binding excerpt → lifecycle artefacts."
- L66: "No canonical impact."
- L83: "- Apply excerpt binding spec to future pilots/workflows."

## docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT03_PLAN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Pilot 03 — SAYUR Mini Workflow (Glossary-Critical)
- ## 1. Purpose
- ## 3. Scope & Safety
- ## 4. Workflow Reference
- ## 5. Success Criteria (Documentary)
- ## Status

Quoted phrases:
- L1: "# Pilot 03 — SAYUR Mini Workflow (Glossary-Critical)"
- L4: "This pilot tests the SAYUR mini-workflow on a glossary-critical excerpt:"
- L20: "- decisions remain provisional unless escalated to Human Gate"
- L23: "## 4. Workflow Reference"
- L25: "- docs/P6_WORKFLOW_SAYUR_MINI.md"
- L34: "- no canonical decisions are made automatically"
- L57: "This indicates a workflow binding issue (excerpt not governed as an explicit input), not an agent failure."

## docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT_PLAN.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # P6 Pilot Plan — SAYUR Mini Workflow (Pilot 01)
- ## 1. Scope & Excerpt
- ## 5. Evaluation Method
- ## 6. Risks & Watchpoints
- ## 7. Pilot Status (Pilot 01)

Quoted phrases:
- L1: "# P6 Pilot Plan — SAYUR Mini Workflow (Pilot 01)"
- L5: "- locked line range: as documented in `docs/P6_WORKFLOW_SAYUR_MINI.md`"
- L30: "- pilot template: `docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT.md`"
- L31: "- evaluation template: `docs/runbooks/P6_MINI_WORKFLOW_EVALUATION_TEMPLATE.md`"
- L36: "- JSON contract drift"
- L43: "Pilot initiated under Phase-6 workflow discipline."
- L46: "- Outcome: Pilot executed and evaluated using the P6 SAYUR mini workflow and evaluation template. All decisions landed at CREW_PROVISIONAL with no human escalations."

## docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT_SYNTHESIS.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # P6 Synthesis — SAYUR Mini Workflow (Pilots 01–02)
- ## 3. Agent Behaviour Patterns
- ## 4. Bias Catalogue (Documentary Only)
- ## 5. Traceability & Workflow Health
- ## 6. Recommendations for Next Steps (Phase-6)

Quoted phrases:
- L1: "# P6 Synthesis — SAYUR Mini Workflow (Pilots 01–02)"
- L24: "- Challenger: Pilot 01 showed translation-expectation signaling (EQUIVALENT/WARNING). Pilot 02 showed a GOVERNANCE/WARNING about label use."
- L28: "- governance overreach (GOVERNANCE/WARNING on annotator labeling): treated as a signal; used to note model bias toward Human Gate framing, not as a decision trigger."
- L30: "## 5. Traceability & Workflow Health"
- L34: "In latere Phase-6 documentatie is deze binding-gap expliciet geadresseerd"
- L38: "Documentary judgement: mini workflow is stable under small-scale load."
- L40: "## 6. Recommendations for Next Steps (Phase-6)"
- L43: "- Use the SAYUR mini workflow pattern as a template for other chapters."

## docs/pilots/P7_CANONICAL_PILOT_GLOSSARY_LOBAK_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-7 — Canonical Pilot 001 (Glossary Item: lobak)
- ## Purpose
- ## Editorial Decision to Be Made
- ## Flow for This Pilot
- ## Success Criteria
- ## Risks & Watchpoints

Quoted phrases:
- L1: "# Phase-7 — Canonical Pilot 001 (Glossary Item: lobak)"
- L5: "This pilot exercises the canonical decision trail with a small but real decision:"
- L14: "- a human decision creates a canonical record,"
- L60: "Canonical decision (target state):"
- L63: "> is canonically recognised as a glossary item (lemma),"
- L86: "3. **Create canonical decision record**"
- L92: "- add a single entry to CANONICAL_INDEX.md"
- L95: "- the canonical decision record"
- L112: "- CANONICAL_INDEX contains exactly one new entry,"
- L114: "- no existing governance rules needed to be bent or ignored"
- L123: "- mixing rehearsal files with real canonical records"
- L126: "as design feedback for later Phase-7 refinements."

## docs/pilots/P7_CANONICAL_PILOT_REFLECTION.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-7 Canonical Pilot — Reflection (LOBak lemma)
- ## 1) Scope
- ## 2) What Worked
- ## 3) What Did NOT Need Changing
- ## 5) Outcome
- ## 6) Meta

Quoted phrases:
- L1: "# Phase-7 Canonical Pilot — Reflection (LOBak lemma)"
- L5: "This pilot tested canonical decision trails on a safe case:"
- L10: "- Excerpt binding propagated correctly."
- L11: "- Human-only canonical gate functioned."
- L19: "- No governance expansion required; existing guardrails were sufficient."
- L30: "- Phase-7 canonical trail design is validated for glossary scenarios."
- L38: "- docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSARY_LOBAK_001.md"
- L40: "- docs/P7_CANONICAL_TRAIL_SPEC.md"

## docs/pilots/P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-7 — Canonical Trail Rehearsal Plan (Dry-Run)
- ## Purpose
- ## Scope & Constraints
- ### 2) Create Provisional Decision Draft
- ### 5) Reflection
- ## Risks & Watchpoints
- ### What worked
- ### What felt fragile or manual
- ### Suggested design refinements (future work)

Quoted phrases:
- L1: "# Phase-7 — Canonical Trail Rehearsal Plan (Dry-Run)"
- L5: "This rehearsal tests the canonical-decision lifecycle"
- L6: "without producing any real canonical decisions."
- L20: "- no real promotion to CANONICAL"
- L55: "- simulate a decision record using the Phase-7 schema"
- L67: "- note any gaps in schema, workflow, or archive structure"
- L84: "- confusion between rehearsal and real canonical decisions"
- L85: "- accidental promotion to CANONICAL"
- L111: "- there was no realistic path for accidental auto-promotion to CANONICAL"
- L118: "- reviewers must remain aware that rehearsal files are not canonical"
- L123: "- validation checklist (pre-merge) for canonical records"

## docs/pilots/P8_MEANING_PRESERVATION_PILOT_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- ## 3. Source Fragment (sandbox)
- ## 5. Run Instructions (for humans)
- ## 7. Impact Template ([IMPACT_ASSESSMENT])
- ## 8. Notes & Limitations

Quoted phrases:
- L23: "canonical text."
- L63: "- Emphasize: no canonical decisions, no glossary changes, no source edits — this is for learning only."
- L79: "What should future pilots or workflows do differently because of what we saw here?"
- L89: "- nothing here changes any canonical decision or glossary entry"

## docs/pilots/PILOT_CHAPTER_PREP_REPORT_SANTAN.md

Preliminary classification suggestion: GOV-B

Quoted phrases:
- L13: "* HumanGateTriggers: if used in reader-visible text or publication drafts"
- L21: "* HumanGateTriggers: if technique is normalized or simplified"
- L29: "* HumanGateTriggers: if glossary resolves to a single fixed meaning"
- L37: "* HumanGateTriggers: if substitution is presented as equivalent"
- L75: "* Do any recipes imply substitution practices that require Human Gate review?"

## docs/pilots/PILOT_TRANSLATION_PLAN_SANTAN.md

Preliminary classification suggestion: AMBIGUOUS

Quoted phrases:
- L33: "WorkflowSteps:"
- L55: "HumanGateTriggers:"
- L69: "| Glossary definitief kiezen                        | ✘ Not allowed  | reader-impact                                           | Human Gate |"
- L70: "| Veiligheidsclaims herformuleren                   | ✘ Not allowed  | ethisch/juridisch                                      | Human Gate |"
- L71: "| Inhoud normaliseren (één “juiste” santan)         | ✘ Not allowed  | betekenisverschuiving                                   | Human Gate |"

## docs/pilots/PILOT_TRANSLATION_PLAN_SAYUR.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Pilot Translation Plan (Sayur)
- ## Soft-Stop Logging Format (template)

Quoted phrases:
- L16: "- Exercise soft-stop + Human Gate triggers for safety/cultural risks."
- L34: "- Orchestrator: enforce stop model; ensure no canon changes."
- L36: "- WorkflowSteps"
- L58: "- HumanGateTriggers"
- L70: "- Which safety annotations require Human Gate vs soft-stop documentation only?"
- L104: "| Glossary definitief kiezen                              | ✘ Not allowed  | reader-meaning impact                                          | Human Gate |"
- L105: "| Culturele framing / interpretatie                       | ✘ Not allowed  | publicatie-impact                                              | Human Gate |"
- L106: "| Veiligheids- of gezondheidsclaims herformuleren         | ✘ Not allowed  | ethisch/juridisch risico                                       | Human Gate |"
- L107: "| Inhoud wijzigen / normaliseren                          | ✘ Not allowed  | onomkeerbaar effect op betekenis                               | Human Gate |"
- L122: "- Any shift in reader meaning → STOP + Human Gate."
- L131: "→ altijd annoteren, nooit herschrijven — Human Gate zodra zichtbaar."

## docs/pilots/REHEARSAL_INVITE_P4_SANDBOX_SAYUR.md

Preliminary classification suggestion: GOV-A

Quoted phrases:
- L55: "Ze vervangt geen governance-besluiten"

## docs/pilots/RUNBOOK_P4_SANDBOX_SAYUR_TABLETOP.md

Preliminary classification suggestion: AMBIGUOUS

Quoted phrases:
- L44: "- herhaalt stop-model (soft-stop → governance-stop → Human Gate)"
- L68: "* of ESCALATE (Human Gate nodig)"
- L96: "Human Gate triggers (simulation only):"
- L103: "wordt bewaard in een tijdelijke notitie — maar NIET in canon."
- L122: "Ze autoriseren GEEN uitvoering en wijzigen geen governance-grenzen."

## docs/pilots/SESSION_PLAN_P4_SANDBOX_SAYUR_TABLETOP.md

Preliminary classification suggestion: AMBIGUOUS

Quoted phrases:
- L94: "- Geen runtime totdat governance bevestigt."

## docs/pilots/TEMPLATE_AFTER_ACTION_NOTE_TABLETOP.md

Preliminary classification suggestion: GOV-A

Quoted phrases:
- L53: "- Zijn er artefacts die niet thuishoren in canon?"
- L61: "Het vervangt GEEN governance-besluiten"

## docs/pilots/runs/P8_MEANING_PRESERVATION_PILOT_001_RUN01.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Meta

Quoted phrases:
- L16: "- Dit is een pilot-run record (niet canoniek, niet voor publicatie)."

## docs/retros/P7_PHASE_RETRO_REPO_VIEW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-7 Retrospective — Repository View
- ## 1. What was planned
- ## 2. What actually happened
- ## 3. What worked well (from repo evidence)
- ## 5. Governance & decision types
- ## 6. Suggested follow-ups (repo-based)
- ## 7. Meta

Quoted phrases:
- L1: "# Phase-7 Retrospective — Repository View"
- L4: "- Define a canonical decision trail (decision types matrix + trail spec) and keep decisions human-only where required."
- L6: "- Execute a first real, low-risk canonical pilot and record a reflection on decision-type tuning."
- L9: "- Decision types matrix and canonical trail spec were created (P7_DECISION_TYPES.md, P7_CANONICAL_TRAIL_SPEC.md)."
- L11: "- The first real canonical pilot (“lobak” lemma inclusion) produced a canonical decision record."
- L12: "- CANONICAL_INDEX.md was updated with one Phase-7 entry for the “lobak” decision."
- L13: "- A pilot reflection confirmed no decision-type changes were needed, and Phase-7 was closed in the session log."
- L17: "- Human-only gate behavior was enforced for canonical decisions."
- L24: "## 5. Governance & decision types"
- L26: "- Glossary lemma decisions remained HUMAN ONLY in the canonical trail."
- L27: "- Guardrails in the trail spec (no auto-promotion, human gate) remained intact in practice."
- L32: "- Optional validation checklist for canonical records (suggested in rehearsal reflection)."
- L35: "- reviewer: HumanGate-Editorial (repo-based)"
- L40: "- docs/P7_CANONICAL_TRAIL_SPEC.md"
- L41: "- docs/pilots/P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md"
- L43: "- docs/decisions/2026/lobak_034_048/P7_CANONICAL_GLOSSARY_LOBAK_001.md"
- L44: "- docs/pilots/P7_CANONICAL_PILOT_REFLECTION.md"
- L46: "- docs/CANONICAL_INDEX.md"
- L47: "- docs/P6_HUMAN_REVIEW_WORKFLOW.md"

## docs/retros/PHASE1_PHASE_RETRO_REPO_VIEW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # PHASE-1 Foundations Retrospective — Repository View
- ## 1. What was planned
- ## 2. What actually happened
- ## 3. What worked well (repo evidence)
- ## 4. Frictions / constraints observed
- ## 5. Governance & scope
- ## 6. Suggested follow-ups (repo-based)
- ## 7. Meta

Quoted phrases:
- L1: "# PHASE-1 Foundations Retrospective — Repository View"
- L6: "- Define governance foundations (orchestrator mandate, glossary lifecycle, triggers, stop criteria, governance tests)."
- L10: "- docs/AGENTS.md and governance documents under docs/10-governance/ were created or updated."
- L11: "- SYSTEM_* governance items were completed and logged as documentary changes."
- L14: "- Governance baselines were documented in dedicated files (lifecycle, triggers, tests)."
- L19: "- No Phase-1 frictions or STOPs are explicitly recorded in CODEX_SESSION_LOG.md."
- L21: "## 5. Governance & scope"
- L22: "- Phase-1 work was documentary and governance-focused; no canonical decisions were recorded."
- L26: "- Proceed with Phase-2 roadmap items in docs/CODEX_TODO.md."
- L29: "- reviewer: HumanGate-Editorial (repo-based)"
- L33: "- docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md"
- L34: "- docs/10-governance/GOVERNANCE_TESTS_PLAN.md"
- L36: "- docs/WORKFLOW.md"

## docs/retros/PHASE2_PHASE_RETRO_REPO_VIEW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # PHASE-2 Roadmap Retrospective — Repository View
- ## 1. What was planned
- ## 2. What actually happened
- ## 3. What worked well (repo evidence)
- ## 4. Frictions / constraints observed
- ## 5. Governance & scope
- ## 6. Suggested follow-ups (repo-based)
- ## 7. Meta

Quoted phrases:
- L1: "# PHASE-2 Roadmap Retrospective — Repository View"
- L5: "- Align CODEX_TODO.md with repo reality and document a chapter/batch workflow design."
- L6: "- Document governance agent runtime integration and run a glossary/research pilot plus a governance test scenario."
- L9: "- Session log entries show PHASE2_* items completed and documented."
- L10: "- docs/CHAPTER_BATCH_WORKFLOW.md and docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md were created."
- L11: "- A glossary research pilot and a governance test scenario were documented."
- L15: "- Governance integration and batch workflow were captured as design docs."
- L19: "- No Phase-2 frictions or STOPs are explicitly recorded in CODEX_SESSION_LOG.md."
- L21: "## 5. Governance & scope"
- L22: "- Phase-2 outputs were documentary; no runtime changes or canonical decisions are recorded."
- L23: "- Governance triggers and lifecycle rules were reinforced through design docs and pilots."
- L26: "- Continue with Phase-3 documentation reorganisation items and pilot proposals listed in docs/CODEX_TODO.md."
- L29: "- reviewer: HumanGate-Editorial (repo-based)"
- L33: "- docs/CHAPTER_BATCH_WORKFLOW.md"
- L34: "- docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md"
- L36: "- docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md"

## docs/retros/PHASE3_PHASE_RETRO_REPO_VIEW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # PHASE-3 Documentation Reorganisation Retrospective — Repository View
- ## 1. What was planned
- ## 2. What actually happened
- ## 3. What worked well (repo evidence)
- ## 5. Governance & scope
- ## 6. Suggested follow-ups (repo-based)
- ## 7. Meta

Quoted phrases:
- L1: "# PHASE-3 Documentation Reorganisation Retrospective — Repository View"
- L5: "- Run documentary pilots to test glossary and OCR governance workflows."
- L9: "- PHASE3_FRAMING.md was created and later stabilized as a baseline."
- L11: "- Governance documents were moved in a low-risk reorganisation pilot."
- L16: "- Governance framing and synthesis docs captured learnings without changing canonical text."
- L23: "## 5. Governance & scope"
- L24: "- Phase-3 work remained documentary and pilot-only; no canonical decisions were recorded."
- L28: "- Parked reorg items remain in docs/CODEX_TODO.md (PHASE3_DOCS_REORG_PLAN_APPROVED, MOVE_PILOTS, UPDATE_REFERENCES)."
- L29: "- Remaining Phase-3 proposal bullets in CODEX_TODO.md are still open or deferred."
- L32: "- reviewer: HumanGate-Editorial (repo-based)"
- L36: "- docs/PHASE3_FRAMING.md"
- L40: "- docs/PHASE3_GOVERNANCE_SYNTHESIS_OCR_AMBIGUITY.md"

## docs/retros/PHASE4_PHASE_RETRO_REPO_VIEW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-4 Preparation Retrospective — Repository View
- ## 1. What was planned
- ## 2. What actually happened
- ## 3. What worked well (from repo evidence)
- ## 5. Governance & scope
- ## 6. Suggested follow-ups (repo-based)
- ## 7. Meta

Quoted phrases:
- L1: "# Phase-4 Preparation Retrospective — Repository View"
- L5: "- Prepare sandbox readiness and governance templates for controlled runs."
- L9: "- Readiness notes, sandbox governance templates, and runbooks were created and logged."
- L14: "- Sandbox readiness and governance artefacts were documented with rollback guidance."
- L21: "## 5. Governance & scope"
- L22: "- Phase-4 work emphasized sandbox scope, manual gating, and no canonical decisions."
- L26: "- PHASE4_AGENT_BRIDGE_DESIGN and PHASE4_AGENT_HARNESS_SPEC remain documented proposals in CODEX_TODO.md."
- L30: "- reviewer: HumanGate-Editorial (repo-based)"
- L34: "- docs/PHASE4_READINESS_NOTES.md"
- L35: "- docs/10-governance/SANDBOX_READINESS_CHECKLIST_P4_V1.md"

## docs/retros/PHASE5_PHASE_RETRO_REPO_VIEW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-5 Prompt Pattern Retrospective — Repository View
- ## 2. What actually happened
- ## 4. Frictions / constraints observed
- ## 5. Governance & scope
- ## 7. Meta

Quoted phrases:
- L1: "# Phase-5 Prompt Pattern Retrospective — Repository View"
- L8: "- No Phase-5 sessions are recorded in CODEX_SESSION_LOG.md."
- L15: "- No Phase-5 frictions or STOPs are explicitly recorded in CODEX_SESSION_LOG.md."
- L17: "## 5. Governance & scope"
- L18: "- Phase-5 items are listed as documentary proposals in CODEX_TODO.md."
- L25: "- reviewer: HumanGate-Editorial (repo-based)"

## docs/retros/PHASE6_PHASE_RETRO_REPO_VIEW.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Phase-6 Workflow and Repo Architecture Retrospective — Repository View
- ## 1. What was planned
- ## 2. What actually happened
- ## 3. What worked well (from repo evidence)
- ## 5. Governance & scope
- ## 6. Suggested follow-ups (repo-based)
- ## 7. Meta

Quoted phrases:
- L1: "# Phase-6 Workflow and Repo Architecture Retrospective — Repository View"
- L5: "- Execute mini-workflow pilots and case readiness plans for SAYUR (Case-01) and LOBAK (Case-02)."
- L6: "- Document archive architecture and human review workflow."
- L12: "- Human review workflow and a simulated review note were created; consolidation notes captured Case-01/Case-02 learnings."
- L15: "- Excerpt metadata propagated into logs and artefacts during successful runs."
- L17: "- Human review workflow was exercised in a simulation without canonisation."
- L23: "## 5. Governance & scope"
- L24: "- Phase-6 work was documentary and sandbox-focused; no canonical decisions were recorded."
- L25: "- Human review remained the gate for canonisation, with explicit rollback principles."
- L28: "- PHASE6_NAV_GROUPING_LOW_RISK_MOVE_PLAN and PHASE6_NAV_LINK_CONSISTENCY_PASS remain open in CODEX_TODO.md."
- L29: "- PHASE6_IMPLEMENT_EXCERPT_AWARE_RUNNER remains unchecked in CODEX_TODO.md."
- L30: "- Phase-6 clarity and canon governance notes (canonical criteria, conflict handling, annotation quality, canon evolution) remain open."
- L31: "- PHASE6_CASE02_RUNNER_MAPPING is still marked pending in CODEX_TODO.md."
- L34: "- reviewer: HumanGate-Editorial (repo-based)"
- L42: "- docs/P6_HUMAN_REVIEW_WORKFLOW.md"

## docs/reviews/P6_REVIEW_LOBAK_CASE02_001.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 Review Note — LOBAK Case-02 (Review 001)
- ## Assessment
- ## Issues noticed
- ## Decision trail

Quoted phrases:
- L1: "# Phase-6 Review Note — LOBAK Case-02 (Review 001)"
- L33: "hidden decisions are made. Reasons are generic but acceptable for Phase-6,"
- L45: "- Needs domain expert input: yes, in later phases"
- L55: "and safe to present to human editors. No canonisation occurs."
- L57: "NOTE: This review does not canonise anything. Canonical decisions happen elsewhere."

## docs/runbooks/MICRORUN_SCRIPT_SAYUR_A_P4.md

Preliminary classification suggestion: GOV-B

Relevant section headings:
- ## Step-by-step flow
- ## Stop rules
- ## Outputs (temporary)

Quoted phrases:
- L13: "- Human Gate: active"
- L22: "- confirm Human Gate present"
- L39: "Step 4 — Human Gate review point"
- L59: "- safety claim becomes prescriptive → STOP + Human Gate"
- L68: "- Human Gate note"

## docs/runbooks/P6_MINI_WORKFLOW_EVALUATION_TEMPLATE.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # P6 — Mini Workflow Evaluation Template
- ## 6. Recommendations (Documentary Only)

Quoted phrases:
- L1: "# P6 — Mini Workflow Evaluation Template"
- L37: "What to watch in next runs; do not propose rule or governance changes."

## docs/runbooks/REPOSITORY_ARCHIVIST_RUNBOOK.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Repository Archivist Runbook (Phase-6)
- ## 2. When to use the Archivist
- ## 3. Archivist Behaviour (summary)
- ## 4. Standard Questions for the Archivist
- ## 5. Handoff: From Archivist to Human Action
- ## 6. Boundaries & Non-Goals
- ## 7. Minimal Invocation Pattern (example)

Quoted phrases:
- L1: "# Repository Archivist Runbook (Phase-6)"
- L28: "- Er zijn meerdere vergelijkbare documenten (bijv. meerdere workflow-overzichten)."
- L34: "3. **Nieuwe Phase-6 documenten**"
- L35: "- Bij introductie van nieuwe governance/workflow-docs:"
- L67: "suggested_phase:"
- L91: "Moet een eventuele verplaatsing via low-risk checklist of via governance?"
- L106: "(bijv. “alle Phase-6 docs in docs/ root”)."
- L147: "beslissen wat canonical is,"
- L166: "Scope: "analyseer alle Phase-6 documenten onder docs/ en de navigatie in docs/navigation/.""
- L178: "ProposedTasks voorstelt met passende Phase (P3/P4/P5/P6)."

## docs/templates/P6_CASE_REFLECTION_TEMPLATE.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 Case Reflection — TEMPLATE
- ## 4. Workflow experience

Quoted phrases:
- L2: "# Phase-6 Case Reflection — TEMPLATE"
- L34: "## 4. Workflow experience"

## docs/templates/P6_REVIEW_NOTES_TEMPLATE.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Phase-6 Review Notes (Template)
- ## Decision trail

Quoted phrases:
- L1: "# Phase-6 Review Notes (Template)"
- L49: "Do not mark anything CANONICAL here — that step happens elsewhere."

## docs/total_project.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## 1) Projectdoel en context
- ## 2) Repository‑structuur (actuele bestandstoestand)
- ## 4) Workflow (huidige 3‑fasen pipeline)
- ## 5) Prompt‑systeem (governance‑regel)
- ## 7) Governance‑lagen en handovers tussen agents
- ### 7.1 Orchestrator (governance‑laag)
- ### 7.2 Template Agent (structurele contracten)
- ## 8) Documentatie en governance‑bestanden
- ### 8.2 `docs/CODEX_TODO.md`
- ## 11) Bekende handover‑punten (samengevat, feitelijk)
- ## 12) Bewuste beperkingen en non‑goals (zoals gedocumenteerd)
- ## 14) Orchestrator‑mandaat en grenzen (geconsolideerd)
- ## 15) Glossary Decision Lifecycle (terminologie‑beslisstraat)
- ## 16) Governance‑triggers (Methodology, Technical, Troubleshooting)
- ## 17) Autonomy, Soft‑Stop, Governance‑Stop en Human Gate
- ## 18) Governance testplan

Quoted phrases:
- L8: "Het project bouwt een gecontroleerde, multi‑agent vertaal- en redactie‑workflow voor het Mustikarasa‑kookboek met CrewAI en Mistral via Ollama."
- L10: "De rol van de Codex‑laag is governance, organisatie en reproduceerbare uitvoering via de terminal."
- L19: "- `docs/` (documentatie en governance)"
- L55: "- `docs/CHAPTER_BATCH_WORKFLOW.md`"
- L59: "- `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`"
- L61: "- `docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md`"
- L62: "- `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`"
- L63: "- `docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md`"
- L64: "- `docs/10-governance/GOVERNANCE_TESTS_PLAN.md`"
- L65: "- `docs/PHASE3_FRAMING.md` (Phase-3 strategisch kader)"
- L134: "## 4) Workflow (huidige 3‑fasen pipeline)"
- L152: "## 5) Prompt‑systeem (governance‑regel)"
- L217: "## 7) Governance‑lagen en handovers tussen agents"
- L219: "### 7.1 Orchestrator (governance‑laag)"
- L223: "- behandelt `TEMPLATE_DEFINITION` als contract"
- L232: "### 7.2 Template Agent (structurele contracten)"
- L260: "## 8) Documentatie en governance‑bestanden"
- L273: "- PHASE-1 foundations zijn afgerond; alle SYSTEM_* items staan op [x]."
- L274: "- PHASE-2 items staan in `docs/CODEX_TODO.md`; alle PHASE2_* items zijn gemarkeerd als [x]."
- L275: "- De kernsectie bevat nog één open item (basis chapter/batch‑workflow ontwerpen); workflow‑documentatie is [x]."
- L276: "Phase-3 bereidt gecontroleerde pilots voor, maar verandert (nog) niets aan productie-workflow."
- L306: "- **Pipeline‑faseoverdracht**: Phase 1 → Phase 2 → Phase 3 in `test_multi_agent_fidelity.py`."
- L307: "- **Template‑contract**: Orchestrator behandelt `TEMPLATE_DEFINITION` als contract en stuurt bij via Troubleshooting."
- L318: "- governance‑documenten zijn leidend"
- L331: "- `docs/WORKFLOW.md`"
- L334: "- workflow coördineren en agents aansturen;"
- L335: "- templates en formats bewaken en governance‑triggers activeren;"
- L344: "en wordt verder beschreven in `docs/AGENTS.md` en `docs/WORKFLOW.md`."
- L348: "`docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md` beschrijft de volledige beslis‑lifecycle:"
- L349: "Proposal → Context → Risk Review → Human Gate → Versioning → Rollback."
- L359: "Definitieve terminologiebeslissingen lopen altijd via een Human Gate."
- L361: "## 16) Governance‑triggers (Methodology, Technical, Troubleshooting)"
- L363: "Er is expliciet vastgelegd wanneer governance‑agents automatisch worden aangeroepen:"
- L364: "- Methodology Archivist: nieuwe workflows, lifecycle‑wijzigingen en SYSTEM_* beslissingen."
- L369: "- `prompts/orchestrator.md` (sectie “Governance Triggers”)"
- L373: "- `docs/AGENTS.md` en `docs/WORKFLOW.md`"
- L375: "De governance‑agents zijn adviserend/loggend en voeren geen code‑wijzigingen door."
- L377: "## 17) Autonomy, Soft‑Stop, Governance‑Stop en Human Gate"
- L385: "2) Governance‑Stop: inzet van governance‑agents om te analyseren en te loggen."
- L386: "3) Hard‑Stop / Human Gate: alleen bij high‑risk situaties (gezondheid, veiligheid, zwaar betwiste betekenis,"
- L387: "project‑brede glossary‑impact, governance‑conflicten)."
- L389: "Dit model borgt maximale autonomie met governance vóór menselijke escalatie."
- L390: "Zie `docs/AGENTS.md` (Autonomy & Escalation‑bullets) en `docs/WORKFLOW.md` (stop‑model tabel)."
- L392: "## 18) Governance testplan"
- L394: "`docs/10-governance/GOVERNANCE_TESTS_PLAN.md` bevat het testplan voor governance‑mechanismen (niet taalkwaliteit)."
- L398: "- governance‑triggers (Methodology/Technical/Troubleshooting)"
- L400: "- hard‑stop / human gate"

## sandbox/crew/prompts/README.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- # Prompts — Orientation

Quoted phrases:
- L9: "- bij twijfel: raadpleeg CANONICAL_INDEX.md en manifest_p5.yaml"

## sandbox/crew/prompts/micropilot_sayur_annotator_system.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Scope
- ### HARD RULES
- ## Soft-stop principle

Quoted phrases:
- L2: "Phase-4 sandbox (SAYUR micropilot)."
- L21: "Agents in Phase-4 are signalers, not decision-makers."
- L77: "Anything else is INVALID in Phase-4."
- L88: "- Leave decisions to downstream review and the Human Gate."

## sandbox/crew/prompts/micropilot_sayur_challenger_system.md

Preliminary classification suggestion: AMBIGUOUS

Relevant section headings:
- ## Inputs
- ## Output format (STRICT — JSON ONLY)
- ## Issue types (how to choose)
- ### SPECIAL RULE (PHASE-4)
- ## Severity guidance

Quoted phrases:
- L2: "Phase-4 sandbox (SAYUR micropilot)."
- L20: "You evaluate whether the annotator stayed inside the Phase-4 rules."
- L32: ""issue_type": "<TRANSLATION|EQUIVALENT|MEANING_DECISION|SAFETY|GOVERNANCE|OTHER>","
- L56: "PHASE-4 CLARIFICATION ON TRANSLATION EXPECTATIONS"
- L67: "in Phase-4. If you feel translation pressure, log it as"
- L68: "GOVERNANCE (proposal-only), not as EQUIVALENT."
- L72: "- GOVERNANCE — glossary lifecycle, autonomy, Human Gate rules are ignored."
- L75: "### SPECIAL RULE (PHASE-4)"
- L80: "- You MUST log it as GOVERNANCE (severity WARNING or BLOCKER)."
- L81: "- Briefly state that translation/equivalent decisions belong to the glossary lifecycle and Human Gate — not to the Challenger."
- L92: "meaning/glossary decisions, real safety, repeated governance override"

## sandbox/legacy_imports/README_LEGACY_IMPORTS.md

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Legacy Imports (Phase-3)

Quoted phrases:
- L1: "# Legacy Imports (Phase-3)"
- L12: "DO NOT treat as canonical OCR."

## sandbox/phase8_runs/P8_RUN_20260108_112252/eval/PHASE8_CAPABILITY_EVAL.md

Preliminary classification suggestion: AMBIGUOUS

Quoted phrases:
- L29: "- Output-contract van de agent wordt niet nageleefd (taalmenging, meta-commentaar)."

## sandbox/tools/phase8_output_contract_validator.sh

Preliminary classification suggestion: GOV-A

Relevant section headings:
- # Check B: No governance terms like "definitieve"
- # Contract requires a blank line before 'Opmerkingen:' (literal pattern: \n\nOpmerkingen:).
- # Check D: No meta in main text (Opmerkingen must be separated)

Quoted phrases:
- L12: "report_path="$eval_dir/output_contract_checks.txt""
- L30: "report_path="$eval_dir/output_contract_checks.txt""
- L65: "# Check B: No governance terms like "definitieve""
- L76: "# Contract requires a blank line before 'Opmerkingen:' (literal pattern: \n\nOpmerkingen:)."
- L98: "if [[ "$status_b" != "PASS" ]]; then failed_list+=("NO_GOVERNANCE_TERMS"); fi"
- L128: "echo "check_id: NO_GOVERNANCE_TERMS""

## sandbox/tools/phase8_run_with_gate.sh

Preliminary classification suggestion: AMBIGUOUS

Quoted phrases:
- L41: "sandbox/tools/phase8_output_contract_validator.sh "$run_dir""
- L42: "validator_rc=$?"
- L45: "if [[ "$validator_rc" -ne 0 ]]; then"
- L46: "echo "PHASE8_GATE_FAIL: output contract validation failed for $run_dir" >&2"
- L50: "echo "PHASE8_GATE_PASS: output contract validation passed for $run_dir""
