# Run Layout Adapter (fact-first)

## Purpose
Normalizes multiple run layouts into a single `RunSummary` schema for indexing/UI use. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)

## Normalized schema (RunSummary.to_dict)
Fields emitted by `RunSummary.to_dict()`:
- `run_id`: run identifier. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- `excerpt_id`: excerpt identifier (Runner V2), `null` for Phase-8/9. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- `status`: derived status (`completed`, `failed`, `gated`). (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- `created_at`: run directory mtime (ISO). (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- `validator_status`: `PASS`/`FAIL` parsed from validator report. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- `blocking_gates`: boolean gate indicator. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- `gate_count`: count of gates (Phase-8/9 uses 0 or 1). (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- `signal_count`: currently 0 (placeholder in adapter). (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- `has_incident`: log-based incident flag. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- `manifest`: parsed `manifest.json` (Runner V2) or `command.txt` metadata (Phase-8/9). (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- `layout_type`: `runner_v2`, `phase8`, or `phase9`. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)

## Supported layouts & scanning behavior

### 1) Runner V2 layout
- Path: `runs/<excerpt_id>/<run_id>/` (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- Scan: `scan_runner_v2_layout` iterates `runs/*/*` without prefix filter. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- Read: `_read_runner_v2_run` reads `manifest.json`, `eval/output_contract_checks.txt`, `logs/run.log`. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- Manifest creation in runner: `create_manifest_json` writes `manifest.json` with output files list. (evidence: `runtime/src/runner_v2/runner.py`)

### 2) Phase-8 layout
- Path: `sandbox/phase8_runs/P8_RUN_*` (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- Scan: `scan_phase8_layout` filters directory names starting with `P8_RUN_` and sorts by mtime desc. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- Read: `_read_phase8_run` parses `eval/output_contract_checks.txt`, `logs/run.log`, and optional `command.txt`. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)

### 3) Phase-9 layout
- Path: `sandbox/phase9_runs/P9_RUN_*` (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- Scan: `scan_all` iterates `phase9_runs`, filters `P9_RUN_`, and sorts by mtime desc. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- Read: Phase-9 uses the Phase-8 read logic (`_read_phase8_run`), then sets `layout_type="phase9"`. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)

## Selection rules (prefix filters + sorting)
- Runner V2: no prefix filter in adapter; any directory under `runs/<excerpt_id>/` is scanned. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- Phase-8: requires name prefix `P8_RUN_`, sorted by `mtime desc`. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)
- Phase-9: requires name prefix `P9_RUN_`, sorted by `mtime desc`. (evidence: `runtime/src/runner_v2/run_layout_adapter.py`)

## Evidence pointers
- Adapter code: `runtime/src/runner_v2/run_layout_adapter.py`
- Runner manifest writer: `runtime/src/runner_v2/runner.py`
- Indexer uses adapter: `runtime/indexer.py`
