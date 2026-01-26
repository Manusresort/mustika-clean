# Run Report — real_material_pilot

## Selection
- recipe_block_id: 
- pages: 

## Commands
- python3 indexer.py
- CI=false ./scripts/qa_full_system.sh

## Exit codes
- indexer.py: 0
- qa_full_system.sh: 0

## QA summary extract
\n
txt
26:index_run_index.json	PASS	exists
27:index_proposal_index.json	PASS	exists
28:index_closure_index.json	PASS	exists
29:index_inbox_index.json	PASS	exists
42:GET_/health	PASS	ok:true
43:GET_/inbox	PASS	items[]
44:GET_/inbox_chapter_id_key	PASS	exists
45:GET_/inbox_counts	PASS	total_matches_items
46:GET_/proposals/P-TEST	PASS	proposal_md_present
54:release_identity_enforced	PASS	latest.json + immutability
59:release_trust_present	PASS	release_trust.json present
61:ui_build	PASS	npm run build

