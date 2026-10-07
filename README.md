# Derrick Opar Portfolio

Professional portfolio for life sciences, data quality and AI evaluation work.

## Featured projects

### Regulated Laboratory Data Reconciliation AI Benchmark
A synthetic audit-sensitive AI benchmark containing realistic data-quality issues across laboratory records. Includes an external Claude trial and a 40-criterion evaluation rubric.

### Anopheles PCR AI Benchmark
A molecular biology benchmark focused on conventional PCR, gel electrophoresis, species identification, protocol fidelity and scientific uncertainty.

## Site structure

- `index.html` — main portfolio
- `styles.css` — Theme 1: white, navy and teal
- `assets/` — visual project assets
- `docs/` — case studies and evaluation workbooks

## Portfolio focus

Biochemistry · Life Sciences · Data Quality · AI Evaluation · Research

## Theme 1 repairs

- Restored the original gel image and four project documents from the local `Derrick_Portfolio_Theme1.zip` package. The data-quality workbook matches `Claude_Evaluation.xlsx` in the supplied `Data_Entry_Portfolio_Package.zip` byte for byte.
- Replaced the oval DNA drawing with a locally hosted SVG double-helix schematic. It is decorative, not an atomic molecular model.
- Added a consistent set of local SVG outline icons; no remote icon service or JavaScript dependency is required.
- Kept all navigation links visible on mobile, added keyboard focus and a skip link, respected reduced-motion settings, and prevented gel cropping.
- Case studies link to original PDFs; workbook links explicitly download XLSX files.

Serve this folder with a local static web server for review. The SVG icon sprite uses same-origin references, so an HTTP preview is preferable to opening the HTML directly from disk.

Publication requires user approval. The live Pages deployment should be checked again after publishing, including both PDFs, both workbook downloads, and the gel image.
