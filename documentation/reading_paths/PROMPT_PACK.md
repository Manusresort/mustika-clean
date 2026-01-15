# PROMPT_PACK (Mustika Rasa Clean Repo)

## Where to look first
1) `documentation/system_overview/PROJECT_STATE_PACK.md`
2) `documentation/operator/RUNBOOK.md`
3) `documentation/system_overview/AS_BUILT_ARCH.md` (if present)
4) `docs/SYSTEM_OVERVIEW.md` (if present)
5) `documentation/reports/CRITICAL_PATH_NEXT_8_WEEKS.md`

---

## A) GPT Online – Project Resume Prompt

You are GPT. Read these files first:
- documentation/system_overview/PROJECT_STATE_PACK.md
- documentation/operator/RUNBOOK.md
- documentation/reports/MVP_TO_FULL_SYSTEM_MAPPING.md
- documentation/reports/CRITICAL_PATH_NEXT_8_WEEKS.md
- documentation/reports/BACKLOG_GITHUB_ISSUES.md
- documentation/system_overview/AS_BUILT_ARCH.md (if present)
- docs/SYSTEM_OVERVIEW.md (if present)

Task:
1) Summarize current system state (what is working, what is limited).
2) Summarize invariants/constraints that must not be broken.
3) Propose a 1–2 week sprint plan using ONLY existing backlog items.
4) Call out any missing info that blocks planning.

Output:
- Short current-state summary
- Sprint plan (bullets)
- Blockers

---

## B) Cursor – Targeted Implementation Prompt (UI/API/Runner)

You are Cursor. Work only inside `runtime/`.
Constraints:
- No breaking changes.
- Respect invariants: filesystem-first, human-in-the-loop, immutable runs/closures,
  no auto-promotion, canonical read-only.
- Implement ONE issue at a time from `documentation/reports/BACKLOG_GITHUB_ISSUES.md`.

Task:
- Pick one issue, restate scope and acceptance criteria.
- Implement the smallest change that meets acceptance.
- Add minimal tests or checks if applicable.
- Update or add documentation under `documentation/` if required.

Acceptance checks (required):
- Existing run bundles remain unchanged.
- Indices can be regenerated without errors.
- API `/health` and `/inbox` still respond.
- UI still loads (no 500s).

Output:
- What changed and why
- Files modified
- How to verify

---

## C) Codex CLI – Repo Mapping Prompt

You are Codex CLI. Work only in the clean repo.
Task:
- Re-scan current repo state and update documentation only.
- Produce/update:
  - documentation/system_overview/PROJECT_STATE_PACK.md
  - documentation/reports/MVP_TO_FULL_SYSTEM_MAPPING.md
  - documentation/reports/CRITICAL_PATH_NEXT_8_WEEKS.md
  - documentation/reports/BACKLOG_GITHUB_ISSUES.md
- Do NOT modify runtime behavior.
- Do NOT change invariants.

Output:
- Summary of updates
- Paths touched

---

## D) Debug Prompt

You are GPT. Diagnose the error with minimal back-and-forth.
Provide: root cause + exact next steps.

Please read:
- `runtime/runs/<excerpt_id>/<RUN_id>/logs/run.log`
- `runtime/runs/<excerpt_id>/<RUN_id>/eval/output_contract_checks.txt`
- `runtime/indices/inbox_index.json`
- `documentation/operator/RUNBOOK.md`

If API/UI issues:
- `runtime/audit/api_server.log` (if present)
- `runtime/audit/ui_dev.log` (if present)

Task:
1) Identify the most likely cause.
2) List concrete steps to verify.
3) Provide the minimal fix that preserves invariants.

Output:
- Root cause (1–2 lines)
- Verification steps
- Minimal fix
