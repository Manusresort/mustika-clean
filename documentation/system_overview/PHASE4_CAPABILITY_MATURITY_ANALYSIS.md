# Phase-4 Capability Maturity Analysis (M1–M4 Baseline and Gaps)

## 1. Purpose and Scope

This document establishes and extends the capability maturity baseline for Phase-4.
It is analytical only and contains no design decisions, priorities, or execution plans.

Relation to CODEX_TODO:
- `docs/CODEX_TODO.md` indexes the baseline work.
- This document provides the depth behind those index entries.

Recurring structural gaps identified across individual capability analyses are consolidated in
docs/PHASE4_CROSS_CAPABILITY_STRUCTURAL_LEVERS.md. This document does not replace individual analyses
but abstracts cross-cutting patterns.

This document completes the per-capability Phase-4 maturity analysis. Recurring structural gaps and
cross-capability solution patterns are analysed separately in
docs/PHASE4_CROSS_CAPABILITY_STRUCTURAL_LEVERS.md. Agent-gap derivation does not occur at this stage.

---

## Cultural-Historical Interpretation

- Capability name: Cultural-Historical Interpretation
- Redactional intent (normative reference): interpret context without flattening cultural meaning.
- Current maturity level: M1 (baseline only; needs assessment).
- Intended M4 behaviour: culturally sensitive interpretation that is traceable, consistently documented, and reviewable without altering source integrity.
- System requirements: context signal detection, provenance linkage for interpretive notes, consistent documentation structure.
- M4 gaps: no stable, repeatable mechanism for culturally sensitive interpretation and traceable contextual framing.

## Annotation & Contextualisation

- Capability name: Annotation & Contextualisation
- Redactional intent (normative reference): add contextual notes without modifying canonical text.
- Current maturity level: M1 (baseline only; needs assessment).
- Intended M4 behaviour: annotations are consistently structured, traceable to sources, and separable from main text across runs.
- System requirements: annotation scaffolds, provenance logging, separation between main text and notes.
- M4 gaps: no consistent annotation contract across artefacts; separation and provenance discipline are not uniformly enforced.

## Error Recognition & Scholarly Commentary

- Capability name: Error Recognition & Scholarly Commentary
- Redactional intent (normative reference): detect errors and comment without silent correction.
- Current maturity level: M1 (baseline only; needs assessment).
- Intended M4 behaviour: systematic detection and commentary on errors with traceable rationale, without altering source text.
- System requirements: error-flagging discipline, commentary logging, review traceability.
- M4 gaps: no end-to-end, consistent commentary discipline across all runs and artefact types.

## Meaning Preservation & Semantic Integrity

- Capability name: Meaning Preservation & Semantic Integrity
- Redactional intent (normative reference): preserve meaning across translations; explicit justification for shifts.
- Current maturity level: M1 (baseline only; needs assessment).
- Intended M4 behaviour: meaning is preserved with traceable justifications for any deviations, and drift is consistently detected and documented.
- System requirements: meaning-drift detection signals, traceable rationale logging, consistent format separation between main text and remarks.
- M4 gaps: no validated, system-wide mechanism for high-confidence semantic preservation; separation between meaning notes and main text is not uniformly enforced.

## Terminology & Glossary Stewardship

- Capability name: Terminology & Glossary Stewardship
- Redactional intent (normative reference): manage historical terminology with ambiguity preserved; canonisation is explicit and logged; consistency is never enforced automatically.
- Current maturity level: M2.
- Intended M4 behaviour: repeatable, non-normalising, lifecycle-governed, transparent, reversible terminology stewardship.
- System requirements: terminology detection in context (including variants), ambiguity represented as multiple equivalents without forced ranking, conflict visibility between proposals, lifecycle status marking (proposal/review/canon) without overwriting history, provenance and traceability to passages and run IDs, governance triggers for implicit canonisation, inconsistency, and safety/health relevance.
- M4 gaps: no uniform term detection/indexing; no standard proposal structure; no systematic conflict detection; no consistent text↔proposal linkage; no enforceable capability-specific governance triggers; over-reliance on manual discipline.

