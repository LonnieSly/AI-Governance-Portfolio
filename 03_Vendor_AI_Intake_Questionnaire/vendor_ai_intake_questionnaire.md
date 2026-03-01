# Vendor AI Intake Questionnaire

| | |
|---|---|
| **Organization** | [Company Name] |
| **Prepared by** | Operations & Compliance Lead |
| **Framework Alignment** | NIST AI RMF (GOVERN, MAP, MEASURE, MANAGE) |
| **Vendor Name** | [To be completed by vendor] |
| **Product / System Name** | [To be completed by vendor] |
| **Completion Date** | [To be completed by vendor] |
| **Vendor Contact** | [Name, Title, Email] |

---

> **Instructions for Vendors:** Please respond to all questions thoroughly and attach supporting documentation where indicated. Incomplete responses will be flagged for follow-up before procurement evaluation proceeds. Responses are subject to verification and may be incorporated by reference into the final contract.

---

## Section 1: Model & Technology

**Q1. Describe the AI model or system being proposed, including its primary function, the type of model architecture used, and any third-party model components or foundation models it relies on.**

*Why This Matters: Vendors sometimes build on top of foundation models (GPT-4, Gemini, Claude, etc.) without proactive disclosure. Understanding the underlying architecture — and any third-party dependencies — is essential for assessing known limitations, governance concerns, and the extent of the vendor's actual control over system behavior.*

---

**Q2. What data was used to train the model? Was any proprietary, customer, or third-party data used in training, and if so, under what authorization?**

*Why This Matters: Training data determines bias exposure and potential intellectual property liability. A model trained on unlicensed or scraped data carries different risk characteristics than one trained on curated, consented datasets. This question establishes the vendor's data provenance accountability.*

---

**Q3. How does the model handle queries that fall outside its training domain or knowledge boundaries? Does the system have a defined, documented behavior for uncertainty or low-confidence outputs?**

*Why This Matters: This is the hallucination risk assessment question. A system that generates confident responses regardless of certainty creates significant liability in customer-facing deployments. Vendors who cannot clearly answer this question are selling systems with no internal accuracy guardrail.*

---

**Q4. Has the model been evaluated for bias across demographic, linguistic, or socioeconomic groups? If so, provide the evaluation methodology, datasets used, and most recent results.**

*Why This Matters: Bias inherited from training data becomes organizational liability when the model is deployed in customer-facing or operational contexts. Pre-deployment bias evaluation is a baseline expectation for responsible AI deployment.*

---

**Q4b. Which POS systems does the solution natively integrate with for real-time data exchange? For non-native integrations, what is the implementation burden on the purchasing organization's staff, and what are the known data latency or integrity limitations?**

*Why This Matters: Non-native integrations introduce data pipeline gaps where the AI system may operate on delayed or incomplete operational data. In a restaurant context, data latency can cause the system to act on stale or anomalous POS records — including void transactions — without the operational context needed to interpret them correctly.*

---

## Section 2: Data Practices

**Q5. What customer or operational data will the vendor's system collect, process, or store during normal operation? Where is this data stored, in what jurisdiction, and under what security classification?**

*Why This Matters: Data jurisdiction determines which privacy laws apply. Data stored in the EU is subject to GDPR regardless of where the purchasing organization is headquartered. Data residency must be explicitly defined and contractually governed.*

---

**Q6. Is customer or operational data used to retrain, fine-tune, or otherwise improve the vendor's model? If so, can the purchasing organization opt out, and is this disclosed in the terms of service?**

*Why This Matters: Many SaaS AI vendors use customer interactions to improve their commercial models by default. For multi-unit restaurant operations, this creates three distinct risk layers: direct CCPA exposure from customer PII, competitive intelligence risk from behavioral and transactional POS data aggregated across locations, and multi-jurisdictional privacy complexity from customers covered by different state privacy frameworks. Opt-out availability and terms must be contractually documented.*

---

**Q7. What is the vendor's data retention policy for data processed through the system? What are the documented deletion procedures and timelines upon contract termination or customer data rights request?**

*Why This Matters: Contractual assurance is required that customer data does not persist in vendor systems after the business relationship ends. Undefined retention is undefined liability.*

---

**Q8. Does the vendor have a Data Processing Agreement (DPA) available? Does it comply with CCPA, applicable state privacy regulations, and GDPR where relevant? Please attach or provide a link to the current DPA.**

*Why This Matters: A DPA is the legal instrument governing how a vendor handles organizational data. Absence of a DPA means absence of contractual data protection — this is a procurement blocker.*

---

## Section 3: Security & Access

**Q9. What access controls govern which vendor personnel can access data processed through the system? Has internal access control been independently audited? Provide the most recent audit summary or certification.**

*Why This Matters: Customer PII in a vendor system is only as secure as that vendor's internal access governance. Independent audit documentation is the minimum acceptable evidence of control effectiveness.*

---

**Q10. Has the system been tested for adversarial inputs, including prompt injection attacks designed to extract protected data or manipulate system behavior? Provide the testing methodology, scope, and most recent testing date.**

*Why This Matters: Customer-facing LLMs are active targets for adversarial input attacks. A system that has not been red-teamed for prompt injection represents a known, unmitigated vulnerability. This is a direct prerequisite for deployment in any environment where customer PII is accessible.*

