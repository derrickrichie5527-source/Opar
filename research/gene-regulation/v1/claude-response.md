# Answers by question

**Notation.** C = control, X = compound X. P = protein R per cell, M = mature mRNA per cell, S = protein synthesis rate per cell, e = S/M. ln 2 = 0.693147.

---

## 1. Audit of the RNA conclusion

**Reported fold change (target/H):**
- ΔCq(C) = 25.0 − 20.0 = 5.0
- ΔCq(X) = 24.0 − 19.0 = 5.0
- ΔΔCq = 0, so 2^(−0) = **1.0**, which is the "unchanged" result.

**Per-cell inference using the independent calibration:**
- Target Cq fell by 1.0, so with an amplification factor of 2 and matched input, target template per cell rose by 2^1 = **2.0×**.
- Cross-check: (target/H ratio = 1.0) × (H per cell = 2.0/1.0) = **2.0×**.

**Why the answers differ.** The method assumes the reference is constant. Here H itself doubled per cell, so dividing target by H removed the real change. The 2^(−ΔΔCq) result is a ratio of two things that both rose. It is not a per-cell measurement.

**Assumptions needed for the 2× inference:**
- Equal viable cell numbers, and RNA recovery and RT efficiency matched per cell.
- The amplification factor is exactly 2 for both assays.
- The independent H calibration is valid.

**Limit:** mature mRNA per cell is a steady-state quantity. A 2× rise reflects the balance of production, processing and decay, so it does not identify transcription or stability as the cause.

---

## 2. Newly made RNA

**Recovery-corrected signal:**
- C: 100 / 0.80 = 125
- X: 100 / 0.40 = 250
- Ratio X/C = **2.0**

The unchanged raw signal was an artifact of the spike recovery halving in X.

**What it supports.** After recovery correction, treated cells yielded about twice as much labeled target RNA per equal-cell input in the pulse. This agrees with the 2× mature mRNA, and it fits a roughly doubled RNA production rate if mRNA decay is unchanged. Decay was not measured, so that is an inference.

**What it fails to establish:**
- It is not a transcription rate. It does not separate initiation, elongation, processing or export.
- It depends on equal label uptake, nucleotide-pool specific activity, uridine content and pulse timing.
- It does not show that X acts on transcription directly.

**Why the spike cannot validate label incorporation.** It is added after extraction, so it reports only downstream purification yield. Cellular 4sU uptake, phosphorylation, pool labeling and incorporation, and extraction losses before the spike, are all invisible to it. A change in any of these would alter the target signal without changing spike recovery.

---

## 3. Defensible turnover evidence

**Can the Panel C half-lives be used as native degradation half-lives? No.**

**Residual synthesis.** In X, 30% of synthesis continues, so P(t)/P₀ = f + (1 − f)e^(−kt) with f = 0.3.
- The time to reach 0.5 is t = ln(0.7/0.2)/k = 1.253/k.
- The true half-life is 0.693/k.
- The apparent half-life is therefore inflated about **1.8×** in X, but not in C, which has 0% residual synthesis. The comparison is biased toward exaggerating the stabilization.

**Other inhibitor concerns:**
- Cycloheximide is a global translation inhibitor. It can deplete short-lived degradation or regulatory factors, cause stress, and alter growth and dilution.
- The data suggest such perturbation. The C values (2 h, 6 h) do not match Panel D's loss half-lives (4 h, 6 h). Even a crude correction of X (6/1.8 ≈ 3.3 h) conflicts with D's 6 h, so Panel C cannot be rescued by simple correction.
- The apparent 3× half-life ratio in C coincides with the 3× abundance, which makes it look more persuasive than it is.

**Why Panel D is the better starting point:**
- It follows a pre-existing labeled cohort without a global translation inhibitor.
- Recycling, recovery and specificity controls pass.
- It has time-zero normalization per condition.
- Its limits are that it measures loss per cell, which includes dilution, and that it assumes first-order kinetics.

---

## 4. Degradation versus dilution

**Reading Panel D:**
- C: 0.5 per 4 h, so a loss half-life of 4 h (0.125 at 12 h = 2⁻³).
- X: 0.629961 = 2^(−2/3) at 4 h, and 0.25 at 12 h = 2⁻², so a loss half-life of **6 h**.

| | k_loss (h⁻¹) | k_growth (h⁻¹) | k_degradation (h⁻¹) | Loss t½ | Degradation-only t½ |
|---|---|---|---|---|---|
| C | 0.693147/4 = 0.173287 | 0.693147/12 = 0.057762 | 0.115525 | 4 h | 0.693147/0.115525 = **6 h** |
| X | 0.693147/6 = 0.115525 | 0.693147/24 = 0.028881 | 0.086644 | 6 h | 0.693147/0.086644 = **8 h** |

**Interpretation:**
- The observed per-cell loss half-life rose 1.5× (4 to 6 h).
- The degradation-only half-life rose only 1.33× (6 to 8 h).
- The remainder comes from slower dilution because the doubling time lengthened from 12 to 24 h.

---

## 5. Reconciling protein and RNA

**Synthesis ratio.** At steady state P = S/k_loss, so S = P·k_loss.
- S_X/S_C = 3.0 × (0.115525/0.173287) = 3.0 × 0.6667 = **2.0**

**Effective synthesis per mRNA.** With M_X/M_C = 2.0 (Q1) and S = e·M:
- e_X/e_C = 2.0/2.0 = **1.0**

