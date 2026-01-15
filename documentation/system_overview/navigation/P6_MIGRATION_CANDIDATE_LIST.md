# Phase-6 — Migration Candidate List (Assessment Only)

This file identifies potential repo elements that might be moved,
reorganized, or renamed during future cleanup,
and classifies them by migration risk.

It does not authorize any moves.

---

## 1. Low-risk (documentary only)

- pilot navigation indexes
- README overview files
- pilot/evaluation templates
- synthesis and analysis notes
- archival consolidation reports (unaltered)

Reason:
These files explain or summarize;
moving them does not affect lifecycle states or editorial meaning.

---

## 2. Medium-risk (contains indirect workflow meaning)

- agent prompt pattern documentation
- lifecycle explanation docs
- guardrail policy descriptions
- meta-workflow notes

Risk:
Moving these may confuse references or version history,
so moves should be logged and reviewed.

---

## 3. High-risk (lifecycle-bearing artefacts)

- glossary drafts and proposals
- editorial decision files
- canonical text or commentary
- any file referenced by Human Gate logs
- runtime prompt files for active agents

Rule:
Do not move without explicit approval and rollback plan.

---

## 4. Next step (documentary only)

1) Cross-check this list against P6_REPO_ARCHITECTURE_MIGRATION_PLAN.md  
2) Mark specific directories for Phase A (mapping only)  
3) Defer real movement to a later, authorized cleanup task

End of list.
