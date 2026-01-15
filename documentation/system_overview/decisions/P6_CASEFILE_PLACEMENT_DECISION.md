# Phase-6 Decision — Placement of Case Files (SAYUR / LOBAK)

Status: DECIDED (documentary)  
Applies to: P6_SAYUR_INTERNAL_WORK_CASE01.md, P6_LOBAK_INTERNAL_WORK_CASE02.md  
Related: PHASE6_NAV_GROUPING_CANDIDATES.md, docs/navigation/EDITORIAL_INDEX.md, P6_REPO_ARCHITECTURE_MIGRATION_PLAN.md

---

## 1. What counts as a “case file”

In Phase-6, a **case file** is a concrete application of a generic workflow
to a specific excerpt/chapter. It usually contains:

- excerpt metadata and binding intent,
- workflow paths and artefact locations,
- constraints (what must NOT be done),
- references to logs, pilots, or eventual reviews.

Case files are *workflow-bearing* — they describe what actually happened
(or will happen) for one specific case.

---

## 2. Decision (summary)

> **Case files remain in `docs/` (editorial/workflow zone), not in `docs/navigation/`.**

Rationale:

1. **Traceability**
   Case files bind excerpts, logs, and artefacts together. Moving them
   increases risk of broken traces and mis-aligned logs.

2. **Workflow role**
   They are part of “how this case was handled”, not part of generic
   navigation or orientation.

3. **Comparability**
   Future cases should live alongside them so they can be compared consistently.

This document *does not* prohibit future redesign — it just records
that the default is: **case files stay where they are.**

---

## 3. Conditions for revisiting this decision

Revisit only if ALL of the following are true:

- there is a dedicated `docs/cases/` zone defined in the migration plan,
- excerpt-binding is consistently enforced in runtime + logs,
- a rollback plan exists for every affected case file,
- Human Gate approves the re-placement (because traces may be affected).

Until then: **no structural moves for case files.**

---

## 4. Editorial Index & Navigation

- docs/navigation/EDITORIAL_INDEX.md should list case files under “workflow/case”.
- Navigation docs may link *to* case files,
  but must not attempt to reorganize them.

---

## 5. Notes

This decision does not grant new governance authority.
It records the current, safest default for Phase-6.

If later revised, a follow-up decision document must reference this one
and explain the change.

End of document.
