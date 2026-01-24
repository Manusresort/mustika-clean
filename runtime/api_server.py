"""
FastAPI server for Mustika Rasa Human UI
Local-only API that wraps filesystem operations and CLI calls.
"""

import json
import subprocess
import logging
import traceback
import sys
from datetime import datetime, timezone
from pathlib import Path


# Ensure runtime/src is importable (filesystem-first runtime)
BASE_DIR = Path(__file__).resolve().parent
import sys
sys.path.insert(0, str(BASE_DIR / "src"))
# Ensure runtime/src is importable (filesystem-first runtime)
from typing import Dict, List, Any, Optional, Tuple
import os
import getpass

from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel, Field, validator

from indexer import Indexer


app = FastAPI(title="Mustika Rasa Human UI API", version="1.0.0")


@app.on_event("startup")
async def startup_event():
    """Log startup banner."""
    logging.info(f"Mustika API running (api_server.py) base={BASE_PATH}")

# CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Base path - should be the repo root
BASE_PATH = Path(__file__).parent.resolve()
indexer = Indexer(BASE_PATH)


def _load_book_required_closures(book_id: str) -> List[str]:
    manifest_path = BASE_PATH / "manifests" / "book_manifest.json"
    if not manifest_path.exists():
        return []
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    entry = data
    books = data.get("books")
    if isinstance(books, list):
        entry = next(
            (b for b in books if isinstance(b, dict) and b.get("book_id") == book_id),
            None,
        )
    if not isinstance(entry, dict):
        return []
    req = entry.get("required_closures") or entry.get("required_closure_ids") or []
    return [c for c in req if isinstance(c, str) and c]


def _closure_exists(closure_id: str) -> bool:
    return (BASE_PATH / "closures" / closure_id / "closure.json").exists()


# Global exception handler for StarletteHTTPException (HTTPException)
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Handle HTTPException and return JSON response."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "http_exception",
            "status_code": exc.status_code,
            "detail": exc.detail,
        }
    )


# Global exception handler for unhandled exceptions
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Handle unhandled exceptions and return JSON response."""
    # Log full traceback
    logging.exception("Unhandled exception in API")
    
    # Return JSON error response
    return JSONResponse(
        status_code=500,
        content={
            "error": "unhandled_exception",
            "message": str(exc),
        }
    )


# Pydantic models
class ClosureCreate(BaseModel):
    """Model for creating a closure."""
    proposal_id: str
    run_id: Optional[str] = None
    decision_type: str = Field(..., description="P7 decision type")
    rationale: str = Field(..., min_length=10, description="Rationale for decision")
    evidence_paths: List[str] = Field(default_factory=list)
    sign_off: bool = Field(..., description="User sign-off required")
    created_by: Optional[str] = None

    @validator("sign_off")
    def sign_off_required(cls, v):
        if not v:
            raise ValueError("Sign-off is required")
        return v


class ClosureResponse(BaseModel):
    """Response model for closure."""
    closure_id: str
    created_at: str
    proposal_id: str
    run_id: Optional[str]
    decision_type: str
    rationale: str
    evidence_paths: List[str]
    created_by: str


class InboxItem(BaseModel):
    """Model for inbox items."""
    id: str
    type: str
    title: str
    severity: str
    status: str
    age: str
    required_action: str
    proposal_id: Optional[str] = None
    run_id: Optional[str] = None


class InboxResponse(BaseModel):
    """Response model for inbox."""
    generated_at: str
    counts: Dict[str, int]
    items: List[InboxItem]

CHAPTER_MANIFEST_PATH = BASE_DIR / "manifests" / "chapter_manifest.json"
CHAPTER_REGISTRY_PATH = BASE_DIR / "indices" / "chapter_registry.json"

def _load_json_if_exists(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        logging.exception("Failed to read %s", path)
        return {}

def _build_chapter_lookup() -> Tuple[Dict[str, str], Dict[str, str], Dict[str, str]]:
    manifest = _load_json_if_exists(CHAPTER_MANIFEST_PATH)
    run_map: Dict[str, str] = {}
    proposal_map: Dict[str, str] = {}
    closure_map: Dict[str, str] = {}
    chapters = manifest.get("chapters", [])
    for chapter in chapters:
        chapter_id = chapter.get("chapter_id")
        if not chapter_id:
            continue
        for run_id in chapter.get("run_ids", []):
            if isinstance(run_id, str):
                run_map[run_id] = chapter_id
        for proposal_id in chapter.get("proposal_ids", []):
            if isinstance(proposal_id, str):
                proposal_map[proposal_id] = chapter_id
        for closure_id in chapter.get("closure_ids", []):
            if isinstance(closure_id, str):
                closure_map[closure_id] = chapter_id
    return run_map, proposal_map, closure_map

def _resolve_chapter_id(item: Dict[str, Any], run_map: Dict[str, str], proposal_map: Dict[str, str], closure_map: Dict[str, str]) -> Optional[str]:
    run_id = item.get("run_id")
    if isinstance(run_id, str) and run_id in run_map:
        return run_map[run_id]
    proposal_id = item.get("proposal_id")
    if isinstance(proposal_id, str) and proposal_id in proposal_map:
        return proposal_map[proposal_id]
    closure_id = item.get("closure_id")
    if isinstance(closure_id, str) and closure_id in closure_map:
        return closure_map[closure_id]
    return None


# Helper functions
def get_username() -> str:
    """Get current username for audit trails."""
    return getpass.getuser()


def ensure_audit_log(message: str, metadata: Dict[str, Any] = None):
    """Append to audit log."""
    audit_path = BASE_PATH / "audit"
    audit_path.mkdir(parents=True, exist_ok=True)
    
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "message": message,
        "metadata": metadata or {},
    }
    
    log_file = audit_path / "api_actions.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")


def derive_inbox_counts(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Derive counts summary from inbox items."""
    by_kind: Dict[str, int] = {}
    by_status: Dict[str, int] = {}
    for item in items:
        kind = item.get("type") or item.get("kind") or "unknown"
        status = item.get("status") or "unknown"
        by_kind[kind] = by_kind.get(kind, 0) + 1
        by_status[status] = by_status.get(status, 0) + 1
    return {
        "total": len(items),
        "by_kind": by_kind,
        "by_status": by_status,
    }


