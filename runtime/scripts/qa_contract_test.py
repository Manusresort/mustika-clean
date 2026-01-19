#!/usr/bin/env python3
import json
import sys
from pathlib import Path
import tempfile

RUNTIME_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RUNTIME_ROOT))

from indexer import Indexer


def read_inbox_items(base: Path):
    inbox_path = base / "indices" / "inbox_index.json"
    data = json.loads(inbox_path.read_text(encoding="utf-8"))
    return data.get("items", [])


def test_closed_proposal_with_closure():
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        (base / "proposals" / "P-002").mkdir(parents=True)
        (base / "closures" / "CL-20260117-P-002").mkdir(parents=True)

        (base / "proposals" / "P-002" / "status.json").write_text(
            json.dumps({"status": "closed", "closure_id": "CL-20260117-P-002"}),
            encoding="utf-8",
        )
        (base / "proposals" / "P-002" / "required_closure.json").write_text(
            json.dumps({"reason": "qa_test"}),
            encoding="utf-8",
        )
        (base / "closures" / "CL-20260117-P-002" / "closure.json").write_text(
            json.dumps({"proposal_id": "P-002", "closure_id": "CL-20260117-P-002"}),
            encoding="utf-8",
        )

        Indexer(base).reindex()
        items = read_inbox_items(base)
        if any(i.get("source_id") == "P-002" and i.get("kind") == "closure_needed" for i in items):
            raise AssertionError("P-002 incorrectly flagged as closure_needed")


def test_open_proposal_requires_closure():
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        (base / "proposals" / "P-003").mkdir(parents=True)

        (base / "proposals" / "P-003" / "status.json").write_text(
            json.dumps({"status": "open"}),
            encoding="utf-8",
        )
        (base / "proposals" / "P-003" / "required_closure.json").write_text(
            json.dumps({"reason": "qa_test"}),
            encoding="utf-8",
        )

        Indexer(base).reindex()
        items = read_inbox_items(base)
        if not any(i.get("source_id") == "P-003" and i.get("kind") == "closure_needed" for i in items):
            raise AssertionError("P-003 missing closure_needed inbox item")


def main():
    test_closed_proposal_with_closure()
    test_open_proposal_requires_closure()
    print("qa_contract_test PASS")


if __name__ == "__main__":
    main()
