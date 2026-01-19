# Troubleshooting Runbook — Mustika Rasa Human UI

## Common Issues

### Backend Won't Start

**Symptoms**: `python3 api_server.py` fails or port already in use.

**Diagnosis**:
```bash
# Check if port 8000 is in use
lsof -i :8010

# Or try starting and check error message
python3 api_server.py
```

**Solutions**:
1. **Port in use**: Kill the process using port 8000:
   ```bash
   lsof -ti:8010 | xargs kill -9
   ```

2. **Missing dependencies**: Install requirements:
   ```bash
   cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
   pip3 install -r requirements-ui.txt
   ```

3. **Python path issues**: Use full path:
   ```bash
   /usr/bin/python3 api_server.py
   ```

4. **Module import error**: Ensure you're in the correct directory:
   ```bash
   cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
   python3 api_server.py
   ```

### Frontend Won't Start

**Symptoms**: `npm run dev` fails or port already in use.

**Diagnosis**:
```bash
# Check if port 5173 is in use
lsof -i :5173

# Check Node.js version
node --version  # Should be 18+

# Check npm
npm --version
```

**Solutions**:
1. **Port in use**: Kill the process:
   ```bash
   lsof -ti:5173 | xargs kill -9
   ```

2. **Missing dependencies**: Install:
   ```bash
   cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy/ui"
   npm install
   ```

3. **Node version**: Update Node.js if version < 18.

4. **Permission errors**: Check directory permissions:
   ```bash
   ls -la ui/
   ```

### Empty Inbox

**Symptoms**: UI shows empty inbox or "No items found".

**Diagnosis**:
1. Check if indices exist:
   ```bash
   ls -la "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy/indices/"
   ```

2. Check if source data exists:
   ```bash
   ls -la runs/
   ls -la proposals/
   ls -la closures/
   ```

**Solutions**:
1. **No indices**: Run indexer:
   ```bash
   cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
   python3 indexer.py
   ```

2. **Or use UI**: Click "Reindex" button in Dashboard.

3. **No source data**: Indices will be empty if no runs/proposals/closures exist. This is expected for new installations.

### API Errors in Browser Console

**Symptoms**: `Failed to fetch` or `404 Not Found` errors in browser console.

**Diagnosis**:
1. Check backend is running:
   ```bash
   curl http://127.0.0.1:8010/
   ```

2. Check CORS: Backend should allow `localhost:5173`.

3. Check API endpoint exists (see `API_CONTRACT.md`).

**Solutions**:
1. **Backend not running**: Start backend (see "Backend Won't Start" above).

2. **CORS error**: Ensure backend CORS allows `http://localhost:5173` (configured in `api_server.py` line 26).

3. **404 on endpoint**: Check endpoint path matches `API_CONTRACT.md`.

4. **Network error**: Check firewall/antivirus blocking localhost connections.

### Closure Creation Fails

**Symptoms**: Error when submitting closure form.

**Diagnosis**:
1. Check browser console for error message.
2. Check backend terminal for error.
3. Check proposal exists:
   ```bash
   ls -la "proposals/{proposal_id}"
   ```

**Solutions**:
1. **Validation error**: Ensure:
   - `decision_type` is selected
   - `rationale` is at least 10 characters
   - `sign_off` checkbox is checked

2. **Proposal not found**: Ensure proposal directory exists in `proposals/`.

3. **Closure already exists**: Check if `closures/{closure_id}/closure.json` exists. Closures are immutable.

4. **Permission error**: Check filesystem permissions:
   ```bash
   ls -la closures/
   ls -la proposals/{proposal_id}/
   ```

### Indexer Errors

**Symptoms**: `python3 indexer.py` fails or produces errors.

**Diagnosis**:
```bash
cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
python3 indexer.py --base-path .
```

**Solutions**:
1. **Missing directories**: Indexer creates `indices/` automatically. Other directories should exist (may be empty).

2. **Permission errors**: Check write permissions:
   ```bash
   ls -la indices/
   ```

3. **Invalid JSON**: If source JSON files are corrupted, indexer will skip them (graceful degradation). Check source files:
   ```bash
   python3 -m json.tool runs/{run_id}/manifest.json
   ```

4. **Path issues**: Use absolute path:
   ```bash
   python3 indexer.py --base-path "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
   ```

### Frontend Build Errors

**Symptoms**: `npm run build` fails.

**Diagnosis**:
```bash
cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy/ui"
npm run build
```

**Solutions**:
1. **TypeScript errors**: Check `tsconfig.json` and fix type errors.

2. **Missing dependencies**: Reinstall:
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

3. **Vite errors**: Check `vite.config.ts` for configuration issues.

## Debugging Commands

### Check Backend Status
```bash
curl http://127.0.0.1:8010/
```

### Check Inbox Index
```bash
cat "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy/indices/inbox_index.json" | python3 -m json.tool
```

### Check Audit Log
```bash
tail -f "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy/audit/api_actions.log"
```

### Manual Reindex
```bash
cd "/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
python3 indexer.py
```

### Check Process Status
```bash
# Backend
ps aux | grep api_server

# Frontend (Vite)
ps aux | grep vite
```

## Log Locations

- **Backend logs**: Terminal output (stdout/stderr)
- **Frontend logs**: Browser console (F12)
- **Audit logs**: `audit/api_actions.log`
- **Run logs**: `runs/{run_id}/logs/*.log` (if created by pipeline)

## Getting Help

1. Check this runbook first.
2. Check `API_CONTRACT.md` for API details.
3. Check `ARCHITECTURE_MVP.md` for system overview.
4. Check `KNOWN_ISSUES_AND_TODO.md` for known limitations.
5. Review source code:
   - `api_server.py` for backend logic
   - `indexer.py` for indexing logic
   - `ui/src/` for frontend code

## Code References

Main source files:

- **`indexer.py`**: Filesystem scanner
  - `build_inbox_index()`: Builds inbox items from runs/proposals/closures
  - `reindex()`: Generates all JSON indices (inbox_index, run_index, proposal_index, closure_index)
  - `main()`: CLI entry point for manual indexing

- **`api_server.py`**: FastAPI backend
  - `GET /inbox`, `GET /runs/{id}`, `GET /proposals/{id}`, `POST /closures`, `POST /reindex`: API endpoints
  - `create_closure()`: Closure creation with immutability check
  - Error handling: HTTPException for 400/404/422/500 responses

- **`ui/src/api.ts`**: API client
  - `API_BASE = '/api'`: Base URL configuration
  - Error handling: Throws errors on failed API calls

- **`ui/src/components/Dashboard.tsx`**: Error state handling and retry logic
- **`ui/src/components/Inbox.tsx`**: Error state handling
- **`ui/src/components/ClosureComposer.tsx`**: Form validation and error display
