# P6 — SAYUR Mini Workflow Validation Checklist

## 1. Repo & Paths
- [ ] All referenced paths exist or are clearly future placeholders
- [ ] sandbox/workflows/p6_sayur_mini/* is used only as a working zone
- [ ] No outputs are mapped into canonical or publication areas

## 2. Lifecycle Fields
- [ ] decision_status is defined and documented
- [ ] decision_origin is defined and documented
- [ ] ready_for_human_review is defined and documented
- [ ] Status transitions match P5_DECISION_LIFECYCLE (reference, do not redefine)

## 3. Escalation Logic
- [ ] Escalation is selective, not default
- [ ] Clear reasons exist (ambiguity, glossary, safety, cultural risk, technical uncertainty)
- [ ] Human Gate is triggered only when impact matters

## 4. Logging & Traceability
- [ ] Annotator, challenger, and crew traces have stable locations
- [ ] Each decision keeps: span + rationale + lifecycle + origin
- [ ] Nothing depends on unstated manual memory

## 5. Governance Boundaries
- [ ] Workflow stays inside sandbox
- [ ] No implicit policy changes appear in documents
- [ ] Bias is documented, not “corrected silently”

## 6. Ready for Pilot?
- [ ] All unchecked items are documented with notes
- [ ] Risks are known and written down
- [ ] Pilot can proceed without structural changes
