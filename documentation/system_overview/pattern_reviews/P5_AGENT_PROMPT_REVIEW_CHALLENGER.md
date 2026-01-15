# P5 — Agent Prompt Review: Challenger Agent

Status: review — documentation only  
Scope: prompts/challenger_agent.md (en varianten voor sandbox/micropilots)  
Related: docs/AGENT_PROMPT_PATTERN_P5.md

Purpose:
Deze review toetst de bestaande challenger-prompt aan het Phase-5 Pattern,
zonder wijzigingen door te voeren. Resultaat dient als input voor eventuele,
governance-gated verbeteringen later.

---

## Fit-check (pattern sections)

- ROLE: helder — signaleert alleen rule-violations
- BOUNDARIES: goed, maar deels impliciet
- INPUT: duidelijk (annotator JSON + tekst)
- OUTPUT CONTRACT: sterk (issue_type / severity / comment)
- RULES: gestructureerd, maar verdeeld over uitlegblokken
- UNCERTAINTY & ESCALATION: aanwezig, vooral via severities
- FORBIDDEN: redelijk (geen vertalingen eisen), mag explicieter
- LOGGING: via pipeline/logs, niet expliciet in prompt
- PURPOSE REMINDER: aanwezig, kan korter en formulematiger

---

## Provisional classification

STATUS: **needs-clarification**

Reden:
De prompt doet precies wat we willen (kritisch, maar niet beslissend),
maar pattern-elementen zoals een vaste forbidden-lijst en expliciete
uncertainty/escaleer-sectie zijn nog niet uniform vastgelegd.

Dit is geen probleem — alleen harmonisatie-potentieel voor Phase-5.

---

## Notes (no changes proposed yet)

- Translation-expectation bias verschijnt soms — dit is nu een documentair signaal.
- Geen vertalingen afdwingen is correct; INFO/WARNING/BLOCKER is passend.
- Aanpassingen (indien nodig) vereisen Human Gate review.

---

## Next step (suggested)

Indien governance akkoord:
- kleine clarificaties voor forbidden + uncertainty toevoegen,
- gedrag NIET veranderen,
- commit-label: `Pattern-alignment only (no behavior change)`.

Einde document.
