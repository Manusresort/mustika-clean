# Definitive Source Build Contract

## Status
Normatief en bindend.

## Scope
- Builds from corrected pages under `runtime/data/ingest/page_ocr_corrected/pages`

## Build artifact locations
- `runtime/data/ingest/definitive_source/builds/<BUILD_ID>/source_nl.txt`
- `runtime/data/ingest/definitive_source/manifests/<BUILD_ID>.json`

## Build manifest schema (STRICT)
```
{
  "build_id": "<BUILD_ID>",
  "built_at": "<ISO-8601>",
  "identity_rule": "page_id filename stem",
  "input_root": "runtime/data/ingest/page_ocr_corrected/pages",
  "pages_included": ["page-0001", "..."],
  "gaps": ["page-0XYZ", "..."],
  "output": "runtime/data/ingest/definitive_source/builds/<BUILD_ID>/source_nl.txt"
}
```

## Non-goals
- No translation
- No canonical publishing
- No segmentation assumptions

