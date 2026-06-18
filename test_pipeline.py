"""Run with: python -m unittest discover -s tests -v"""
import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from transform import compute_kpis, aggregate_by_campaign


def _make_df():
    return pd.DataFrame([{
        "date": "2026-04-01", "campaign_id": "CMP001", "campaign_name": "Test Campaign",
        "impressions": 10000, "clicks": 300, "cost": 1200.0,
        "sessions": 280, "conversions": 14, "bounce_rate": 0.40,
        "new_subscribers": 10, "churned_subscribers": 1, "revenue": 3000.0,
    }])


class TestKPIs(unittest.TestCase):
    def test_ctr_correct(self):
        df = compute_kpis(_make_df())
        self.assertAlmostEqual(df.iloc[0]["ctr"], 300 / 10000, places=4)

    def test_roas_correct(self):
        df = compute_kpis(_make_df())
        self.assertAlmostEqual(df.iloc[0]["roas"], 3000 / 1200, places=2)

    def test_cpa_correct(self):
        df = compute_kpis(_make_df())
        self.assertAlmostEqual(df.iloc[0]["cpa"], 1200 / 14, places=2)

    def test_churn_rate_correct(self):
        df = compute_kpis(_make_df())
        self.assertAlmostEqual(df.iloc[0]["churn_rate"], 1 / 10, places=4)

    def test_aggregate_sums_revenue(self):
        df = compute_kpis(pd.concat([_make_df(), _make_df()], ignore_index=True))
        agg = aggregate_by_campaign(df)
        self.assertAlmostEqual(agg.iloc[0]["revenue"], 6000.0)


if __name__ == "__main__":
    unittest.main()