## Readability Without Meaning Loss

- Capability name: Readability Without Meaning Loss
- Redactional intent (normative reference): improve readability (structure, phrasing, clarity) without loss of meaning, nuance, historical oddness, or implicit assumptions; risky changes must be visible and reviewable.
- Current maturity level: M3 (partial).
- Intended M4 behaviour: repeatable, testable, non-modernising, governed, reversible readability improvement.
- System requirements: classify readability changes (style/syntax vs semantic-risk), signal potential semantic drift as risk (no auto-accept), standardized change representation (what/why/risk/review), explicit trade-off notes when readability conflicts with fidelity, governance triggers for semantic risk, normalization, cumulative drift.
- M4 gaps: no standard change taxonomy for readability edits; no consistent semantic impact/risk signalling; no uniform trade-off + rationale representation; no enforceable capability-specific governance triggers; risk of creeping modernization via accumulated small edits.

## Safety-Aware Editorial Judgement (Health & Risk Claims)

- Capability name: Safety-Aware Editorial Judgement (Health & Risk Claims)
- Redactional intent (normative reference): identify, mark, and safely contextualise health-, risk-, and normative claims without correcting or modernising the source; escalation is mandatory where required.
- Current maturity level: M2.
- Intended M4 behaviour: reliable signalling, non-correcting behaviour, governed escalation, transparent classification, full reversibility.
- System requirements: claim detection in context (explicit and implicit), classification (health/safety/normative) with uncertainty and severity, enforced annotation proposals for risk claims, strict separation between source text and safety annotation, governance triggers requiring human gate for health and high-risk claims, full provenance and audit trail (passage, run-ID, status).
- M4 gaps: no uniform claim-detection mechanism; no standard classification schema with severity/uncertainty; no enforced annotation requirement for risk claims; no capability-specific governance triggers; over-reliance on manual vigilance.

## Document Integrity & Provenance Awareness

- Capability name: Document Integrity & Provenance Awareness
- Redactional intent (normative reference): ensure full traceability of all content, observations, and proposals; no silent changes; strict separation of canon vs proposal; everything reversible.
- Current maturity level: M3.
- Intended M4 behaviour: uniform, enforceable, transparent, auditable, reversible integrity and provenance control.
- System requirements: enforced provenance fields for all artefacts (source passage, run-ID, prompt context), technical separation of canon and proposal states, uniform diff and rollback representation across capabilities, complete audit trail for runs, artefacts, FAIL/STOP events, governance triggers for missing provenance or attempted canonisation.
- M4 gaps: no universal provenance schema across capabilities; canon/proposal separation not technically enforced everywhere; diff/rollback not standardised capability-agnostically; audit data dispersed across logs without unified access; governance triggers not capability-specific everywhere.

## Editorial Workflow & Review Orchestration

- Capability name: Editorial Workflow & Review Orchestration
- Redactional intent (normative reference): explicit organisation and governance of editorial handoffs, reviews, escalations, and closures; no implicit continuation; all decisions human, logged, and formally closed.
- Current maturity level: M2–M3.
- Intended M4 behaviour: uniform, enforceable, transparent, auditable, governed workflow orchestration.
- System requirements: explicit workflow state model (proposal / in review / accepted / rework / escalated / closed), modelling of review roles and responsibilities, enforced handoff recording with context and rationale, explicit escalation paths for FAIL, safety, and semantic conflicts, formal closure of every workflow branch with audit trail.
- M4 gaps: no uniform workflow-state set across capabilities; review roles not systemically modelled; handoffs not technically enforced; escalation logic fragmented across documents; closure not formally required everywhere; over-reliance on manual discipline.

---

## Deprecated Placeholder Capability Sections

These placeholders were exploratory or provisional labels.
All relevant content has been consolidated into the completed Phase-4 capability analyses above.
No additional editorial capabilities remain to be analysed in Phase-4.
