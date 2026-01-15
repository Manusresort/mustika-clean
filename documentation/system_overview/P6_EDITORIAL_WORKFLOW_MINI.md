> NOTE (Phase-6, naming alignment):
> This workflow is generic and applies to all chapters.
> SAYUR Case-01 is only the first application — not the design target.

---

# Phase-6 — Mini Editorial Workflow (Internal)

This workflow describes how a small SAYUR excerpt moves from
raw source → scholarly edition → provisional crew output → human review,
without producing canonical or public text.

It is intended for repeatable internal work.

---

## 1. Scope

- applies to short SAYUR excerpts (1–3 paragraphs, or ~1 recipe fragment)
- internal only — no publication impact
- all AI outputs remain provisional
- humans remain the ultimate decision makers
- every step produces traceable artefacts

---

## 2. Roles

### Annotator Agent
Produces CANDIDATE labels with rationale.
Cannot escalate or decide glossary terms.

### Challenger Agent
Flags risk, bias, overreach, and lifecycle problems.
Cannot force translation or glossary choice.

### Crew Synthesizer
Combines annotator + challenger into CREW_PROVISIONAL decisions.

### Human Reviewer
Only actor allowed to move anything beyond READY_FOR_HUMAN_REVIEW.
Adds commentary — not edits — to the text itself.

### Archivist (meta)
Ensures logs are preserved, structure consistent, and rollback is possible.

---

## 3. Lifecycle Contract

We use the existing lifecycle:

CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL (human-only)

Agents may ONLY move items up to CREW_PROVISIONAL.

Humans may mark READY_FOR_HUMAN_REVIEW,
but CANONICAL decisions require editorial governance
and are outside this mini-workflow.

---

## 4. Step-by-Step Workflow

1️⃣ Select excerpt  
Log selection and rationale.

2️⃣ Run annotator  
Store JSON in:
sandbox/workflows/sayur_internal/annotator_raw.json

3️⃣ Run challenger  
Store JSON in:
sandbox/workflows/sayur_internal/challenger_raw.json

4️⃣ Crew synthesis  
Produce:
sandbox/workflows/sayur_internal/crew_decisions_provisional.json

5️⃣ Human triage  
Reviewer marks:
READY_FOR_HUMAN_REVIEW only when necessary.

Record notes in:
sandbox/workflows/sayur_internal/human_review_notes.md

6️⃣ Archive  
Link all files to the excerpt in a trace note.

---

## 5. Logging Rules

Every excerpt must have:

- excerpt source reference
- annotator JSON
- challenger JSON
- crew decision JSON
- human review notes (even if empty)
- pointer to session log(s)

### Excerpt metadata (Phase-6)
Elke workflowrun die op een excerpt werkt, registreert minimaal:
- excerpt_id
- excerpt_source
- excerpt_version

Dit zijn documentaire velden voor traceability.
Ze veranderen geen agent-autonomie en voeren geen automatische validatie uit
(zie: P6_EXCERPT_BINDING_SPEC.md).

No artefacts are deleted — only superseded.

---

## 6. What This Workflow Must NOT Do

- no translations  
- no canonical glossary decisions  
- no silent auto-fixes  
- no rewriting of source text  
- no publishing artefacts  

Any time uncertainty appears,
record it — don’t solve it silently.

---

## 7. When to Escalate to Human Gate

Escalate only when:

- decision would change meaning
- glossary status requires commitment
- translation is implied
- cultural interpretation could mislead readers

Otherwise: keep it provisional and documented.

---

## 8. Outcome of This Workflow

End state should be:

- a well-annotated SAYUR excerpt
- clear rationale trails
- identified uncertainties
- NO irreversible editorial choices

---

End of workflow.
