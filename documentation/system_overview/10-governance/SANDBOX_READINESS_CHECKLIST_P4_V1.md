[SANDBOX_READINESS_CHECKLIST_P4_V1]

Title: Sandbox Readiness Checklist — Phase-4 (v1)

Status:
GOVERNANCE CHECKLIST — NOT A RUNTIME APPROVAL

Purpose:
Zichtbaar maken of de sandbox veilig, beperkt en omkeerbaar is —
en expliciet maken wat nog NIET mag.

---

## 1) Scope Confirmation (must all be YES)

- [ ] Corpus is beperkt tot: _______________
- [ ] Alleen pilot-artefacts (geen canon, geen productie)
- [ ] Agent-taken = detecteren / signaleren / annoteren (geen beslissingen)
- [ ] Maximaal aantal stappen per run: ______
- [ ] Rollback = volledig door eenvoudig verwijderen van pilot-map

If any NO → STOP (do not proceed)

---

## 2) Autonomy Envelope Alignment

- [ ] Agent mag alleen documenteren, niet normaliseren
- [ ] Variants/interpretaties = proposal-only
- [ ] Max 2 iteraties per conflict → ESCALATE
- [ ] Culture / safety / glossary impact → Human Gate
- [ ] “Reader-meaning shift” → STOP + log

If uncertain → SOFT-STOP + clarify before continuing

---

## 3) Logging Requirements

- [ ] EvidenceRef per item aanwezig
- [ ] Issue type gelabeld (Ambiguity / OCR / Safety / Culture)
- [ ] Action gelogd (Document / Soft-stop / Escalate)
- [ ] 1–2 regels rationale
- [ ] Run krijgt unieke ID + sessielog

Missing logs → FAIL (run invalid)

---

## 4) Incident / Recovery Path

- [ ] Procedure bij onbedoelde normalisatie
- [ ] Procedure bij ontbrekende logs
- [ ] Procedure bij publicatie-achtige output
- [ ] Default: STOP → documenteren → rollback → post-mortem
- [ ] Archivist verantwoordelijk voor incident-dossier

If any unclear → DO NOT RUN

---

## 5) Human Gate Definition

- [ ] Rol (niet persoon) aangewezen: __________________
- [ ] Criteria wanneer Human Gate wordt geroepen vastgelegd
- [ ] Besluiten worden gelogd in governance-artefact
- [ ] Geen automatische overrides
- [ ] Escalatiepad bij twijfel

Human Gate not defined → NO-GO

---

## 6) First-Run Constraints

- [ ] Only SAYUR-A excerpt (proposal)
- [ ] Only Annotation/Flagging agent
- [ ] No glossary edits
- [ ] No translation normalization
- [ ] Stop bij eerste buiten-envelope ambiguity

---

## 7) Readiness Decision (non-binding record)

- Overall assessment:
  - [ ] Ready
  - [ ] Maybe (conditions below)
  - [ ] Not ready

Conditions / notes:

_____________________________________

_____________________________________

---

## Final Reminder

Deze checklist is een veiligheidshek.
Het geeft GEEN toestemming om te draaien.
Een aparte governance-notitie moet expliciet “GO” zeggen
en alleen binnen de gevinkte voorwaarden.

[/SANDBOX_READINESS_CHECKLIST_P4_V1]
