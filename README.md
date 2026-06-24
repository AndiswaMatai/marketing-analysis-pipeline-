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

📡 Data Sources
- Google Ads (Paid Media)
- Google Analytics 360 (Web Behaviour)
- Salesforce CRM (Conversions / Revenue)

        ↓

🥉 Bronze Layer
- Raw daily extracts from each platform

        ↓

🥈 Silver Layer
- Campaign standardisation
- Identity alignment (campaign_id, date)
- Data cleaning and deduplication

        ↓

🥇 Gold Layer
- Unified campaign performance dataset
- KPI computation layer
- Business-ready analytics model

        ↓

📊 Consumption Layer
- Reporting datasets
- Power BI / BI dashboards
- Performance reports

## KPIs explained

The platform computes core marketing performance metrics:

| KPI | Formula | Business Insight |
|-----|--------|------------------|
| CTR | clicks / impressions | Ad creative effectiveness |
| CPA | spend / conversions | Cost efficiency per acquisition |
| ROAS | revenue / spend | Return on ad spend |
| Conversion Rate | conversions / sessions | Funnel effectiveness |
| Churn Rate | churned / new customers | Retention performance |

## Tech stack

Python, pandas, matplotlib, SQLite-free (pure CSV/in-memory transform).

## Engineering Design

This platform demonstrates key data engineering patterns:

- Multi-source ingestion and harmonisation
- Schema alignment across marketing systems
- Campaign-level identity resolution
- Star-schema style analytical modelling
- Batch processing for daily marketing data refresh cycles
---

## Output

The system produces:

- Unified campaign performance dataset
- Aggregated marketing KPI tables
- Daily campaign performance reports
- Visual performance summaries (charts + markdown reports)

---
## Business Value

This platform enables organisations to:

- Eliminate reporting discrepancies across marketing platforms
- Reduce marketing reporting latency from days to hours
- Improve ROI visibility across campaigns
- Enable faster budget allocation decisions
- Provide a single source of truth for marketing performance
  
## License

MIT
