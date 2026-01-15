# Pilot: Glossary — “daging” (Conflict Run)
Pilot ID: P3_DAGING_002
Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Scenario
A recipe lists “daging” among ingredients without specifying species. In some contexts this could mean meat in general, while in others it may implicitly mean beef. A wrong assumption could shift cultural and dietary interpretation.

## Agent Outcomes (simulated, plausible)
- Translation Quality: prefers “meat” as a general, simple mapping.
- Readability Editor: favors “meat” to avoid confusing explanations.
- Fidelity Agent: warns meaning may imply beef and flags risk of oversimplification.
- Cultural/Historical Editor: argues context (halal norms, regional usage, time period) matters and opposes choosing one English default.

## Divergence Summary
The agents disagree on whether to simplify for clarity or preserve cultural nuance. Collapsing to one translation would hide ambiguity that matters for historical and religious context.

[GLOSSARY_PROPOSALS]
- term: daging
  proposed_equivalents:
    - "meat"
    - "beef (context-dependent)"
    - "retain original + gloss: daging (meat; often beef depending on context)"
  lifecycle_stage: proposal
  risk_classification: CULTURAL_TERMINOLOGY_RISK
  source: P3_DAGING_002
  status: EXPERIMENTAL — proposal only
  notes: explicit conflict between simplicity and cultural fidelity; decision deferred
[/GLOSSARY_PROPOSALS]

## Governance Note
Decision deferred; Human Gate would be considered only if publication risk emerges.

[METHODOLOGY_LOG]
Event: P3_GLOSSARY_DAGING_002 conflict simulation.
Scope: surface divergent interpretations without choosing a default.
Method: document disagreement; keep proposals only.
Result: ambiguity preserved; decision deferred to lifecycle.
[/METHODOLOGY_LOG]

[FAILURE_NOTEBOOK]
CaseID: P3_DAGING_002_F1
Expected: keep conflict visible and avoid choosing a single gloss.
Observed: temptation to standardize to “meat” for readability.
Mitigation: documented as proposal-only; decision deferred.
Lesson: cultural terms require explicit review gates.
[/FAILURE_NOTEBOOK]

## Exit Criteria
Conflict documented; ambiguity preserved; lifecycle respected.

## Rollback
Delete this file to revert.

Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Consolidation Summary (Phase-3)

What we validated:  
Cultural terminology can generate legitimate tension between clarity and fidelity. “Daging” shows how a term may look generic in
English while carrying culturally specific expectations in context.

What failed safely:  
The pilot avoided choosing a default translation. Simplification pressure was documented rather than acted on. Ambiguity remained
visible; rollback remained trivial.

Governance behavior:  
Glossary entries stayed proposal-only. Interpretation was deferred to the glossary lifecycle and, if needed, Human Gate — not decided
inside the pilot.

Key insight:  
Language encodes social context. When meanings shift with culture or religion, the system must prefer documentation and review over
assumption.

Status: CONSOLIDATED — learning captured, no decisions promoted.
