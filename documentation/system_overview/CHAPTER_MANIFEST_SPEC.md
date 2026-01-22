# Chapter Manifest Specification

## 0. Discovery overview

- **Existing chapter/excerpt model** is documentary-only: `CHAPTER_EXCERPT_RELATION_MODEL.md` states that chapters may hold many excerpts, that each excerpt belongs to exactly one chapter, that sequences follow source order, and that no concrete IDs or artifacts exist yet (`CHAPTER_EXCERPT_RELATION_MODEL.md:1-40`).  
- **Search results for “chapter manifest”** returned no manifest files under `mustika-rasa-clean/runtime` or `mustika-rasa-clean/documentation` (commands `rg ... chapter_manifest` and `find ... | rg chapter manifest` produced no hits). **NOT FOUND**: there is no runtime chapter manifest yet.

## 1. AS-IS chapter mapping context

- The documentary model enforces cardinality and sequencing rules for chapter↔excerpt pairs but explicitly states no runtime mapping artifacts exist (`CHAPTER_EXCERPT_RELATION_MODEL.md:5-33`).  
- Run bundles already emit `manifest.json` with excerpt metadata (`runner.py`: `create_manifest` populates excerpt_id/source/version/run_id plus inputs/outputs; `runner.py:305-327`), yet these remain excerpt-centric.
- The indexer stores those manifest blobs inside `run_index.json` along with run status, gates, signals, and `manifest` (mustika-rasa-clean/runtime/indexer.py:128-223,528-545). These ingredients provide the only current chapter-aware signals.

## 2. Target manifest vision (NEW)

- **Intent**: define a filesystem-first `chapter_manifest.json` catalog derived from runs/excerpts/proposals/closures so every chapter export references concrete provenance, status, and closure evidence.  
- **Location**: `mustika-rasa-clean/runtime/manifests/chapter_manifest.json` (derived artifact, not hand-edited).  
- **Minimal JSON shape (NEW)**:
  ```json
  {
    "generated_at": "<timestamp>",
    "chapter_id": "CH-001",
    "plan": [
      {
        "segment_id": "SEG-001",
        "excerpt_id": "sayur_052_066",
        "run_id": "RUN_sayur_202601",
        "status": "reviewed",
        "proposal_id": "P-BOOK-CH1",
        "closure_id": "CL-202601-book-CH1",
        "checksum": "<sha256>",
        "output_formats": ["docx","pdf"],
        "evidence_paths": ["runs/.../manifest.json","proposals/.../status.json"]
      }
    ]
  }
  ```
- Each entry reuses RunnerV2 metadata (`excerpt_id`, `run_id`, `manifest`) and closure/proposal outcomes from the API – the chapter manifest therefore ties excerpts, proposals, closures, and outputs together.

## 3. Indexer DoD (NEW)

- The indexer must ingest `runs/<excerpt>/<run>/manifest.json`, `proposals/<id>/status.json`, and closures, then emit `chapter_manifest.json` and update `indices/run_index.json` with a `chapter_plan` reference for each run.  
- DoD: `chapter_manifest.json` is regenerated via `POST /reindex`, contains at least one `chapter_id` entry per active book, and its version/`generated_at` value is recorded in `audit/api_actions.log`.  
- DoD: manifest generation is deterministic (reuses `_write_index_json_if_changed` semantics) and marked as derived-only (never hand-edit).  

## 4. AS-IS linkage summary

- Runner metadata already captures the necessary excerpt identifiers (`runner.py:24-135`).  
- The API yields runs, proposals, closures, and reindex points (`api_server.py:415-762`).  
- The chapter manifest simply aggregates these provenances in a book-level catalogue, enabling downstream book builds and governance without inventing new runtime contracts beyond derived outputs.
