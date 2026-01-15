# Micropilot — Provisional Translation Discipline (Phase 5)

Purpose:
testen of agents en crews veilig voorlopige vertaalbeslissingen
kunnen nemen volgens het lifecycle-model, zonder onnodige escalatie.

Scope:
- SAYUR excerpts (2–3 korte passages)
- annotator → challenger → meta/crew
- output = logs/JSON (proposal-only)

Lifecycle focus:
CANDIDATE → CREW_PROVISIONAL → (optioneel) READY_FOR_HUMAN_REVIEW

Success indicators:
- meeste beslissingen eindigen in CREW_PROVISIONAL
- escalaties alleen bij risk/publication/impasse
- rationale compact en tekst-gebaseerd
- alle lifecycle-velden aanwezig

Non-goals (Phase 5):
- model tuning
- policy-wijziging
- publicatie-voorbereiding

Risks to observe (not fix):
- translation-expectation bias
- defensieve over-escalatie
- te stellig “closure” gedrag

Outputs:
- run log
- decision lifecycle trace
- short analyst note

End document.
