[HUMAN_GATE_POLICY_P4_SANDBOX]

Title: Human Gate — Phase-4 Sandbox Policy

Status:
GOVERNANCE POLICY — NOT A RUNTIME APPROVAL

Purpose:
Zorgen dat beslissingen met betekenis-, cultuur- of veiligheidsimpact
ALTIJD door mensen worden genomen — traceable, reversibel en gedocumenteerd.

Scope:
Geldt uitsluitend voor Phase-4 sandbox-runs (design pilots, beperkte excerpten).
Niet van toepassing op productie of publicatie.

---

## 1) Human Gate — Role (not a person)

Role name: Editorial & Cultural Review Gate

Responsibilities:
- beoordelen van agent-signalen met potentiële impact
- besluiten: PASS / REWORK / NO-GO
- rationale registreren
- escaleren naar governance indien structureel probleem

This role does NOT:
- schrijven of herschrijven van inhoud,
- beslissen over definitieve glossary,
- medische/veiligheidsclaims moderniseren,
- productie-publicatie toestaan.

---

## 2) Triggers (WHEN Human Gate must be called)

Human Gate is VERPLICHT wanneer:

- [MeaningShift] lezer-betekenis kan merkbaar veranderen
- [GlossaryImpact] een term impliciet definitief lijkt
- [CulturalSensitivity] koloniale / identitaire framing geraakt wordt
- [SafetyRisk] tekst mogelijk medisch/advies-achtig leest
- [PublicationDrift] output te “af” / publieksklaar lijkt
- [RepeatedIncident] zelfde incident herhaald optreedt
- [OutsideEnvelope] agent doet iets buiten autonomie-kader

Bij twijfel → ALTIJD Human Gate.

---

## 3) Decision Model

Elke beslissing heeft exact een uitkomst:

- PASS — veilig om door te gaan (documentair)
- REWORK — terug naar pilot/agent, met duidelijke reden
- NO-GO — stop, rollback, governance bespreken

Default wanneer onzeker:
→ NO-GO (safe failure)

---

## 4) Logging Requirements

Elke Human Gate-actie moet bevatten:

- Run-ID
- EvidenceRef(s)
- Trigger type
- Decision (PASS / REWORK / NO-GO)
- Rationale (2–5 zinnen)
- Follow-up (indien van toepassing)

Wordt opgeslagen in:
docs/10-governance/HUMAN_GATE_LOG.md (append-only).

Geen log = besluit bestaat niet.

---

## 5) Interaction with Agents

Agents mogen:

- signaleren
- alternatieven opsommen
- onzekerheid markeren

Agents mogen NIET:

- besluiten forceren
- Human Gate omzeilen
- rationale verzinnen
- output presenteren als “definitief”

Elke poging tot omzeilen → incident + escalatie.

---

## 6) Interaction with Incident Playbook

Als Human Gate wordt opgeroepen naar aanleiding van incident:

- volg eerst INCIDENT_PLAYBOOK (containment)
- daarna Human Gate review
- daarna pas eventuele vervolg-experimenten

Geen parallelle beslissingen.

---

## 7) Boundaries & Sunset

Dit beleid geldt:
- alleen binnen sandbox-runs
- alleen totdat een apart Phase-4 governance-kader productie-klaar is
- en kan alleen worden gewijzigd via governance-logbesluit.

Reminder:
Dit document geeft GEEN toestemming om agents te draaien.
Het beschrijft uitsluitend het vangnet.

[/HUMAN_GATE_POLICY_P4_SANDBOX]
