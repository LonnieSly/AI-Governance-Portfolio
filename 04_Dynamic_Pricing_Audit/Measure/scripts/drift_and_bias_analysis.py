"""
Dynamic Pricing AI Audit Suite
================================
Audit Framework: NIST AI RMF — MAP 5.1, MEASURE 2.3, MEASURE 2.6
Scenario: Multi-unit restaurant group dynamic pricing model
Purpose: Detect model drift and geographic/socioeconomic pricing bias

Auditor's Question: Is the pricing model encoding zip code-level bias,
and has its behavior shifted materially over the 6-month audit window?
"""

import numpy as np
import pandas as pd
from scipy import stats
from datetime import datetime, timedelta
import json
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────
# SECTION 0: SYNTHETIC DATA GENERATION
# Simulates 6 months of dynamic pricing outputs across 5 restaurant
# locations in zip codes with varying median household incomes.
# In a real audit, this is replaced with POS/model output exports.
# ─────────────────────────────────────────────────────────────────

np.random.seed(42)

ZIP_PROFILES = {
    "70112": {"label": "Lower-income urban",   "median_hhi": 28000,  "base_price_modifier": 1.00},
    "70115": {"label": "Mixed-income",         "median_hhi": 45000,  "base_price_modifier": 1.00},
    "70118": {"label": "Middle-income",        "median_hhi": 62000,  "base_price_modifier": 1.00},
    "70124": {"label": "Upper-middle suburban","median_hhi": 87000,  "base_price_modifier": 1.00},
    "70131": {"label": "High-income suburban", "median_hhi": 115000, "base_price_modifier": 1.00},
}

MENU_ITEMS = {
    "Jambalaya":     10.99,
    "Red Beans":      8.99,
    "Shrimp Po-boy": 12.99,
    "Gumbo":         11.99,
    "Beignets":       5.99,
}

def generate_pricing_data(n_days=180, bias_introduced_at_day=90):
    """
    Generate synthetic model pricing outputs over 6 months.
    Introduces subtle upward price drift in lower-income zip codes
    starting at day 90 — simulating a bias pattern an audit should catch.
    """
    records = []
    start_date = datetime(2024, 1, 1)

    for day in range(n_days):
        current_date = start_date + timedelta(days=day)
        month = current_date.month
        is_post_drift = day >= bias_introduced_at_day

        for zip_code, zip_info in ZIP_PROFILES.items():
            for item, base_price in MENU_ITEMS.items():
                # Legitimate demand-based adjustments (time, season)
                hour_factor = np.random.choice([0.95, 1.00, 1.05, 1.10], p=[0.2, 0.4, 0.3, 0.1])
                seasonal = 1.03 if month in [11, 12] else 1.0

                # Model drift: post day-90, lower-income zips get
                # progressively higher price adjustments — a bias signal
                drift_penalty = 0.0
                if is_post_drift:
                    income_rank = sorted(ZIP_PROFILES.keys(), 
                                         key=lambda z: ZIP_PROFILES[z]["median_hhi"]).index(zip_code)
                    # Lower income rank = larger (unfair) upward drift
                    drift_penalty = (4 - income_rank) * 0.004 * (day - bias_introduced_at_day) / 90

                final_price = base_price * hour_factor * seasonal * (1 + drift_penalty)
                final_price = round(final_price + np.random.normal(0, 0.05), 2)

                records.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "month": month,
                    "day_num": day,
                    "zip_code": zip_code,
                    "zip_label": zip_info["label"],
                    "median_hhi": zip_info["median_hhi"],
                    "item": item,
                    "base_price": base_price,
                    "model_price": max(final_price, base_price * 0.90),
                    "price_ratio": round(max(final_price, base_price * 0.90) / base_price, 4),
                    "post_drift_period": is_post_drift,
                })
    return pd.DataFrame(records)


# ─────────────────────────────────────────────────────────────────
# SECTION 1: MODEL DRIFT DETECTION
# NIST AI RMF: MEASURE 2.6 — Performance metrics tracked over time
#
# Auditor's Test: Has the distribution of price ratios shifted
# significantly between Period 1 (months 1-3) and Period 2 (months 4-6)?
# KS-test provides statistical evidence for or against drift.
# ─────────────────────────────────────────────────────────────────

