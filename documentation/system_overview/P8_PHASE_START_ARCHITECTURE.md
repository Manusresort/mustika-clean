# Phase-8 Architecture & Start — Agentic Work Within Canonical Rails

## 1. Context and Inheritance

Phase-7 established canonical decision trails with a human-only canonical gate,
rollback-by-superseding, and strict separation between provisional agent output
and canonical decisions. Phase-8 inherits these guardrails and MUST NOT change them.

- Phase-7 outcome: canonical trail proven on a low-risk glossary case (“lobak” lemma).
- Agents are provisional; all canonical decisions are human-only.
- Rollback uses new decision records; no overwrites of artefacts.

## 2. Phase-8 Goals (What Phase-8 WILL do)

- Reduce unnecessary human workload by improving agent support, NOT by granting agents more authority.
- Improve agent handling of ambiguity and escalation (better [AUTO-OK] vs [AMBIGUOUS] vs [ESCALATE-HUMAN]).
- Improve batch-preparation for human review (clustering, context-bundling, risk tagging).
- Introduce light-weight validators and checkers that run before the human gate (e.g. excerpt-binding, trail completeness).
- Keep all AI output strictly provisional, clearly separated from canonical decisions.

## 3. Non-Goals (What Phase-8 Will NOT Do)

- No new governance layers or decision types that weaken Phase-7 guardrails.
- No auto-promotion to CANONICAL, no automated creation of canonical decision records.
- No agent-driven glossary meaning or interpretation decisions.
- No human rationale auto-generation that pretends to be human-authored.

## 4. Agentic Capabilities in Phase-8

### 4.1 Agent Roles (examples)

- Ambiguity-Detector:
  - Flags where decisions might touch meaning/interpretation.
  - Suggests [AMBIGUOUS] / [ESCALATE-HUMAN] markers, but never decides.
- Context-Bundler:
  - Collects relevant excerpt snippets, line numbers, and variant readings.
  - Produces compact dossiers for human reviewers.
- Escalation-Triage:
  - Distinguishes low-risk technical issues (typographic/OCR) from high-impact semantic issues.
  - Proposes which items can be batch-processed vs escalated.
- Record-Preflight Checker:
  - Validates whether a canonical decision record is mechanically complete
    (excerpt binding, artefact links, rationale present) BEFORE human promotion.

### 4.2 Agent Constraints

- Agents may annotate, cluster, summarize, and flag risks.
- Agents may NOT:
  - create or update canonical decision records,
  - modify canonical indices,
  - set lifecycle to CANONICAL.

## 5. Orchestration Patterns (Agentic Workflows)

- annotator → challenger → reconciler (all provisional):
  - annotator labels spans and issues.
  - challenger critiques or complements annotator output.
  - reconciler produces a “provisional dossier” for the human, not a decision.
- detector → summarizer → reviewer-assistant:
  - detector finds potential issues.
  - summarizer condenses context.
  - reviewer-assistant organizes items into reviewable batches.

All flows end in READY_FOR_HUMAN_REVIEW, never in CANONICAL.
Human review sessions are the only place where canonical decisions are made.

## 6. Human Workload & Interaction Model

Humans should spend more time on:

- interpreting meaning,
- making canonical decisions,
- writing rationales.

Humans should spend less time on:

- searching for context,
- manually checking trail completeness,
- triaging obviously low-risk items.

Phase-8 features (better agents + validators) should support this without
changing authority or responsibility.

## 7. Risks and Mitigations

- Risk: over-reliance on agents (humans read less carefully).
  - Mitigation: keep human checklists and explicit review prompts.
- Risk: agent over-escalation ([ESCALATE-HUMAN] spam).
  - Mitigation: tune prompts and evaluation to minimize false positives.
- Risk: document drift between agents, trail spec, and decision records.
  - Mitigation: add preflight validators and ensure trails are single source of truth.

## 8. Phase-8 Deliverables (Architecture-Level)

- P8_AGENT_ROLES_AND_PROMPTS.md — description of agent roles + core prompts.
- P8_ORCHESTRATION_PATTERNS.md — diagrams/text for safe multi-agent flows.
- P8_VALIDATION_CHECKLISTS.md — human + tool-based validation steps.
- P8_PILOTS_PLAN.md — plan for a small set of Phase-8 pilots (e.g. OCR/typographic, structural, glossary support).

## 9. Alignment with Existing Guardrails

Phase-8 respects:

- P5_DECISION_LIFECYCLE,
- Phase-6 infrastructure (excerpt-binding, runner),
- Phase-7 canonical trail spec and decision types.

Key guarantee:

- All AI/agent output is provisional.
- Human gate is the only path to CANONICAL.

---

- author: HumanGate-Editorial + Architecture/Agentic-Design
- date: 2026-01-07
- references:
  - docs/P7_DECISION_TYPES.md
  - docs/P7_CANONICAL_TRAIL_SPEC.md
  - docs/retros/P7_PHASE_RETRO_REPO_VIEW.md
