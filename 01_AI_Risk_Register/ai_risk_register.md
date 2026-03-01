# AI Risk Register
**Deployment Scenario:** LLM-Powered Customer Service Bot — Multi-Unit Restaurant Operation
**Framework:** NIST AI RMF (MAP / MEASURE / MANAGE)
**Version:** 1.0
**Prepared by:** Lionel Sylvester
**Review Cycle:** Quarterly

---

## Rating Scale

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Rare — unlikely under normal conditions | Minimal — negligible operational or reputational effect |
| 2 | Unlikely — possible but not expected | Minor — limited, easily recoverable harm |
| 3 | Possible — could occur under foreseeable conditions | Moderate — notable harm requiring meaningful response |
| 4 | Likely — expected to occur in normal operation | Significant — material financial, legal, or reputational damage |
| 5 | Near Certain — expected to occur regularly | Severe — major legal liability, brand crisis, or safety event |

---

## Risk Register

### Risk 1: Hallucination on Pricing or Promotion Information

| Field | Detail |
|---|---|
| **Category** | Technical / Operational |
| **Likelihood** | 4 |
| **Impact** | 5 |
| **Risk Score** | 20 |

**Description:**
The model generates confident but factually incorrect pricing, promotional offers, or menu availability information. In a restaurant context, incorrect promotions can spread rapidly through social media before the operations team is aware, creating a secondary reputational impact that compounds the direct financial liability.

**Mitigation:**
- Ground the model with RAG connected to live POS and menu data
- Implement confidence thresholds below which the bot escalates to a human agent
- Establish social media monitoring protocol for AI-attributed misinformation
- Require human approval for any promotional content surfaced by the bot

**NIST AI RMF Mapping:** MEASURE 2.5 (accuracy evaluation), MANAGE 2.2 (human escalation protocols)

---

### Risk 2: Customer PII Exposure Through Prompt Injection

| Field | Detail |
|---|---|
| **Category** | Technical / Legal |
| **Likelihood** | 5 |
| **Impact** | 5 |
| **Risk Score** | 25 |

**Description:**
Adversarial users manipulate the bot through crafted inputs to extract customer order history, contact details, or payment patterns. Worst-case likelihood posture is applied here: when impact is severe and legal consequences are irreversible, underestimating probability carries unacceptable organizational risk.

**Mitigation:**
- Input sanitization and strict system prompt boundary enforcement
- Regular red-team and adversarial testing with documented results
- Incident response plan specific to PII breach via AI system
- Quarterly penetration testing log maintained and reviewed by compliance lead

**NIST AI RMF Mapping:** GOVERN 1.4 (organizational risk policies), MEASURE 2.8 (adversarial testing)
**NIST SP 800-53:** SI-10 (Information Input Validation)

---

### Risk 3: Biased Upselling Recommendations

| Field | Detail |
|---|---|
| **Category** | Ethical / Legal |
| **Likelihood** | 3 |
| **Impact** | 5 |
| **Risk Score** | 15 |

**Description:**
The model's upselling recommendations reflect demographic or socioeconomic bias embedded in historical purchase patterns. A single viral social media post documenting biased recommendation behavior can trigger reputational and regulatory consequences simultaneously, particularly given the speed at which restaurant review content spreads.

**Mitigation:**
- Pre-deployment bias evaluation across customer segments
- Quarterly demographic parity audits on recommendation outputs
- Social media sentiment monitoring with AI-specific flagging keywords
- Defined threshold for recommendation disparity that triggers immediate review

**NIST AI RMF Mapping:** MEASURE 2.3 (bias evaluation), MAP 5.1 (impact assessment on affected groups)

---

### Risk 4: Model Drift Degrading Complaint Resolution Quality

| Field | Detail |
|---|---|
| **Category** | Operational |
| **Likelihood** | 4 |
| **Impact** | 3 |
| **Risk Score** | 12 |

**Description:**
Menu changes, seasonal items, policy updates, and shifting customer language patterns are not reflected in a static model. Complaint resolutions become increasingly misaligned with current operations, increasing staff intervention burden and degrading customer satisfaction scores over time.

**Mitigation:**
- Quarterly model performance reviews tied to customer satisfaction KPIs
- Defined retraining triggers documented in governance policy (e.g., >10% complaint escalation rate increase)
- Drift monitoring dashboard reviewed by operations lead monthly

**NIST AI RMF Mapping:** MANAGE 4.1 (post-deployment monitoring), MEASURE 2.6 (performance metrics)

---

### Risk 5: Over-Reliance by Staff Reducing Human Oversight

| Field | Detail |
|---|---|
| **Category** | Operational / Governance |
| **Likelihood** | 4 |
| **Impact** | 5 |
| **Risk Score** | 20 |

**Description:**
Automation bias — the documented tendency for humans to defer to automated systems even when outputs appear incorrect — leads staff to accept bot resolutions without review. This creates a governance failure where HITL controls exist on paper but not in practice, with direct ROI impact as incorrect resolutions compound undetected.

