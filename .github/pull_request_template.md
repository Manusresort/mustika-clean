## Summary
What changes are introduced?

## Evidence
List relevant file paths and any run/audit artefacts.

## Invariant checklist (AS_BUILT_ARCH.md)
- [ ] Filesystem-first preserved (no moving runtime truth into GitHub)
- [ ] No canonical auto-promotion / no forbidden writes
- [ ] Page sources remain read-only for agents
- [ ] runtime/ and indices/ handling unchanged unless explicitly decided

## Verification
- [ ] I followed documentation/operator/RUNBOOK.md where relevant
- [ ] I did not commit runtime-generated state (runtime/, indices/)
