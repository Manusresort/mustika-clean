# Runner V2 — Created and Modified Files

## Created Files

### Core Runner Implementation
- `src/runner_v2/__init__.py` - Package init
- `src/runner_v2/runner.py` - Core runner logic (preflight, pipeline execution, output generation)
- `src/runner_v2/llm_client.py` - Model-agnostic LLM interface (placeholder for future backends)
- `src/runner_v2/run_layout_adapter.py` - Adapter that normalizes Runner V2 and Phase-8/9 layouts

### CLI Entrypoint
- `scripts/mustika_run_excerpt.py` - CLI entrypoint script (executable)

### Tests
- `tests/runner_v2/__init__.py` - Test package init
- `tests/runner_v2/test_runner_v2.py` - Unit tests for runner (preflight, directory creation, output files, manifest)
- `tests/runner_v2/test_indexer_adapter.py` - Tests for layout adapter (scanning both layouts)

### Documentation
- `docs/implementation/RUNNER_V2_INVENTORY.md` - Inventory of existing filesystem and tools
- `docs/implementation/RUNNER_V2.md` - Complete Runner V2 documentation
- `docs/implementation/RUNNER_V2_FILES.md` - This file (file listing)

## Modified Files

### Indexer
- `indexer.py` - Updated to use `RunLayoutAdapter` for dual layout support
  - Imports `RunLayoutAdapter` from `src/runner_v2/run_layout_adapter.py`
  - `scan_runs()` now uses adapter if available, falls back to original logic
  - Supports both `runs/<excerpt_id>/<run_id>/` (Runner V2) and `sandbox/phase8_runs/` (Phase-8) layouts

### Documentation
- `docs/implementation/README_QUICKSTART.md` - Added "Running an Excerpt End-to-End" section with exact commands

## File Structure Summary

```
codex cli project repo copy/
├── src/
│   └── runner_v2/
│       ├── __init__.py
│       ├── runner.py
│       ├── llm_client.py
│       └── run_layout_adapter.py
├── scripts/
│   └── mustika_run_excerpt.py
├── tests/
│   └── runner_v2/
│       ├── __init__.py
│       ├── test_runner_v2.py
│       └── test_indexer_adapter.py
├── docs/
│   └── implementation/
│       ├── RUNNER_V2_INVENTORY.md
│       ├── RUNNER_V2.md
│       └── RUNNER_V2_FILES.md
├── indexer.py (modified)
└── runs/ (created by runner, not in repo)
    └── <excerpt_id>/
        └── <run_id>/
            ├── command.txt
            ├── env_allowlist.txt
            ├── manifest.json
            ├── logs/
            ├── inputs/
            ├── outputs/
            └── eval/
```

## Integration Points

### Existing Systems Used
- `test_multi_agent_fidelity.py` - Pipeline execution (3-phase: Translation → Readability → Fidelity)
- `sandbox/tools/phase8_output_contract_validator.sh` - Output contract validation
- `indexer.py` - Filesystem scanning (updated to support dual layouts)
- `api_server.py` - API backend (no changes, works with new run structure via indexer)
- `ui/` - Frontend (no changes, works with new run structure via indexer)

### No Changes To
- `canonical/` - Read-only, never written to
- `closures/` - Immutable closure system unchanged
- `proposals/` - Proposal system unchanged
- `audit/` - Audit logging unchanged
- Validator scripts - Used as-is, no modifications

## Dependencies

### Python Dependencies
- `crewai` - For LLM agents (already in project)
- `pathlib` - Standard library
- `json` - Standard library
- `subprocess` - Standard library
- `datetime` - Standard library

### External Tools
- `ollama` - Must be running with `mistral` model
- `ripgrep` (rg) - Required by validator script

### No New Dependencies
- Uses existing `mustikarasa_agents.py` and `test_multi_agent_fidelity.py`
- No new Python packages required

## Testing

Run all tests:
```bash
cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
python3 -m pytest tests/runner_v2/ -v
```

Or run individual test files:
```bash
python3 tests/runner_v2/test_runner_v2.py
python3 tests/runner_v2/test_indexer_adapter.py
```

## Next Steps

1. **Test on real excerpt**: Run on `sayur_052_066` or `lobak_034_048` excerpts
2. **Verify indexer integration**: Run `python3 indexer.py` and check `indices/run_index.json` includes Runner V2 runs
3. **Verify UI integration**: Check runs appear in UI after reindex
4. **Add challenger agent**: Currently placeholder, integrate actual challenger logic
5. **Model config support**: Implement config file parsing in `llm_client.py`
