# MAP Risk Assessment — Dynamic Pricing AI Model
**Deployment:** AI-Driven Dynamic Pricing — Multi-Unit Restaurant Group
**NIST AI RMF Function:** MAP (Categorize and Contextualize Risk)
**Version:** 1.0 | Prepared by: AI Audit Lead
**Audit Period:** January 2024 – June 2024

---

## MAP 1.1 — System Context

The dynamic pricing model adjusts menu prices in near-real-time based on demand signals, time-of-day, historical sales velocity, and location-level inputs. Pricing decisions are automated with no human review gate before customer display. The model was last retrained 7 months prior to this audit.

**Intended Use:** Revenue optimization across 5 restaurant locations.
**Actual Use Risk:** Without fairness constraints, the model optimizes purely for revenue — which can systematically disadvantage price-sensitive customers in lower-income geographies.

---

## MAP 5.1 — Affected Groups and Impact Assessment

| Affected Group | Potential Harm | Severity | Likelihood |
|---|---|---|---|
| Customers in lower-income zip codes (70112, 70115) | Pay disproportionately higher prices for the same items | High | Likely if no fairness constraint exists |
| Price-sensitive household segments | Reduced access to affordable meal options | High | Likely |
| Restaurant group (organizational) | Consumer protection regulatory exposure | Critical | Possible |
| Staff / Operations team | No visibility into pricing decisions; unable to intervene | Moderate | Near-certain without HITL controls |

**Auditor's Note:** Harm here is *structural*, not intentional. The model was not designed to discriminate — it was designed to maximize revenue. But without income-segment fairness constraints, revenue optimization and geographic equity are in direct conflict. This is the MAP function's core purpose: surface the conflict *before* it becomes a legal finding.

---

## MAP Risk Register — Geographic Pricing Bias

### Risk GP-01: Income-Correlated Price Adjustment (Primary)

| Field | Detail |
|---|---|
| **Category** | Ethical / Legal |
| **NIST AI RMF** | MAP 5.1 (impact on affected groups), MEASURE 2.3 (bias evaluation) |
| **Likelihood** | 4 — Likely |
| **Impact** | 5 — Severe |
| **Risk Score** | 20 |

**Description:** The model ingests location-level demand signals that are correlated with zip code income demographics. Because lower-income areas have more price-sensitive demand curves, the model may learn to apply higher markups during off-peak hours in these locations — inverting the intended demand-response logic.

**Audit Test:** Pearson correlation between median household income (HHI) and average price ratio across locations over the 6-month window. A negative correlation (r < -0.5, p < 0.05) is the evidentiary threshold for a material finding.

**Consumer Protection Standard Applied:** No zip code should deviate more than ±3% from the system-average price ratio for an equivalent item. This mirrors FTC fair pricing guidance on algorithmic price discrimination.

**Mitigation:**
- Add income-segment fairness constraint to model objective function
- Implement price cap rules: no location may exceed system average + 3% for equivalent items
- Human review required for any automated price change >5% above baseline

---

### Risk GP-02: Model Drift Encoding Bias Post-Deployment

| Field | Detail |
|---|---|
| **Category** | Technical / Ethical |
| **NIST AI RMF** | MEASURE 2.6 (performance over time), MANAGE 4.1 (post-deployment monitoring) |
| **Likelihood** | 4 — Likely |
| **Impact** | 4 — Significant |
| **Risk Score** | 16 |

**Description:** A model that passes pre-deployment bias testing can still drift into biased behavior as it responds to live operational data. Demand patterns, competitor pricing, and local events create feedback loops that amplify small biases over time. This risk does not exist at launch — it emerges over months.

**Audit Test:** Kolmogorov-Smirnov test comparing price ratio distributions between Period 1 (days 1–90) and Period 2 (days 91–180) by location. KS p-value < 0.05 = statistically significant drift.

**Mitigation:**
- Monthly KS-test on price distributions by zip code (automated)
- Defined drift trigger: price ratio delta > 2% over any 90-day window initiates retraining review
- Drift findings escalated to AI Risk Owner within 5 business days

---

### Risk GP-03: Lack of Pricing Decision Transparency (Explainability)

| Field | Detail |
|---|---|
| **Category** | Governance |
| **NIST AI RMF** | GOVERN 1.4 (organizational risk policies), MAP 2.1 (system transparency) |
| **Likelihood** | 5 — Near-certain |
| **Impact** | 3 — Moderate |
| **Risk Score** | 15 |

**Description:** If a customer or regulator asks "Why is this item $1.50 more expensive at this location?", the current system has no explainability mechanism. Inability to explain a pricing decision is itself a governance failure — and in states with algorithmic transparency laws, a regulatory exposure.

**Mitigation:**
- Implement model logging: every price adjustment must record its input features and decision rationale
- Customer-facing disclosure: "Prices may vary by location based on demand and availability"
- Regulatory disclosure protocol: documented process for producing pricing audit trails on request

---

### Risk GP-04: Absence of Human Override Capability

| Field | Detail |
|---|---|
| **Category** | Operational / Governance |
| **NIST AI RMF** | MANAGE 2.4 (HITL requirements) |
| **Likelihood** | 5 — Near-certain (current state) |
| **Impact** | 4 — Significant |
| **Risk Score** | 20 |

**Description:** The pricing model currently has no human-in-the-loop gate. Prices are set and displayed without operations review. A biased or anomalous pricing event can run for hours before staff become aware. In a social media environment, one screenshot of a discriminatory price can become a crisis before the operations team has breakfast.

**Mitigation:**
- Implement automated alerting: any price >10% above baseline triggers operations notification within 15 minutes
- Designated Price Review Officer for each location
- Daily pricing digest report reviewed by operations lead

---

## MAP Summary: Risk Inventory

| Risk ID | Risk Name | Score | Primary RMF Mapping |
|---|---|---|---|
| GP-01 | Income-Correlated Price Adjustment | 20 | MAP 5.1 / MEASURE 2.3 |
| GP-02 | Model Drift Encoding Bias | 16 | MEASURE 2.6 / MANAGE 4.1 |
| GP-03 | Pricing Decision Opacity | 15 | GOVERN 1.4 / MAP 2.1 |
| GP-04 | No Human Override Capability | 20 | MANAGE 2.4 |

**Total Material Risks Identified:** 4
**Risks Requiring Immediate Remediation:** GP-01, GP-04
**Next MAP Review:** Quarterly

---

*This MAP Assessment feeds directly into the MEASURE Report. Risks identified here define the specific metrics tracked in Section 3.*
