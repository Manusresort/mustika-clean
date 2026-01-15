# Chapter ↔ Excerpt Relation Model (Documentary Only)

Status: DOCUMENTARY MODEL (no mappings assigned)

This document defines the formal relationship between chapters and excerpts
without assigning any concrete chapter or excerpt IDs.

---

## Cardinality

- One chapter can contain zero, one, or many excerpts.
- One excerpt belongs to exactly one chapter in the intended model.
- Cross-chapter excerpts are not supported in this model.

---

## Sequence

- Excerpts within a chapter are ordered.
- Sequence is defined by their position in the chapter source text
  (e.g., line ranges or segment order).
- Sequence indices are chapter-scoped and do not imply global ordering.

---

## Coverage (Completeness)

- A chapter is fully covered when all intended excerpt spans
  for that chapter are enumerated in the excerpt registry.
- Coverage is a structural measure only; it does not imply
  any processing or review has occurred.

---

## Non-goals

- No chapter or excerpt IDs are assigned here.
- No runtime behavior is implied.
- No mapping artifacts are created by this document.
