# Execution Layer Gaps (Facts Only)

This document lists execution-layer gaps observed in the current repo.
It does not propose fixes or designs.

| gap_statement | evidence_paths | impact (facts-only) | disclaimer |
|---|---|---|---|
| Validator path mismatch | `runtime/src/runner_v2/runner.py` expects `runtime/sandbox/tools/phase8_output_contract_validator.sh`; actual validator exists at `sandbox/tools/phase8_output_contract_validator.sh` | Output contract validation may not run if path is not aligned | NOT A PROPOSAL |
| Pipeline boundary violation | `runtime/src/runner_v2/runner.py` imports `test_multi_agent_fidelity` (a test-named module); file exists under runtime but should not be imported by runtime core | Pipeline is coupled to a test-named module | NOT A PROPOSAL |
| No chapter → excerpt mapping | run manifests only include excerpt metadata; no chapter registry link | Cannot answer chapter coverage or chapter-based execution | NOT A PROPOSAL |
| No excerpt → segment mapping | no RB/BLK/SAJUR references in run manifests or indices | Cannot anchor runs to segments or page ranges | NOT A PROPOSAL |
| No run intent metadata beyond excerpt metadata | run manifests contain only excerpt + inputs + outputs | Cannot answer why a run was executed | NOT A PROPOSAL |
| No batch runner/orchestrator | no scripts for chapter-level batch execution found in runtime/scripts | Cannot execute chapter-sized runs in one operation | NOT A PROPOSAL |
| No cross-run comparison artifacts | no run comparison files found under runtime/ | Cannot compare runs structurally in filesystem | NOT A PROPOSAL |
