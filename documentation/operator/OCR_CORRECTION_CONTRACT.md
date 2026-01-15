# OCR Correction Contract

## Status
Normatief en bindend.

## Scope
- Read-only bronlaag: `runtime/data/ingest/page_sources/`
- Corrected output: `runtime/data/ingest/page_ocr_corrected/`

## Allowed READ
- `runtime/data/ingest/page_sources/png/<page_id>.png`
- `runtime/data/ingest/page_sources/ocr_txt/<page_id>.txt`
- `runtime/data/ingest/page_sources/ocr_tsv/<page_id>.tsv`

## Allowed WRITE
- Alleen naar `runtime/data/ingest/page_ocr_corrected/**`

## Required per-page corrected file
- `runtime/data/ingest/page_ocr_corrected/pages/<page_id>.txt`

## Required per-page provenance manifest
- `runtime/data/ingest/page_ocr_corrected/manifests/<page_id>.json`
- Schema (STRICT):
```
{
  "page_id": "...",
  "sources": {
    "png": "runtime/data/ingest/page_sources/png/<page_id>.png",
    "ocr_txt": "runtime/data/ingest/page_sources/ocr_txt/<page_id>.txt",
    "ocr_tsv": "runtime/data/ingest/page_sources/ocr_tsv/<page_id>.tsv"
  },
  "corrected_at": "<ISO-8601>",
  "corrected_by": "<agent_or_operator_id>",
  "method": "manual correction | re-ocr | hybrid",
  "notes": "<short, optional>"
}
```

## Validator rules (structure only)
- Missing corrected TXT or missing manifest for a page ⇒ FAIL for that page.

