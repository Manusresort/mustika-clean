# P6 Pilot Plan — SAYUR Mini Workflow (Pilot 01)

## 1. Scope & Excerpt
- reference: `data/sayur_groente_excerpt_v1.txt`
- locked line range: as documented in `docs/P6_WORKFLOW_SAYUR_MINI.md`
- sandbox-only; no publication outcome

### Excerpt metadata
- excerpt_id:
- excerpt_source:
- excerpt_version:

## 2. Objectives
- verify lifecycle behaviour
- observe challenger bias without correcting it
- achieve majority CREW_PROVISIONAL

## 3. Tools & Runners (reference only)
- `sandbox/crew/micropilot_sayur_multi_runner.py`
- `sandbox/crew/codex_p5_micropilot_provisional_runner.py`
- note: human runs only; no autonomous agent execution

## 4. Expected Artifacts
- annotator JSON: <path>
- challenger JSON: <path>
- crew_decisions_provisional.json: <path>
- human_review_notes (optional): <path_or_none>

## 5. Evaluation Method
- pilot template: `docs/pilots/P6_SAYUR_MINI_WORKFLOW_PILOT.md`
- evaluation template: `docs/runbooks/P6_MINI_WORKFLOW_EVALUATION_TEMPLATE.md`

## 6. Risks & Watchpoints
- bias pressure (translation-expectation)
- over-escalation beyond CREW_PROVISIONAL
- JSON contract drift

## 7. Pilot Status (Pilot 01)

- Status: COMPLETED
- Date: 2026-01-05
- Notes:
  Pilot initiated under Phase-6 workflow discipline.
  Runs will follow the checklist, pilot template and evaluation template.
  No runtime or policy changes are made during this pilot.
- Outcome: Pilot executed and evaluated using the P6 SAYUR mini workflow and evaluation template. All decisions landed at CREW_PROVISIONAL with no human escalations.
