# P8 – Meaning Preservation Under Pressure (Micro-pilot)

## 1. Title & Status

Status: EXPERIMENTAL — SANDBOX — NOT FOR PUBLICATION

This pilot observes how meaning shifts when different agents touch the same text.

## 2. Pilot Goal

- detect where meaning starts to drift when Translation and Readability try to help
- make Fidelity’s role explicit as a meaning-safety net
- capture small, reusable heuristics for future runs
- see which phrases consistently trigger ambiguity notes

## 3. Source Fragment (sandbox)

"Fry the spices until fragrant, but do not let them brown.
Add the sliced chilies and cook until half-soft."

Note: in later runs this fragment can be replaced by a real Mustika Rasa snippet,
but this file itself remains generic. This fragment is a SANDBOX example, not
canonical text.

## 4. Agent Roles & Tasks

### Translation Agent

- translate as faithfully as possible
- explicitly note where the source felt ambiguous
- do NOT improve or modernise for style

### Readability Agent

- improve flow and clarity for a modern reader
- for every change that might affect meaning, add a short inline comment or bullet
  explaining what changed
- never silently remove warnings or constraints (e.g. "do not let them brown")

### Fidelity Agent

- compare Translation and Readability outputs
- list any spots where meaning may have drifted
- propose safer alternatives as suggestions only (no final decisions)
- explicitly point out any loss of important nuance or caution

### Annotation Agent

- only act where context is really needed
- propose short, neutral annotations that explain:
  - why a phrase is tricky
  - what a cook or reader must understand
- do not rewrite the main text; all changes go into notes/annotations

## 5. Run Instructions (for humans)

- Step 1: Copy the Source Fragment into a working note.
- Step 2: Ask the Translation Agent (or its prompt) to produce a faithful translation + ambiguity notes.
- Step 3: Ask the Readability Agent to produce a more fluid version + explicit change notes.
- Step 4: Ask the Fidelity Agent to compare both and list potential meaning drift.
- Step 5: Ask the Annotation Agent to propose 1–3 annotations where this helps the reader.
- Step 6: Fill in the [CAPABILITY_CHECK] and [IMPACT_ASSESSMENT] blocks at the bottom of this file.
- Emphasize: no canonical decisions, no glossary changes, no source edits — this is for learning only.

## 6. Analysis Template ([CAPABILITY_CHECK])

[CAPABILITY_CHECK]
Which phrases showed the highest risk of meaning drift?
Where did Translation and Readability diverge in a meaningful way?
What did Fidelity identify as unacceptable drift vs. acceptable variation?
Did Annotation help clarify the problem for a future editor or reader?
What simple heuristics should we reuse in future runs?
[/CAPABILITY_CHECK]

## 7. Impact Template ([IMPACT_ASSESSMENT])

[IMPACT_ASSESSMENT]
What changed in our ability to keep meaning intact when multiple agents touch the same text?
What should future pilots or workflows do differently because of what we saw here?
Is there any concrete checklist or "watch out for this" pattern we can add to our editorial practice?
If we deleted this pilot tomorrow, which specific insight would we miss?
[/IMPACT_ASSESSMENT]

## 8. Notes & Limitations

- micro scope: one fragment, a few agents
- intended for repeat runs with different fragments
- does not define policy or lifecycle; it only informs practice
- nothing here changes any canonical decision or glossary entry