**Combining synthesis and clearance:**
- P_X/P_C = (S ratio 2.0) × (1/k_loss ratio = 0.173287/0.115525 = 1.5) = **3.0** ✓.

**How the clearance change splits.** The absolute drop in k_loss is 0.057762 h⁻¹. Half of it (0.028881) is degradation and half (0.028881) is dilution. In fold terms, a degradation change alone, with growth held at the control rate, gives 0.173287/0.144406 = 1.20×. A growth change alone gives 0.144406/0.115525 = 1.25×. The two multiply to 1.5×, and the split is order-dependent.

**Does this prove that no individual translation-regulatory process changed? No.**
- e is a composite quantity. It includes initiation, elongation, ribosome loading, the fraction of mRNA that is translatable, mRNA localization, nascent-chain quality control and protein folding.
- Changes in these could offset each other and still give e ≈ 1.
- M is total mature mRNA, not translating mRNA.
- The result also depends on the model's steady-state and first-order assumptions.

---

## 6. Competing claims

- **A (degradation alone explains it): Rejected.** If synthesis were unchanged, the maximum effect from the full 1.5× loss change would be 1.5×, not 3×. Using the degradation-only decomposition it is 1.2–1.33×. In addition, mRNA and the inferred synthesis both doubled.
- **B (translation efficiency must have risen threefold): Rejected.** The model gives e ratio ≈ 1.0 (2× synthesis ÷ 2× mRNA). The 3× comes from 2× × 1.5×.
- **C (model supports increased synthesis and reduced total clearance): Supported, conditionally.** The model infers S ×2 and k_loss ÷1.5. The caveats are that it is model-dependent, and that "reduced clearance" is half slower dilution (a growth effect) and half slower degradation.
- **D (X directly inhibits a proteasome enzyme): Not supported.** There is no enzyme assay, target engagement, route-specific inhibitor or ubiquitination evidence. Slower loss does not identify a pathway, and "directly" requires binding or biochemical evidence.

---

## 7. Follow-up work

**Experiment 1: test e_X/e_C ≈ 1.**
- *Design:* A short R-specific pulse-labeling experiment (for example a non-canonical amino acid, with an R-specific capture), shorter than the half-life. Measure mRNA per cell in the same samples with spike-in and calibrated RT-qPCR, and add polysome or ribosome-profiling occupancy for R.
- *Controls:* A no-label control, a nonspecific capture control, a translation-inhibited control to show the signal is synthesis-dependent, matched precursor-pool labeling, a capture-recovery spike, and a control protein.
- *Predictions:* If the inference holds, new-R synthesis X/C ≈ 2 and per-mRNA ≈ 1. A per-mRNA ratio above or below 1 would challenge it.
- *Limitation:* This still measures a composite. It will not say which sub-step of translation (if any) shifted or cancelled, and cotranslational degradation is lumped in.

**Experiment 2: is a candidate cis element necessary for the RNA response?**
- *Design:* Precisely edit (delete or mutate) the element at the endogenous locus, preserving coding sequence and splicing. Use independent clones or guides, compare with isogenic wild type, and test the genotype × X interaction. Measure mRNA per cell and recovery-corrected nascent RNA, with a pulse-chase for decay.
- *Controls:* Edited-but-neutral clones, a scrambled-sequence substitution, add-back rescue, off-target sequencing, unaffected reference genes, and matched viability and uptake.
- *Outcomes:* If the element is necessary, the ~2× response to X is lost or reduced in the edited cells.
- *Limitation:* The edit may alter basal expression, chromatin or RNA structure, and clones vary. Necessity does not show sufficiency.

**Why element dependence is not direct molecular action by X.** Dependence shows only that the element participates in the response. X could act upstream through signaling, a transcription factor, chromatin, metabolism, cell cycle or stress, with the element as a downstream effector. Direct action needs separate evidence: target engagement or binding, dose-response and structure-activity relationships, an inactive analog, and ideally in vitro reconstitution.

**One control before attributing slower degradation to a pathway:** an epistasis (occlusion) test. Inhibit or knock down the pathway chemically and genetically, and verify in the pulse-chase that it raises R in control cells and removes the additional stabilization by X. Measure the perturbation's effects on synthesis, growth and global translation in parallel.

---

## 8. Defensible conclusion

**Observations:** In these simulated data, X increased R protein 3×, calibrated mature mRNA per cell about 2×, and recovery-corrected labeled target RNA 2×, while the reference transcript H also doubled. Independent pulse-chase measurements show a per-cell loss half-life of 4 h (C) versus 6 h (X) with doubling times of 12 h versus 24 h.

**Model-dependent interpretation:** Under the supplied model, degradation-only half-lives are 6 h and 8 h, and the 3× increase factors into about 2× synthesis (matching 2× mRNA, so effective synthesis per mRNA is about unchanged) times 1.5× lower total clearance, half of which is slower dilution.

**Unresolved:** The mechanism, whether the mRNA rise reflects transcription or altered RNA stability, which sub-steps compose e, the degradation route, and the molecular target of X all remain unknown.

**Why no significance claim is possible.** The values are single idealized point values with no biological replicates, no variance, no sampling distribution and no uncertainty. A p-value or confidence interval needs replicate-to-replicate variation, and without it the numbers cannot be distinguished from noise. Propagating them through a multi-step model would also compound any real uncertainty, so replicated experiments with effect sizes and confidence intervals would be required before any statistical claim.
