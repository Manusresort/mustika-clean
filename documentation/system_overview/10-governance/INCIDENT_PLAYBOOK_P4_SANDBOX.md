[INCIDENT_PLAYBOOK_P4_SANDBOX]

Title: Incident Playbook — Phase-4 Sandbox

Status:
SAFETY PROCEDURE — NOT A RUNTIME APPROVAL

Purpose:
Zorgen dat incidenten veilig, traceable en herstelbaar worden afgehandeld.
Default gedrag = STOP → DOCUMENTEREN → ROLLBACK → LEREN.

Definition (sandbox incident):
Elke situatie waarin:
- agent impliciet beslist i.p.v. documenteert, of
- lezer-betekenis kan verschuiven, of
- output lijkt op publicatie-klaar materiaal, of
- log ontbreekt / inconsistent is, of
- code / pipeline gedrag afwijkt van design.

---

## 1) Immediate Actions (EVERY TIME)

1️⃣ STOP
- onderbreek de run
- noteer tijd + run-ID

2️⃣ FREEZE
- niets aanpassen, niets wissen
- alleen kopieen maken naar sandbox/incident_logs/

3️⃣ LOG (minimal triage)
- EvidenceRef
- Issue type (Ambiguity / OCR / Safety / Culture / Automation)
- Observed behavior
- Why this is risky (1–2 regels)

4️⃣ NOTIFY (record only)
- note: “incident flagged — sandbox only”

No debugging, no fixes, no decisions.

---

## 2) Classification

Markeer precies EEN classificatie:

- NORMALIZATION: agent herschrijft / vereenvoudigt inhoud
- GLOSSARY-SLIP: term wordt beslissend gebruikt
- SAFETY-BLEED: tekst klinkt medisch/advies-achtig
- PUBLICATION-LOOK: output lijkt ‘klaar voor lezer’
- MISSING-LOG: stap zonder EvidenceRef/rationale
- MEANING-SHIFT: mogelijke verschuiving in interpretatie
- TECH-DRIFT: gedrag wijkt af van ontwerp

If unsure → classify as MEANING-SHIFT.

---

## 3) Containment (sandbox-only)

- verwijder niets uit het origineel
- verplaats kopie naar: sandbox/incidents/{RUN_ID}/
- voeg TRIAGE.md toe met:
  * wat zagen we
  * waarom stop
  * welke classificatie

Rollback model:
→ “terugdraaien = pilot-artefact verwijderen + lognotitie”.

---

## 4) Escalation Rules

Escalate NA containment wanneer:

- glossary / cultuur / veiligheid geraakt wordt
- publicatie-impact mogelijk is
- herhaalincident optreedt
- autonomie-grenzen overschreden werden

Escalation target:
Human Gate (rol), niet individu.

Human Gate acties:
- beoordeling = PASS / REWORK / NO-GO
- besluit wordt gelogd in governance-artefact
- geen inhoudelijke correcties door agents

---

## 5) Post-Incident Review (documentary only)

Create AFTER-ACTION addendum:

- root cause (process / autonomy / tooling / unclear rule)
- what prevented harm (if any)
- proposal-only improvements
- decision: “safe to retry?” (Yes/Maybe/No)

No blame. Only learning.

---

## 6) Non-Negotiable Rules

- Geen live fixes tijdens incident
- Geen publicatie van incident-output
- Geen glossaries veranderen
- Geen pipeline-wijzigingen
- Bij twijfel: STOP, log, escaleren

---

## 7) Linkage to Other Governance

This playbook works together with:
- SANDBOX_READINESS_CHECKLIST_P4_V1
- AGENT_AUTONOMY_ENVELOPE
- RUNBOOK_P4_SANDBOX_*
- AFTER-ACTION NOTE templates

If conflict → STOP and clarify before next run.

---

Closing reminder:
Dit playbook beschermt betekenis en reproduceerbaarheid.
Het is GEEN toestemming om sandbox-runs te starten.

[/INCIDENT_PLAYBOOK_P4_SANDBOX]
