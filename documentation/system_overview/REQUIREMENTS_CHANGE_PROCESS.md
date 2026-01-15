# Requirements Change Process — Mustikarasa Platform

## 1. Purpose
- Dit document beschrijft hoe requirements worden beheerd zodat wijzigingen herleidbaar,
  verantwoord en reproduceerbaar blijven.
- Dit proces introduceert GEEN nieuwe inhoud — alleen governance.

## 2. Scope
- Geldt voor docs/REQUIREMENTS.md en alle toekomstige requirement‑documenten.
- Geldt voor: functional, non‑functional, governance, automation‑safety, pilots.
- Niet van toepassing op notities, research of ideeën totdat ze als requirement
  worden voorgedragen.

## 3. Roles
- **Proposer** — doet voorstel (kan elk teamlid/agent zijn).
- **Orchestrator** — bewaakt proces en logging.
- **Governance Agents** — leveren advies, nooit beslissen.
- **Human Gate / Editorial Board** — keurt high‑impact wijzigingen goed of af.

## 4. Change Types
- **ADD** — nieuwe requirement toevoegen.
- **UPDATE** — bestaande requirement aanpassen.
- **REMOVE** — requirement deprecaten/verwijderen.

Voor alle types geldt:
- MUST worden gelogd.
- MUST herleidbaar zijn naar context en reden.

## 5. Proposal Template
Voorstellen gebruiken verplicht dit format; zonder template is het voorstel niet geldig:

[REQUIREMENT_CHANGE_PROPOSAL]
ID:
Type: ADD | UPDATE | REMOVE
Motivation:
Impact:
RelatedDocs:
ProposedText:
Risks:
Rollback:
[/REQUIREMENT_CHANGE_PROPOSAL]

## 6. Governance Flow
1) Voorstel wordt gemaakt met template.
2) Orchestrator logt en valideert de vorm.
3) Governance‑agents leveren advies (indien relevant).
4) Risico‑check:
   - cultural / glossary / publication / safety → governance‑stop.
5) Human Gate beslist bij high‑risk wijzigingen.
6) Wijziging wordt vastgelegd in REQUIREMENTS.md.
7) CODEX_SESSION_LOG krijgt entry.
8) Indien nodig: rollback‑strategie documenteren.

Governance‑agents geven advies — beslissen NIET.

## 7. Human Gate Criteria
Human Gate is verplicht bij:
- wijzigingen met culturele of historische impact.
- wijzigingen die automatisering uitbreiden.
- wijzigingen die glossary/publicatie raken.
- wijzigingen die rollback onmogelijk zouden maken.
- wijzigingen die bestaande governance‑mechanismen verzwakken.

Human Gate is niet vereist bij:
- kleine verduidelijkingen,
- typo‑fixes,
- referentie‑correcties.

Alle wijzigingen worden gelogd.

## 8. Logging & Traceability
- Elke wijziging krijgt een `[SESSION]` entry in docs/CODEX_SESSION_LOG.md.
- REQUIREMENTS.md verwijst naar wijzigingsbeslissingen.
- Geen “stille” wijzigingen toegestaan.

## 9. Rollback Policy
- Elke wijziging MUST beschrijven hoe deze kan worden teruggedraaid.
- Rollback zelf MUST worden gelogd.
- Beslissingen blijven zichtbaar (geen herschrijven van geschiedenis).

## 10. Interaction with PHASES / TODO
- Grote wijzigingen krijgen een SYSTEM_REQUIREMENTS_* of PHASE3_* taak.
- Kleine wijzigingen mogen zonder nieuwe fase, maar blijven gelogd.
- PHASE‑promoties mogen NOOIT zonder requirements‑validatie.

## 11. Open Questions
- Moeten we versienummers aan requirements koppelen?
- Moeten sommige requirements “frozen” zijn?
- Hoe communiceren we breaking changes buiten het team?
