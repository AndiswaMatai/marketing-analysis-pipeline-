"""
Unifies Google Ads, GA360, and Salesforce extracts on (date, campaign_id)
and computes the KPIs that actually drive marketing/exec decisions:
CTR, CPA, ROAS, conversion rate, and churn rate.
"""
from pathlib import Path

import pandas as pd

RAW = Path(__file__).resolve().parent.parent / "data" / "raw"
PROCESSED = Path(__file__).resolve().parent.parent / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)


def load_sources():
    ads = pd.read_csv(RAW / "google_ads.csv")
    ga = pd.read_csv(RAW / "ga360.csv")
    sf = pd.read_csv(RAW / "salesforce.csv")
    return ads, ga, sf


def unify(ads, ga, sf):
    df = ads.merge(ga, on=["date", "campaign_id"], how="left") \
            .merge(sf, on=["date", "campaign_id"], how="left")
    return df


def compute_kpis(df):
    df = df.copy()
    df["ctr"] = (df["clicks"] / df["impressions"]).round(4)
    df["cpa"] = (df["cost"] / df["conversions"].replace(0, float("nan"))).round(2)
    df["roas"] = (df["revenue"] / df["cost"]).round(2)
    df["conversion_rate"] = (df["conversions"] / df["sessions"]).round(4)
    df["churn_rate"] = (df["churned_subscribers"] / df["new_subscribers"].replace(0, float("nan"))).round(4)
    return df


def aggregate_by_campaign(df):
    agg = df.groupby("campaign_name").agg(
        impressions=("impressions", "sum"),
        clicks=("clicks", "sum"),
        cost=("cost", "sum"),
        sessions=("sessions", "sum"),
        conversions=("conversions", "sum"),
        new_subscribers=("new_subscribers", "sum"),
        churned_subscribers=("churned_subscribers", "sum"),
        revenue=("revenue", "sum"),
    ).reset_index()
    agg["ctr"] = (agg["clicks"] / agg["impressions"]).round(4)
    agg["cpa"] = (agg["cost"] / agg["conversions"]).round(2)
    agg["roas"] = (agg["revenue"] / agg["cost"]).round(2)
    agg["churn_rate"] = (agg["churned_subscribers"] / agg["new_subscribers"]).round(4)
    return agg.sort_values("revenue", ascending=False)


def run():
    ads, ga, sf = load_sources()
    unified = unify(ads, ga, sf)
    with_kpis = compute_kpis(unified)
    by_campaign = aggregate_by_campaign(with_kpis)

    with_kpis.to_csv(PROCESSED / "daily_unified.csv", index=False)
    by_campaign.to_csv(PROCESSED / "campaign_summary.csv", index=False)
    return with_kpis, by_campaign


if __name__ == "__main__":
    daily, summary = run()
    print(f"Unified {len(daily)} daily campaign rows across 3 sources.")
    print("\nCampaign summary:")
    print(summary.to_string(index=False))
