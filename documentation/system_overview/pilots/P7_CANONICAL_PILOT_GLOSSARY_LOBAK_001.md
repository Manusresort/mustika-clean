# Phase-7 — Canonical Pilot 001 (Glossary Item: lobak)

## Purpose

This pilot exercises the canonical decision trail with a small but real decision:

- confirm that **"lobak"** in excerpt `lobak_034_048`
  is treated as a glossary item in the editorial inventory
- without deciding its meaning, translation, or cultural interpretation.

The goal is to prove that:

- AI proposals remain provisional,
- a human decision creates a canonical record,
- the trail is fully traceable and rollback-safe.

---

## Scope & Constraints

In scope:

- one lemma: "lobak"
- one excerpt: `lobak_034_048`
- one decision type: "glossary itemisation" (lemma inclusion, NOT meaning)

Out of scope:

- semantic gloss or translation of "lobak"
- historical or cultural interpretation
- changes to the scholarly edition text

If any semantic or interpretive questions arise,
they must be documented but left unresolved in this pilot.

---

## Excerpt & Artefact References

- excerpt_id: lobak_034_048  
- excerpt_source: docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md  
- excerpt_version: locked-2026-01-12  

Primary artefact for this pilot:

- annotator JSON (LOBAK Case-02 run):
  sandbox/crew/run_outputs/lobak_034_048/RUN_lobak_034_048_20260106T220558/annotator_primary.json

Related references (for traceability):

- challenger JSON:
  sandbox/crew/run_outputs/lobak_034_048/RUN_lobak_034_048_20260106T220558/challenger_primary.json
- run log:
  sandbox/crew/run_logs/lobak_034_048/RUN_lobak_034_048_20260106T220558_20260106T220558.log

---

## Editorial Decision to Be Made

Canonical decision (target state):

> In excerpt `lobak_034_048`, the string **"lobak"**
> is canonically recognised as a glossary item (lemma),
> eligible for future semantic and contextual work.

Important:

- This decision **only** asserts glossary inclusion (itemisation),
  not that we know or fix its meaning.
- Meaning-related decisions will be handled later,
  using a separate decision type (glossary meaning).

---

## Flow for This Pilot

1. **Review AI proposal**
   - locate where "lobak" is flagged as a glossary candidate
     in `annotator_primary.json`
   - verify excerpt-binding metadata

2. **Human review session**
   - confirm that "lobak" is indeed a glossary-worthy lemma
   - check for any immediate reasons NOT to include it

3. **Create canonical decision record**
   - new file under docs/decisions/
   - decision_type: glossary-itemisation (non-semantic)
   - link to excerpt, artefacts, reviewer, rationale

4. **Index integration**
   - add a single entry to CANONICAL_INDEX.md
     that points to:
       - the excerpt
       - the canonical decision record
       - related artefacts

5. **Reflection**
   - capture what worked, what was awkward,
     and what needs refining in the decision trail.

---

## Success Criteria

This pilot is considered successful if:

- the decision record is fully traceable:
  excerpt → run → AI proposal → review → decision file
- the distinction between "glossary inclusion" and "glossary meaning"
  is clear in the documentation
- CANONICAL_INDEX contains exactly one new entry,
  with clean references and no rehearsal artefacts
- no existing governance rules needed to be bent or ignored

---

## Risks & Watchpoints

- confusion between "this is a glossary lemma" and "we know its meaning"
- accidental drift into semantic interpretation
- forgetting to link the decision record in the index
- mixing rehearsal files with real canonical records

If any of these occur, document them and treat them
as design feedback for later Phase-7 refinements.

---

## Reflection (to fill after pilot)

What worked:

What was awkward:

Required design changes:

END OF FILE
