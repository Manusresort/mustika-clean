# Migration Closeout Note — Mustika Rasa Clean Runtime

MIGRATION STATUS: ✅ DONE

De migratie is afgerond omdat de indexer counts > 0 laten zien én zowel de API (localhost:8010) als de UI-proxy (127.0.0.1:5173/api)
HTTP 200 teruggeven.

## Scope

Wat is gemigreerd

- Runtime state: runs/, proposals/, closures/, audit/
- Entrypoints en scripts voor runtime (API/UI/indexer)
- UI + Vite proxy configuratie

Niet gemigreerd / niet onderdeel

- Canonical governance: blijft read-only
- Geen wijzigingen aan policy/invariants in canon

## Evidence (compact)

- Counts na reindex:
    - runs: 8
    - proposals: 9
    - closures: 6
    - inbox items: 5
- API endpoints:
    - http://localhost:8010/health => 200
    - http://localhost:8010/inbox => 200 (5 items)
- UI proxy endpoints:
    - http://127.0.0.1:5173/api/health => 200
    - http://127.0.0.1:5173/api/inbox => 200
- Inbox toont 5 proposal_* items met review_required

## Operational commands (for humans)

- runtime/scripts/reindex_runtime.sh
- runtime/scripts/dev_start_api.sh
- runtime/scripts/dev_start_ui.sh
- runtime/scripts/dev_up.sh
- runtime/scripts/dev_down.sh

API port

- API_PORT env var (default: 8010)

## Belangrijke configuratiewijzigingen

- API draait op 8010 (niet 8000)
- runtime/ui/vite.config.ts proxy target => http://localhost:8010
- runtime/scripts/dev_start_api.sh gebruikt --host ::1 --port 8010 (IPv6 loopback)
- runtime/scripts/dev_start_ui.sh gebruikt --host 0.0.0.0 --port 5173

## Safe-to-commit vs Never-commit

Safe-to-commit

- runtime/scripts/dev_start_api.sh
- runtime/scripts/dev_start_ui.sh
- runtime/scripts/reindex_runtime.sh
- runtime/scripts/dev_up.sh
- runtime/scripts/dev_down.sh
- runtime/ui/vite.config.ts

Never commit

- runtime/.venv/
- runtime/ui/node_modules/
- runtime/ui/dist/
- runtime/runs/
- runtime/proposals/
- runtime/closures/
- runtime/indices/
- runtime/audit/*.log
- runtime/audit/*.pid

## Git hygiene recommendation

- Commit niet runtime_migrate_full/ en runtime_migrate_strict/.
- Verplaats naar runtime/audit/ als referentie, of verwijder na verificatie.

### .gitignore snippet

# Runtime state (never commit)
runtime/.venv/
runtime/ui/node_modules/
runtime/ui/dist/
runtime/runs/
runtime/proposals/
runtime/closures/
runtime/indices/
runtime/audit/*.log
runtime/audit/*.pid
runtime_migrate_full/
runtime_migrate_strict/

## Next steps

- Voer een extra review uit op de 5 proposals in inbox.
- Bevestig dat review_required items consistent verdwijnen na closure.
- Maak een korte operator runbook-update (start/stop + reindex).
