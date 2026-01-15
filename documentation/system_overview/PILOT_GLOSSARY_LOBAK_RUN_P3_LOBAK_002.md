# Pilot Run — Glossary Lobak (P3_LOBAK_002)

**Status:** EXPERIMENTAL — P3_LOBAK_002 — NOT FOR PUBLICATION

## 1. Source Passage (sandbox copy)
7. Lobak

Djuga disini jang dimakan umbinja, jang berwarna putih. Ada
jang pandjang-pandjang tetapi ada pula jang bundar2 besar. Kalau
membeli supaja dipilih jang besar-besar, karena tidak berserat, dan
djangan dibeli jang warnanja hidjau. Lobak dapat dimakan mentah,
rasanja getir karena alliin, kalau dimasak menjadi manis. Baik untuk
membantjarkan air kentjing. Daun lobak suka dimakan djuga.

## 2. Translation Quality Output (EXPERIMENTAL)
- status: EXPERIMENTAL — P3_LOBAK_002
- override applied: prefer literal/standard translation "radish"

Radish

Here the edible part is the white root. Some are long, while others
are large and round. When buying, choose the larger ones because
they are not fibrous, and do not buy those with green coloring.
Radish can be eaten raw; it tastes bitter because of alliin, but when
cooked it becomes sweet. It is good for increasing urine flow.
Radish leaves are also often eaten.

Rationale: “radish” is a literal/common equivalent; ambiguity noted for lifecycle review.
Uncertainties: lobak may refer specifically to white radish/daikon.

## 3. Readability Output (EXPERIMENTAL)
- status: EXPERIMENTAL — P3_LOBAK_002
- override applied: prefer clarity "white radish / daikon"

White radish / daikon

The edible part here is the white root. Some are long and slender,
others large and round. When buying, pick the larger ones because
they are less fibrous, and avoid those that are greenish. White radish
/ daikon can be eaten raw; it tastes bitter because of alliin, but
becomes sweet when cooked. It is said to help increase urine flow.
The leaves are also commonly eaten.

Readability tradeoff: improved clarity for general readers, but terminology decision is deferred.

## 4. Fidelity Notes (TERMINOLOGY_RISK)
- Divergence detected: Translation uses “radish”; Readability uses “white radish / daikon”.
- Risk: potential mismatch of specific variety (generic vs white/daikon).
- Classification: TERMINOLOGY_RISK.
- Action: soft‑stop triggered (documentary); no resolution applied.
- Health claims are preserved as historical statements; no rewrites.

## 5. Glossary Proposals (proposal-only)
[GLOSSARY_PROPOSALS]
Terms:
  - term: lobak
    proposed_equivalents:
      - "radish"
      - "white radish / daikon"
      - "retain original + gloss: lobak (white radish)"
    notes: divergence detected between translation/readability; ambiguity requires lifecycle review.
    Meta:
      lifecycle_stage: proposal
      source: P3_LOBAK_002
      risk_classification: TERMINOLOGY_RISK
      lifecycle_reference: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md
      status: EXPERIMENTAL — P3_LOBAK_002
[/GLOSSARY_PROPOSALS]

## 6. Research Notes (EVIDENCE ONLY)
[RESEARCH_REPORT]
Scope: historical and culinary context for "lobak".
Summary: "lobak" is commonly used for white radish/daikon in Indonesian contexts; generic
"radish" can be ambiguous in English.
RelevantSources: RESEARCH_GLOSSARY materials; historical recipe context notes.
KeyInsights: lobak ~ white radish/daikon; red radish is a different reference.
OpenQuestions: consistent glossing across chapters; spelling standardization.
Recommendations: decision deferred to Human Gate; proposal-only.
Status: EXPERIMENTAL — P3_LOBAK_002
[/RESEARCH_REPORT]

## 7. Methodology Log (excerpt)
[METHODOLOGY_LOG]
Event: P3_LOBAK_002 pilot run.
Focus: forced divergence between "radish" vs "white radish / daikon".
Why this matters: This pilot intentionally creates a terminology conflict to test whether the workflow documents ambiguity without collapsing it into a premature decision.
Result: ambiguity detected; governance-stop triggered; no final glossary outcome.
Phase-3 constraint: final glossary outcomes prohibited.
Status: EXPERIMENTAL — P3_LOBAK_002
[/METHODOLOGY_LOG]

## 8. Failure Notebook (expected test failure)
[FAILURE_NOTEBOOK]
CaseID: P3_LOBAK_002_F1
Severity: LOW (learning objective)
Expected: divergence should trigger governance handling without a decision.
Observed: agents produced conflicting terms by design.
Mitigation: proposal-only glossary entry + research evidence + explicit deferral.
Reversibility: no canonical sources modified; rollback is trivial (discard pilot artefacts).
Status: EXPERIMENTAL — P3_LOBAK_002
[/FAILURE_NOTEBOOK]

## 9. Pilot Workspace Diff (sandbox)
All changes are confined to this pilot artefact file; no source text or glossary files modified.
Rollback instruction: delete `docs/PILOT_GLOSSARY_LOBAK_RUN_P3_LOBAK_002.md` to revert pilot outputs.

## Methodology Insight (Phase-3 — Proposal)
**Insight:** Chat-window excerpts can drift from the actual repository state.  
**Implication:** Pilot review steps should reference the canonical stored artefact, not pasted excerpts.  
**Status:** PROPOSAL — pending governance review (do not enforce yet).  
**Provenance:** P3_LOBAK_002.

## Consolidation Summary (Phase-3)
**What we validated:** the system correctly surfaced a terminology conflict without collapsing it into a decision.  
**What failed safely:** chat excerpts diverged from canonical files; ambiguity remained visible; rollback preserved.  
**Governance behavior:** soft-stop + governance-stop worked as documentary stops; decision deferred.  
**Key insight:** verify against stored artefacts, not chat excerpts (Proposal).  
**Status:** CONSOLIDATED — learning captured, no decisions promoted.

## 10. Pilot Outcome (no decisions)
- ambiguity_detected: YES
- soft_stop_triggered: YES (documentary)
- governance_stop_triggered: YES (documentary)
- governance_agents_involved: Glossary, Research, Methodology
- decision_deferred: YES
- rollback_possible: YES (no canonical changes; delete pilot artefact)

EXPERIMENTAL — P3_LOBAK_002 — NOT FOR PUBLICATION.
