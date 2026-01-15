
## Governance Clarifications (added for safety — documentary only)

### Canonical vs Non-Canonical Layers

| Layer | Role | Agent Editing Allowed? |
|------|------|------------------------|
| OCR scans / facsimile | historical record | ❌ no |
| OCR restored text | canonical working text | ❌ no |
| Editorial annotations (draft) | proposals | ✔ sandbox only |
| Glossary canonical | reference layer | ❌ no |
| Research notes | proposals | ✔ sandbox only |
| Pilot artifacts | documentary | ✔ sandbox only |

> **Rule:** If a layer shapes what readers eventually see, it is treated as canonical unless explicitly labeled otherwise.

---

### Moving Proposals Out of the Sandbox

Moving proposals from sandbox → docs is allowed **only if**:

1. provenance remains (`source_run`, `lifecycle_stage: proposal`)
2. the move is logged in `docs/CODEX_SESSION_LOG.md`:

[PROPOSAL_MOVED]
from: sandbox/agent_runs/<run_id>
to: <path>
reason: review

3. wording does not imply a decision.

> Missing provenance → **Governance-STOP**.

---

### Lifetime of Sandbox Runs

Sandbox runs persist until governance review concludes  
(archival is explicit — not automatic).

> Deletion equals rollback, not cleanup.

---

### Standard Run ID Format

RUN_<YYYYMMDD>_<NNN>  
Example: RUN_20260104_003

---

### Log Structure

logs/
  warnings.log
  stop.log
  governance_notes.log

`stop.log` must always capture STOP events.

---

### Agent Research is Hypothesis, Not Evidence

Agent “research” is treated as **claims requiring verification**, not sources.

---

### Explicit Human Gate Triggers

Human Gate applies when:

- cultural / religious meaning risks distortion
- health or safety statements appear
- glossary choices affect publication layers
- ambiguity approaches reader-visible text
- governed processes conflict

Otherwise: **document → defer → review**.

---

### Conflicting Proposals

Conflicting proposals enter the Glossary Lifecycle as
**competing proposals** — never merged informally.

---

### Not Implementation

These constraints describe safe expectations —
**not approval for runtime execution**.

---

## Methodology Note

Clarifications reduce ambiguity without enabling behavior.