def detect_model_drift(df):
    """
    Kolmogorov-Smirnov test on price ratio distributions.
    Period 1 = first 90 days (baseline). Period 2 = days 91-180.
    A statistically significant shift = evidence of model drift.
    """
    print("\n" + "="*65)
    print("MEASURE 2.6 — MODEL DRIFT DETECTION")
    print("Test: Kolmogorov-Smirnov (KS) on Price Ratio Distributions")
    print("="*65)

    drift_results = {}

    for zip_code in df["zip_code"].unique():
        zip_df = df[df["zip_code"] == zip_code]
        period1 = zip_df[~zip_df["post_drift_period"]]["price_ratio"]
        period2 = zip_df[ zip_df["post_drift_period"]]["price_ratio"]

        ks_stat, p_value = stats.ks_2samp(period1, period2)
        drift_detected = p_value < 0.05
        label = df[df["zip_code"] == zip_code]["zip_label"].iloc[0]

        drift_results[zip_code] = {
            "zip_label": label,
            "median_hhi": ZIP_PROFILES[zip_code]["median_hhi"],
            "p1_mean_ratio": round(period1.mean(), 4),
            "p2_mean_ratio": round(period2.mean(), 4),
            "delta": round(period2.mean() - period1.mean(), 4),
            "ks_statistic": round(ks_stat, 4),
            "p_value": round(p_value, 6),
            "drift_detected": drift_detected,
            "flag": "⚠ DRIFT DETECTED" if drift_detected else "✓ Stable",
        }

        print(f"\nZip {zip_code} | {label}")
        print(f"  Period 1 Avg Price Ratio: {period1.mean():.4f}")
        print(f"  Period 2 Avg Price Ratio: {period2.mean():.4f}")
        print(f"  Delta:                   +{period2.mean() - period1.mean():.4f}")
        print(f"  KS Statistic:             {ks_stat:.4f}")
        print(f"  P-Value:                  {p_value:.6f}")
        print(f"  Verdict:                  {'⚠ DRIFT DETECTED (p<0.05)' if drift_detected else '✓ No significant drift'}")

    return drift_results


# ─────────────────────────────────────────────────────────────────
# SECTION 2: ZIP CODE BIAS ANALYSIS
# NIST AI RMF: MAP 5.1 — Impact on affected groups
#              MEASURE 2.3 — Bias evaluation across segments
#
# Auditor's Test: Is price_ratio inversely correlated with median HHI?
# If lower-income zips pay systematically more, that's actionable bias.
# Consumer protection standard: ≤3% disparity across geographies.
# ─────────────────────────────────────────────────────────────────

def analyze_geographic_bias(df):
    """
    Tests whether pricing correlates with zip code income level.
    Uses Pearson correlation and a disparity ratio test.
    FAIR PRICING THRESHOLD: No zip should pay >3% above the system average.
    """
    print("\n" + "="*65)
    print("MAP 5.1 / MEASURE 2.3 — GEOGRAPHIC PRICING BIAS ANALYSIS")
    print("Fair Pricing Threshold: ±3% of system average price ratio")
    print("="*65)

    DISPARITY_THRESHOLD = 0.03  # 3% — consumer protection standard

    # Period 2 only (post-drift) — this is the current model state
    period2_df = df[df["post_drift_period"]]
    zip_summary = period2_df.groupby(["zip_code", "zip_label", "median_hhi"])["price_ratio"].mean().reset_index()
    zip_summary.columns = ["zip_code", "zip_label", "median_hhi", "avg_price_ratio"]
    zip_summary = zip_summary.sort_values("median_hhi")

    system_avg = zip_summary["avg_price_ratio"].mean()
    zip_summary["deviation_from_avg"] = zip_summary["avg_price_ratio"] - system_avg
    zip_summary["pct_deviation"] = (zip_summary["deviation_from_avg"] / system_avg * 100).round(2)
    zip_summary["exceeds_threshold"] = zip_summary["deviation_from_avg"].abs() > DISPARITY_THRESHOLD

    print(f"\nSystem Average Price Ratio (Period 2): {system_avg:.4f}")
    print(f"\n{'Zip':<8} {'Income Label':<25} {'Median HHI':>10} {'Avg Ratio':>10} {'% Dev':>8} {'Status'}")
    print("-"*80)

    bias_findings = []
    for _, row in zip_summary.iterrows():
        status = "⚠ EXCEEDS THRESHOLD" if row["exceeds_threshold"] else "✓ Within bounds"
        print(f"{row['zip_code']:<8} {row['zip_label']:<25} ${row['median_hhi']:>9,} "
              f"{row['avg_price_ratio']:>10.4f} {row['pct_deviation']:>7.2f}% {status}")
        if row["exceeds_threshold"]:
            bias_findings.append(row.to_dict())

    # Pearson correlation: HHI vs price ratio
    corr, p_val = stats.pearsonr(zip_summary["median_hhi"], zip_summary["avg_price_ratio"])
    print(f"\nPearson Correlation (HHI vs Price Ratio): {corr:.4f} (p={p_val:.4f})")

    if corr < -0.5 and p_val < 0.05:
        print("⚠ FINDING: Significant negative correlation detected.")
        print("  Lower-income zip codes are receiving higher price adjustments.")
        print("  This pattern constitutes evidence of geographic pricing bias.")
    elif abs(corr) < 0.3:
        print("✓ No meaningful correlation between income level and price ratio.")

    return zip_summary, bias_findings, {"pearson_r": corr, "p_value": p_val}


