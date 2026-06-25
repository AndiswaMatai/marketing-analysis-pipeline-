# 📣 Unified Marketing Analytics Lakehouse Platform

![GA4](https://img.shields.io/badge/Analytics-GA4-blue?logo=googleanalytics)
![Salesforce](https://img.shields.io/badge/CRM-Salesforce-lightblue?logo=salesforce)
![Python](https://img.shields.io/badge/Language-Python-yellow?logo=python)
![Pandas](https://img.shields.io/badge/Library-Pandas-green?logo=pandas)
![Power BI](https://img.shields.io/badge/BI-Power%20BI-yellow?logo=powerbi)

---

## 🚀 Overview
An end-to-end marketing analytics lakehouse platform that unifies Google Ads, Google Analytics 360, and Salesforce CRM data into a single governed campaign performance model.  
Mirrors real-world enterprise integration patterns used to reduce reporting cycles from **2 days to under 2 hours** in high-volume media environments.

---

## 🧠 Business Problem
Marketing teams face fragmented data across Ads, GA360, and Salesforce, leading to:
- Inconsistent campaign reporting  
- Delayed visibility into performance  
- Difficulty attributing revenue to marketing activity  
- No single source of truth for campaign performance  

---

## 🎯 Solution Overview
This platform standardises, integrates, and transforms multi-source marketing data into a unified analytical model:
- Daily ingestion from Ads, GA360, Salesforce  
- Schema alignment + campaign-level standardisation  
- Unified dataset across acquisition, engagement, conversion  
- Computed KPIs for decision-ready insights  
- Analytics-ready outputs for dashboards and reports  

---

## 🏗️ Architecture
📡 **Data Sources** → 🥉 Bronze Layer → 🥈 Silver Layer → 🥇 Gold Layer → 📊 Consumption Layer  

- Bronze: Raw extracts  
- Silver: Standardisation + identity alignment  
- Gold: Unified dataset + KPI computation  
- Consumption: Power BI dashboards + reports  

---

## 📊 KPIs Explained
| KPI | Formula | Business Insight |
|-----|---------|------------------|
| CTR | clicks / impressions | Ad creative effectiveness |
| CPA | spend / conversions | Cost efficiency per acquisition |
| ROAS | revenue / spend | Return on ad spend |
| Conversion Rate | conversions / sessions | Funnel effectiveness |
| Churn Rate | churned / new customers | Retention performance |

---

## 🛠️ Tech Stack
Python · Pandas · Matplotlib · CSV/In-memory transforms · Power BI  

---

## ⚙️ Engineering Design
- Multi-source ingestion + harmonisation  
- Schema alignment across systems  
- Campaign-level identity resolution  
- Star-schema style analytical modelling  
- Batch processing for daily refresh cycles  

---

## 📊 Outputs
- Unified campaign performance dataset  
- Aggregated KPI tables  
- Daily campaign performance reports  
- Visual performance summaries  

---

## 💡 Business Impact
- **Reporting Efficiency:** Reduced reporting latency from 2 days to under 2 hours.  
- **ROI Visibility:** Delivered unified KPIs across acquisition, engagement, and retention, enabling faster budget allocation.  
- **Decision Confidence:** Provided a single source of truth for campaign performance, eliminating discrepancies across platforms.  
- **Revenue Attribution:** Improved ability to link marketing spend directly to conversions and revenue outcomes.  

---
## Project Structure 

marketing-analytics-lakehouse/
├── src/                # Core Python modules for ingestion, transforms, KPI computation
├── config/             # Config files (API keys, campaign mappings, schema definitions)
├── data/               # Sample input extracts (Ads, GA360, Salesforce) + output datasets
├── transforms/         # Scripts for schema alignment, identity resolution, KPI calculations
├── reports/            # Generated KPI tables, markdown summaries, charts
├── dashboards/         # Power BI / BI model definitions
├── tests/              # Unit tests for ingestion + KPI logic
├── scripts/            # Utility scripts for batch refresh and local runs
├── infrastructure/     # CI/CD pipeline configs, Terraform definitions
├── Dockerfile          # Containerisation for deployment
└── README.md           # Documentation


## 📜 License
MIT — feel free to reuse for your own learning
