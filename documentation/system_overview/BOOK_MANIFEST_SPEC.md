# Book Manifest Specification

## 0. Discovery overview

- `rg -n "book_manifest|book manifest|boek manifest|build_manifest|export manifest|publication|canonical build|book build"` under `mustika-rasa-clean/runtime` and `mustika-rasa-clean/documentation` returns only governance/publication notes but no runtime manifest artefact, so the book manifest does not yet exist (search output contained only references such as `CHAPTER_MANIFEST_SPEC.md:50` and other policy notes). **NOT FOUND**: no book-level manifest file currently present.
- `find mustika-rasa-clean -maxdepth 10 -type f | rg -n "book|manifest|export|build"` likewise lists only docs/venv artefacts and manifest_p5.yaml but no actual book manifest artifact. **NOT FOUND** for a runtime book manifest.

## 1. AS-IS building blocks

- Run bundles follow the `runs/<excerpt_id>/<RUN_...>` layout with `outputs/`, `eval/`, `logs/`, `manifest.json` and helper files (`runner.py:72-327`; ADR-001 states that layout is canonical for MVP runs).  
- Proposals, closures and reindex flows already exist: proposals contain `proposal.md` + `status.json`, closures are immutable `closures/<id>/closure.json`, and `POST /closures` updates proposals and triggers reindex (api_server.py:550-762; GOVERNANCE.md:59-66; ADR-002 documents limited governance enforcement).  
- Derived indices principle: `indexer.py` reads manifests and writes `run_index.json`, `proposal_index.json`, `closure_index.json`, `inbox_index.json` via `_write_index_json_if_changed`, so all runtime metadata is derived-only and reindexable (`indexer.py:33-545`; GOVERNANCE.md:78-82).  
- Chapter manifest spec documents the desired chapter↔excerpt mapping and explicitly notes no runtime artifact yet even though the spec aggregates provenance (`CHAPTER_MANIFEST_SPEC.md:5-50`). Thus the book manifest must build on that foundation rather than creating a parallel model.

## 2. Target book manifest vision (NEW)

- **Intent**: provide a filesystem-first book manifest that aggregates chapter manifests, closure requirements and export artifacts so a published build can trace every contribution back to runs/proposals/closures (extends CHAPTER_MANIFEST_SPEC.md:10-50).  
- **Location**: derived-only file at `mustika-rasa-clean/runtime/manifests/book_manifest.json` (NEW, never hand-edited).  
- **Derived-only definition**: book manifest is overwritten only by the indexer/reindex workflow; manual edits violate the derived-only policy noted for indices (`GOVERNANCE.md:78-82`).  
- **Minimal JSON shape (NEW)**:
  ```json
  {
    "generated_at": "2026-01-22T13:00:00Z",
    "book_id": "BOOK-MUSTIKA-2026",
    "title": "Mustika Rasa",
    "chapters": [
      {
        "chapter_id": "CH-001",
        "plan": "runtime/manifests/chapter_manifest_CH-001.json"
      }
    ],
    "required_closures": [
      "CL-20260121-BOOK-APPROVAL"
    ],
    "status": "reviewable",
    "exports": [
      {
        "format": "pdf",
        "path": "runtime/exports/BOOK-MUSTIKA-2026/BUILD-001/BOOK-MUSTIKA-2026.pdf",
        "sha256": "<checksum>",
        "built_at": "2026-01-22T12:45:00Z",
        "tool_versions": {
          "runner": "v2",
          "exporter": "<tool> <version>"
        },
        "input_closure_ids": [
          "CL-20260121-BOOK-APPROVAL"
        ]
      }
    ],
    "provenance": [
      "runs/CH-001/RUN_.../manifest.json",
      "proposals/P-BOOK-CH1/status.json",
      "closures/CL-20260121-BOOK-APPROVAL/closure.json"
    ]
  }
  ```

## 3. Build manifest (NEW)

- Each export run writes `runtime/exports/<book_id>/<build_id>/build_manifest.json` containing `format`, `path`, checksums, tool versions, and source closure IDs.  
- This build manifest links to `book_manifest.exports`; the book manifest entry references the export manifest record so QA can compare `sha256` + tool versions (NEW relation).

## 4. Indexer DoD (NEW)

- The indexer must ingest `chapter_manifest.json`, runs, proposals, and closures, then emit `book_manifest.json` during `POST /reindex` and log the new `generated_at` via `audit/api_actions.log` (api_server.py:215-277; the API already logs reindex actions in `ensure_audit_log`).  
- `_write_index_json_if_changed` ensures deterministic writes and prevents needless diffs (`indexer.py:33-50`).  
- Reindex regenerates book manifest each time the underlying data change; users trigger it via the existing `reindex` endpoint (api_server.py:215-277).
- Book status is a rollup; excerpt-level statuses remain owned by the chapter manifest entries so the book manifest stays derived while chapter/segment progress stays granular.

## 5. Book closure definition (NEW)

- A book closure is `status = approved/locked` in `book_manifest.json` once all `required_closures` exist (`closures/<id>/closure.json`, `api_server.py:692-762`).  
- Until then the book `status` stays `draft` or `reviewable`; exported builds require the book closure to reach `locked/exported` status, mirroring human-gate semantics from `GOVERNANCE.md:33-55`.

## 6. Implementation roadmap (NEW)

1. **Stabilize**: extend the indexer to compute `book_manifest.json` using chapter manifests + closure/proposal metadata and add QA checks in `qa_full_system.sh`.  
2. **Editorialize**: add reviewer dashboards referencing `book_manifest.status` and require `required_closures` before changing status to `locked`.  
3. **Book-ready**: implement the `build_manifest.json` workflow and tie exported artifacts to `book_manifest.exports` for deterministic audits.

## Evidence index

- `mustika-rasa-clean/documentation/system_overview/CHAPTER_MANIFEST_SPEC.md`: existing chapter manifest intent and discovery note.  
- `mustika-rasa-clean/documentation/system_overview/CHAPTER_EXCERPT_RELATION_MODEL.md`: documentary chapter↔excerpt cardinality (CHAPTER_MANIFEST_SPEC references).  
- `mustika-rasa-clean/documentation/adrs/ADR-001-run-bundle-layout.md`: run bundle layout evidence.  
- `mustika-rasa-clean/documentation/adrs/ADR-002-governance-layer-enforcement.md`: governance enforcement scope (closure immutability, canonical write).  
- `mustika-rasa-clean/runtime/src/runner_v2/runner.py`: run bundle manifest creation (`create_manifest`).  
- `mustika-rasa-clean/runtime/api_server.py`: API for runs/proposals/closures/reindex + audit logging.  
- `mustika-rasa-clean/runtime/indexer.py`: derived indices, deterministic writes, manifest ingestion.  
- `mustika-rasa-clean/runtime/ui/src/api.ts`: UI view of runs/proposals/closures guiding book manifest usage.
