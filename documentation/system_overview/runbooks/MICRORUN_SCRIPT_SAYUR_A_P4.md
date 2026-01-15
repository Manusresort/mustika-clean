[MICRORUN_SCRIPT_SAYUR_A_P4]

Title: Microrun Script — SAYUR-A (Annotation Only)

Status:
RUNBOOK — NOT A RUNTIME APPROVAL

Scope:
- Corpus: SAJUR-A excerpt
- Agent: Annotation/Flagging
- Max steps: 5
- Manual confirmation required per step
- Human Gate: active

---

## Step-by-step flow

Step 0 — Preflight
- confirm RUN-ID
- confirm manual step-gating ON
- confirm Human Gate present
- confirm rollback test plan available

Step 1 — Load excerpt
- EvidenceRef recorded
- No changes made
- If excerpt mismatch → STOP

Step 2 — First annotation pass
- agent proposes labels (short, stylecard)
- log uncertainty
- if ambiguity touches glossary → soft-stop

Step 3 — Challenger check (simulated)
- mark implied decisions
- enforce [AMBIGUOUS] where needed

Step 4 — Human Gate review point
- PASS / REWORK / NO-GO (document only)
- rationale logged

Step 5 — Rollback test
- delete pilot artefact copy
- verify state restoration
- log result (PASS/FAIL)

Run ends:
- compile After-Action draft
- no second run without new GO

---

## Stop rules

- outside autonomy envelope → STOP
- missing logs → STOP
- agent normalizes text → STOP + incident
- safety claim becomes prescriptive → STOP + Human Gate
- confusion about scope → STOP (do not guess)

---

## Outputs (temporary)

- annotations (proposal-only)
- soft-stop list
- Human Gate note
- rollback test note
- after-action draft

All reversible.

Reminder:
This script describes a potential run.
It does NOT authorize execution.

[/MICRORUN_SCRIPT_SAYUR_A_P4]
