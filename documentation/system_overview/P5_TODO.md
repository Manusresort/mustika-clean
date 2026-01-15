# Phase-5 TODO — Preparation & Consolidation (Draft)

Purpose: Phase-5 is about consolidating what works, choosing what to
improve, and preparing for a production-ready workflow.  
It is NOT a new sandbox and NOT a build-everything phase.

All items here are candidates, not commitments.

---

## 1) Agent behaviour: definiëren wat "goed genoeg" is

Goal: Describe when agents are helpful instead of confusing.

- [ ] Define criteria for when Challenger feedback is considered useful
      (vs. noise or bias).
- [ ] Define criteria for acceptable Annotator "reason" fields
      (grounded in visible text, not speculation).
- [ ] Document a few concrete examples of:
      - “OK” behaviour
      - “Overreach”
      - “Clearly out of bounds”

Output: short guideline; no new tooling.

---

## 2) Consolidatie van Phase-4 inzichten

Goal: Capture what we learned so Phase-5 does not repeat Phase-4.

- [ ] Summarise key sandbox patterns (±1 page).
- [ ] List known biases (e.g. translation-expectation) with status:
      “monitor only, do not fix in Phase-5 unless explicitly decided.”
- [ ] Explicitly mark which issues are intentionally NOT solved
      in Phase-5 (to avoid scope creep).

Output: consolidation note, not a new policy layer.

---

## 3) Geselecteerde pilots (max. 1–2 tegelijk)

Goal: Choose a few focused experiments that actually test value.

Candidate pilots:

- [ ] Challenger clarity pilot
      (Does small wording change reduce false positives without hiding bias?)
- [ ] Annotator reason-discipline pilot
      (Do stricter reason rules improve human interpretation?)
- [ ] Meta-summary helper pilot
      (Faster multi-log understanding for humans, no auto-decisions.)

Constraint: At most 2 pilots active at once.  
Others stay “later / maybe”.

---

## 4) Voorbereiding richting productie-workflow

Goal: Avoid chaos when scaling up later (Phase-6).

- [ ] Identify which decisions MUST go through Human Gate
      (e.g. meaning, cultural impact, safety).
- [ ] Identify which tasks agents may “prepare” but never decide
      (flagging, summarising, proposing).
- [ ] Review rollback paths for larger runs
      (are current plans enough if we scale up?).

Output: a short “production guardrails” note.

---

## 5) Repo & document-architectuur opschonen (jouw punt)

Goal: Make the repo navigable for humans and Codex, without
rewriting history.

- [ ] Classify existing docs into:
      - canonical (project overview, key governance, core workflow)
      - sandbox/runtime logs
      - archival/historical experiments
- [ ] Update or create a central map:
      - docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md
      - and/or docs/total_project.md
      so they reflect the current structure.
- [ ] Create a simple machine-readable manifest, e.g.:
      - docs/manifest_p5.yaml or docs/manifest_p5.json
      listing key doc groups:
      {
        "governance": [...],
        "crew_prompts": [...],
        "phase4_logs": [...],
        "meta_docs": [...]
      }
- [ ] Update CODEX_META_PROMPT.md to reference this manifest/map,
      so future Codex sessions always know “where what lives”
      instead of guessing paths.

Constraint: No heavy reorganisation. Prefer adding structure on top
of what exists over moving lots of files around.

---

## 6) Publicatievooruitblik (boek als eindproduct)

Goal: Keep the real end goal visible: a published, responsible edition.

- [ ] Draft the high-level structure of the eventual book workflow:
      Source → Scholarly → Public → Accountability note.
- [ ] Identify safe “first chapters” or sections to run through a
      future production pipeline.
- [ ] Note what Phase-5 pilots need to prove for this to be realistic.

---

## Status & scope

- Phase-5 remains governed and reversible.
- No learning agents or automation without explicit approval.
- This TODO is a planning aid, not a binding contract.
