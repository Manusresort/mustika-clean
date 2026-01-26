# Audit Report — real_material_pilot

## 1) Non-empty checks
- ledgers .tsv count: 15
- blocks file count: 3
- images .png count: 1196
- ocr .txt count: 1193

## 2) Page coverage cross-check
- pages detected in images_png: 1196
- pages detected in ocr_txt: 1193
- overlap: 1193
- missing in ocr_txt: 3
- missing in images_png: 0
- images_png filenames without digits: 0
- ocr_txt filenames without digits: 0
- sample missing in ocr_txt: ['0213', '0719', '1149']

## 3) Ledger sanity
- batch_001.tsv
  - header: 4	page-1156	bahan,bumbu,resep,masakan
  - row_count: 9
  - page_cols_detected: True
- batch_002_candidates.tsv
  - header: 4	page-1110	bahan,bumbu,resep,masakan
  - row_count: 9
  - page_cols_detected: True
- extract_plan_by_rb.tsv
  - header: recipe_block_id	page_ids_joined	planned_output_path	status	notes
  - row_count: 28
  - page_cols_detected: True
- page_candidate_ledger.tsv
  - header: score	page	triggers	class	note
  - row_count: 1097
  - page_cols_detected: True
- page_candidate_ledger_batch_001.tsv
  - header: pageclasstriggersnote
  - row_count: 10
  - page_cols_detected: True
- page_candidate_ledger_batch_002.tsv
  - header: pageclasstriggersnote
  - row_count: 10
  - page_cols_detected: True
- page_exceptions_ledger.tsv
  - header: pageexception_codenote
  - row_count: 8
  - page_cols_detected: True
- page_to_recipe_block.tsv
  - header: page_id	recipe_block_id
  - row_count: 1214
  - page_cols_detected: True
- recipe_block_file_manifest.tsv
  - header: recipe_block_id	page_id	canonical_txt_path	canonical_txt_exists
  - row_count: 932
  - page_cols_detected: True
- recipe_block_ledger_skeleton.tsv
  - header: recipe_block_id	source_block_id	start_page	end_page	pages	boundary_flag	review_status	title_raw	notes
  - row_count: 28
  - page_cols_detected: True
- recipe_block_manifest.tsv
  - header: recipe_block_id	source_block_id	start_page	end_page	page_count	missing_in_canonical_count	boundary_flag	review_status
  - row_count: 28
  - page_cols_detected: True
- recipe_block_pages.tsv
  - header: recipe_block_id	page_id	page_num	missing_in_canonical
  - row_count: 932
  - page_cols_detected: True
- recipe_record_ledger_skeleton.tsv
  - header: recipe_id	recipe_block_id	extract_status	extract_notes	output_path
  - row_count: 28
  - page_cols_detected: False
- step4_outputs_index.tsv
  - header: path	exists	bytes	mtime_epoch
  - row_count: 7
  - page_cols_detected: False
- step5_outputs_index.tsv
  - header: path	exists	bytes	mtime_epoch
  - row_count: 5
  - page_cols_detected: False

## 4) Top issues
- None detected
