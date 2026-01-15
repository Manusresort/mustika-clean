[PILOT_TRANSLATION_PLAN_SANTAN]

Title: Pilot Translation Plan — SANTAN (Design Only)

Status:
DESIGN DOCUMENT — NOT APPROVED FOR RUNTIME

PilotPurpose:
- Test hoe ambiguïteit rond "santan" zichtbaar kan blijven.
- Oefen annotatieflow zonder normalisatie.
- Test autonomie binnen veilige grenzen (signalering > beslissen).
- Traceability: elke stap herleidbaar naar excerpt en EvidenceRef.

Scope:
- Alleen passages in excerpt die "santan" bevatten
  (ingredient / technique / extract context).
- GEEN volledige recepten.
- Alleen voorstelvertalingen + annotaties (experiment status).

SuccessCriteria:
- Alle voorstellen refereren naar EvidenceRef uit prep-report.
- Ambiguïteit blijft zichtbaar (geen normalisering).
- Ten minste 1 soft-stop rond veiligheid OF betekenis.
- Geen glossary-resolutie; volledige rollback mogelijk.

AgentRoles:
- Translation (proposal-only, ambiguity-first)
- Annotation (HISTORICAL / GLOSSARY / SAFETY / OCR)
- Challenger (detect overly-confident choices)
- Archivist (traceability + stop-log)
- Orchestrator (enforce stop model + sequencing)

WorkflowSteps:
1) Orchestrator selecteert relevante excerptregels uit prep-report.
2) Translation maakt concept-vertaling (met onzekerheidsmarkeringen).
3) Annotation voegt notities toe, gekoppeld aan EvidenceRef.
4) Challenger zoekt impliciete beslissingen en markeert ze.
5) Glossary-proposals alleen waar nodig — proposal-only.
6) Archivist registreert log + soft-stops.
7) Orchestrator bundelt outputs — GEEN beslissingen.

ExpectedArtifacts:
- Draft translation (EXPERIMENTAL)
- Annotatiepakket
- Glossary proposals
- Soft-stop log
- Traceability map (excerpt → EvidenceRef → proposal)

SoftStops (auto-trigger guidance):
- santan zonder kwalificatie (kental/encer) met betekenisrisico
- canned vs fresh implicaties
- veiligheids-/bederfcontexten
- gevallen waar annotatie feitelijk besluitvorming zou vervangen

HumanGateTriggers:
- cultuur- of koloniale framing-impact
- voedselveiligheid die lezersgedrag kan beïnvloeden
- normalisatie van santan tot één “juiste” vorm

AUTONOMY_DELEGATION_SANTAN:

| Task / decision                                   | Agent autonomy | Conditions / safeguards                                | Escalation |
|---------------------------------------------------|----------------|---------------------------------------------------------|-----------|
| Santan-gebruik detecteren en groeperen            | ✔ Allowed      | markeren, niet interpreteren                            | Soft-stop bij twijfel |
| Annotatie-labels toevoegen                        | ✔ Allowed      | labels + rationale, geen normatieve taal                | Soft-stop |
| Varianten opsommen (kental/encer/unknown)         | ✔ Allowed      | voorstel-only, onzekerheid expliciet                    | Escalate bij normatieve framing |
| Vergelijkingen met andere passages                | ✔ Allowed      | referenties, geen conclusies                            | Soft-stop |
| Consistency cross-checks tussen agent-proposals   | ✔ Allowed      | alleen conflicts signaleren, NIET oplossen              | Escalate if unresolved |
| Glossary definitief kiezen                        | ✘ Not allowed  | reader-impact                                           | Human Gate |
| Veiligheidsclaims herformuleren                   | ✘ Not allowed  | ethisch/juridisch                                      | Human Gate |
| Inhoud normaliseren (één “juiste” santan)         | ✘ Not allowed  | betekenisverschuiving                                   | Human Gate |

RollbackModel:
- Alle pilot-output staat in een aparte pilotdirectory.
- Verwijderen = volledige revert.
- Geen bronbestanden / glossary geraakt.

OpenQuestions:
- Hoe gaan we om met regionale varianten van santan?
- Wanneer is “kental” vs “encer” impliciet maar cruciaal?
- Hebben we toekomstige cross-pilot vergelijkingen nodig (Sayur ↔ Santan)?

Status reminder:
Dit document beschrijft ontwerp.
Het autoriseert GEEN uitvoering.

[/PILOT_TRANSLATION_PLAN_SANTAN]
