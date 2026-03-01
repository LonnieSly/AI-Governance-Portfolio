# Project 2: AI Acceptable Use Policy

## Scenario

The same multi-unit restaurant group deploying the LLM customer service bot needs a formal **AI Acceptable Use Policy** governing how all employees interact with approved AI tools — including a generative AI writing assistant for marketing and the customer service bot itself.

This policy needed to serve two audiences simultaneously: corporate leadership requiring formal governance documentation, and frontline staff who need clear, unambiguous guidance they can follow under operational pressure.

---

## Methodology

This policy was structured using standard AUP governance architecture — Purpose, Scope, Definitions, Approved Tools, Acceptable Use, Prohibited Use, Data Handling, Human Oversight, Violations, and Review — and then pressure-tested against real operational conditions before finalization.

The Human-in-the-Loop review process identified two significant gaps in the initial draft that required operational domain knowledge to catch:

**Gap 1 — Void Transaction SOP:** A generic policy would not address how the bot should handle POS void transactions. In restaurant operations, voids represent data anomalies that the AI system cannot interpret without operational context — creating a risk of automated refund offers or incorrect complaint responses triggered by reorder records.

**Gap 2 — Peak Hour Support Requirements:** Standard SLA language does not account for the operational reality of restaurant peak hours. An AI system that degrades or fails at 7pm on a Saturday creates a staff burden and revenue impact that requires a specific vendor support protocol — not a standard 24-hour response window.

---

## Key Decisions

**1. Whitelist approach for approved tools.**
Rather than prohibiting specific tools, the policy explicitly lists approved tools and treats everything else as implicitly prohibited. This is the standard governance posture for risk-sensitive operational environments.

**2. HITL escalation triggers grounded in operational reality.**
The escalation triggers in Section 8 (refund requests, food safety concerns, customer distress) were defined based on the actual situations where AI error causes compounding harm — not generic "high-stakes decisions" language.

**3. Data retention boundary aligned to the Risk Register.**
The 90-day active access limitation in Section 7 directly implements the mitigation for Risk 6 (Excessive POS Data Access) from the Risk Register. Policy controls and risk register entries reference each other, creating a coherent governance chain.

**4. Healthcare transferability analysis.**
This policy was evaluated for industry portability. Sections 6 and 7 require the most significant revision for healthcare — Section 6 needs additions for clinical decision-making prohibitions and PHI handling, and Section 7's retention schedule must align with HIPAA's 6-year minimum rather than business-driven timelines. Core structure, Sections 1–5 and 8–10, transfers across industries with terminology adjustments.

---

## Framework Alignment

| Policy Section | NIST AI RMF Function | Control Purpose |
|---|---|---|
| Section 4 (Approved Tools) | GOVERN 1.1 | Organizational AI inventory and authorization |
| Section 6 (Prohibited Use) | GOVERN 1.4 | Risk boundary definition |
| Section 7 (Data Handling) | GOVERN 1.7 | Data governance requirements |
| Section 8 (Human Oversight) | MANAGE 2.4 | HITL control implementation |
| Section 10 (Review Cycle) | MANAGE 4.1 | Post-deployment governance maintenance |

---

## Artifact

**→ [View the Full Acceptable Use Policy](./ai_acceptable_use_policy.md)**
