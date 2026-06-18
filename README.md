# Marketing Analytics Pipeline

An end-to-end advertising analytics pipeline that unifies Google Ads, Google Analytics 360, and Salesforce into a single campaign performance view — the same integration pattern used to cut reporting turnaround from 2 days to under 2 hours at Arena Holdings.

## What it does

Takes three separate daily extracts that share only `date` and `campaign_id`, joins them, computes the KPIs that actually drive marketing decisions (CTR, CPA, ROAS, conversion rate, churn rate), and produces both an aggregated campaign summary and a visual performance report.

## Architecture

```
data/raw/
  google_ads.csv      ─┐
  ga360.csv            ├─▶ transform.py ─▶ daily_unified.csv
  salesforce.csv      ─┘                   campaign_summary.csv
                                                   │
                                              report.py
                                                   │
                                    campaign_performance.png + report.md
```

| Module | What it does |
|---|---|
| `src/generate_sample_data.py` | Synthesises 30 days × 4 campaigns of realistic ad/analytics/CRM data |
| `src/transform.py` | Unifies the three sources and computes CTR, CPA, ROAS, conversion rate, churn rate |
| `src/report.py` | Generates a bar chart and Markdown report — a lightweight stand-in for the Power BI dashboard this mirrors |

## KPIs explained

| KPI | Formula | What it tells you |
|---|---|---|
| CTR | clicks / impressions | How compelling the ad creative is |
| CPA | spend / conversions | Efficiency per acquisition |
| ROAS | revenue / spend | Overall return on investment |
| Conversion rate | conversions / sessions | Landing page effectiveness |
| Churn rate | churned / new subscribers | Subscriber retention signal |

## Tech stack

Python, pandas, matplotlib, SQLite-free (pure CSV/in-memory transform).

## Running it

```bash
pip install -r requirements.txt
python src/generate_sample_data.py
python src/transform.py
python src/report.py
# outputs land in data/processed/
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## Sample output

| Campaign | Cost | Revenue | ROAS | CPA | Churn |
|---|---|---|---|---|---|
| Spring Subscriptions | R181k | R221k | 1.22x | R166 | 10.8% |
| Brand Awareness Q2 | R172k | R190k | 1.10x | R166 | 9.5% |
| New Market Launch | R158k | R187k | 1.18x | R175 | 11.8% |
| Retargeting - Lapsed Users | R170k | R176k | 1.04x | R194 | 10.1% |

## What I'd add for production

- Schedule daily ingestion from the real Google Ads API, GA4, and Salesforce REST API using Azure Data Factory.
- Load the unified table into a Power BI dataset with DirectQuery refresh for live dashboards.
- Add anomaly detection: flag campaigns where ROAS drops >20% week-on-week.

## License

MIT
