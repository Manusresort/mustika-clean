# Pilot: Workflow Map — Ambiguity & Governance (Phase-3)
Pilot ID: P3_WORKFLOWMAP_001
Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Purpose
Provide a visual explanation of how ambiguity moves through the system, based solely on what pilots have demonstrated — not what we think the system “should” do.

## Scope
Descriptive only. The map does not define policy or architecture.

## Diagram (documentary)

```
[Translation]
   |  (ambiguous term spotted, workable meaning chosen)
   v
[Readability]
   |  (clarity push; risk of simplification)
   v
[Fidelity]
   |  (ambiguity surfaced, risk flagged)
   v
[Glossary Proposals]
   |  (proposal-only entries logged)
   v
[Governance Layer]
   |  (soft-stop, logs, notebooks)
   v
[Human Gate]
   |  (reasoned review only when risk is high)
   v
[Decision Deferred]
```

## Annotations (documentary)
- Ambiguity often increases between Translation and Readability (clarity pressure can hide uncertainty).
- Ambiguity is documented at Fidelity and in Glossary Proposals (proposal-only logging).
- Decisions are explicitly deferred at Glossary Proposals and after Governance Layer review.
- Rollback remains trivial throughout because outputs stay documentary and proposals are reversible.

## Notes from Pilots (observed)
- Lobak: ambiguity surfaced at Fidelity and logged as glossary proposals.
- Santan: translation/readability tension documented; proposals deferred.
- Daging: cultural ambiguity escalated to Human Gate consideration without decisions.
- OCR/“²”: ambiguity flagged and logged; no normalization applied.
- Annotation pilots: readability pressure documented; no policy created.

## Risks (documentary)
- The map is dangerous if treated as a rule book.
- The map is dangerous if used to skip governance steps.
- The map is dangerous if used to justify default decisions.

## [METHODOLOGY_LOG]
Event: P3_WORKFLOWMAP_001 documentary diagram.
Scope: record pilot-observed behavior without proposing improvements.
Method: ASCII map + annotations derived from pilots; no prescriptions.
Result: descriptive map only; no policies introduced.
[/METHODOLOGY_LOG]

## [FAILURE_NOTEBOOK]
CaseID: P3_WORKFLOWMAP_001_F1
Expected: descriptive map only.
Observed: temptation to add new arrows and decision points.
Mitigation: kept flow unchanged and limited to observed behavior.
Lesson: even small diagram tweaks can imply policy outside Phase-3 scope.
[/FAILURE_NOTEBOOK]

## Exit Criteria
Map exists, improves understanding, makes ambiguity lifecycle visible, and changes nothing operational.

## Rollback
Delete this file to revert.

Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Consolidation Summary (Phase-3)

What we validated:  
A simple diagram helps people see how ambiguity flows through Translation → Readability → Fidelity → Glossary proposals →
Governance → (rare) Human Gate. The map improved shared understanding without changing behavior. Documentation remains the primary
safety mechanism.

What failed safely:  
The pilot resisted the urge to “optimize” the arrows or add decision points. Any structural ideas stayed out of scope. The artifact is
descriptive only; rollback remains trivial.

Governance behavior:  
The map was treated as an educational aid, not a rule book. It reinforces existing stops and lifecycles but does not define them.

Key insight:  
Visual clarity can reduce accidental shortcuts — but diagrams become risky the moment they are mistaken for policy.

Status: CONSOLIDATED — learning captured, no rules promoted.
