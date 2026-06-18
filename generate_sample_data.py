"""
Generates synthetic exports mimicking Google Ads, Google Analytics 360, and
Salesforce — the three source systems referenced on the CV — with enough
shared keys (campaign_id / date) to demonstrate a real unification join.
"""
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(11)
RAW = Path(__file__).resolve().parent.parent / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

CAMPAIGNS = [
    ("CMP001", "Spring Subscriptions"),
    ("CMP002", "Brand Awareness Q2"),
    ("CMP003", "Retargeting - Lapsed Users"),
    ("CMP004", "New Market Launch"),
]

start = datetime(2026, 4, 1)
google_ads, ga360, salesforce = [], [], []

for day in range(30):
    d = (start + timedelta(days=day)).strftime("%Y-%m-%d")
    for campaign_id, name in CAMPAIGNS:
        impressions = random.randint(8000, 60000)
        clicks = int(impressions * random.uniform(0.01, 0.045))
        cost = round(clicks * random.uniform(3.5, 9.0), 2)
        google_ads.append({
            "date": d, "campaign_id": campaign_id, "campaign_name": name,
            "impressions": impressions, "clicks": clicks, "cost": cost,
        })

        sessions = int(clicks * random.uniform(0.8, 1.3))
        conversions = int(sessions * random.uniform(0.01, 0.06))
        bounce_rate = round(random.uniform(0.25, 0.65), 3)
        ga360.append({
            "date": d, "campaign_id": campaign_id,
            "sessions": sessions, "conversions": conversions, "bounce_rate": bounce_rate,
        })

        new_subscribers = int(conversions * random.uniform(0.5, 0.9))
        churned_subscribers = int(new_subscribers * random.uniform(0.05, 0.2))
        revenue = round(new_subscribers * random.uniform(150, 450), 2)
        salesforce.append({
            "date": d, "campaign_id": campaign_id,
            "new_subscribers": new_subscribers, "churned_subscribers": churned_subscribers,
            "revenue": revenue,
        })

for name, rows in [("google_ads.csv", google_ads), ("ga360.csv", ga360), ("salesforce.csv", salesforce)]:
    with open(RAW / name, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)

print(f"google_ads: {len(google_ads)} | ga360: {len(ga360)} | salesforce: {len(salesforce)} rows")
