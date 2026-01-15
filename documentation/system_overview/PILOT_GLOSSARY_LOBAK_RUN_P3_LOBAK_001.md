# Pilot Run — Glossary Lobak (P3_LOBAK_001)

**Status:** EXPERIMENTAL — NOT FOR PUBLICATION

## 1. Source Passage
7. Lobak

Djuga disini jang dimakan umbinja, jang berwarna putih. Ada
jang pandjang-pandjang tetapi ada pula jang bundar2 besar. Kalau
membeli supaja dipilih jang besar-besar, karena tidak berserat, dan
djangan dibeli jang warnanja hidjau. Lobak dapat dimakan mentah,
rasanja getir karena alliin, kalau dimasak menjadi manis. Baik untuk
membantjarkan air kentjing. Daun lobak suka dimakan djuga.

## 2. Translation Output (EXPERIMENTAL)
- status: EXPERIMENTAL
Lobak

Here the edible part is the white root. Some are long, while others
are large and round. When buying, choose the larger ones because
they are not fibrous, and do not buy those with green coloring.
Lobak can be eaten raw; it tastes bitter because of alliin, but when
cooked it becomes sweet. It is good for increasing urine flow.
Lobak leaves are also often eaten.

## 3. Readability Output (EXPERIMENTAL)
- status: EXPERIMENTAL
Lobak

The edible part here is the white root. Some are long and slender,
others large and round. When buying, pick the larger ones because
they are less fibrous, and avoid those that are greenish. Lobak can
be eaten raw; it tastes bitter because of alliin, but becomes sweet
when cooked. It is said to help increase urine flow. Lobak leaves are
also commonly eaten.

Note: “lobak” remains as-is to avoid premature terminology decisions.

## 4. Fidelity Notes
- “lobak” plausibly maps to multiple English equivalents (radish, white radish, daikon).
- Risk: generic “radish” could mislead readers about the specific variety.
- Soft-stop would be triggered due to glossary-sensitive ambiguity.
- No correction applied; ambiguity is only signaled.

## 5. Glossary Proposals (proposal-only)
[GLOSSARY_PROPOSALS]
Terms:
  - term: lobak
    proposed_equivalents:
      - "lobak (white radish)"
      - "daikon (white radish)"
      - "retain original + gloss: lobak (white radish)"
    notes: risk of confusion with generic 'radish'; context suggests white, elongated root.
Meta:
  lifecycle_stage: proposal
  source: P3_LOBAK_001
  lifecycle_reference: docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md
[/GLOSSARY_PROPOSALS]

## 6. Research Notes (simulated)
[RESEARCH_REPORT]
Scope: historical and culinary use of "lobak" in Indonesian context.
Summary: Lobak is commonly used to refer to white radish/daikon; red radish is typically
referred to as “radish” in English but is a distinct culinary reference.
RelevantSources: RESEARCH_GLOSSARY materials; historical recipe context references.
KeyInsights: lobak ~ white radish/daikon; radijs ~ red radish.
OpenQuestions: spelling standardization; consistent gloss across chapters.
Recommendations: decision deferred to Human Gate in glossary lifecycle.
[/RESEARCH_REPORT]

## 7. Methodology Log (excerpt)
[METHODOLOGY_LOG]
Event: P3_LOBAK_001 pilot run.
Focus: terminology ambiguity for "lobak".
Result: ambiguity detected; proposals logged; decision explicitly deferred.
[/METHODOLOGY_LOG]

## 8. Failure Notebook (required)
[FAILURE_NOTEBOOK]
CaseID: P3_LOBAK_001_F1
Expected: glossary-sensitive term should not be silently fixed.
Observed: model tended to prefer generic "radish".
Mitigation: glossary proposals + research report + explicit decision deferral.
RiskIfUnnoticed: reader may assume generic red radish instead of the intended white radish/daikon.
Lesson: culturally loaded plant terms must go through glossary lifecycle.
[/FAILURE_NOTEBOOK]

## 9. Pilot Outcome (no decisions)
- ambiguity_detected: YES
- soft_stop_triggered: YES (documentary)
- governance_agents_involved: Glossary, Research, Methodology
- decision_deferred: YES
- rollback_possible: YES (documentary; no canonical sources modified)

EXPERIMENTAL — NOT FOR PUBLICATION. This pilot documents governance behavior only.
