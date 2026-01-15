# Regression Harness Spec — Run Outputs (M5)

## A) Purpose
Dit document specificeert een minimale regression harness voor run outputs/eval in de filesystem-first runtime, met audit-rapportage onder `runtime/audit/` zonder mutatie van runs, proposals, closures of canonical. (Bron: documentation/reports/BACKLOG_GITHUB_ISSUES.md:122-127; documentation/system_overview/GOVERNANCE.md:10-13, 44-47)

## B) Inputs
- Twee run directories (baseline en candidate), beide verwijzend naar `runtime/runs/<excerpt_id>/<RUN_id>/`. (Bron: documentation/system_overview/PROJECT_STATE_PACK.md:85-95)
- Selectie gebeurt via CLI‑argumenten (paden), geen inference uit indices. (Design choice for this item)

## C) Comparable contract
Comparable als en alleen als:
1) Beide run directories bestaan; en
2) Beide bevatten `outputs/` en `eval/` directories (mag leeg zijn). (Bron: documentation/operator/RUNBOOK.md:90-92; documentation/system_overview/PROJECT_STATE_PACK.md:85-95)

INCONCLUSIVE als een van deze voorwaarden niet voldoet, met expliciete reden in het rapport. (Design choice for this item)

## D) Scope contract
Vergelijk uitsluitend:
- `outputs/` bestanden
- `eval/` bestanden  
(Bron: documentation/operator/RUNBOOK.md:90-92; documentation/system_overview/PROJECT_STATE_PACK.md:89-95)

Bestandslisting is top-level only (geen recursive traversal). (Design choice for this item)

Geen vergelijking van `inputs/`, `logs/`, `manifest.json` of indices. (Design choice for this item)

## E) Comparison method
- JSON‑bestanden: canonical JSON dump (sort_keys, compacte separators) en byte‑vergelijking. (Design choice for this item)
- Tekstbestanden: unified diff, met max 200 regels output in rapport; volledige diff in aparte file. (Design choice for this item)
- Overige bestanden: byte‑vergelijking met “binary differs” notitie. (Design choice for this item)

Motivatie: repo bevat zowel JSON als tekst outputs (outputs/*.json, outputs/final.txt, eval/output_contract_checks.txt). (Bron: documentation/system_overview/PROJECT_STATE_PACK.md:89-95)

## F) Status semantics
- PASS: Comparable en geen verschillen in outputs/ of eval/. (Design choice for this item)
- FAIL: Comparable en 1+ verschillen (added/removed/changed). (Design choice for this item)
- INCONCLUSIVE: Niet‑comparable (ontbrekende directories of niet‑bestaande run). (Design choice for this item)

## G) Audit artefact
- Pad‑conventie (default):  
  `runtime/audit/regression_runs/<baseline_run_id>__vs__<candidate_run_id>/regression_report.md` (Design choice for this item)
- Rapport bevat minimaal: timestamp, baseline path, candidate path, status, comparable‑reden, scope, samenvatting verschillen, diff‑pointers. (Design choice for this item)
- Geen overschrijving van bestaande audits; bij conflict wordt een timestamp‑suffix gebruikt. (Design choice for this item)
- Eén rapport per regression-run; dit dekt “reports saved per batch run”. (Bron: documentation/reports/CRITICAL_PATH_NEXT_8_WEEKS.md:90-98)

## H) Non-goals
- Geen writes naar `canonical/`. (Bron: documentation/system_overview/GOVERNANCE.md:10-13, 44-47)
- Geen mutatie van closures. (Bron: documentation/system_overview/GOVERNANCE.md:11-12, 36-40)
- Geen auto‑promotion naar canonical. (Bron: documentation/system_overview/GOVERNANCE.md:12-13; documentation/system_overview/PROJECT_STATE_PACK.md:67-68)
- Geen UI‑wijzigingen. (Design choice for this item)
- Index‑regressie (indices snapshot/compare) valt buiten deze harness; scope is outputs/eval. (Bron: documentation/operator/RUNBOOK.md:95-100; documentation/system_overview/AS_BUILT_ARCH.md:56-66)

## I) Reproducibility notes
Het rapport logt:
- baseline path, candidate path
- run_id’s (afgeleid uit directorynamen)
- timestamp (UTC)
- gebruikte vergelijkingsmethode per bestand
- overzicht van verschillen en locatie van diff‑artefacten  
zodat dezelfde vergelijking herhaalbaar is zonder mutatie van runs. (Design choice for this item)