**Mitigation:**
- Staff training on model limitations and documented failure modes
- Mandatory human review for all complaint resolutions above defined dollar threshold
- Quarterly oversight audits tracking escalation rates as a governance KPI
- ROI impact tracking for bot-initiated resolutions versus human-reviewed resolutions

**NIST AI RMF Mapping:** GOVERN 4.1 (organizational culture for oversight), MANAGE 2.4 (HITL requirements)

---

### Risk 6: Excessive POS Data Access Violating Least Privilege

| Field | Detail |
|---|---|
| **Category** | Technical / Legal |
| **Likelihood** | 4 |
| **Impact** | 4 |
| **Risk Score** | 16 |

*Identified from operational domain expertise.*

**Description:**
The bot has access to full POS transaction history when only a 90-day window is needed for routine customer service functions. Unrestricted access violates the principle of least privilege and increases breach impact if the system is compromised. It also creates unnecessary CCPA exposure for historical customer behavioral data.

**Mitigation:**
- Implement role-based access controls limiting bot to 90-day active transaction window
- Data access scope documented, approved, and reviewed quarterly
- Archive access requires separate authorization with audit logging
- Align with Data Retention Policy (Risk 8)

**NIST AI RMF Mapping:** GOVERN 1.4 (organizational risk policies), MANAGE 2.2 (access control requirements)
**NIST SP 800-53:** AC-3 (Access Enforcement)

---

### Risk 7: Complaint Data Encoding Emergent Bias Over Time

| Field | Detail |
|---|---|
| **Category** | Technical / Ethical |
| **Likelihood** | 3 |
| **Impact** | 4 |
| **Risk Score** | 12 |

*Identified from operational domain expertise.*

**Description:**
High complaint volume fed into the model's operational context skews its behavior post-deployment — treating customers as adversarial, over-compensating with discounts, or encoding complaint patterns as demographic signals. This is an emergent risk: it does not exist at deployment but develops over time as the model is exposed to operational data. It will not be caught by pre-deployment testing alone.

**Mitigation:**
- Separate complaint training data from live operational context
- Establish bias drift monitoring on complaint-influenced outputs
- Quarterly review of model behavior changes following significant complaint volume spikes
- Flag unusual discount or compensation patterns for human review

**NIST AI RMF Mapping:** MEASURE 2.3 (bias evaluation), MANAGE 4.1 (post-deployment monitoring)

---

### Risk 8: Insufficient Order History Retention Policy Creating Legal Exposure

| Field | Detail |
|---|---|
| **Category** | Legal / Governance |
| **Likelihood** | 4 |
| **Impact** | 5 |
| **Risk Score** | 20 |

*Identified from operational domain expertise.*

**Description:**
The absence of a defined data retention boundary for customer order history accessed by the bot creates CCPA and state privacy law exposure. Without a documented retention schedule, there is no contractual or policy basis for limiting data persistence, no deletion procedure, and no defensible response to a customer data rights request.

**Mitigation:**
- Define and document data retention schedule: 90-day active access → 12-month archive → deletion
- Restrict bot access to active window only; archived data requires separate authorization
- Align retention policy with applicable state privacy frameworks
- Include retention requirements in Vendor DPA for any third-party AI tools

**NIST AI RMF Mapping:** GOVERN 1.7 (data governance policies)
**Regulatory Alignment:** CCPA, applicable state privacy frameworks

---

## Risk Summary Matrix

| Risk | Category | Likelihood | Impact | Score | Priority |
|---|---|---|---|---|---|
| R2: PII Exposure via Prompt Injection | Technical / Legal | 5 | 5 | 25 | Critical |
| R1: Hallucination on Pricing | Technical / Operational | 4 | 5 | 20 | Critical |
| R5: Staff Over-Reliance | Operational / Governance | 4 | 5 | 20 | Critical |
| R8: Retention Policy Gap | Legal / Governance | 4 | 5 | 20 | Critical |
| R6: Excessive POS Data Access | Technical / Legal | 4 | 4 | 16 | High |
| R3: Biased Upselling | Ethical / Legal | 3 | 5 | 15 | High |
| R4: Model Drift | Operational | 4 | 3 | 12 | Medium |
| R7: Complaint Data Bias | Technical / Ethical | 3 | 4 | 12 | Medium |

---

## Key Findings

Four risks score at Critical level (20+) and should be addressed before deployment authorization. The most significant is **Risk 2 (PII Exposure via Prompt Injection)** at a score of 25 — the only risk rated Likelihood 5 — reflecting that customer-facing LLMs are active targets for adversarial input attacks and the legal consequences of a breach are severe. **Risk 8 (Retention Policy Gap)** represents a pre-existing legal exposure that exists independent of deployment and should be resolved immediately regardless of deployment timeline.

The three operationally-derived risks (6, 7, 8) would not appear in a standard framework-generated register. They reflect domain-specific knowledge of how restaurant POS data, complaint workflows, and customer history interact with AI system behavior — and they represent the highest-value additions a governance professional with operational experience brings to an assessment.
