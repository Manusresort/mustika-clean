# Sayur Pilot Translation Plan (Design Record)
Status: DESIGN ONLY — NOT APPROVED FOR RUNTIME

## References
- CHAPTER_PREP_REPORT (documentary output for Sayur/Sajuran excerpt)
- data/source_imports/sayur_groente_001/EXCERPT_MAP.md
- data/source_imports/sayur_groente_001/sayur_groente_excerpt_v1.txt

## Pilot Translation Plan (Sayur)

[PILOT_TRANSLATION_PLAN_SAYUR]
- PilotPurpose
  - Test traceability of proposals to excerpt IDs and line ranges (SAJUR-A + SAJUR-B top lines).
  - Preserve ambiguity for key terms (sajuran, lalab, seupan, tumis, lobak, ubi).
  - Validate annotation flow without altering source text.
  - Exercise soft-stop + Human Gate triggers for safety/cultural risks.

- Scope
  - SAJUR-A (INTRO/CONTEXT) full excerpt range.
  - SAJUR-B: first 6–10 lines only (menu/list portion).
  - No full recipes; no structural edits; proposal-only outputs.

- SuccessCriteria
  - Every translation/annotation/glossary proposal cites EXCERPT_MAP ID + line range.
  - Ambiguous terms remain proposal-only with explicit uncertainty labels.
  - At least one soft-stop recorded for ambiguity or safety note.
  - No glossary decisions; no source edits; full rollback possible by deletion.

- AgentRoles
  - Translation Quality: produce draft translation as proposal-only; preserve ambiguity.
  - Annotation Agent: propose context notes (HISTORICAL/GLOSSARY/SAFETY/OCR).
  - Challenger: challenge ambiguous term choices; ensure uncertainty is visible.
  - Methodology Archivist: log lifecycle stage + traceability per artefact.
  - Orchestrator: enforce stop model; ensure no canon changes.

- WorkflowSteps
  1) Orchestrator loads SAJUR-A + SAJUR-B top lines from excerpt file.
  2) Translation drafts proposal-only translation with uncertainty markers.
  3) Annotation proposes notes tied to EXCERPT_MAP IDs.
  4) Challenger flags any implicit decisions.
  5) Glossary proposals generated for key terms only (proposal-only).
  6) Archivist logs traceability + stop events.
  7) Orchestrator compiles risk/soft-stop log; no decisions.

- ExpectedArtifacts
  - Draft translation (proposal-only, marked EXPERIMENTAL)
  - Annotation set with labels
  - Glossary proposals (proposal-only)
  - Risk/soft-stop log (methodology / incident notes)
  - Traceability map referencing EXCERPT_MAP IDs + line ranges

- SoftStops
  - Any ambiguity in sajuran category definition.
  - Any health/safety advice (kalium permanganate / metabisulfiet) flagged.
  - OCR ambiguity markers (e.g., “?2”, “€” symbol, “kentanyg”).
  - Dish-name vs method ambiguity (tumis / sayur lodeh/asam).

- HumanGateTriggers
  - Cultural/colonial framing risk in category descriptions.
  - Safety/health claims approaching reader-visible translation.
  - Root-crop ambiguity (ubi kaju/djalar) if it affects meaning.

- RollbackModel
  - Delete all pilot output artefacts (proposal files/log entries).
  - No source or glossary files touched; rollback = delete pilot directory + log entries.

- OpenQuestions
  - Are SAJUR-A and SAJUR-B definitively within the same chapter boundary?
  - Is there a preferred glossary handling for “sajuran” as a category vs dish?
  - Which safety annotations require Human Gate vs soft-stop documentation only?
[/PILOT_TRANSLATION_PLAN_SAYUR]

## Additions (design constraints)
- no fluency optimization — ambiguity first
- glossary-scope = only terms present in pilot excerpt

## Soft-Stop Logging Format (template)
[SOFT_STOP]
RunID:
ExcerptID:
LineRange:
Trigger:
ObservedRisk:
Action: document + defer
[/SOFT_STOP]

[AUTONOMY_DELEGATION_SAYUR]

Purpose:
Maak zichtbaar welke taken veilig gedelegeerd mogen worden,
zodat mensen niet onnodig micromanagen — terwijl betekenis,
cultuur en publicatie-impact beschermd blijven.

Delegation Map:

| Task / decision                                         | Agent autonomy | Conditions / safeguards                                  | Escalation |
|---------------------------------------------------------|----------------|----------------------------------------------------------------|-----------|
| OCR-ruis detecteren en clusteren                        | ✔ Allowed      | markeren, niet corrigeren in bron                              | Soft-stop bij twijfel |
| Annotatie-labels toevoegen (HISTORICAL/GLOSSARY/OCR)    | ✔ Allowed      | labels + rationale, geen normatieve herformulering             | Soft-stop |
| Mogelijke interpretaties van termen opsommen            | ✔ Allowed      | voorstel-only, met bewijs en onzekerheidslabel                 | Escalate bij normatieve taal |
| Vergelijkbare passages aanwijzen in andere excerpts     | ✔ Allowed      | alleen referenties, geen conclusies                            | Soft-stop |
| Ambiguïteit markeren + alternatieven structureren       | ✔ Allowed      | [AMBIGUOUS] met uitleg waarom                                 | n.v.t. |
| Cross-checking of agent proposals for consistency       | ✔ Allowed      | alleen conflicten signaleren; GEEN resolutie                   | Escalate if conflict persists |
| Glossary definitief kiezen                              | ✘ Not allowed  | reader-meaning impact                                          | Human Gate |
| Culturele framing / interpretatie                       | ✘ Not allowed  | publicatie-impact                                              | Human Gate |
| Veiligheids- of gezondheidsclaims herformuleren         | ✘ Not allowed  | ethisch/juridisch risico                                       | Human Gate |
| Inhoud wijzigen / normaliseren                          | ✘ Not allowed  | onomkeerbaar effect op betekenis                               | Human Gate |

Soft-stop triggers (guidance):
- wanneer de agent de keuze niet met excerpt-evidence kan verantwoorden, OF
- wanneer meerdere plausible interpretaties zichtbaar de lezer-betekenis kunnen verschuiven.

Status reminder:
Dit document blijft proposal-only. Deze tabel vergroot gedelegeerde, veilige autonomie,
maar autoriseert GEEN nieuwe inhoudelijke beslissingen.

Explicit Rules:

- Default behavior: Document — don’t decide.
- Max 2 agent-iterations per conflict → then ESCALATE.
- All autonomous steps must be logged and reversible.
- Any shift in reader meaning → STOP + Human Gate.

Notes for Sayur pilot:

- Terms zoals sajuran, lalab, seupan, lobak, ubi:
  → agents mogen varianten opsommen, maar geen definitieve gloss kiezen.
- OCR symbolen ("?2", "€"):
  → agents mogen DO_NOT_AUTOMATE markeren, niet corrigeren.
- Veiligheidsadviezen (permanganate/metabisulfiet):
  → altijd annoteren, nooit herschrijven — Human Gate zodra zichtbaar.

Status:
proposal-only, design document, not an approval.

[/AUTONOMY_DELEGATION_SAYUR]