def check_canonical_write(path: Path) -> bool:
    """Check if path is within canonical/ - returns True if write should be denied."""
    canonical_path = BASE_PATH / "canonical"
    try:
        path.resolve().relative_to(canonical_path.resolve())
        return True  # Path is in canonical, deny write
    except ValueError:
        return False  # Path is not in canonical, allow


# API Endpoints

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "service": "Mustika Rasa Human UI API",
        "version": "1.0.0",
        "base_path": str(BASE_PATH),
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return JSONResponse(
        status_code=200,
        content={
            "ok": True,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "paths": {
                "base": str(BASE_PATH),
                "indices": str(BASE_PATH / "indices"),
            }
        }
    )


@app.get("/version")
async def version():
    """Version endpoint to confirm running server code."""
    indices_path = BASE_PATH / "indices"
    inbox_index_path = indices_path / "inbox_index.json"
    
    return JSONResponse(
        status_code=200,
        content={
            "name": "mustika_rasa_api",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "base_path": str(BASE_PATH),
            "has_indices": indices_path.exists() and indices_path.is_dir(),
            "inbox_index_exists": inbox_index_path.exists() and inbox_index_path.is_file(),
        }
    )


@app.post("/reindex", status_code=status.HTTP_200_OK)
async def reindex():
    """Trigger filesystem reindex via subprocess."""
    indexer_script = BASE_PATH / "indexer.py"
    
    # Check if indexer.py exists
    if not indexer_script.exists():
        return JSONResponse(
            status_code=500,
            content={
                "error": "indexer_missing",
                "message": f"indexer.py not found at {indexer_script}",
                "path": str(indexer_script),
            }
        )
    
    try:
        # Run indexer.py as subprocess
        process = subprocess.run(
            [sys.executable, str(indexer_script)],
            cwd=str(BASE_PATH),
            capture_output=True,
            text=True,
            timeout=60,
        )
        
        # Trim stdout/stderr to max ~20k chars
        max_output_length = 20000
        stdout = process.stdout[:max_output_length] if process.stdout else ""
        stderr = process.stderr[:max_output_length] if process.stderr else ""
        
        # Check which index files were generated
        indices_path = BASE_PATH / "indices"
        expected_files = [
            "run_index.json",
            "inbox_index.json",
            "proposal_index.json",
            "closure_index.json",
        ]
        generated_files = []
        for filename in expected_files:
            file_path = indices_path / filename
            if file_path.exists():
                generated_files.append(f"indices/{filename}")
        
        response = {
            "ok": process.returncode == 0,
            "exit_code": process.returncode,
            "stdout": stdout,
            "stderr": stderr,
            "generated_files": generated_files,
            "base_path_used": str(BASE_PATH),
            "timestamp": datetime.utcnow().isoformat(),
        }
        
        # Log to audit
        ensure_audit_log("Reindex triggered", {
            "exit_code": process.returncode,
            "generated_files": generated_files,
        })
        
        return JSONResponse(status_code=200, content=response)
        
    except subprocess.TimeoutExpired:
        return JSONResponse(
            status_code=500,
            content={
                "error": "reindex_timeout",
                "message": "Indexer execution exceeded 60 second timeout",
                "timeout_seconds": 60,
            }
        )
    except Exception as e:
        logging.exception("Reindex subprocess failed")
        return JSONResponse(
            status_code=500,
            content={
                "error": "reindex_exception",
                "message": str(e),
            }
        )


