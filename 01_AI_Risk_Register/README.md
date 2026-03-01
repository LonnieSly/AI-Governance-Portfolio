# Project 1: AI Risk Register

## Scenario

A multi-unit restaurant group is deploying an **LLM-powered customer service bot** that handles order inquiries, complaint resolution, and upselling recommendations. The system has access to customer order history and live POS transaction data across multiple locations.

This scenario was chosen deliberately. Twenty years of restaurant operations experience informed risk identification in ways a purely academic governance approach would miss — particularly around void transaction handling, complaint data integrity, and peak-hour operational continuity.

---

## Methodology

This risk register was developed using the **NIST AI Risk Management Framework (AI RMF)** MAP and MEASURE functions as the primary structure:

- **MAP** — Identifying the context, stakeholders, and potential harms of this specific AI deployment
- **MEASURE** — Analyzing and rating identified risks by likelihood and impact
- **MANAGE** — Defining mitigation strategies and control requirements for each risk

Each risk entry includes:
- Risk category (Technical, Operational, Legal, Ethical)
- Likelihood rating (1–5)
- Impact rating (1–5)
- Mitigation strategy
- NIST AI RMF function mapping
- Where applicable, NIST SP 800-53 control mapping

---

## Key Decisions

**1. Impact ratings were adjusted upward to account for social media amplification.**
Risks 1 and 3 were initially rated at Impact 4. In a restaurant context, a hallucinated promotion or biased upselling recommendation can become a viral event before operations are aware of it. Secondary impact pathways — brand damage, review platform exposure — compounded the direct harm, justifying Impact 5 ratings.

**2. Three risks were identified from operational domain expertise, not framework checklists.**
- **Risk 6 (POS Data Access / Least Privilege):** A model with unrestricted POS history access violates data minimization principles and the AC-3 access control standard.
- **Risk 7 (Complaint Data Encoding Emergent Bias):** High complaint volume fed into the model's context can skew behavior over time — an emergent risk that doesn't exist at deployment but develops post-launch.
- **Risk 8 (Order History Retention Policy):** The absence of a defined data retention boundary creates CCPA exposure that most governance frameworks address only in general terms.

**3. Risk 2 (PII Exposure) was rated Likelihood 5 to match its Impact 5.**
For high-impact legal risks, worst-case likelihood posture is appropriate. The cost of underestimating probability on a data breach is categorically higher than the cost of over-investing in prevention.

---

## Framework Mapping Summary

| NIST AI RMF Function | Risks Addressed |
|---|---|
| GOVERN | Risks 2, 6, 8 — organizational policy, accountability, data access scope |
| MAP | Risks 3, 8 — impact assessment on affected groups, regulatory alignment |
| MEASURE | Risks 1, 2, 3, 4, 7 — accuracy evaluation, bias testing, adversarial testing, drift monitoring |
| MANAGE | Risks 1, 4, 5, 6, 7 — human escalation, post-deployment monitoring, oversight audits |

---

## Artifact

**→ [View the Full Risk Register](./ai_risk_register.md)**
