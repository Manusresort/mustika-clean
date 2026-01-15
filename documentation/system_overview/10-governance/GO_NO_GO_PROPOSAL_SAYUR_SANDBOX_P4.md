[GO_NO_GO_PROPOSAL_SAYUR_SANDBOX_P4]

Title: GO / NO-GO Proposal — Phase-4 Sandbox (SAYUR-A, Annotation-Only)

Status:
PROPOSAL — NOT AN APPROVAL

Purpose:
Beoordelen of een ZEER BEPERKTE sandbox-run verantwoord is,
uitsluitend om het proces te testen (niet de inhoud).

---

## 1) Proposed Scope

- Corpus: SAJUR-A excerpt (v1)
- Agent: Annotation / Flagging agent
- Autonomy: detecteren, labelen, signaleren — GEEN beslissingen
- Outputs: pilot-artefacts (proposal-only), volledig reversibel
- Max 5 stappen. Elke stap vereist MANUELE bevestiging (“continue?”).
- Stop bij eerste outside-envelope event
- Human Gate is ACTIEF aanwezig tijdens de volledige run.

---

## 2) Controls Already in Place

- ✔ Autonomy Envelope
- ✔ Sandbox Readiness Checklist (v1)
- ✔ Human Gate Policy
- ✔ Incident Playbook
- ✔ Runbook (table-top rehearsal tested)
- ✔ Rollback: delete pilot directory + session log reference
- ✔ RUN-ID registry aanwezig in CODEX_SESSION_LOG.md (format: RUN-P4-SAYUR-A-0001)

---

## 3) Expected Risks (and mitigations)

- Ambiguity → soft-stop + Human Gate
- OCR-ruis → DO_NOT_AUTOMATE labels
- Publication-drift → stop + rollback
- Glossary-slip → escalate
- Missing logs → run invalid → rollback + review

No irreversible actions possible under this scope.

---

## 4) Success Criteria (process, not content)

- Elke agent-actie heeft EvidenceRef
- Minstens 1 soft-stop correct gelogd
- Geen beslissingen vermomd als annotaties
- Rollback getest en werkend
- After-Action ingevuld met leerpunten
- Rollback wordt minimaal 1× daadwerkelijk uitgevoerd (test), daarna wordt de run opnieuw gestart.

---

## 5) Explicit No-Permission Boundaries

- Geen glossary-wijzigingen
- Geen vertaal-normalisatie
- Geen publicatie-artefacts
- Geen code of pipeline-wijzigingen
- Geen uitbreiding van scope zonder nieuw voorstel
- Geen ketting-runs: GO vervalt direct na afloop van de run. Elke nieuwe run vereist nieuw GO-document.

---

## 6) Proposed GO / NO-GO question

> “Mag een sandbox-run worden uitgevoerd,
>  binnen bovenstaande scope en met alle controles actief?”

Dit GO geldt EXACT voor een (1) sandbox-run binnen deze scope, en verloopt automatisch na uitvoering.

Governance answers:
- [ ] GO — onder deze voorwaarden
- [ ] NO-GO — redenen hieronder

Notes / conditions:

_____________________________________

_____________________________________

---

## 7) If GO — Preconditions Checklist

- [ ] Checklist v1 ingevuld (alles YES or documented)
- [ ] Incident Playbook bekend bij betrokkenen
- [ ] Human Gate logbestand aanwezig
- [ ] Human Gate reviewer toegewezen en bekend
- [ ] RUN-ID vooraf aangemaakt en gelogd
- [ ] Run krijgt unieke RUN-ID
- [ ] Rollback-test wordt gepland
- [ ] Manual-step gating bevestigd (geen auto-continue)

---

## 8) If NO-GO — Follow-up

- Documenteer redenen
- Herzie pilots / governance docs
- Plan nieuwe evaluatie
- Geen sandbox-activiteiten tot nieuw besluit

---

Closing reminder:
Dit document is een voorstel.
Er kan GEEN sandbox-run plaatsvinden
zonder een expliciete, gelogde GO-beslissing.

[/GO_NO_GO_PROPOSAL_SAYUR_SANDBOX_P4]
