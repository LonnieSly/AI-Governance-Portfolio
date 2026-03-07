# Project 4a: Dynamic Pricing AI — MAP Risk Assessment

## Scenario

A multi-unit restaurant group operates an **AI-driven dynamic pricing model** that adjusts menu prices in near-real-time based on demand signals, time-of-day patterns, and location-level inputs. Prices are pushed to customer-facing menus automatically, with no human review gate before display.

The audit question driving this assessment: **Is the model encoding geographic or socioeconomic bias — and how would we prove it either way?**

This MAP assessment was developed as the entry point for a full NIST AI RMF audit engagement. Before any statistical test is run, MAP forces the auditor to answer: *Who is affected? What could go wrong for them? And what does "going wrong" actually look like at the output level?*

---

## Methodology

This risk assessment applies the **NIST AI RMF MAP function** to identify and contextualize risks specific to this deployment before measurement begins.

The MAP function answers three questions:
- **MAP 1.1** — What is this system actually doing, and what is the gap between intended and actual use?
- **MAP 5.1** — Who is affected by this system's outputs, and what harms are plausible for each group?
- **MAP 2.1** — Can the system's decisions be explained to the people they affect?

Each risk entry includes the affected population, the nature of potential harm, a defined auditor test, and a remediation direction. Risks are scored on the same 1–5 likelihood/impact scale used in Project 1 for portfolio consistency.

---

## Key Decisions

**1. The audit scope was defined around outputs, not inputs.**
A pricing model can use entirely legitimate inputs — demand, time, location — and still produce discriminatory outputs if those inputs are correlated with protected characteristics. MAP 5.1 requires the auditor to trace the *effect on people*, not just evaluate the model's stated methodology. This is the distinction between a technical review and a governance review.

**2. Risk GP-04 (No Human Override) was rated a standalone Critical risk.**
The absence of a human override mechanism is not just an operational gap — it is a governance failure. A model with no override capability has, by design, removed human accountability from its decision loop. Under MANAGE 2.4, HITL controls are a baseline expectation for any customer-facing automated pricing system. Rating this separately ensures it cannot be bundled into a lower-priority remediation workstream.

**3. Risk GP-03 (Explainability) was included despite not being a direct pricing harm.**
Regulators do not only investigate harm — they investigate the *inability to demonstrate the absence of harm*. A system that cannot produce an audit trail for its pricing decisions fails on both dimensions. This risk was included because an auditor who can't explain why a price was set cannot defend a "no finding" conclusion either.

---

## Framework Mapping

| Risk ID | Risk Name | Risk Score | NIST AI RMF Mapping |
|---|---|---|---|
| GP-01 | Income-Correlated Price Adjustment | 20 | MAP 5.1, MEASURE 2.3 |
| GP-02 | Model Drift Encoding Bias Post-Deployment | 16 | MEASURE 2.6, MANAGE 4.1 |
| GP-03 | Pricing Decision Opacity | 15 | GOVERN 1.4, MAP 2.1 |
| GP-04 | No Human Override Capability | 20 | MANAGE 2.4 |

---

## How This Connects to the Portfolio

This MAP assessment feeds directly into **Project 4b (MEASURE Report)**. Every risk identified here has a corresponding quantitative test in the MEASURE report — the MAP function defines what to look for; the MEASURE function proves whether it's actually happening.

The progression across the portfolio follows the RMF lifecycle:

| Project | RMF Function | What It Does |
|---|---|---|
| Project 1 — Risk Register | MAP / MEASURE / MANAGE | Identifies and rates risks for an LLM customer service deployment |
| Project 2 — Acceptable Use Policy | GOVERN | Sets organizational rules and accountability structures |
| Project 3 — Vendor Intake Questionnaire | GOVERN / MAP | Evaluates third-party AI risk before procurement |
| **Project 4a — MAP Risk Assessment** | **MAP** | **Identifies geographic bias risks before measurement begins** |
| Project 4b — MEASURE Report | MEASURE | Quantitatively tests whether identified risks are materializing |

---

## Artifact

**→ [View the Full MAP Risk Assessment](./04_MAP_Risk_Assessment.md)**
