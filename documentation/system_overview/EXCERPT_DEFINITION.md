# Excerpt Definition (Facts Only)

This document defines the excerpt concept as an object in the current repository,
based solely on observed artifacts and registries. It does not assign IDs or enforce mappings.

---

## What an excerpt IS

An excerpt is a bounded, referenced text unit used for runs and review in this repo.
Evidence of excerpts exists as:
- run metadata (`excerpt_id`, `excerpt_source`, `excerpt_version`) in run manifests and indices,
- excerpt-labeled ranges in `EXCERPT_MAP.md` (e.g., SAJUR-A/SAJUR-B line ranges in `canonical_concat.txt`).

An excerpt is therefore a *referenced slice* of a source text, identified by explicit metadata
or by a documented line-range within a canonical text view.

---

## What an excerpt is NOT

- It is not a recipe block (RB) or source block (BLK).
- It is not a chapter.
- It is not a page range by default.
- It is not equivalent to a run (runs are executions *about* an excerpt).
- It is not canon by itself; it is a reference unit for processing and review.

---

## Relation to RB / BLK / SAJUR

Observed relationships in the repo:
- SAJUR-A and SAJUR-B are excerpt-labeled ranges tied to `canonical_concat.txt`.
- RB/BLK are structural segments with page ranges (from `recipe_block_manifest.tsv`).
- No authoritative mapping exists between excerpts (SAJUR-*/run excerpt_ids) and RB/BLK.

Therefore:
- Excerpt labels (e.g., SAJUR-A) are currently *independent* of RB/BLK segmentation.
- Any alignment between excerpts and RB/BLK would require explicit mapping artifacts, which are not present.

---

## Evidence sources

- `documentation/system_overview/SEGMENT_REGISTRY.md`
- `documentation/system_overview/BOOK_STRUCTURE_FACTS.md`
- `runtime/indices/run_index.json`
- `runtime/data/source_imports/sayur_groente_001/EXCERPT_MAP.md`
