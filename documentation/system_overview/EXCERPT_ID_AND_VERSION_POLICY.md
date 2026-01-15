# Excerpt ID and Version Policy (Documentary Only)

Status: DOCUMENTARY POLICY (no runtime implications)

This document records how excerpt identity and versioning are intended to be
interpreted for registry use. It does not create or populate any excerpt IDs.

---

## Identity: When it is the same excerpt

An excerpt is treated as the same excerpt when all of the following are stable:
- `source_chapter_id(s)` (same chapter scope),
- `segment_refs` (same RB/BLK/SAJUR references, if any),
- the referenced text span (same source path and range definition).

If the source path and range are unchanged, the excerpt remains the same
even if it is re-run multiple times.

---

## Versioning: When a new version exists

A new version of the same excerpt exists when the excerpt identity remains
unchanged but the referenced text span changes in-place, such as:
- adjusted line range within the same source file,
- updated OCR text for the same page range,
- corrected boundaries that still target the same excerpt scope.

Version changes should remain within the same `excerpt_id` and be tracked
via `version_group` or a version tag.

---

## New excerpt: When a new excerpt is created

A new excerpt is created when any of the identity conditions change:
- different chapter scope,
- different segment references (RB/BLK/SAJUR),
- a different source path or non-overlapping range.

In these cases, a new `excerpt_id` should be created rather than
versioning the existing one.

---

## Non-goals

- This policy does not assign IDs or version tags.
- This policy does not define runtime behavior or enforcement.
- This policy does not override existing run metadata.
