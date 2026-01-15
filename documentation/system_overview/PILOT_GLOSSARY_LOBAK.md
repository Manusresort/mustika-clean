# Pilot #1 — Lobak

## Goal
Test een kleinschalige, proposal‑only glossary‑pilot rond de term “lobak” om
de Glossary Decision Lifecycle en governance‑stop expliciet te demonstreren,
zonder definitieve beslissingen of runtime‑activiteiten.

## Scope
- Eén term: lobak
- Alleen documentair: geen pipeline‑runs, geen glossary‑wijzigingen
- Output: proposals, research‑context en governance‑logverwachting

## Source
- docs/RESEARCH_GLOSSARY.md (bronverwijzingen en eerder genoemd materiaal)
- docs/GLOSSARY_PILOT_REPORT.md (pilot‑format en lifecycle‑context)

## Hypothesis
De term “lobak” vereist expliciete lifecycle‑stappen vanwege mogelijke
variant‑spellingen en meerdere interpretatie‑opties; proposal‑only is noodzakelijk
tot Human Gate.

## Workflow (documentary)
1) Glossary Agent maakt proposal‑only entry voor “lobak”.
2) Research Agent levert context/evidence‑blok.
3) Orchestrator markeert governance‑stop bij terminologie‑risico.
4) Human Gate wordt expliciet uitgesteld (pilot‑only).

## Glossary Behaviour
- Proposal‑only output in [GLOSSARY_PROPOSALS] format.
- Geen definitieve termkeuze, geen publicatie‑effect.
- Verwijst naar Glossary Decision Lifecycle voor risk review en Human Gate.

## Research Role
- Levert [RESEARCH_REPORT] met bestaande bronnen en context.
- Neemt geen eindbeslissing; ondersteunt het voorstel.

## Failure Notebook
Verplichte failure case:
- Simuleer inconsistentie tussen twee mogelijke equivalente termen.
- Verwacht: governance‑stop, geen automatische keuze.
- Log: expected vs actual, lessons learned, governance‑evaluatie.

### Health-related statements (clarification)

Some passages in Mustika Rasa contain medical or health claims
(e.g. statements about digestion, urine flow, stamina, etc.).

In this pilot — and in the scientific edition generally —

- these claims MUST NOT be rewritten or “modernised”
- they MAY be annotated
- they MUST be logged as historical claims, not medical advice
- any contradiction or risk is handled through annotation,
  not through silent changes to the source text.

This ensures we preserve the historical document
while still protecting modern readers through context.

## Expected Governance Outcome
- Soft‑stop bij terminologie‑ambiguïteit.
- Governance‑stop geactiveerd door Orchestrator.
- Human Gate expliciet uitgesteld (pilot‑only).
- Alle outputs gelogd; geen glossary‑mutaties.
