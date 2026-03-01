# AI Risk Register

## Overview
This document details an eight-risk assessment for an LLM-powered customer service bot deployed in a multi-unit restaurant operation. Each risk includes its category, likelihood and impact ratings, specific mitigation strategies, and relevant mappings to the NIST AI Risk Management Framework (AI RMF), NIST SP 800-53, and applicable regulatory frameworks.

## Identified Risks

### Risk 1: Hallucination on Pricing or Promotion Information
*   **Category:** Technical / Operational
*   **Likelihood:** 4 | **Impact:** 5
*   **Mitigation:** RAG grounding with live POS data; confidence thresholds triggering human escalation; social media monitoring protocol for AI-attributed misinformation.
*   **NIST AI RMF:** MEASURE 2.5, MANAGE 2.2

### Risk 2: Customer PII Exposure Through Prompt Injection
*   **Category:** Technical / Legal
*   **Likelihood:** 5 | **Impact:** 5
*   **Mitigation:** Input sanitization; strict system prompt boundaries; regular red-team/adversarial testing; incident response plan for PII breach scenarios.
*   **NIST AI RMF:** GOVERN 1.4, MEASURE 2.8

### Risk 3: Biased Upselling Recommendations
*   **Category:** Ethical / Legal
*   **Likelihood:** 3 | **Impact:** 5
*   **Mitigation:** Quarterly demographic parity audits on recommendation outputs; pre-deployment bias evaluation across customer segments; social media sentiment monitoring for bias-related complaints.
*   **NIST AI RMF:** MEASURE 2.3, MAP 5.1

### Risk 4: Model Drift Degrading Complaint Resolution Quality
*   **Category:** Operational
*   **Likelihood:** 4 | **Impact:** 3
*   **Mitigation:** Quarterly model performance reviews tied to customer satisfaction KPIs; defined retraining triggers documented in governance policy.
*   **NIST AI RMF:** MANAGE 4.1, MEASURE 2.6

### Risk 5: Over-Reliance by Staff Reducing Human Oversight
*   **Category:** Operational / Governance
*   **Likelihood:** 4 | **Impact:** 5
*   **Mitigation:** Staff training on model limitations; human review required for complaint resolutions above defined dollar threshold; quarterly oversight audits tracking escalation rates and ROI impact; escalation rate treated as governance KPI.
*   **NIST AI RMF:** GOVERN 4.1, MANAGE 2.4

### Risk 6: Excessive POS Data Access Violating Least Privilege
*   **Category:** Technical / Legal
*   **Likelihood:** 4 | **Impact:** 4
*   **Mitigation:** Implement role-based access controls limiting bot to 90-day transaction window; data access scope documented and reviewed quarterly; map to AC-3 access enforcement controls.
*   **NIST AI RMF:** GOVERN 1.4, MANAGE 2.2
*   **NIST 800-53:** AC-3

### Risk 7: Complaint Data Encoding Emergent Bias Over Time
*   **Category:** Technical / Ethical
*   **Likelihood:** 3 | **Impact:** 4
*   **Mitigation:** Separate complaint training data from live operational context; establish bias drift monitoring on complaint-influenced outputs; quarterly review of model behavior changes post-complaint data ingestion.
*   **NIST AI RMF:** MEASURE 2.3, MANAGE 4.1

### Risk 8: Insufficient Order History Retention Policy Creating Legal Exposure
*   **Category:** Legal / Governance
*   **Likelihood:** 4 | **Impact:** 5
*   **Mitigation:** Define and document data retention schedule (recommended: 90-day active access, 12-month archive, deletion thereafter); restrict bot access to archived data; align policy with applicable state privacy laws.
*   **NIST AI RMF:** GOVERN 1.7
*   **Regulatory alignment:** CCPA, state privacy frameworks
