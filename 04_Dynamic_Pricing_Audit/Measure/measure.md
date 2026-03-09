# MEASURE Report — Dynamic Pricing AI Model
## Fair Pricing Assurance & Consumer Protection Compliance
**Deployment:** AI-Driven Dynamic Pricing — Multi-Unit Restaurant Group
**NIST AI RMF Function:** MEASURE 2.3 (Bias), 2.6 (Performance), 2.8 (Adversarial/Disparity Testing)
**Audit Period:** January 1, 2024 – June 30, 2024 (180 days)
**Report Status:** CONDITIONAL PASS — See Findings

---

## Executive Summary

This MEASURE Report documents the quantitative evaluation of the restaurant group's dynamic pricing AI model against consumer protection fair-pricing standards. The audit covered 4,500 pricing records across 5 locations representing zip codes with median household incomes ranging from $28,000 to $115,000.

**Overall Compliance Verdict:**

| Standard | Result |
|---|---|
| Geographic Price Disparity (±3% threshold) | ✓ PASS — All zip codes within threshold |
| Model Drift — Stability Over 6 Months | ⚠ CONDITIONAL — Drift detected in 3 of 5 locations |
| Income-Pricing Correlation | ⚠ FINDING — Statistically significant negative correlation |
| Human Override Capability | ✗ FAIL — No override mechanism present |

**Auditor's Assessment:** The model does not currently breach the ±3% geographic disparity threshold. However, the negative income-to-price correlation (r = -0.89, p = 0.04) and statistically significant drift in lower-income locations constitute leading indicators of a future consumer protection breach. Without remediation, the model will likely breach the threshold within one to two additional quarters.

---

## MEASURE 2.3 — Bias Evaluation: Geographic Pricing Equity

### Standard Applied
No zip code location shall receive average pricing that deviates more than ±3% from the system-wide average price ratio for equivalent menu items. This threshold is derived from FTC algorithmic pricing guidance and mirrors geographic price discrimination standards applied in consumer protection enforcement.

### Measurement Methodology
- **Unit of measure:** Price Ratio (model-output price ÷ menu base price)
- **Aggregation:** 90-day rolling average by zip code and item
- **Statistical test:** Pearson correlation between median HHI and average price ratio
- **Test period:** Period 2 (days 91–180) — current model state

### Results

| Zip Code | Income Label | Median HHI | Avg Price Ratio | Deviation from System Avg | Status |
|---|---|---|---|---|---|
| 70112 | Lower-income urban | $28,000 | 1.0185 | +0.28% | ✓ Pass |
| 70115 | Mixed-income | $45,000 | 1.0179 | +0.22% | ✓ Pass |
| 70118 | Middle-income | $62,000 | 1.0156 | -0.01% | ✓ Pass |
| 70124 | Upper-middle suburban | $87,000 | 1.0126 | -0.30% | ✓ Pass |
| 70131 | High-income suburban | $115,000 | 1.0137 | -0.20% | ✓ Pass |

**System Average Price Ratio (Period 2):** 1.0156

### Correlation Analysis

| Metric | Value | Interpretation |
|---|---|---|
| Pearson r (HHI vs Price Ratio) | -0.8939 | Strong negative correlation |
| P-value | 0.0408 | Statistically significant (p < 0.05) |
| Direction | Lower income → Higher price ratio | Adverse direction |

**Finding MEASURE-01 (Moderate):** While no individual zip code breaches the ±3% threshold, the income-to-price-ratio correlation is statistically significant and adverse in direction. The model is systematically — if marginally — applying higher price adjustments in lower-income locations. This is a leading indicator finding: it does not constitute a current consumer protection violation, but trajectory analysis indicates breach risk within 2 quarters without remediation.

**Auditor's Evidence Standard Met:** Yes. Statistical significance at p < 0.05 with r = -0.89 satisfies the evidentiary burden for a material finding under MEASURE 2.3.

---

## MEASURE 2.6 — Performance Over Time: Model Drift Analysis

### Standard Applied
Price ratio distributions for each location shall remain statistically stable over any 90-day comparison window. Material drift is defined as a KS-test p-value < 0.05 between baseline (days 1–90) and current (days 91–180) periods.

