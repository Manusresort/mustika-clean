# Source & Structure Layer — Definition of Done (Documentary)

Status: DOCUMENTARY CHECKLIST (no planning, no roadmap)

This checklist defines when the source & structure layer is considered complete
as a documentation and evidence layer.

---

## Must exist (artifacts present)

- Physical sources staged (PDF/images) with paths recorded.
- OCR text layers staged (ocr_txt + ocr_tsv) with paths recorded.
- Canonical text views staged (page-*.txt and canonical_concat.txt).
- Segment ledgers staged (RB/BLK manifests and page-to-RB ledger).
- Chapter inputs staged (hoofdstuk_*.txt).
- Chapter registry present (formal listing of chapter inputs).
- Excerpt registry structure present (even if empty by design).
- Alignment tables present (page->segment, segment->text).

---

## Must be demonstrable (evidence-based)

- Counts for physical sources, OCR, canonical views, segments, and chapters are measurable.
- Page->RB mapping is demonstrable from a ledger.
- Segment->text references are demonstrable (line ranges or page ranges).
- Excerpt metadata is demonstrable in run manifests (excerpt_id/source/version).

---

## Explicitly allowed UNKNOWN

- Chapter -> segment mapping (if no authoritative ledger exists).
- Chapter -> excerpt mapping (if no registry yet).
- Excerpt -> RB/BLK alignment (until mapping is authored).
- Version/lock policy (if not declared in source materials).

---

## Non-goals (out of scope for DoD)

- No canonical decisions or publication.
- No runtime enforcement.
- No normalization or correction of source text.
- No excerpt population unless authoritative mapping exists.
