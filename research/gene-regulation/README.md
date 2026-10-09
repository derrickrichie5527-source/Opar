# Gene regulation: versioned assessment materials

The website is the reader-facing assessment. These files provide provenance and reproducibility without adding technical detail to the main reading flow. All experimental measurements are simulated. No V2 model responses or independent reviews have been collected.

## Versions

- **V1:** `../../gene-regulation-v1.html` from repository commit `1b53250` preserves the original assessment, answers, rubric and Claude pilot. The `v1/` directory preserves the original submitted prompt, verbatim response, historical rubric and score record. **39/40 applies only to this single V1 response.**
- **V2.0:** `v2/prompt.txt` is the complete closed-book solver input; `v2/reference-answers.txt` and `v2/rubric.txt` are withheld from the solver. The revised rubric totals 40 but changes weights and criteria. V1 and V2 scores are not interchangeable. `v2/data.json` contains the simulated measurements, in control/treatment order.
- **V3:** only a proposed less-scaffolded variant on the website; no V3 task or results exist yet.

The V1 public report contains the historical grading explanations. V2 adds an explicit handling rule for unsupported calculations; it does not retroactively change V1 scores. The original records were copied from the published gene-regulation-reasoning-portfolio project. Newline-normalized SHA-256 hashes in `manifest.json` identify preserved and revised files. Reformatting substantive content requires a new version and new hashes.

## Reproduce the checks

From this repository root, with Python 3 (standard library only):

```text
python research/gene-regulation/verify.py
```

This recalculates RNA corrections, endpoint and rounded-data regression rates, synthesis, effective synthesis per mRNA, standalone and combined counterfactuals. It checks the displayed table values against data, rubric totals, archive hashes, internal links and basic HTML structure/accessibility. It is not a substitute for browser layout testing or independent scientific review. No statistical uncertainty is estimated from the simulated points.

## Future evaluation procedure

1. Freeze assessment and rubric versions and record prompt/reference/rubric hashes. Predeclare models, repetitions, settings, tool permissions, exclusion rules and scoring rules. Do not tune these after inspecting results.
2. Use a fresh session for each attempt. Submit only `v2/prompt.txt`, preserving every user/system instruction. The standard condition is closed-book, with no access to answers, rubric or website. Record exact model identifier when exposed; otherwise explicitly mark it unavailable. Browsing-enabled runs are a separate condition.
3. Create a directory `v2/runs/<run-id>/` for each actual attempt. Save `prompt.txt`, unedited `response.txt`, `record.json` based on `v2/run-template.json`, and criterion-level `scores.csv` with columns `criterion,max_points,awarded_points,response_excerpt,rationale,reviewer,adjudication`. Save tool traces if any. Retain failed or truncated attempts and report exclusions transparently.
4. Score every criterion with an evidence excerpt. Record unsupported claims and contradictions. Blinded second scoring and documented adjudication should be obtained when available; never label a reviewer independent unless that is true. Preserve original scores when recording adjudications.
5. Report all runs, per-question results, dispersion and methodological limitations. Do not invent a pass threshold or claim validation from a single run. Publicly available task answers also create a potential contamination limitation.

The run template contains null fields because no V2 run has occurred. It is a template, not a result. Reviewer identity, elapsed time and model settings must be observed or marked unavailable rather than inferred.

## Scientific limits

The exercise assumes matched extraction and incorporation, a homogeneous first-order labeled protein pool, stable mean cell size, per-cell steady state and no unmeasured loss route. Real experiments require biological replication, uncertainty propagation, model diagnostics and orthogonal validation. Net effective synthesis per mRNA cannot resolve individual translation or RNA-processing steps. The cited literature supports methodology; the data and numerical counterfactuals are original simulations.
