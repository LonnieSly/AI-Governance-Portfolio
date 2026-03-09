# Project 4b: Dynamic Pricing AI — MEASURE Report & Drift Analysis

## Scenario

Following the MAP risk assessment of the restaurant group's dynamic pricing model, this project executes the **quantitative audit** — translating identified risks into statistical tests, running those tests against 6 months of model output data, and producing a compliance determination against consumer protection fair-pricing standards.

The central audit question: **Can we prove — with statistical evidence — whether the model is pricing fairly across zip codes with different income profiles?**

---

## Two Deliverables, One Audit Function

### `drift_and_bias_analysis.py` — The Audit Engine
A Python script that generates synthetic pricing data, runs four sequential audit tests, and produces structured findings. In a live engagement, the data generation section is replaced with a direct export from the client's POS and model logging systems.

### `02_MEASURE_Report_Fair_Pricing.md` — The Compliance Report
The formal deliverable. Translates statistical output into GRC language: what standard was applied, what the test found, what it means for the organization's legal exposure, and who owns remediation.

---

## Audit Tests Executed

### Test 1: Model Drift Detection — MEASURE 2.6
**Method:** Kolmogorov-Smirnov (KS) two-sample test
**Question:** Has the distribution of price adjustments shifted significantly between the first and second 90-day periods?
**Threshold:** p < 0.05 = statistically significant drift

The KS test was selected over simpler delta comparison because it evaluates the *entire distribution shape*, not just averages. A model can maintain the same average price ratio while developing a much wider or skewed distribution — the KS test catches this; a mean comparison does not.

### Test 2: Geographic Bias Analysis — MAP 5.1 / MEASURE 2.3
**Method:** Pearson correlation (median HHI vs. average price ratio) + per-zip disparity test
**Question:** Is there a statistically significant relationship between a zip code's income level and the prices customers pay there?
**Consumer Protection Threshold:** No zip code may deviate more than ±3% from the system-average price ratio for equivalent items

### Test 3: Item-Level Disparity — MEASURE 2.8
**Method:** Direct ratio comparison between lowest and highest income zip codes by menu item
**Question:** Is bias concentrated in staple/essential items (greater legal significance) or distributed across the menu?
**Threshold:** No single item gap >2% between income extremes

---

## Audit Results Summary

| Finding | Severity | Result |
|---|---|---|
| MEASURE-01: Income-pricing correlation | Moderate | ⚠ r = -0.89, p = 0.04 — Adverse direction |
| MEASURE-02: Income-stratified model drift | High | ⚠ Drift in 3 lower-income zips; stable in 2 higher-income zips |
| MEASURE-03: Item-level disparity | Low-Moderate | ✓ All items within threshold; Beignets gap flagged for monitoring |
| Overall fair-pricing compliance | Conditional Pass | ✓ No current breach; trajectory indicates risk within 2 quarters |

---

## Key Decisions

**1. A "Conditional Pass" verdict was used rather than a binary Pass/Fail.**
The model does not currently breach the ±3% disparity threshold. A clean "Pass" would be technically accurate but professionally irresponsible. The income-correlated drift pattern (r = -0.89) is statistically significant and moving in the adverse direction. Issuing a Pass without surfacing the trajectory would give the organization false assurance and expose the auditor to liability if the model breaches the threshold in the next review cycle. GRC work requires accurately representing *current state and directional risk*, not just checking a box.

**2. The KS-test result pattern — drift in lower-income zips, stability in higher-income zips — is the most important finding in the report.**
Random model degradation would produce drift across all locations. Income-stratified drift — where exactly the three lowest-income locations drift and the two highest-income locations remain stable — is not consistent with random variation. It is consistent with the model's feedback mechanisms amplifying income-correlated signals over time. This elevates the finding from a technical observation to a potential legal one.

**3. Staple items were weighted more heavily in the item-level analysis.**
A bias pattern on a premium item affects customers who chose to buy a premium item. A bias pattern on a staple item — Red Beans, Beignets — affects customers' access to affordable everyday meals. Consumer protection enforcement consistently treats essential goods differently from discretionary ones. The audit methodology reflects this distinction.

---

## Framework Mapping

| Report Section | NIST AI RMF Function | Governance Purpose |
|---|---|---|
| Model Drift Detection | MEASURE 2.6 | Prove performance stability over time |
| Geographic Bias Analysis | MAP 5.1, MEASURE 2.3 | Prove equitable treatment across affected groups |
| Item-Level Disparity | MEASURE 2.8 | Adversarial/disparity testing on highest-risk item categories |
| Remediation Requirements | MANAGE 4.1 | Post-deployment response and retraining triggers |

---

## How to Run the Audit Script

```bash
pip install numpy pandas scipy
python drift_and_bias_analysis.py
```

To run against real data: replace the `generate_pricing_data()` function with a CSV import of your model's pricing output logs. The required columns are `date`, `zip_code`, `item`, `base_price`, and `model_price`. All downstream analysis runs automatically.

---

## How This Connects to the Portfolio

This MEASURE report is the direct output of the MAP risk assessment in Project 4a. Every finding here traces back to a risk identified in that MAP register — this is the RMF loop closing.

The next artifact in this project will complete the loop with a **MANAGE 4.1 Incident Response Protocol** — the playbook that activates when the KS-test flags income-stratified drift in a live monitoring environment.

---

## Artifact

**→ [View the Full MEASURE Report](./02_MEASURE_Report_Fair_Pricing.md)**
**→ [View the Audit Script](../scripts/drift_and_bias_analysis.py)**