---

**Q11. What is the vendor's incident response process in the event of a data breach involving customer data processed through the system? What are the notification timelines to the purchasing organization, and do they meet applicable regulatory requirements (typically 72 hours)?**

*Why This Matters: Most state privacy laws require breach notification within 72 hours. Vendor incident response timelines that do not meet this threshold create regulatory exposure for the purchasing organization that cannot be contractually transferred.*

---

## Section 4: Performance & Reliability

**Q12. How does the vendor monitor for model drift post-deployment? What performance metrics are tracked, what thresholds trigger intervention, and who within the vendor organization is notified and accountable?**

*Why This Matters: A model without documented drift monitoring will degrade over time with no warning mechanism. Drift accountability — including who owns detection and response — must be established contractually before deployment.*

---

**Q13. What is the vendor's documented accuracy or performance benchmark for this system? Provide the evaluation methodology, dataset characteristics, and the date of most recent benchmark assessment.**

*Why This Matters: Vendor performance claims in sales materials are frequently measured under ideal conditions using curated datasets. Understanding the methodology is necessary to evaluate whether the benchmark is meaningful for the purchasing organization's actual use case and data environment.*

---

**Q14. What is the system's defined uptime SLA? What compensation or remediation is provided for downtime that affects purchasing organization operations?**

*Why This Matters: For operational AI tools, downtime has direct revenue and customer experience impact. Uptime commitments and remediation terms must be contractually defined and financially meaningful.*

---

**Q14b. What is the vendor's support response protocol during system outages occurring during peak operational hours (e.g., Friday–Sunday evenings for restaurant operations)? Is dedicated real-time support available during these windows, and what is the guaranteed response time for critical system failures?**

*Why This Matters: A standard 24-hour support response window is operationally inadequate when system failure during peak service hours creates immediate staff burden, customer impact, and revenue loss. Peak-hour support coverage must be explicitly addressed in the service agreement.*

---

## Section 5: Compliance & Legal

**Q15. What regulatory frameworks does the vendor's system currently comply with? Provide available documentation or third-party certifications (e.g., SOC 2 Type II, ISO 27001, HIPAA, EU AI Act conformity assessment).**

*Why This Matters: Third-party certifications are not guarantees but they signal governance maturity, establish contractual reference points, and provide evidentiary basis for the purchasing organization's own compliance posture.*

---

**Q16. If the system produces an output that causes harm to a customer — financial, reputational, or physical — what is the vendor's stated liability position? Is contractual indemnification available for AI-generated harm?**

*Why This Matters: This is the question most procurement processes skip and most vendors hope is not asked. Liability for AI-generated harm must be defined before deployment when organizational leverage exists. Post-incident liability negotiation is categorically less favorable. This question's answer directly shapes contract terms.*

---

**Q17. Has this system or the vendor organization been subject to any regulatory investigation, enforcement action, legal proceeding, or significant documented customer complaint related to AI system behavior in the past 24 months? If yes, provide a summary and resolution status.**

*Why This Matters: Undisclosed regulatory or legal history is a material omission in a vendor assessment. Past enforcement is a leading indicator of governance culture — organizations that have faced regulatory action without adequate resolution represent elevated ongoing risk.*

---

## Section 6: Governance & Oversight

**Q18. Does the vendor have a published AI ethics policy, responsible AI framework, or equivalent governance documentation? If so, please provide or attach.**

*Why This Matters: A vendor with no documented AI ethics position is making AI development and deployment decisions without governance guardrails. That governance gap becomes the purchasing organization's inherited risk.*

---

**Q19. What human oversight mechanisms are built into the system? Can human review be configured as a required step before the system takes consequential actions — such as issuing a refund, resolving a complaint, or communicating a policy decision to a customer?**

*Why This Matters: Human-in-the-Loop configurability is a core governance requirement for high-stakes AI deployments. A system that cannot support configurable human oversight checkpoints may be unsuitable for operational contexts where AI error carries meaningful financial or reputational consequences.*

---

**Q20. Who within the vendor organization holds named accountability for this AI system's behavior post-deployment? What is the escalation path if the purchasing organization identifies a performance failure, ethical concern, or compliance issue after go-live?**

*Why This Matters: Accountability without a named person and a defined escalation process is not accountability — it is organizational diffusion of responsibility. This is the most important governance question in any vendor assessment: if something goes wrong, who answers for it, and how do we reach them? A vendor who cannot answer Q20 clearly has not assigned real accountability for their system's behavior.*

---

## Vendor Assessment Summary

*To be completed by [Company Name] Compliance Lead following vendor response review.*

| Domain | Assessment | Notes |
|---|---|---|
| Model & Technology | Pass / Conditional / Fail | |
| Data Practices | Pass / Conditional / Fail | |
| Security & Access | Pass / Conditional / Fail | |
| Performance & Reliability | Pass / Conditional / Fail | |
| Compliance & Legal | Pass / Conditional / Fail | |
| Governance & Oversight | Pass / Conditional / Fail | |
| **Overall Recommendation** | **Proceed / Conditional / Do Not Proceed** | |

**Red Flags Identified:**

**Conditions Required Before Procurement Approval:**

**Reviewed by:** _________________________________ **Date:** _____________
