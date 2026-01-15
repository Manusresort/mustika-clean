# Safety M4 — Proposal Requirement (Safety-Aware Editorial Judgement)

## Purpose
This document defines when a Canonical Proposal Record is mandatory
for safety-related observations within the Safety-Aware Editorial
Judgement capability.

The goal is to ensure that safety-relevant considerations are never
handled implicitly or silently.

---

## Mandatory Proposal Cases

A Canonical Proposal Record is REQUIRED when any of the following
conditions apply:

### 1. Safety-Relevant Signal Detected
Any instance that meets the criteria defined in
docs/SAFETY_M4_SIGNAL_DEFINITION.md must be recorded as a proposal.

### 2. Intentional Non-Action
If a safety signal is identified and the decision is to take no
editorial action (e.g. no annotation, no clarification), this
non-action must still be documented via a proposal.

### 3. Deferral or Uncertainty
When safety relevance is acknowledged but deferred due to uncertainty,
lack of evidence, or pending review, a proposal is mandatory.

### 4. Divergent Interpretations
If multiple reasonable interpretations exist, at least one of which
has plausible safety implications, the situation must be captured
as a proposal.

---

## Optional Proposal Cases

A proposal MAY be created when:
- safety relevance is suspected but later ruled out,
- similar safety issues have already been documented elsewhere,
- the signal is purely informational with no plausible reader impact.

Optional cases should err toward documentation when ambiguity exists.

---

## Boundary Conditions

- Creating a proposal does not imply agreement, correction, or change.
- A proposal may remain unresolved indefinitely.
- Multiple proposals may exist for the same source material.
- Proposals may reference earlier proposals without replacing them.

---

## Non-Goals (Explicit)

- This document does not decide outcomes.
- This document does not define workflow or gating.
- This document does not authorize editorial changes.
