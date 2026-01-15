# Phase-6 Consolidation — Case-01 (SAYUR) and Case-02 (LOBAK)

## 1. Context
Phase-6 had to prove not only that an excerpt-aware design was *theoretically* sound,
but that it survives real workflow friction. Case-01 (SAYUR) gave us the happy-path:
excerpt chosen, runner works, artefacts generated.

However, relying on a single case risked a false sense of stability.
Case-02 (LOBAK) intentionally reused the same structure — and immediately exposed
a structural weakness: config files were not reliably mapped to runnable pipelines.

This was not a failure, but exactly the type of design-trigger Phase-6 exists for.

## 2. Excerpt-binding (proved working)
Excerpt metadata is now explicit, stable, and traceable:

- excerpt_id
- excerpt_source
- excerpt_version

It flows through:

CLI → run logs → runner JSON → annotator/challenger outputs.

Critically: mismatches are *documented and stop work* — not silently patched.

Excerpt binding is documentary (not enforced by code), and that is intentional:
humans remain responsible for the governing excerpt.

## 3. Excerpt-aware runner (proved under pressure)
The excerpt-aware entrypoint successfully dispatches runs based on config.
Case-02 revealed the missing mapping layer. We designed and implemented:

- config → runner wrapper file (bridge)
- stable resolution based on repo structure
- no behavioural changes in pipelines themselves

Result: Case-02 now executes end-to-end with exit code 0 and correct artefacts.

## 4. Payload refinement (now standard)
Runner outputs now contain:

- raw_output  — full TUI/console trace
- payload     — parsed JSON when available, null otherwise

Parse failures are not catastrophic but clearly logged (`[WARN] JSON parse failed…`).

This allows forward-only evolution without rewriting historical artefacts.

## 5. What Case-02 added beyond Case-01
- Demonstrated error-handling in a real run
- Validated STOP-on-mismatch thinking
- Proved the runner mapping layer is necessary
- Ensured excerpt metadata survives failure states
- Produced a reflection doc that mirrors Case-01

Case-02 therefore validates design resilience, not just happy-path success.

## 6. Risks now reduced
- ❌ Silent excerpt mismatch
- ❌ Untraceable runner behaviour
- ❌ Tight coupling between YAML and runtime
- ❌ Ad-hoc fixes without documentary trace

All replaced by explicit design, documented artefacts, and reproducibility.

## 7. What remains intentionally open
- JSON extraction can become smarter (not urgent)
- Human-review lane must still be formalised
- No canonical editorial decisions yet — by design

Phase-6 is about infrastructure and lifecycle clarity, not content decisions.

## 8. Next safe steps
1. Design the human-review lane (READY_FOR_HUMAN_REVIEW → CANONICAL remains human-gated).
2. Consolidate archive layout for excerpt-aware runs.
3. Reuse Case-02 structure as template for future cases.

This consolidation closes the loop: excerpt-aware workflows are now demonstrated,
documented, repeatable, and diagnosable — exactly as Phase-6 intended.
