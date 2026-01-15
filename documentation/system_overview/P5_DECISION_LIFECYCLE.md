# Decision Lifecycle — Translation & Interpretation (Phase 5)

Purpose:
Duidelijk vastleggen hoe beslissingen rond vertaling/interpretatie
door het systeem bewegen — en wie welke status mag zetten.

This lifecycle applies to agents, crews, Codex/meta, and Human Gate.

---

## Status Model

1) CANDIDATE_TRANSLATION
   origin: individual agent
   meaning: voorstel, open, nog niet besproken
   challenge_open: true

2) CREW_PROVISIONAL
   origin: crew (annotator + challenger + reasoning/meta)
   meaning: werkversie; voldoende stabiel voor verdere stappen
   reopen_possible: true
   rationale_logged: required

3) READY_FOR_HUMAN_REVIEW
   origin: crew or meta
   meaning: inhoud lijkt publicatie-relevant of gevoelig
   trigger: uncertainty, sensitivity, downstream impact

4) CANONICAL
   origin: Human Gate / editorial decision
   meaning: definitieve keuze; traceable; herziening vereist proces

---

## Authority Matrix (Who may set which state?)

- Individual agent:
  may → CANDIDATE_TRANSLATION
  may NOT → set CREW_PROVISIONAL, READY_FOR_HUMAN_REVIEW, CANONICAL

- Crew (multi-agent):
  may → promote to CREW_PROVISIONAL
  may → mark items READY_FOR_HUMAN_REVIEW
  may NOT → set CANONICAL

- Codex / meta-agent:
  may → re-open CREW_PROVISIONAL if reasoning is weak
  may → cluster decisions and mark READY_FOR_HUMAN_REVIEW
  may NOT → set CANONICAL

- Human Gate:
  may → set CANONICAL
  may → remand a decision back to CREW_PROVISIONAL

---

## Design Principles

- decisions are allowed,
- but they must stay reversible,
- must remain challengeable,
- and must be documented.

Agents decide for work.
Humans decide for publication.

End of document.
