# Runner V2 — Phase-6 Excerpt-Aware Runner

## Overview

Runner V2 is a clean implementation of the Phase-6 excerpt-aware runner, aligned with Phase-6 specifications and integrated with the existing Mustika Rasa infrastructure (UI, indexer, validators).

## Key Features

- **Explicit Excerpt Metadata**: Requires `excerpt_id`, `excerpt_source`, `excerpt_version` (no inference)
- **Pre-flight Validation**: Stops before any model calls if metadata is missing
- **Standardized Outputs**: Creates required JSON files per Phase-6 spec
- **Validator Integration**: Calls existing `phase8_output_contract_validator.sh`
- **Model-Agnostic**: Supports Ollama/Mistral (current) and configurable for other backends
- **Immutable Runs**: Each run gets unique directory, never overwrites

## Architecture

```
src/runner_v2/
├── __init__.py
├── runner.py          # Core runner logic
├── llm_client.py      # Model-agnostic LLM interface
└── run_layout_adapter.py  # Normalizes different run layouts

scripts/
└── mustika_run_excerpt.py  # CLI entrypoint
```

## Run Directory Structure

Runner V2 creates runs under: `runs/<excerpt_id>/<run_id>/`

```
runs/
└── <excerpt_id>/
    └── <run_id>/
        ├── command.txt                    # CLI command for reproducibility
        ├── env_allowlist.txt              # Redacted environment variables
        ├── manifest.json                  # Run metadata (for indexer)
        ├── logs/
        │   └── run.log                    # Run log with header
        ├── inputs/
        │   ├── english.txt                # English source
        │   └── rough_nl.txt              # Rough Dutch translation
        ├── outputs/
        │   ├── annotator_primary.json     # Main structured output
        │   ├── challenger_primary.json    # Challenger output
        │   ├── crew_provisional.json      # Consolidated output
        │   ├── final.txt                  # Final text (for validator)
        │   └── review_notes.md            # Review template
        └── eval/
            └── output_contract_checks.txt # Validator report
```

## Usage

### Basic Command

```bash
cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"

python3 scripts/mustika_run_excerpt.py \
    --excerpt-id sayur_052_066 \
    --excerpt-source data/origineel/hoofdstuk1.txt \
    --excerpt-version v1 \
    --english data/origineel/hoofdstuk1.txt \
    --rough-nl data/hoofdstuk1_rough_nl_dummy.txt
```

### With Custom Run ID

```bash
python3 scripts/mustika_run_excerpt.py \
    --excerpt-id sayur_052_066 \
    --excerpt-source data/origineel/hoofdstuk1.txt \
    --excerpt-version v1 \
    --run-id RUN_SAYUR_CASE01_001 \
    --english data/origineel/hoofdstuk1.txt \
    --rough-nl data/hoofdstuk1_rough_nl_dummy.txt
```

## Workflow

1. **Pre-flight Validation**: Checks required metadata, generates run_id if missing
2. **Create Run Directory**: Creates `runs/<excerpt_id>/<run_id>/` structure
3. **Write Log Header**: Logs excerpt metadata, run_id, timestamp, status
4. **Save Inputs**: Copies input files to `inputs/` directory
5. **Run Pipeline**: Calls `test_multi_agent_fidelity.run_pipeline()`
6. **Create Output Files**: Generates JSON outputs with embedded metadata
7. **Run Validator**: Calls `sandbox/tools/phase8_output_contract_validator.sh`
8. **Create Manifest**: Writes `manifest.json` for indexer compatibility
9. **Update Log Status**: Final status (COMPLETED, GATED, or FAILED)

## Output Files

### annotator_primary.json
Main structured output from annotation/editing pass:
```json
{
  "excerpt_id": "sayur_052_066",
  "excerpt_source": "data/origineel/hoofdstuk1.txt",
  "excerpt_version": "v1",
  "run_id": "RUN_SAYUR_001",
  "output_type": "annotator_primary",
  "main_text": "...",
  "remarks": "...",
  "created_at": "2026-01-09T12:00:00"
}
```

### challenger_primary.json
Challenger output (placeholder in current pipeline):
```json
{
  "excerpt_id": "...",
  "output_type": "challenger_primary",
  "issues": [],
  ...
}
```

### crew_provisional.json
Consolidated provisional output combining annotator and challenger:
```json
{
  "excerpt_id": "...",
  "output_type": "crew_provisional",
  "main_text": "...",
  "remarks": "...",
  "annotator_output": {...},
  "challenger_output": {...},
  ...
}
```

## Integration with Existing Systems

### Indexer
- Indexer uses `RunLayoutAdapter` to scan both Runner V2 and Phase-8/9 layouts
- All runs appear in `indices/run_index.json` with normalized schema
- UI can display runs from all layouts

### Validator
- Runner calls `sandbox/tools/phase8_output_contract_validator.sh` after outputs created
- Validator report written to `eval/output_contract_checks.txt`
- Validator status (PASS/FAIL) determines run status (COMPLETED/GATED)

### UI
- UI reads from `runs/` directory (via indexer)
- Run details available via `GET /runs/{run_id}` API endpoint
- Validator reports visible in Run Detail view

## Pre-flight Validation

Runner stops immediately if:
- `excerpt_id` is missing
- `excerpt_source` is missing
- `excerpt_version` is missing
- `run_id` contains invalid characters (if provided)

**No model calls are made** until validation passes.

## Log Format

Log header format:
```
mode: excerpt-aware
excerpt_id: sayur_052_066
excerpt_source: data/origineel/hoofdstuk1.txt
excerpt_version: v1
run_id: RUN_SAYUR_001
started_at: 2026-01-09T12:00:00
status: RUNNING

---
```

## Status Values

- `PENDING`: Initial state
- `RUNNING`: Pipeline executing
- `COMPLETED`: Pipeline succeeded, validator passed
- `GATED`: Pipeline succeeded, validator failed (blocking gate)
- `FAILED`: Pipeline failed or error occurred

## Model Configuration

Currently uses Ollama/Mistral via `mustikarasa_agents.py`.

Future: Support config file for model selection:
```json
{
  "type": "ollama_mistral",
  "base_url": "http://localhost:11434",
  "model": "ollama/mistral",
  "temperature": 0.3
}
```

## Testing

Run tests:
```bash
cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
python3 -m pytest tests/runner_v2/ -v
```

Tests verify:
- Pre-flight validation stops on missing metadata
- Run directory structure created
- Required output files created
- Manifest created
- Indexer adapter scans both layouts

## Constraints

- ✅ Does not write to `canonical/`
- ✅ Does not modify closures
- ✅ No auto-promotion
- ✅ Uses existing validator scripts
- ✅ Aligns with UI expectations

## Code References

- **`src/runner_v2/runner.py`**: Core runner logic
  - `validate_preflight()`: Pre-flight validation
  - `run()`: Main workflow execution
  - `create_output_files()`: Generate JSON outputs
  - `run_validator()`: Call validator script

- **`src/runner_v2/run_layout_adapter.py`**: Layout normalization
  - `scan_runner_v2_layout()`: Scan Runner V2 structure
  - `scan_phase8_layout()`: Scan Phase-8 structure
  - `scan_all()`: Scan all layouts

- **`scripts/mustika_run_excerpt.py`**: CLI entrypoint

- **`indexer.py`**: Updated to use `RunLayoutAdapter` for dual layout support
