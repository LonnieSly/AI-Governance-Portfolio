# Project 4c: Dynamic Pricing AI — Disparate Impact Drift Response Protocol

## Scenario

Following the MAP Risk Assessment and MEASURE Audit Report for the restaurant group's dynamic pricing model, this protocol completes the NIST AI RMF audit loop by governing what happens when the audit finding activates in production.

The MEASURE Report established a critical finding: the model passes the ±3% geographic disparity threshold today but carries an income-correlated drift pattern (r = −0.89, p = 0.04) projecting a consumer protection breach within two quarters. This protocol answers the question the MEASURE Report leaves open — **when the KS-test fires, who does what, in what order, and how is every decision documented?**

---

## What This Protocol Governs

The Disparate Impact Drift Response Protocol (IRP-DYN-001) covers the complete incident lifecycle from trigger detection through controlled reactivation:

- **Activation criteria** — the specific statistical threshold that triggers the protocol and the false positive validation checklist that must pass before any response action is authorized
- **Incident command structure** — a four-tier succession ladder with automatic authority transfer mechanics, a named Scribe role separate from the Commander, and explicit re-engagement rules
- **2-hour response runbook** — three named phases (Detection, Decision Window, Containment) with owners and time boundaries on every action
- **Containment actions** — the Supersede → Disengage → Deactivate progression with GP-04 remediation status as the decision gate
- **Documentation standards** — the Trigger Justification Record, Activation Log Entry field standard, and record retention schedule tied to consumer protection statute of limitations
- **Return-to-production criteria** — asymmetric revalidation thresholds, a four-item safeguard checklist, and dual sign-off authority

---

## Key Decisions

**1. Supersede is the default first response — but only if the prerequisite exists.**
The protocol's first response is Supersede: the model continues running but a human review gate sits between its output and the customer-facing menu. However, Supersede requires the human override capability from GP-04 to be implemented and tested. If that remediation is incomplete at the time of trigger, the protocol skips directly to Disengage. This sequencing problem — where the ideal response depends on remediation completion — is what most IRPs miss entirely by assuming prerequisite infrastructure exists.

**2. Authority transfers automatically — not by delegation.**
The four-tier succession ladder transfers command authority if the current Incident Commander does not acknowledge the alert within 15 minutes. No delegation from the outgoing Commander is required. This eliminates the failure mode where an unreachable primary blocks the response chain waiting for permission that cannot come. The design principle came directly from restaurant operations: someone is always accountable, and the service does not stop because one person is unavailable.

**3. Activation and documentation are separated by role.**
The Incident Commander makes the call. The Incident Scribe logs it in parallel. These cannot be the same person during an active incident. A single person cannot execute a high-pressure technical decision and produce an accurate real-time record of that decision simultaneously. The Scribe role is explicitly prohibited from falling to anyone executing a containment action.

**4. Reactivation is asymmetrically harder than activation.**
The trigger threshold is p < 0.05. The reactivation clearance standard is p > 0.10. This asymmetry is intentional — it should be harder to return the model to production than it was to take it out. The 30-day controlled deployment window before full reactivation is authorized creates a canary period that the original deployment never had.

**5. The Trigger Justification Record is the primary regulatory document.**
Most IRPs focus on what happened during the response. Regulators ask first why the response was authorized. The Trigger Justification Record — five specific validation items completed before the Decision Window closes — is the pre-activation evidence package that answers that question. Without it, a defensible response reads as reactive overreach.

---

## Framework Alignment

| Protocol Section | NIST AI RMF Function | Governance Purpose |
|---|---|---|
| Section 2 — Activation Criteria | MEASURE 2.6, MEASURE 2.3 | Statistical thresholds for drift and bias detection |
| Section 3 — Command Structure | GOVERN 2.1, GOVERN 4.1 | Defined roles, responsibilities, and accountability lines |
| Section 4 — Response Runbook | MANAGE 4.1 | Post-deployment monitoring and incident response execution |
| Section 5 — Containment Actions | MANAGE 2.4 | Supersede, disengage, deactivate authority and protocol |
| Section 6 — Documentation | GOVERN 1.4, MANAGE 4.3 | Transparent documentation, audit trails, incident records |
| Section 7 — Return to Production | MANAGE 2.4, MANAGE 4.2 | Reactivation criteria and continual improvement integration |

---

## How This Connects to the Portfolio

This protocol is the third deliverable under Project 4 and completes the RMF audit loop for this engagement:

| Deliverable | RMF Function | What It Does |
|---|---|---|
| Project 4a — MAP Risk Assessment | MAP | Identifies GP-01 through GP-04 risks before measurement begins |
| Project 4b — MEASURE Report | MEASURE | Quantitatively proves whether identified risks are materializing |
| **Project 4c — Drift Response Protocol** | **MANAGE** | **Governs the response when the MEASURE finding activates in production** |

The MAP Assessment identified the risk. The MEASURE Report quantified it. This protocol closes the loop. An audit engagement that ends at the finding without a governed response is incomplete — this is what completion looks like.

---

## Artifact

**→ [View the Full Drift Response Protocol](./Disparate_Impact_Drift_Response_Protocol.docx)**
