---
# Phase-6 — Runner Payload Refinement Design

Status: DRAFT (Phase-6)  
Scope: excerpt-aware runner JSON payloads (annotator/challenger)

## 1. Context

In the first excerpt-aware Case-01 run (SAYUR 052–066), the runner wrote JSON files:

- `sandbox/crew/run_outputs/sayur_052_066/{run_id}/annotator_primary.json`
- `sandbox/crew/run_outputs/sayur_052_066/{run_id}/challenger_primary.json`

with the structure:

```json
{
  "excerpt": { "id": "...", "source": "...", "version": "..." },
  "run": { "id": "...", "timestamp": "..." },
  "payload": "<full console / TUI output as a single string>"
}
```

This is acceptable for validation (traceability + layout), but noisy for downstream
reviewers and tooling.

This design refines how payloads should be structured in *future* runs.
It does **not** retro-edit existing artefacts.

---

## 2. Design Goals

- Preserve traceability (excerpt + run metadata).
- Keep raw output available for audit.
- Provide a clean, structured “annotation payload” for reviewers.
- Avoid retroactive rewriting of existing run outputs.

---

## 3. Proposed Payload Structure (Future Runs)

For future runs, each JSON artefact should include **both**:

1) `raw_output` — full console/TUI output as captured.
2) `payload` — structured JSON (if parseable) or `null` if not.

### Example (annotator_primary.json)

```json
{
  "excerpt": { "id": "...", "source": "...", "version": "..." },
  "run": { "id": "...", "timestamp": "..." },
  "raw_output": "<full console output>",
  "payload": [
    { "line": 52, "span": "...", "label": "HISTORICAL", "reason": "..." }
  ]
}
```

### Example (challenger_primary.json)

```json
{
  "excerpt": { "id": "...", "source": "...", "version": "..." },
  "run": { "id": "...", "timestamp": "..." },
  "raw_output": "<full console output>",
  "payload": [
    { "line": 54, "span": "...", "issue_type": "GOVERNANCE", "severity": "WARNING", "comment": "..." }
  ]
}
```

If the runner cannot parse JSON cleanly, set:

- `payload: null`
- include `raw_output` unchanged
- log a parse warning in the run log

---

## 4. Compatibility & Non-Retroactivity

- Existing Case-01 outputs remain unchanged.
- No attempt is made to rewrite or “clean” historical artefacts.
- Refinements only apply to future excerpt-aware runs.

---

## 5. Implementation Note (Future Work)

This refinement should be implemented in the runner layer, not in post-processing.
The runner should:

- capture raw output as-is,
- attempt to parse structured JSON output (if present),
- write both to the JSON artefact in the format above.

No lifecycle changes or governance shifts are implied by this refinement.

---

End of document.
