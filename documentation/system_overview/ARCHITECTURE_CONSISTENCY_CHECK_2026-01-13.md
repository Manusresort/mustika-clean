# Architecture Consistency Check — 2026-01-13

## 1. Scope & method (read-only)
Checked docs, code, and filesystem with read-only inspection. Evidence is file-based (path + snippet/line range).

## 2. Principle constraints extracted (with sources)
- Filesystem-first; indices are derived:
  - `documentation/system_overview/GOVERNANCE.md`:
    - “indices zijn afgeleid van filesystem”
- Closures immutable / canonical read-only / no auto-promotion:
  - `documentation/system_overview/GOVERNANCE.md`:
    - “closures muteren (closures zijn immutable)”
    - “schrijven naar `canonical/`”
    - “auto-promotion naar canonical”
  - `documentation/system_overview/PROJECT_STATE_PACK.md`:
    - “`runtime/canonical/` is read-only (no direct writes).”
    - “No auto-promotion to canonical.”
- page_sources read-only:
  - `documentation/operator/AGENT_USAGE_CONTRACT_PAGE_SOURCES.md`:
    - “`page_sources` is read-only voor agents.”
    - “Geen writes, overwrites, renames of deletes in `page_sources`.”

## 3. Checks performed
- Code scan for writes/paths: `runtime/indexer.py`, `runtime/api_server.py`, `runtime/scripts/`, `runtime/src/`
  - `rg -n "canonical" ...`
  - `rg -n "page_sources" ...`
- Presence checks:
  - `runtime/data/ingest/page_sources/**` + `PROVENANCE.json`
  - `runtime/data/ingest/page_ocr_corrected/**`
  - `runtime/data/ingest/definitive_source/**`
  - `runtime/indices/page_sources_coverage_index.json`
- Doc cross-consistency:
  - `documentation/system_overview/PROJECT_STATE_PACK.md`
  - `documentation/system_overview/REPO_INVENTORY.md`
  - `documentation/system_overview/STATE_EVIDENCE_MAP.md`

## 4. Findings

### Confirmed consistent
- Indices are derived and written to `runtime/indices/`:
  - `runtime/indexer.py` writes:
    - `(self.indices_path / "run_index.json").write_text(...)` (lines 575–577)
    - `(self.indices_path / "proposal_index.json").write_text(...)` (lines 581–583)
    - `(self.indices_path / "closure_index.json").write_text(...)` (lines 586–587)
    - `(self.indices_path / "inbox_index.json").write_text(...)` (lines 591–592)
    - `(self.indices_path / "review_queue_index.json").write_text(...)` (lines 597–598)
    - `(self.indices_path / "page_sources_coverage_index.json").write_text(...)` (lines 602–603)
- canonical read-only enforcement in API:
  - `runtime/api_server.py`:
    - `check_canonical_write()` (lines 152–159) denies writes under `canonical/`.
- page_sources used for derived coverage only:
  - `runtime/indexer.py`:
    - `page_sources_path = .../data/ingest/page_sources` (lines 511–514)
    - writes derived coverage index (lines 602–603).
- Filesystem presence matches docs for ingest layers:
  - `runtime/data/ingest/page_sources/` with `png/`, `ocr_txt/`, `ocr_tsv/`, `PROVENANCE.json`
  - `runtime/data/ingest/page_ocr_corrected/` (structure only)
  - `runtime/data/ingest/definitive_source/` (structure only)
- Doc cross-consistency for ingest:
  - `PROJECT_STATE_PACK.md`, `REPO_INVENTORY.md`, and `STATE_EVIDENCE_MAP.md` all reference
    `runtime/data/ingest/page_sources/` and `runtime/indices/page_sources_coverage_index.json`.

### Potential inconsistencies
- STOP log required by doc, but not present on disk:
  - `documentation/system_overview/AGENT_RUNTIME_SAFETY_BRIDGE.md`:
    - “`stop.log` must always capture STOP events.”
  - Filesystem scan found no `runtime/**/stop.log`.
  - Evidence: `find runtime -name "stop.log"` returned no matches.

### Confirmed violations
- None observed in scanned paths.

## 5. Evidence index (paths referenced)
- `documentation/system_overview/GOVERNANCE.md`
- `documentation/system_overview/PROJECT_STATE_PACK.md`
- `documentation/system_overview/STATE_EVIDENCE_MAP.md`
- `documentation/system_overview/REPO_INVENTORY.md`
- `documentation/operator/AGENT_USAGE_CONTRACT_PAGE_SOURCES.md`
- `runtime/indexer.py`
- `runtime/api_server.py`
- `runtime/data/ingest/page_sources/`
- `runtime/data/ingest/page_ocr_corrected/`
- `runtime/data/ingest/definitive_source/`
- `runtime/indices/page_sources_coverage_index.json`
