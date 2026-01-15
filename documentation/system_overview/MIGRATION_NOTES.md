# Repo Migration Notes (Phase-6)

This file records every migration action taken during Phase-6
and links it to checklist steps, justification, and rollback notes.

Entries are chronological. Nothing here authorizes a migration —
it only records what happened once approved and executed.

---

### MIGRATION — Navigation Move 01
Date: 2026-01-05
Scope: LOW-RISK
Action: Moved PILOT_LOG_OVERVIEW.md to docs/navigation/
Reason: Improves navigation clarity; document is index-only, no lifecycle meaning.
Rollback: move file back to original location; note rollback here if performed.

### MIGRATION — Workflow Rename (Generic Alignment)
Scope: LOW-RISK (documentary)
Action: renamed generic workflow file and updated references.
Rollback: restore file name + revert updated references.

DATE: 2026-01-05
ACTION: Moved DOCS_INFORMATION_ARCHITECTURE.md to docs/navigation/
TYPE: LOW-RISK (navigation / documentation)
ROLLBACK: Move file back to repo root and restore any adjusted links.

DATE: 2026-01-05
ACTION: Moved P6_MIGRATION_CANDIDATE_LIST.md to docs/navigation/
TYPE: LOW-RISK (navigation / overview)
ROLLBACK: Move the file back to docs/ and restore any adjusted links.
