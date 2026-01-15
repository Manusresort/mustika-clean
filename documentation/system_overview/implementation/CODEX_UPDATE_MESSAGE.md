# Codex Update Message — Mustika Rasa Human UI MVP

## What is Implemented (MVP)

✅ **Backend (FastAPI)**
- Filesystem-based storage (runs/, proposals/, closures/, indices/, audit/)
- Indexer that scans filesystem and generates JSON indices
- API endpoints: GET /inbox, GET /runs/{id}, GET /proposals/{id}, GET /closures/{id}, POST /closures, POST /reindex
- Policy enforcement: closure immutability, required fields validation, audit logging

✅ **Frontend (React + TypeScript)**
- Dashboard with inbox counters
- Inbox with filtering (all/review/gate/closure/incident)
- Review Pack Viewer for proposals
- Closure Composer form with validation
- Run Detail viewer

✅ **Governance Features**
- Immutable closures (400 error on duplicate creation)
- Proposal status updates on closure creation
- Append-only audit log (audit/api_actions.log)
- Deterministic UI state from filesystem artefacts

## What is Proven Working

✅ **End-to-End Closure Workflow**
1. Create proposal with `required_closure.json` → triggers inbox item
2. Run indexer → `closure_needed=1` in inbox_index.json
3. Create closure via UI → closure.json created, proposal status updated
4. Immutability enforced → second creation attempt returns 400 error
5. Audit log entry created → `audit/api_actions.log` contains closure metadata

**Verified test**: See `README_QUICKSTART.md` section "Verified End-to-End Test"

## How to Run It

**Backend:**
```bash
cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
pip3 install -r requirements-ui.txt
python3 api_server.py
```
→ http://127.0.0.1:8000

**Frontend:**
```bash
cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy/ui"
npm install
npm run dev
```
→ http://localhost:5173

**Generate indices:**
```bash
cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
python3 indexer.py
```

## Current Limitations

⚠️ **Inbox Review Items**
- Proposals with status "open" or "in_review" only appear in inbox if they have `required_closure.json`
- Proposals without closure requirement don't show up in "Review Required" count
- **Workaround**: Add `required_closure.json` to proposals that need review

⚠️ **500 Error on First Submit**
- First closure creation may show 500 error in UI even though closure is successfully created
- Closure file exists, proposal status updated, audit log written
- **Root cause**: Reindex triggered after closure creation may fail or timeout
- **Workaround**: Refresh inbox after creation; closure will appear

⚠️ **Other Known Issues** (see `KNOWN_ISSUES_AND_TODO.md`)
- No CLI validator integration (placeholder)
- No user authentication (uses `getpass.getuser()`)
- No Promote Wizard (Phase 2)
- No Canonical Viewer (Phase 2)
- No pagination for large lists
- Evidence paths not validated

## Next Recommended Steps

### Immediate Fixes (High Priority)

1. **Fix Inbox Review Items**
   - Update `indexer.py` `build_inbox_index()` to include all proposals with status "open"/"in_review" in "Review Required", not just those with `required_closure.json`
   - Ensure proposals without closure requirement still appear in inbox

2. **Improve 500 Error Handling**
   - Make reindex after closure creation non-blocking (async or background task)
   - Return success response before reindex completes
   - Add error handling for reindex failures that doesn't fail closure creation
   - Or: remove automatic reindex, require manual reindex via UI button

3. **Better Error Messages**
   - Return more descriptive error messages from API
   - Show closure creation success even if reindex fails
   - Display warning if reindex needed manually

### Phase 2 Features

4. **Promote Wizard**
   - UI component for selecting artefacts to promote
   - API endpoint `POST /cli/promote`
   - Validation of output contracts
   - Atomic promotion with rollback

5. **Canonical Viewer**
   - Read-only view of canonical content
   - Provenance trail display
   - Related decisions list

6. **Observability Dashboards**
   - Signal frequency charts
   - Gate frequency charts
   - Run health metrics

## Code References

- **`indexer.py`**: `build_inbox_index()` (line 227-326) - inbox item generation
- **`api_server.py`**: `create_closure()` (line 358-427) - closure creation with reindex trigger
- **`ui/src/components/ClosureComposer.tsx`**: Form submission and error handling

## Documentation

All implementation docs in `docs/implementation/`:
- `README_QUICKSTART.md` - Setup and verified e2e test
- `ARCHITECTURE_MVP.md` - System architecture
- `GOVERNANCE_GUARANTEES.md` - Policy enforcement
- `API_CONTRACT.md` - API endpoints
- `ARTEFACTS_AND_STORAGE.md` - File structure
- `RUNBOOK_TROUBLESHOOTING.md` - Troubleshooting guide
- `KNOWN_ISSUES_AND_TODO.md` - Known issues and Phase 2 TODO
