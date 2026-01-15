# Agent Autonomy Envelope (draft)

Purpose:
Define which decisions agents may take independently,
which require peer-discussion, and which require Human Gate.

## Allowed Autonomous Decisions
- formatting fixes within an agreed template
- spelling/typo corrections that do not change meaning
- reordering of sentences for clarity without semantic change
- flagging ambiguity and adding non-committal notes

## Peer-Resolution First (Agent Meetings)
agents discuss, challenge, propose;
no final meaning or publication decisions.

## Human Gate Mandatory
meaning changes, glossary resolution, cultural interpretation,
reader-impact trade-offs, publication visibility.

## Logging Rule
all autonomous actions + meetings documented;
reversible by design.

Status: draft — improves workability, not policy.

## Clarifying Examples (what “autonomy” means in practice)

**Allowed autonomous decisions (low-risk, reversible)**  
- formatting and clarity tweaks that do **not** change meaning  
- standardizing units where policy already allows (e.g. “½ liter” → “500 ml”)  
- consistent spelling within a single recipe (no cross-book harmonization)  
- adding short clarifying markers such as *(editorial note: uncertain / ambiguous)*  
- flagging OCR suspicion without correcting it

**Not allowed autonomously (Human Gate required)**  
- resolving ambiguous cultural or historical terms  
- choosing between competing glossary meanings  
- softening or reframing colonial/ethical language  
- substituting ingredients and labeling them “equivalent”  
- any change that could alter reader interpretation or historical framing  

Rule of thumb:  
> **If a reader’s understanding could shift, it is NOT an autonomous decision.**

## Agent Meetings — Exit Rule

Agents are encouraged to discuss conflicts with each other before escalation.  
To avoid infinite loops and analysis paralysis:

> **Maximum 2 iterations per conflict.  
> If still unresolved → escalate with rationale.**

Each meeting should end in one of three outcomes:

1. **SAFE:** proceed (logged)  
2. **AMBIGUOUS:** document, do not resolve  
3. **ESCALATE:** Human Gate required (with notes)

## Uncertainty Default

When available evidence is insufficient or conflicting:

> **Default = document, don’t decide.**

Agents must:

- add an *AMBIGUOUS* label  
- briefly explain *why* the case is ambiguous  
- defer rather than guess  
- optionally propose what kind of evidence would be needed to resolve it

No “best guess” decisions on meaning.

## Audit Tags (traceability)

Every autonomous or collaborative step must carry one visible tag, e.g.:

```text
[AUTO-OK]        — autonomous change, low risk, reversible
[AGENT-MEETING]  — discussion occurred, no final meaning decision
[AMBIGUOUS]      — documented uncertainty, left unresolved
[ESCALATE-HUMAN] — Human Gate requested
```
