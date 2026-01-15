[ROLLBACK_TESTPLAN_P4_SANDBOX]

Title: Rollback Test Plan — Sandbox Microruns

Status:
SAFETY PROCEDURE — NOT AN APPROVAL

Purpose:
Bewijzen dat elke microrun volledig omkeerbaar is.

When:
Mandatory during first sandbox microrun (RUN-P4-SAYUR-A-0001)

---

## Test steps (table-top rehearsal first)

1) Identify all artefacts created during run
   (annotations, logs, temporary files)

2) Create TEMP snapshot list

3) Execute rollback:
   - delete pilot artefacts
   - revert session log entry
   - confirm no residual files remain

4) Validate:
   - repo matches pre-run state
   - logs clearly reflect rollback

5) Record test result (PASS / FAIL)
   in AFTER-ACTION NOTE.

If FAIL:
- STOP any further runs
- open incident
- fix governance/process before retry.

Reminder:
Rollback test prevents silent accumulation of state.
This test does not authorize any run.

### Rehearsal: RUN-P4-SAYUR-A-0001 (Sandbox)

Scope:
- Annotation-only shakedown (CrewAI + Mistral), sandbox.
- No persistent edits to source or canonical docs.

Rollback objective:
- Bevestigen dat alle artefacten herleidbaar en verwijderbaar zijn zonder verlies van brondata.

Rollback steps (table-top):
1. Identify run artefacts:
   - session entry in `docs/CODEX_SESSION_LOG.md`
   - log files in `sandbox/crew/run_logs/`
2. Confirm that source files under `data/source_imports/` are unchanged.
3. Simulate rollback (DO NOT EXECUTE):
   - mark the session entry as `rolled_back:true` (metadata only)
   - move/delete run logs (sandbox only) IF governance approves.
4. Verify state:
   - project can be re-run from scratch
   - excerpt + locked evidence remain identical.
5. Record the rehearsal result below.

Result:
- PASS (documentary rehearsal)
- No state needed to be changed.
- Rollback is reversible, traceable, low-risk in sandbox scope.

Notes:
- Any real rollback requires Human Gate confirmation.

[/ROLLBACK_TESTPLAN_P4_SANDBOX]
