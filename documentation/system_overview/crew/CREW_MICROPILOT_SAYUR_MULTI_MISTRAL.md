[CREW_MICROPILOT_SAYUR_MULTI_MISTRAL]

Title: Crew Micro-Pilot Plan — SAYUR (Annotator + Challenger)

Status:
RUNTIME TEST PLAN — NOT A GOVERNANCE DECISION

Purpose:
Prove annotator + challenger coordination on the SAJUR-A locked mini-excerpt
without meaning decisions or content changes.

Agents:
- annotator_mistral: produces JSON annotations (array of {line, span, label, reason}).
- challenger_mistral: reviews annotations for overreach and rule violations.

JSON contract (high level):
- annotator: JSON array of {line, span, label, reason}
- challenger: JSON array of {line, span, issue_type, severity, comment}

Run recipe:
- runner: sandbox/crew/micropilot_sayur_multi_runner.py (manual, human-triggered)
- logs: sandbox/crew/run_logs/

Governance:
- challenger MUST NOT add new content or decide meaning
- issue_type touching culture/safety/meaning → Human Gate, not auto-fix

[/CREW_MICROPILOT_SAYUR_MULTI_MISTRAL]
