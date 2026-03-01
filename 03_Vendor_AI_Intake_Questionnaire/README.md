# Project 3: Vendor AI Intake Questionnaire

## Scenario

The same restaurant group is evaluating an external AI vendor to supply the LLM-powered customer service bot. Before signing a contract, the procurement and compliance team needs a structured assessment framework to evaluate whether the vendor's system meets the organization's governance, security, privacy, and operational standards.

This questionnaire was designed to surface the risks that most procurement processes miss — particularly around data reuse, operational continuity, and accountability — before organizational leverage is lost at contract signing.

---

## Methodology

The questionnaire is organized across **six governance domains**, each targeting a specific category of vendor risk:

| Domain | Risk Category Targeted |
|---|---|
| Model & Technology | Technical capability, architectural transparency, hallucination risk |
| Data Practices | PII handling, data reuse, retention, DPA compliance |
| Security & Access | Access controls, adversarial testing, breach response |
| Performance & Reliability | Drift monitoring, accuracy benchmarks, operational continuity |
| Compliance & Legal | Regulatory certifications, liability position, legal history |
| Governance & Oversight | Vendor AI ethics maturity, HITL configurability, accountability structure |

Each question includes a **"Why This Matters"** annotation explaining the governance reasoning behind the question. These annotations serve two purposes: they help non-technical procurement stakeholders understand what they're evaluating, and they demonstrate the risk reasoning behind each assessment criterion.

---

## Key Decisions

**1. Two questions were added from operational domain expertise.**
Standard procurement frameworks do not account for restaurant-specific operational continuity requirements. **Q14b** addresses peak-hour support response protocols — a generic SLA is insufficient when AI system downtime during a Friday dinner rush creates immediate operational and revenue impact. **Q4b** addresses POS integration depth — non-native integrations create data latency gaps that directly enable the void transaction risk identified in the Risk Register.

**2. Q6 is rated the highest-priority data practices question.**
For multi-unit restaurant operations, the PII risk in vendor data reuse is three-layered: direct CCPA exposure from customer contact data, competitive intelligence risk from behavioral POS patterns aggregated across locations, and multi-jurisdictional compliance complexity from customers covered by different state privacy laws. Most procurement teams catch the first layer. The questionnaire is designed to surface all three.

**3. The three most critical questions for any AI vendor assessment:**
- **Q20 (Accountability):** Named accountability is the load-bearing wall. Without it, every other vendor assurance is unenforceable.
- **Q1 (What Are You Buying):** You cannot govern a system you don't understand. Evasion on Q1 is itself a governance red flag.
- **Q16 (Legal Liability):** Liability must be negotiated before deployment when organizational leverage exists — not after an incident when it doesn't.

---

## Framework Alignment

| Questionnaire Domain | NIST AI RMF Function | Governance Purpose |
|---|---|---|
| Model & Technology | MAP 1.1, MEASURE 2.5 | Understand what is being deployed and its failure modes |
| Data Practices | GOVERN 1.7, MAP 5.1 | Assess privacy risk and data governance maturity |
| Security & Access | GOVERN 1.4, MEASURE 2.8 | Evaluate adversarial resilience and access controls |
| Performance & Reliability | MEASURE 2.6, MANAGE 4.1 | Assess drift monitoring and operational continuity |
| Compliance & Legal | GOVERN 1.1, MAP 5.2 | Verify regulatory alignment and liability position |
| Governance & Oversight | GOVERN 4.1, MANAGE 2.4 | Evaluate vendor AI maturity and HITL configurability |

---

## How to Use This Questionnaire

This questionnaire is designed to be sent to vendors during the procurement evaluation phase — after initial product demonstration and before contract negotiation. Vendor responses should be evaluated against the organization's documented risk appetite and reviewed by compliance and legal counsel prior to contract execution.

**Red Flags — Consider Pausing Procurement If:**
- Vendor cannot clearly answer Q1 (architectural transparency)
- Vendor has no documented response for Q6 (data reuse opt-out)
- Vendor cannot produce a DPA for Q8
- Vendor has no named accountable person for Q20
- Q17 reveals undisclosed regulatory or legal history

---

## Artifact

**→ [View the Full Vendor Intake Questionnaire](./vendor_ai_intake_questionnaire.md)**