@app.get("/chapters")
async def get_chapters():
    """Return the chapter registry index."""
    registry = _load_json_if_exists(CHAPTER_REGISTRY_PATH)
    if not registry:
        registry = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "chapters": [],
            "unassigned": {
                "run_ids": [],
                "proposal_ids": [],
                "closure_ids": [],
            },
        }
    return JSONResponse(status_code=200, content=registry)


@app.get("/inbox")
async def get_inbox():
    """Get inbox items from index."""
    inbox_path = BASE_PATH / "indices" / "inbox_index.json"

    try:
        if not inbox_path.exists():
            return JSONResponse(
                status_code=200,
                content={
                    "generated_at": None,
                    "counts": {
                        "total": 0,
                        "by_kind": {},
                        "by_status": {},
                    },
                    "items": [],
                }
            )

        data = json.loads(inbox_path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            normalized = {
                "generated_at": None,
                "items": data,
            }
        elif isinstance(data, dict):
            normalized = {
                "generated_at": data.get("generated_at"),
                "items": data.get("items", []),
            }
        else:
            normalized = {
                "generated_at": None,
                "items": [],
            }
        run_map, proposal_map, closure_map = _build_chapter_lookup()
        for item in normalized["items"]:
            item["chapter_id"] = _resolve_chapter_id(item, run_map, proposal_map, closure_map)
        normalized_counts = derive_inbox_counts(normalized["items"])
        normalized["counts"] = normalized_counts

        return JSONResponse(status_code=200, content=normalized)

    except Exception as e:
        logging.exception("Failed to read inbox index")
        return JSONResponse(
            status_code=500,
            content={
                "error": "inbox_handler_error",
                "message": str(e),
                "path": str(inbox_path),
            }
        )


def locate_run_directory(run_id: str) -> Optional[Path]:
    """Locate run directory by run_id. Returns Path or None."""
    # Try run_index.json first
    run_index_path = BASE_PATH / "indices" / "run_index.json"
    if run_index_path.exists():
        try:
            data = json.loads(run_index_path.read_text(encoding="utf-8"))
            runs = data.get("runs", [])
            for run in runs:
                if run.get("run_id") == run_id:
                    path_str = run.get("path")
                    if path_str:
                        run_path = Path(path_str)
                        if run_path.exists() and run_path.is_dir():
                            return run_path
        except (json.JSONDecodeError, IOError, ValueError):
            pass
    
    # Fallback: scan runs/**/<run_id>/
    runs_path = BASE_PATH / "runs"
    if runs_path.exists():
        # Try nested layout: runs/<excerpt_id>/<run_id>/
        for excerpt_dir in runs_path.iterdir():
            if excerpt_dir.is_dir():
                run_path = excerpt_dir / run_id
                if run_path.exists() and run_path.is_dir():
                    return run_path
        # Try legacy layout: runs/<run_id>/
        run_path = runs_path / run_id
        if run_path.exists() and run_path.is_dir():
            return run_path
    
    return None


def read_text_file_safe(file_path: Path) -> Optional[str]:
    """Read text file safely, return None on error."""
    try:
        if file_path.exists() and file_path.is_file():
            return file_path.read_text(encoding="utf-8")
    except IOError:
        pass
    return None


def read_json_file_safe(file_path: Path, warnings: List[Dict[str, str]]) -> Optional[Any]:
    """Read JSON file safely, return None on error, add warning if parse fails."""
    try:
        if file_path.exists() and file_path.is_file():
            content = file_path.read_text(encoding="utf-8")
            return json.loads(content)
    except json.JSONDecodeError as e:
        warnings.append({
            "type": "json_parse_error",
            "file": str(file_path.relative_to(BASE_PATH)),
            "message": str(e),
        })
    except IOError:
        pass
    return None


@app.get("/runs/{run_id}")
async def get_run(run_id: str):
    """Get run details."""
    # Locate run directory
    run_path = locate_run_directory(run_id)
    if not run_path:
        return JSONResponse(
            status_code=404,
            content={
                "error": "run_not_found",
                "run_id": run_id,
            }
        )
    
    warnings = []
    
    # Read manifest
    manifest = read_json_file_safe(run_path / "manifest.json", warnings) or {}
    
    # Read validator report (try multiple candidates)
    validator_report_text = None
    validator_report_json = None
    validator_candidates = [
        run_path / "eval" / "output_contract_checks.txt",
        run_path / "validator" / "report.json",
    ]
    for candidate in validator_candidates:
        if candidate.exists():
            if candidate.suffix == ".txt":
                validator_report_text = read_text_file_safe(candidate)
                if validator_report_text:
                    break
            else:
                validator_report_json = read_json_file_safe(candidate, warnings)
                if validator_report_json:
                    break
    
    # Read gates
    gates = []
    gates_data = read_json_file_safe(run_path / "validator" / "gates.json", warnings)
    if gates_data:
        gates = gates_data.get("gates", [])
    
    # Read signals
    signals = []
    signals_data = read_json_file_safe(run_path / "signals.json", warnings)
    if signals_data:
        if isinstance(signals_data, dict) and "signals" in signals_data:
            signals = signals_data["signals"]
        elif isinstance(signals_data, list):
            signals = signals_data
    
    # Read final_text (try multiple candidates)
    final_text = None
    final_candidates = [
        run_path / "final.txt",
        run_path / "outputs" / "final.txt",
        run_path / "outputs" / "final.md",
    ]
    for candidate in final_candidates:
        final_text = read_text_file_safe(candidate)
        if final_text:
            break
    
    # Read review_notes (try multiple candidates)
    review_notes = None
    review_candidates = [
        run_path / "review_notes.md",
        run_path / "outputs" / "review_notes.md",
    ]
    for candidate in review_candidates:
        review_notes = read_text_file_safe(candidate)
        if review_notes:
            break
    
    # Read JSON outputs
    outputs = {
        "annotator_primary": read_json_file_safe(run_path / "outputs" / "annotator_primary.json", warnings),
        "challenger_primary": read_json_file_safe(run_path / "outputs" / "challenger_primary.json", warnings),
        "crew_provisional": read_json_file_safe(run_path / "outputs" / "crew_provisional.json", warnings),
    }
    
    # List output files (existing field, keep for backward compatibility)
    outputs_path = run_path / "outputs"
    output_files = []
    if outputs_path.exists():
        output_files = [
            {
                "name": f.name,
                "path": str(f.relative_to(BASE_PATH)),
                "size": f.stat().st_size,
            }
            for f in outputs_path.iterdir()
            if f.is_file()
        ]
    
    # List log files (existing field, keep for backward compatibility)
    logs_path = run_path / "logs"
    log_files = []
    if logs_path.exists():
        log_files = [
            {
                "name": f.name,
                "path": str(f.relative_to(BASE_PATH)),
                "size": f.stat().st_size,
            }
            for f in logs_path.iterdir()
            if f.is_file()
        ]
    
    # validator_report: prefer text, fallback to JSON stringified, else null
    validator_report = validator_report_text
    if not validator_report and validator_report_json:
        validator_report = json.dumps(validator_report_json, indent=2)
    
    response = {
        "run_id": run_id,
        "manifest": manifest,
        "validator_report": validator_report,
        "gates": gates,
        "signals": signals,
        "final_text": final_text,
        "review_notes": review_notes,
        "outputs": outputs,
        "output_files": output_files,
        "log_files": log_files,
    }
    
    if warnings:
        response["warnings"] = warnings
    
    return JSONResponse(status_code=200, content=response)


@app.get("/proposals/{proposal_id}")
async def get_proposal(proposal_id: str):
    """Get proposal details."""
    proposal_path = BASE_PATH / "proposals" / proposal_id
    
    if not proposal_path.exists() or not proposal_path.is_dir():
        return JSONResponse(
            status_code=404,
            content={
                "error": "proposal_not_found",
                "proposal_id": proposal_id,
            }
        )
    
    warnings = []
    
    # Read proposal.md
    proposal_md = read_text_file_safe(proposal_path / "proposal.md")
    
    # Extract title from proposal.md (first heading or first line)
    title = proposal_id
    if proposal_md:
        lines = proposal_md.split("\n")
        for line in lines:
            line_stripped = line.strip()
            if line_stripped and not line_stripped.startswith("#"):
                title = line_stripped[:100]  # Limit length
                break
            elif line_stripped.startswith("#"):
                title = line_stripped.lstrip("#").strip()[:100]
                break
    
    # Read status
    status_data = read_json_file_safe(proposal_path / "status.json", warnings)
    if not status_data:
        status_data = {"status": "open"}
    
    # Read gates
    gates_data = read_json_file_safe(proposal_path / "gates.json", warnings)
    gates = gates_data.get("gates", []) if gates_data else None
    
    # Check required closure
    required_closure = (proposal_path / "required_closure.json").exists()
    
    # List top-level files
    files = []
    if proposal_path.exists():
        files = [
            f.name
            for f in proposal_path.iterdir()
            if f.is_file()
        ]
    
    # Check for review pack (keep for backward compatibility)
    review_pack_path = proposal_path / "review_pack"
    review_pack_files = []
    if review_pack_path.exists():
        review_pack_files = [
            {
                "name": f.name,
                "path": str(f.relative_to(BASE_PATH)),
            }
            for f in review_pack_path.iterdir()
            if f.is_file()
        ]
    
    # Check for linked runs (keep for backward compatibility)
    links_data = read_json_file_safe(proposal_path / "links.json", warnings)
    linked_runs = links_data.get("run_ids", []) if links_data else []
    
    response = {
        "proposal_id": proposal_id,
        "path": str(proposal_path.resolve()),
        "status": status_data,
        "title": title,
        "proposal_md": proposal_md,
        "required_closure": required_closure,
        "gates": gates,
        "files": files,
        "review_pack_files": review_pack_files,
        "linked_runs": linked_runs,
    }
    
    if warnings:
        response["warnings"] = warnings
    
    return JSONResponse(status_code=200, content=response)


@app.get("/closures/{closure_id}")
async def get_closure(closure_id: str):
    """Get closure details."""
    closure_path = BASE_PATH / "closures" / closure_id
    
    if not closure_path.exists() or not closure_path.is_dir():
        return JSONResponse(
            status_code=404,
            content={
                "error": "closure_not_found",
                "closure_id": closure_id,
            }
        )
    
    warnings = []
    
    # Read closure.md
    closure_md = read_text_file_safe(closure_path / "closure.md")
    
    # Read closure.json (prefer closure.json, fallback to status.json)
    closure_json = read_json_file_safe(closure_path / "closure.json", warnings)
    if not closure_json:
        closure_json = read_json_file_safe(closure_path / "status.json", warnings)
    
    # Extract source_run_id from closure_json if present
    source_run_id = None
    if closure_json and isinstance(closure_json, dict):
        source_run_id = closure_json.get("source_run_id")
    
    # List top-level files
    files = []
    if closure_path.exists():
        files = [
            f.name
            for f in closure_path.iterdir()
            if f.is_file()
        ]
    
    response = {
        "closure_id": closure_id,
        "path": str(closure_path.resolve()),
        "closure_md": closure_md,
        "closure_json": closure_json,
        "source_run_id": source_run_id,
        "files": files,
    }
    
    if warnings:
        response["warnings"] = warnings
    
    return JSONResponse(status_code=200, content=response)


@app.post("/closures", response_model=ClosureResponse, status_code=status.HTTP_201_CREATED)
async def create_closure(closure: ClosureCreate):
    """Create a new closure."""
    decision_type = (closure.decision_type or "").strip()

    # B10: BOOK closure (book-level lock)
    if decision_type.upper() == "BOOK":
        book_id = (closure.proposal_id or "BOOK-DEFAULT").strip()
        if book_id.startswith("BOOK-"):
            book_id = book_id[len("BOOK-"):]
        required = _load_book_required_closures(book_id)
        missing = [cid for cid in required if not _closure_exists(cid)]
        if missing:
            raise HTTPException(
                status_code=400,
                detail=f"Missing required closures for BOOK-{book_id}: {missing}",
            )
        closure_id = f"BOOK-{book_id}"
        closure_dir = BASE_PATH / "closures" / closure_id
        closure_dir.mkdir(parents=True, exist_ok=True)

        closure_json_path = closure_dir / "closure.json"
        if closure_json_path.exists():
            raise HTTPException(
                status_code=409,
                detail=f"Closure {closure_id} already exists and is immutable",
            )

        closure_data = {
            "closure_id": closure_id,
            "created_at": datetime.utcnow().isoformat(),
            "created_by": closure.created_by or get_username(),
            "proposal_id": book_id,
            "run_id": closure.run_id,
            "source_run_id": closure.run_id,
            "decision_type": "BOOK",
            "rationale": closure.rationale,
            "evidence_paths": closure.evidence_paths,
            "sign_off": closure.sign_off,
            "book_id": book_id,
            "required_closure_ids": required,
            "present_closure_ids": required,
        }

        closure_json_path.write_text(
            json.dumps(closure_data, indent=2),
            encoding="utf-8",
        )

        ensure_audit_log(
            f"Book closure created: {closure_id}",
            {
                "closure_id": closure_id,
                "book_id": book_id,
                "decision_type": "BOOK",
            },
        )

        indexer.reindex()
        return ClosureResponse(**closure_data)

    # Policy check: ensure proposal exists
    proposal_path = BASE_PATH / "proposals" / closure.proposal_id
    if not proposal_path.exists():
        raise HTTPException(status_code=404, detail=f"Proposal not found: {closure.proposal_id}")
    
    # Generate closure ID
    timestamp = datetime.utcnow().strftime("%Y%m%d")
    closure_id = f"CL-{timestamp}-{closure.proposal_id[:8]}"
    closure_dir = BASE_PATH / "closures" / closure_id
    closure_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if closure already exists (immutability)
    closure_json_path = closure_dir / "closure.json"
    if closure_json_path.exists():
        raise HTTPException(
            status_code=400,
            detail=f"Closure {closure_id} already exists and is immutable"
        )
    
    # Build closure data
    closure_data = {
        "closure_id": closure_id,
        "created_at": datetime.utcnow().isoformat(),
        "created_by": closure.created_by or get_username(),
        "proposal_id": closure.proposal_id,
        "run_id": closure.run_id,
        "source_run_id": closure.run_id,
        "decision_type": decision_type,
        "rationale": closure.rationale,
        "evidence_paths": closure.evidence_paths,
        "sign_off": closure.sign_off,
    }
    
    # Write closure.json
    closure_json_path.write_text(
        json.dumps(closure_data, indent=2),
        encoding="utf-8"
    )
    
    # Update proposal status
    proposal_status_path = proposal_path / "status.json"
    status_data = {"status": "closed", "closed_at": datetime.utcnow().isoformat(), "closure_id": closure_id}
    if proposal_status_path.exists():
        try:
            existing_status = json.loads(proposal_status_path.read_text(encoding="utf-8"))
            status_data.update(existing_status)
        except (json.JSONDecodeError, IOError):
            pass
    status_data["status"] = "closed"
    proposal_status_path.write_text(
        json.dumps(status_data, indent=2),
        encoding="utf-8"
    )
    
    # Append to audit log
    ensure_audit_log(
        f"Closure created: {closure_id}",
        {
            "closure_id": closure_id,
            "proposal_id": closure.proposal_id,
            "decision_type": closure.decision_type,
        }
    )
    
    # Trigger reindex
    indexer.reindex()
    
    return ClosureResponse(**closure_data)


@app.post("/cli/validate")
async def validate_run(run_id: str):
    """Run validator on a run (CLI wrapper)."""
    run_path = BASE_PATH / "runs" / run_id
    if not run_path.exists():
        raise HTTPException(status_code=404, detail=f"Run not found: {run_id}")
    
    # Call CLI validator (assumes mustikarasa_codex_cli.py has validate command)
    # For MVP, we'll assume validator is called separately or return placeholder
    try:
        # This is a placeholder - actual CLI integration depends on CLI structure
        result = subprocess.run(
            ["python", str(BASE_PATH / "mustikarasa_codex_cli.py"), "validate", "--run", run_id],
            capture_output=True,
            text=True,
            cwd=str(BASE_PATH),
        )
        
        if result.returncode != 0:
            raise HTTPException(
                status_code=500,
                detail=f"Validator failed: {result.stderr}"
            )
        
        ensure_audit_log(f"Validator run: {run_id}")
        return {"status": "success", "output": result.stdout}
    except FileNotFoundError:
        # CLI command not found - return placeholder
        return {
            "status": "not_implemented",
            "message": "CLI validator not yet integrated",
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server:app", host="127.0.0.1", port=8010, reload=True)
