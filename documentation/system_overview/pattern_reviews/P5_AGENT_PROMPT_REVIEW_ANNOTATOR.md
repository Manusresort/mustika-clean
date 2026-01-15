# P5 — Agent Prompt Review: Annotation Agent

Status: review — documentation only  
Scope: prompts/annotation_agent.md  
Related: docs/AGENT_PROMPT_PATTERN_P5.md

Purpose:
Deze review toetst de bestaande annotator-prompt aan het Phase-5 Pattern,
zonder wijzigingen door te voeren. Resultaat is input voor eventuele
(governance-gated) verbeteringen later.

---

## Fit-check (pattern sections)

- ROLE: present — duidelijk signalerend
- BOUNDARIES: aanwezig, kan compacter en explicieter
- INPUT: voldoende, maar aannames zitten deels impliciet
- OUTPUT CONTRACT: sterk (machine-checkbaar JSON)
- RULES: duidelijk, maar verspreid over meerdere blokken
- UNCERTAINTY & ESCALATION: aanwezig, maar niet als aparte sectie
- FORBIDDEN: aanwezig (vertalen/equivalents), mag strakker
- LOGGING: impliciet via run-logs — niet in prompt zelf
- PURPOSE REMINDER: aanwezig maar niet standaard-formeel

---

## Provisional classification

STATUS: **needs-clarification**

Reden:
De prompt volgt het juiste gedrag (signalerend, JSON, geen beslissingen),
maar mist enkele expliciete pattern-elementen (uncertainty section,
logging expectations, één vaste forbidden-lijst).

Dit is geen fout — alleen een kans voor harmonisatie in Phase-5.

---

## Notes (no changes proposed yet)

- Translation-expectation bias blijft zichtbaar — intended.
- Eventuele aanscherpingen vereisen Human Gate review.
- Pattern-adoptie is documentair; geen runtime-autoriteit.

---

## Next step (suggested)

Wanneer governance dat goedkeurt:
- alleen kleine, tekstuele klarificaties toevoegen,
- zonder gedragswijziging,
- met commit-comment: `Pattern-alignment only (no behavior change)`.

Einde document.
