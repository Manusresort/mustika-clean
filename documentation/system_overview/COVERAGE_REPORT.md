# Coverage Report (Facts Only)

Scope: `runtime/data/origineel/`, `runtime/data/source_imports/`,
`documentation/legacy_imports/`, `runtime/runs/`.

## Counts by origin

### CLEAN_REPO
- PHYSICAL_SOURCE: 0
- OCR_TEXT: 0
- CANONICAL_TEXT_VIEW: 0
- SEGMENT (RB/BLK): 0
- SEGMENT (non-RB/BLK): 0
- SEGMENT with runs: 0 (no mapping between segments and runtime runs)
- Chapter inputs: 1 (`hoofdstuk1.txt`)
- Runs (excerpt IDs): 1 (`sayur_052_066`)
- Run bundles: 3

### CLEAN_REPO_STAGED
- PHYSICAL_SOURCE: 1215 (1214 images + 1 PDF)
- OCR_TEXT: 2428 (1214 OCR txt + 1214 OCR tsv)
- CANONICAL_TEXT_VIEW: 1215 (1214 page-*.txt + canonical_concat.txt)
- SEGMENT (RB): 28
- SEGMENT (BLK): 28
- SEGMENT (non-RB/BLK): 2 (SAJUR-A, SAJUR-B)
- Chapter inputs: 16 (`hoofdstuk_*.txt` in agentic inputs)

## Gaps / ID-sprongen
- No explicit mapping between hoofdstuk_* inputs and RB/BLK or SAJUR-* segments.
- No explicit mapping between run excerpt IDs (e.g., sayur_052_066) and RB/BLK or SAJUR-*.

## Not demonstrable
- Book-level coverage completeness (no chapter registry).
- Chapter to segment alignment as an authoritative mapping.
- Segment to run alignment.

## Layer status
- STRUCTURALLY_COMPLETE

## INTENTIONAL_GAPS (not blockers)
- Chapter -> excerpt mapping (no mapping artifact found).
- Excerpt registry population (registry is empty by design).
- Excerpt versions in data (policy-only).
- Chapter -> segment alignment (no mapping artifact found).

## Duplicate reconciliation checklist (facts only)

Duplicate candidates identified:
- None within scanned clean repo paths.

Available signals to test equivalence (not executed here):
- Filenames and page counts
- Ledger manifests (page_to_recipe_block.tsv, recipe_block_manifest.tsv)
- Timestamps (mtime)
- Checksums (if generated)

Missing signals:
- Explicit manifest linking duplicated sets
- Verified checksums for all staged sources

Unknowns:
- Whether any duplicates exist outside scanned paths

No reconciliation performed.
