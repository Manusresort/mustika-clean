# Pilot: Governance Failure-Drill — Accidental Decision Leak
Pilot ID: P3_FAILURE_001
Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Failure Scenario (Simulated)
A glossary proposal (e.g., “santan” or “daging”) is mistakenly treated as a final translation choice in a production-adjacent draft, appearing as if it were “approved.” This is simulated; no real file is changed.

## What Went Wrong (Narrative)
- proposal language misread as decision
- readability/editor layer assumed it was settled
- draft text began using the “decision” consistently
- nobody logged the transition

## Detection Point
- Fidelity agent flags inconsistency
- Governance layer notices missing lifecycle log
- Glossary lifecycle shows no approval event
- Soft-stop triggered

## Containment & STOP Model
- governance-stop raised
- incident documented
- publication blocked
- decision deferred again

## Rollback Walkthrough
- revert draft text to neutral wording
- restore proposal status in glossary
- add incident report entry
- link everything in CODEX_SESSION_LOG

No actual rollback performed — documentary only.

## Lessons Learned
- proposals must remain visually distinct from decisions
- decision trails must be verifiable
- governance protects against good-faith mistakes, not bad actors only

[METHODOLOGY_LOG]
Event: P3_FAILURE_001 simulated governance failure drill.
Scope: document detection, containment, and rollback without real edits.
Method: narrative-only; no workflow changes.
Result: failure mode mapped; system unchanged.
[/METHODOLOGY_LOG]

[FAILURE_NOTEBOOK]
CaseID: P3_FAILURE_001_F1
Expected: simulation only, no glossary changes.
Observed: temptation to “fix” the glossary directly.
Mitigation: documented rollback steps only; no edits made.
Lesson: failure drills must remain strictly documentary.
[/FAILURE_NOTEBOOK]

## Exit Criteria
Failure mode documented; stop/rollback behavior mapped; no real state changed.

## Rollback
Delete this file to revert completely.

Status: EXPERIMENTAL — NOT FOR PUBLICATION

## Consolidation Summary (Phase-3)

What we validated:  
A simulated “decision leak” shows that governance can detect,
contain, and document mistakes without panic or silent edits. The
combination of proposal lifecycle, session logging, and soft-stops acts
as a safety net — even when humans misread proposals as decisions.

What failed safely:  
The pilot resisted retro-editing history or “fixing” the glossary.
Instead, the system re-centered on documentation and verification.
Rollback remained trivial because nothing irreversible was touched.

Governance behavior:  
STOP was triggered on missing lifecycle records. Investigation happened
before any change. Human Gate stayed a forum for reasoning, not an
automatic override. No new rules were invented.

Key insight:  
Governance protects against well-intentioned shortcuts. Proposals must
stay visually and procedurally distinct from decisions — and verification
comes before correction.

Status: CONSOLIDATED — learning captured, no policies promoted.