### Measurement Methodology
- **Statistical test:** Kolmogorov-Smirnov two-sample test
- **Input:** Price ratio distributions by zip code, Period 1 vs. Period 2
- **Trigger threshold:** p < 0.05 = drift detected; price ratio delta > 2% = material drift

### Results

| Zip Code | Income Label | P1 Avg Ratio | P2 Avg Ratio | Delta | KS Stat | P-Value | Status |
|---|---|---|---|---|---|---|---|
| 70112 | Lower-income urban | 1.0076 | 1.0185 | +0.0109 | 0.2422 | <0.0001 | ⚠ Drift |
| 70115 | Mixed-income | 1.0172 | 1.0179 | +0.0007 | 0.1133 | 0.0061 | ⚠ Drift |
| 70118 | Middle-income | 1.0148 | 1.0156 | +0.0008 | 0.1044 | 0.0147 | ⚠ Drift |
| 70124 | Upper-middle suburban | 1.0163 | 1.0126 | -0.0037 | 0.0622 | 0.3487 | ✓ Stable |
| 70131 | High-income suburban | 1.0146 | 1.0137 | -0.0010 | 0.0444 | 0.7664 | ✓ Stable |

**Finding MEASURE-02 (High):** Statistically significant model drift detected in 3 of 5 locations. Critically, drift is concentrated in the three lower-income zip codes (70112, 70115, 70118) while the two higher-income locations remain stable. This pattern — income-stratified drift — is not consistent with random performance variation. It suggests the model's feedback mechanisms are amplifying income-correlated signals over time.

**Income-Stratified Drift = Elevated Risk Classification.** Random drift across all locations would be a technical finding. Drift that tracks income demographics is a potential legal finding.

---

## MEASURE 2.8 — Adversarial / Disparity Testing

### Item-Level Staple vs. Premium Disparity

Essential and staple menu items (lower-cost, high-frequency) are weighted more heavily in consumer protection assessment. A bias pattern on staple items affects food affordability for the most price-sensitive customers.

| Item | Category | Low-Income Ratio | High-Income Ratio | Gap | Risk Weight | Status |
|---|---|---|---|---|---|---|
| Jambalaya | Staple | 1.024 | 1.018 | +0.56% | High | ✓ |
| Red Beans | Staple | 1.010 | 1.013 | -0.25% | High | ✓ |
| Shrimp Po-boy | Mid-tier | 1.018 | 1.013 | +0.54% | Medium | ✓ |
| Gumbo | Mid-tier | 1.018 | 1.016 | +0.18% | Medium | ✓ |
| Beignets | Staple/Dessert | 1.022 | 1.008 | +1.35% | High | ✓ |

**Finding MEASURE-03 (Low-Moderate):** All item-level gaps are within acceptable bounds (<2% threshold for individual items). However, the Beignets gap of +1.35% warrants monitoring — it is the highest per-item disparity and applies to a staple-category dessert item. No action required at current levels; include in next quarterly review.

---

## Remediation Requirements

| Finding ID | Severity | Required Action | Owner | Deadline |
|---|---|---|---|---|
| MEASURE-01 | Moderate | Add income-segment fairness constraint to model retraining | AI Model Owner | 60 days |
| MEASURE-02 | High | Initiate model retraining review; implement monthly KS-test monitoring | AI Model Owner + Ops Lead | 30 days |
| MEASURE-03 | Low | Monitor Beignets disparity in next quarterly audit | Ops Lead | Next quarterly review |
| MAP GP-04 | Critical | Implement human override capability and price alerting | CTO / Engineering | 30 days |

---

## MEASURE Report Attestation

This report documents the results of a systematic quantitative assessment of the dynamic pricing AI model's compliance with consumer protection fair-pricing standards. Findings are based on 180 days of model output data analyzed using established statistical methods (KS-test, Pearson correlation) against documented thresholds.

**Current Compliance Status:** CONDITIONAL PASS
**Compliance Breach Risk Horizon:** 2 quarters without remediation
**Next Scheduled Review:** September 30, 2024

| Role | Name | Date |
|---|---|---|
| AI Audit Lead | __________________ | __________ |
| AI Risk Owner | __________________ | __________ |
| Legal / Compliance Review | __________________ | __________ |

---

*Prepared under: NIST AI Risk Management Framework Rev. 1*
*Controls mapped: MEASURE 2.3, 2.6, 2.8 | Supporting: MAP 5.1, MANAGE 4.1*
