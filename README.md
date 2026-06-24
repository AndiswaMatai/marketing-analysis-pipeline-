# 📣 Unified Marketing Analytics Lakehouse Platform

![Sector](https://img.shields.io/badge/Sector-Advertising-8a4a00?style=flat)
![CI](https://img.shields.io/badge/CI-passing-0f7a4b?style=flat&logo=githubactions)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)

**[← Back to live portfolio](https://andiswamatai.github.io)**

---

## 🚀 Overview

An end-to-end marketing analytics lakehouse platform that unifies Google Ads, Google Analytics 360, and Salesforce CRM data into a single governed campaign performance model.

This system demonstrates how fragmented marketing data sources can be consolidated into a unified analytics layer to enable consistent, decision-ready KPIs across acquisition, engagement, and retention.

It mirrors a real-world enterprise integration pattern used to reduce marketing reporting cycles from **2 days to under 2 hours** in high-volume media environments.

---

## 🧠 Business Problem

Modern marketing teams operate across multiple disconnected platforms:

- Google Ads for paid acquisition
- Google Analytics 360 for web behaviour
- Salesforce for CRM and conversion tracking

This fragmentation results in:

- Inconsistent campaign reporting across platforms
- Delayed performance visibility for decision-making
- Difficulty attributing revenue to marketing activity
- Lack of a single source of truth for campaign performance

---
## 🧠 Solutions Overview

This platform implements a unified marketing lakehouse that standardises, integrates, and transforms multi-source marketing data into a consistent analytical model.

The system:

- Ingests daily extracts from Google Ads, GA360, and Salesforce
- Performs schema alignment and campaign-level standardisation
- Builds a unified dataset across acquisition, engagement, and conversion layers
- Computes business-critical marketing KPIs
- Produces analytics-ready outputs for reporting and dashboards
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
