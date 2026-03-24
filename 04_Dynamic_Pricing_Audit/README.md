# Project 4: Dynamic Pricing AI Audit

## Overview

This project demonstrates a complete NIST AI RMF audit engagement across two phases:

- **Phase 1 — MAP (Map Risk Assessment):** Identifies and contextualizes bias risks specific to a dynamic pricing model before any measurement begins
- **Phase 2 — MEASURE (Audit Report):** Quantitatively tests whether identified risks are materializing through drift analysis and bias detection

---

## Project Structure

### Map_Risk_Assessment/
**NIST AI RMF MAP Function** — Risk identification and contextualization

Answers the critical questions: *Who is affected? What could go wrong? How would we detect it?*

**→ [Go to MAP Risk Assessment](./Map_Risk_Assessment/README.md)**

---

### Measure/
**NIST AI RMF MEASURE Function** — Quantitative audit and testing

Implements the auditor tests defined in MAP. Includes drift analysis engine, bias measurement reports, and remediation timeline.

**→ [Go to MEASURE Audit Report](./Measure/README.md)**

---

## The Audit Question

A dynamic pricing model passed every compliance threshold at point-in-time review. Income-correlated drift analysis revealed r = −0.89 — projecting a compliance breach within two quarters.

**Verdict:** Conditional Pass with mandatory remediation timeline.

This audit demonstrates why threshold compliance is necessary but not sufficient. Trajectory matters more than the snapshot.

---

## Framework Mapping

| Phase | NIST AI RMF Function | Deliverable |
|---|---|---|
| MAP | Identify risks and affected populations | Risk Assessment Document + Auditor Test Plan |
| MEASURE | Quantitatively test identified risks | Python Audit Engine + Bias Report + Remediation Timeline |