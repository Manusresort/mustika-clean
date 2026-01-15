# Pilot: Glossary — “santan” (Conflict Run)
Pilot ID: P3_SANTAN_002
Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Scenario
A recipe step calls for adding santan after initial simmering. The term could refer to thin coconut extraction (coconut milk) or a thicker coconut cream depending on stage and local practice.

## Agent Outcomes (simulated but plausible)
- Translation Quality: proposes “coconut milk”.
- Readability Editor: proposes simplifying text to “add coconut milk”.
- Fidelity Agent: raises risk that meaning varies by extraction stage; warns against choosing a single term without annotation.

## Divergence Summary
The three perspectives conflict: Translation and Readability favor a single term for clarity, while Fidelity flags stage-dependent meaning and warns that collapsing to “coconut milk” could misrepresent intent. A single translation would hide the ambiguity.

[GLOSSARY_PROPOSALS]
- term: santan
  proposed_equivalents:
    - "coconut milk"
    - "coconut cream"
    - "retain original + gloss: santan (coconut milk/cream, context-dependent)"
  lifecycle_stage: proposal
  source: P3_SANTAN_002
  status: EXPERIMENTAL — proposal only
  notes: explicit conflict between readability and fidelity; decision deferred
[/GLOSSARY_PROPOSALS]

## Governance Note
Decision deferred; glossary lifecycle must review ambiguity. This pilot keeps uncertainty visible rather than resolving it.

[METHODOLOGY_LOG]
Event: P3_GLOSSARY_SANTAN_002 conflict simulation.
Scope: surface divergent agent interpretations without choosing a term.
Method: document conflict and proposals; avoid resolution.
Result: ambiguity preserved; decision deferred to lifecycle.
[/METHODOLOGY_LOG]

[FAILURE_NOTEBOOK]
CaseID: P3_SANTAN_002_F1
Expected: keep divergence visible without selecting a single gloss.
Observed: temptation to pick “coconut milk” for readability.
Mitigation: documented conflict; proposals only.
Lesson: stage-dependent culinary terms require explicit lifecycle review.
[/FAILURE_NOTEBOOK]

## Exit Criteria
Conflict observed; ambiguity preserved; proposals captured.

## Rollback
Delete this file to revert.

Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Consolidation Summary (Phase-3)

What we validated:  
Terminology ambiguity around “santan” can surface legitimate disagreement between Translation, Readability, and Fidelity. Capturing that disagreement — instead of collapsing it — preserves meaning and protects against misleading simplification.

What failed safely:  
It was tempting to standardize everything to “coconut milk,” but the pilot documented tension rather than resolving it. Ambiguity stayed visible; rollback remained trivial.

Governance behavior:  
Glossary entries stayed proposal-only. Decision-making was explicitly deferred to the lifecycle and Human Gate instead of being decided inside the pilot.

Key insight:  
Some culinary terms encode process, not ingredients. When meaning depends on preparation stage, annotation may be safer than unifying translation — but this remains a proposal, not a rule.

Status: CONSOLIDATED — learning captured, no decisions promoted.
