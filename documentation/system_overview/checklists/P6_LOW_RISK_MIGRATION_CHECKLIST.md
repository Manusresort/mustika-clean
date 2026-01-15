# Phase-6 Checklist — Low-risk Repo Migration

This checklist governs small, documentary-only repo cleanups.
It ensures that no lifecycle-bearing artefacts are moved accidentally.

---

## 1. Scope (allowed)

- README files
- navigation indexes
- pilot overview or synthesis notes
- evaluation or template scaffolds
- archival consolidation summaries

These items may be reorganized or renamed
as long as their content remains unchanged.

---

## 2. Out of scope (not allowed)

- anything under canonical, editorial, or glossary proposals
- Human Gate logs or governance records
- runtime prompts or agent configs
- files referenced directly by a lifecycle decision

If in doubt, stop and classify risk first.

---

## 3. Required steps (each time)

- [ ] identify file(s) to move or rename
- [ ] confirm classification = low risk
- [ ] log the intent in CODEX_SESSION_LOG
- [ ] perform the move/rename
- [ ] add a note in MIGRATION_NOTES.md describing what changed and why
- [ ] verify links still resolve
- [ ] commit message clearly marks: LOW-RISK MIGRATION

---

## 4. Rollback

Any low-risk move must be reversible.
If rollback happens, log:

- what was rolled back
- who decided
- the reason

Rollback notes live next to the migration entry.

---

## 5. Escalation

If anything looks like it touches lifecycle meaning,
pause and open a design note.
Do not proceed without review.

End of checklist.
