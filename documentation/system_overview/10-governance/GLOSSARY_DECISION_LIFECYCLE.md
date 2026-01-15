# Glossary Decision Lifecycle

## Purpose
Dit document beschrijft de verplichte beslis-lifecycle voor terminologie in Mustikarasa.
Het borgt governance, reproduceerbaarheid en een audit-trail voor glossary-beslissingen.

## Scope
Van eerste voorstel tot definitieve glossary-beslissing, inclusief versiebeheer en rollback.

## Roles
- Glossary Agent (voorstellen, geen beslissingen)
- Research Agent (context + evidence)
- Orchestrator (proces sturen, geen eindbeslisser)
- Methodology Archivist (audit trail)
- Human Reviewer / Editorial Board (definitieve beslissing)

## Lifecycle Stages

1) Proposal
- Glossary Agent produceert [GLOSSARY_PROPOSALS].
- Verplicht: bronverwijzingen, onzekerheid, alternatieven.

2) Context
- Research Agent levert [RESEARCH_REPORT] gericht op de term(en).
- Koppelt naar bestaande RESEARCH_* documenten.

3) Risk Review
- Check op:
  - betekenisverschuiving
  - culturele/historische nuance
  - veiligheid/allergie-informatie
  - consistentie met bestaande beslissingen

4) Human Gate (Decision)
- Mens beslist.
- Besluit bevat: rationale, bronnen, datum, impact.

5) Versioning & Publication
- Beslissingen worden versie-beheerbaar vastgelegd.
- Wijzigingen krijgen changelog + referentie naar eerdere beslissingen.

6) Rollback Policy
- Wanneer rollback nodig is.
- Hoe rollback wordt vastgelegd (rationale en impact).

## STOP & Escalation Criteria
Pauzeer en escaleer bij:
- onvoldoende bronnen
- conflicterende historische interpretaties
- grote risico's (gezondheid, veiligheidsclaims)
- inconsistente terminologie met bestaande publicaties

Escalatiepad:
Troubleshooting Agent -> Orchestrator -> human reviewer.

## Required Artifacts
Elke beslissing levert op:
- Proposal (Glossary)
- Context (Research)
- Decision note (mens)
- Changelog entry (versiebeheer)
- Audit log (Methodology Archivist)

## Relationship to Other Documents
- prompts/glossary_agent.md
- prompts/research_agent.md
- prompts/orchestrator.md
- docs/AGENTS.md
- docs/CODEX_META_PROMPT.md