# ─────────────────────────────────────────────────────────────────
# SECTION 3: ITEM-LEVEL DISPARITY ANALYSIS
# Tests whether bias is concentrated in specific menu items
# (e.g., staple/essential items vs. premium items)
# ─────────────────────────────────────────────────────────────────

def item_level_disparity(df):
    """
    Breaks down pricing disparity by item.
    Auditor insight: Bias on staple items (Red Beans, Beignets)
    is more harmful and legally significant than on premium items.
    """
    print("\n" + "="*65)
    print("ITEM-LEVEL DISPARITY — Lowest vs. Highest Income Zip")
    print("="*65)

    period2 = df[df["post_drift_period"]]
    low_zip  = "70112"
    high_zip = "70131"

    for item in MENU_ITEMS.keys():
        low_avg  = period2[(period2["zip_code"]==low_zip)  & (period2["item"]==item)]["price_ratio"].mean()
        high_avg = period2[(period2["zip_code"]==high_zip) & (period2["item"]==item)]["price_ratio"].mean()
        diff_pct = (low_avg - high_avg) / high_avg * 100
        flag = "⚠" if diff_pct > 2.0 else "✓"
        print(f"  {flag} {item:<20} Low-income: {low_avg:.3f} | High-income: {high_avg:.3f} | Gap: {diff_pct:+.2f}%")


# ─────────────────────────────────────────────────────────────────
# SECTION 4: AUDIT FINDINGS SUMMARY
# Produces structured findings in the format a GRC team can act on
# ─────────────────────────────────────────────────────────────────

def generate_audit_findings(drift_results, bias_findings, correlation_stats):
    print("\n" + "="*65)
    print("AUDIT FINDINGS SUMMARY")
    print("Framework: NIST AI RMF — MAP 5.1, MEASURE 2.3, MEASURE 2.6")
    print("="*65)

    drift_flags = [z for z, r in drift_results.items() if r["drift_detected"]]
    
    print(f"\nFINDING 1 — MODEL DRIFT (MEASURE 2.6)")
    if drift_flags:
        print(f"  Status:   ⚠ MATERIAL FINDING")
        print(f"  Zips affected: {', '.join(drift_flags)}")
        print(f"  Evidence: KS-test p<0.05 in {len(drift_flags)} of {len(drift_results)} locations.")
        print(f"  Observation: Drift is concentrated in lower-income zip codes,")
        print(f"               suggesting income-correlated model behavior shift.")
        print(f"  Recommendation: Initiate model retraining review per MANAGE 4.1.")
        print(f"                  Trigger: Price ratio delta >2% over 90-day window.")
    else:
        print("  Status: ✓ No material drift detected.")

    print(f"\nFINDING 2 — GEOGRAPHIC PRICING BIAS (MAP 5.1 / MEASURE 2.3)")
    if bias_findings:
        print(f"  Status:   ⚠ MATERIAL FINDING")
        print(f"  Zips exceeding ±3% fair pricing threshold: {len(bias_findings)}")
        print(f"  Pearson r = {correlation_stats['pearson_r']:.4f} (p={correlation_stats['p_value']:.4f})")
        print(f"  Observation: Negative income-to-price-ratio correlation indicates")
        print(f"               lower-income consumers face systematically higher prices.")
        print(f"  Recommendation: Engage legal counsel re: consumer protection exposure.")
        print(f"                  Add income-based fairness constraint to model retraining.")
    else:
        print("  Status: ✓ No zip codes exceed the 3% disparity threshold.")

    print(f"\nFINDING 3 — CONSUMER PROTECTION FAIR-PRICING STANDARD")
    passed = len(bias_findings) == 0
    print(f"  Compliance Status: {'✓ PASS' if passed else '⚠ FAIL — Does not meet fair-pricing standard'}")
    print(f"  Standard Applied:  ±3% geographic disparity threshold")
    print(f"  Evidence Source:   6-month model output distribution analysis")
    print(f"  Next Review:       Quarterly (per MANAGE 4.1 post-deployment monitoring)")

    print("\n" + "="*65)
    print("END OF AUDIT OUTPUT — For GRC team use only")
    print("Prepared under: NIST AI RMF Rev. 1 | Audit Date:", datetime.now().strftime("%Y-%m-%d"))
    print("="*65)


# ─────────────────────────────────────────────────────────────────
# MAIN EXECUTION
# ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\nDYNAMIC PRICING AI AUDIT SUITE")
    print("Creole Kitchen Restaurant Group — Hypothetical Audit")
    print("Generating 6 months of synthetic pricing data...\n")

    df = generate_pricing_data(n_days=180, bias_introduced_at_day=90)
    print(f"Dataset: {len(df):,} pricing records | {df['zip_code'].nunique()} locations | {df['item'].nunique()} menu items")

    drift_results = detect_model_drift(df)
    zip_summary, bias_findings, corr_stats = analyze_geographic_bias(df)
    item_level_disparity(df)
    generate_audit_findings(drift_results, bias_findings, corr_stats)
