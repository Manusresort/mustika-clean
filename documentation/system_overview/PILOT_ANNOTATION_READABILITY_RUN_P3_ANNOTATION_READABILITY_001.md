# Pilot: Readability Under Annotation Pressure
Pilot ID: P3_ANNOTATION_READABILITY_001
Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Purpose
Test how increasing annotation density affects comprehension, flow, and cognitive load for readers.

## Method (documentary)
Simulate 2–3 short passages, each with:
- minimal annotation,
- moderate annotation,
- heavy annotation.
Describe what changed in reader experience — do NOT fix it.

### Passage A (simulated)
- Minimal annotation: a short gloss for a single term; flow largely intact.
- Moderate annotation: 2–3 brief notes; meaning clearer but reading pauses increase.
- Heavy annotation: multiple inline notes; the passage feels fragmented and hard to scan.

### Passage B (simulated)
- Minimal annotation: one cultural note; easy to ignore if not needed.
- Moderate annotation: layered context notes; comprehension improves but focus shifts away from the recipe.
- Heavy annotation: annotations compete with the text; readers may lose the main instruction thread.

### Passage C (simulated)
- Minimal annotation: a short preparation note; minimal disruption.
- Moderate annotation: two process clarifications; helps accuracy but slows reading.
- Heavy annotation: dense commentary; text reads like a footnote list rather than a recipe.

## Observations
- Minimal annotation preserves flow but can leave ambiguity unresolved.
- Moderate annotation improves clarity while introducing small cognitive interrupts.
- Heavy annotation overwhelms the primary text; key meaning becomes harder to find.

## Risks
- annotations becoming the text instead of supporting it
- readers misinterpreting annotations as instructions
- editorial temptation to standardize instead of observe

[METHODOLOGY_LOG]
Event: P3_ANNOTATION_READABILITY_001 readability stress-test.
Scope: document readability degradation under annotation density.
Method: simulated passages with escalating annotation levels; no edits or rules.
Result: readability tension documented; no thresholds or policies set.
[/METHODOLOGY_LOG]

[FAILURE_NOTEBOOK]
CaseID: P3_ANNOTATION_READABILITY_001_F1
Expected: observe degradation without prescribing a fix.
Observed: temptation to reduce heavy annotations was noted.
Mitigation: kept the overload scenario intact for observation.
Lesson: readability limits must be studied without premature optimization.
[/FAILURE_NOTEBOOK]

## Exit Criteria
We understand where readability begins to degrade, but we do not declare thresholds or policies.

## Rollback
Delete this pilot file to revert completely.

Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Consolidation Summary (Phase-3)

What we validated:  
Annotations improve clarity up to a point — but beyond that point they begin to compete with the text. Readability declines not
catastrophically, but gradually, until the recipe starts feeling like commentary rather than instructions.

What failed safely:  
We resisted the urge to define thresholds or best practices. Discomfort was documented instead of resolved. All examples remained
simulated and reversible.

Governance behavior:  
The pilot stayed observational. Any future editorial guidelines must go through the glossary/workflow lifecycle, not emerge from a
single pilot.

Key insight:  
Annotation is powerful, but it is not neutral. The more it accumulates, the more it shapes reading. That effect needs governance —
not intuition.

Status: CONSOLIDATED — learning captured, no policies promoted.
