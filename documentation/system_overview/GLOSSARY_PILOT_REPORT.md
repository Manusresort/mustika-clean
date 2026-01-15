# Glossary / Research Pilot Report

## Scope
Deze pilot toetst de Glossary + Research workflow op een kleine, veilige set termen
met mogelijke interpretatie-verschillen. We beperken ons tot drie termen uit een
enkele extractbron en nemen geen definitieve beslissingen.

Pilot-termen:
- aron
- arem arem
- temu kuntji

Herkomst (contextbron):
- Extract: `RB-0001` uit `/Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/ARCHIVE/HANDOVERS/2025-12-22_135929_step4_step5/step5_extraction/extracts/RB-0001.txt`

## Method
De Glossary Agent levert proposal-only voorstellen in het format [GLOSSARY_PROPOSALS].
De Research Agent levert context in het format [RESEARCH_REPORT].
Lifecycle-stappen zijn documentair doorlopen tot en met Risk Review, waarna
de Human Gate expliciet is uitgesteld (pilot-only).

## Term Analyses

### Term: aron
Raw context:
- "ARON (Tengger)"
- "Bahan: djagung putih pipilan"
- "Aron ini tahan disimpan 1 minggu lamanja..."

[GLOSSARY_PROPOSALS]
Terms:
  - term: aron
    proposed_equivalents: ["steamed corn preparation", "corn-based Tengger dish"]
    notes: Based on local dish name (Tengger) with white corn ingredients and steaming steps.
Meta:
  source: RB-0001 extract (page-0186)
  lifecycle_stage: proposal
[/GLOSSARY_PROPOSALS]

[RESEARCH_REPORT]
Scope: Local dish term "aron" from Tengger context in RB-0001.
Summary: The extract frames "aron" as a named dish with white corn, soaked, hulled, pounded, and steamed.
RelevantFiles:
  - /Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/ARCHIVE/HANDOVERS/2025-12-22_135929_step4_step5/step5_extraction/extracts/RB-0001.txt
  - docs/RESEARCH_GLOSSARY.md
KeyInsights:
  - Term appears as a dish name with regional marker "(Tengger)".
  - Process suggests a steamed corn staple; no explicit translation provided.
OpenQuestions:
  - Is "aron" a proper name that should remain untranslated?
  - Are there known equivalents in Indonesian culinary glossaries?
Recommendations:
  - Check referenced archive glossary sources for prior usage or definitions.
[/RESEARCH_REPORT]

Lifecycle Notes:
- Proposal: documented.
- Context: captured via extract and research summary.
- Risk Review: cultural/regional specificity may require keeping original term.
- Human Gate: Decision deferred — pilot stage only.
- Versioning: N/A until Human Gate.

Risks:
- Over-translating could erase regional specificity.
- Under-translating may reduce reader comprehension.

Deferred Decision:
Decision deferred — pilot stage only.

---

### Term: arem arem
Raw context:
- "AREM AREM"
- "Dibungkus seperti membuat lontong..."
- "AREM AREM ARON"

[GLOSSARY_PROPOSALS]
Terms:
  - term: arem arem
    proposed_equivalents: ["arem-arem (stuffed rice roll)", "rice roll similar to lontong"]
    notes: Appears as a named preparation; context compares wrapping to lontong.
Meta:
  source: RB-0001 extract (page-0186 to page-0187)
  lifecycle_stage: proposal
[/GLOSSARY_PROPOSALS]

[RESEARCH_REPORT]
Scope: Term "arem arem" in recipe context with wrapping instructions.
Summary: The extract describes a rice-based preparation wrapped like lontong, with filling.
RelevantFiles:
  - /Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/ARCHIVE/HANDOVERS/2025-12-22_135929_step4_step5/step5_extraction/extracts/RB-0001.txt
  - docs/RESEARCH_GLOSSARY.md
KeyInsights:
  - Lontong is used as an analog; the term may be better retained with a short gloss.
  - "Arem-arem" also appears as part of "AREM AREM ARON", suggesting a derived variant.
OpenQuestions:
  - Is "arem arem" standardized as "arem-arem" in modern spelling?
  - Should the glossary standardize hyphenation?
Recommendations:
  - Cross-check archive glossary files for preferred spelling and prior usage.
[/RESEARCH_REPORT]

Lifecycle Notes:
- Proposal: documented.
- Context: captured via extract and research summary.
- Risk Review: spelling/standardization may affect indexing and search.
- Human Gate: Decision deferred — pilot stage only.
- Versioning: N/A until Human Gate.

Risks:
- Inconsistent spelling may fragment glossary and index.
- Over-glossing could reduce authenticity.

Deferred Decision:
Decision deferred — pilot stage only.

---

### Term: temu kuntji
Raw context:
- "temu kuntji 2 Ibr."
- Listed under spices alongside "laos", "lombok merah", "terasi".

[GLOSSARY_PROPOSALS]
Terms:
  - term: temu kuntji
    proposed_equivalents: ["temu kunci (fingerroot)", "fingerroot (temu kunci)"]
    notes: Spice term with archaic spelling; likely standardized in modern Indonesian.
Meta:
  source: RB-0001 extract (page-0187)
  lifecycle_stage: proposal
[/GLOSSARY_PROPOSALS]

[RESEARCH_REPORT]
Scope: Spice term "temu kuntji" from ingredients list.
Summary: The term appears as a spice ingredient alongside common aromatics; spelling suggests older orthography.
RelevantFiles:
  - /Users/vwvd/Millway/AI-folder/mustika_archive/Mustikarasa 2026/ARCHIVE/HANDOVERS/2025-12-22_135929_step4_step5/step5_extraction/extracts/RB-0001.txt
  - docs/RESEARCH_GLOSSARY.md
KeyInsights:
  - The surrounding list implies a culinary spice, not a method.
  - Modern spelling may differ, which affects glossary consistency.
OpenQuestions:
  - Should the glossary retain historic spelling or normalize to modern spelling?
  - Do other chapters use the same term with different spelling?
Recommendations:
  - Scan referenced archive materials for frequency and spelling variants.
[/RESEARCH_REPORT]

Lifecycle Notes:
- Proposal: documented.
- Context: captured via extract and research summary.
- Risk Review: normalization choices affect search and reader clarity.
- Human Gate: Decision deferred — pilot stage only.
- Versioning: N/A until Human Gate.

Risks:
- Normalization may erase historical orthography.
- Retention of old spelling may confuse modern readers.

Deferred Decision:
Decision deferred — pilot stage only.

## Findings
- Terminology risk is highest where regional dish names and archaic spelling intersect.
- Ambiguity is present around whether to translate, gloss, or retain original terms.
- Reader comprehension likely benefits from short glosses, but authenticity must be preserved.
- Human review is necessary for standardization choices (spelling, hyphenation, naming).

## Recommendations (pilot level)
- Define explicit policy for handling historical spelling vs. modernized forms.
- Ensure proposals include both original term and possible gloss for reader clarity.
- Require cross-reference checks in archive glossary sources before Human Gate.

## Next Steps
- Run a Human Gate review once evidence from archive glossary sources is available.
- Decide on term retention vs. glossing strategy per term category (dish, spice, tool).
- Record final decisions via the Glossary Decision Lifecycle (no changes in this pilot).
