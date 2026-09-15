# Customer Support Analytics

## Support operations → measurable decisions

A recruiter-ready **business and operations analytics** project that turns support-ticket data into measurable insights across workload, service levels, customer experience, and operational complexity.

> **Recruiter takeaway:** this project demonstrates how I move from operational data to KPIs, segmentation, root-cause questions, and practical improvement priorities.

## Interactive Dashboard

Run the project as an interactive local dashboard:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The dashboard lets users filter by **channel** and **priority**, then explore ticket volume, SLA attainment, response/resolution performance, CSAT, and escalation patterns. The app automatically generates the fixed-seed synthetic dataset if it is not present.

For a hosted version, deploy `app.py` on any Streamlit-compatible hosting service.

## The Business Problem

Support teams can look healthy on average while a smaller group of high-priority, slow, escalated, or reopened cases creates most of the operational pain. This project analyzes those patterns instead of relying on a single average.

### Questions the analysis answers

- Where is ticket demand concentrated by month, channel, priority, and issue type?
- Are service-level targets being met?
- Does P90 response/resolution time reveal a long tail hidden by averages?
- Where are escalations and reopenings concentrated?
- Which channels or teams show weaker operational performance?
- How does SLA performance relate to CSAT?
- Which issue categories deserve attention first?

## Executive View

| Lens | Measures | Decision question |
|---|---|---|
| **Demand** | Ticket volume + trend | Where is workload concentrated? |
| **Responsiveness** | Avg / median / P90 first response | Are slow cases hidden by averages? |
| **Resolution** | Avg / median / P90 resolution | Where does handling slow down? |
| **SLA** | Overall + priority attainment | Which commitments are at risk? |
| **Customer** | CSAT + low-CSAT rate | Where is customer experience weakest? |
| **Complexity** | Escalation + reopen rate | Which cases create repeat work? |
| **Root cause** | Priority + issue type | Which segments need attention? |

## Visual Analysis

The key charts are visible directly on GitHub:

![Monthly Support Ticket Volume](visualizations/monthly_ticket_volume.svg)

![SLA Attainment by Priority](visualizations/sla_by_priority.svg)

![Average CSAT by Channel](visualizations/csat_by_channel.svg)

![Median Resolution Time by Issue Type](visualizations/resolution_by_issue.svg)

These visuals are generated from the project's fixed-seed synthetic dataset and committed as SVG so a recruiter can inspect the analytical output without opening the source code.

**[Open the Executive Support Dashboard](reports/executive_dashboard.md)** for the KPI and operational decision framework.

## Analytical Workflow

```text
Synthetic Support Data
        ↓
Validation & Cleaning
        ↓
KPI Calculation → P90 Service Metrics
        ↓
SLA / CSAT Analysis → Escalation & Reopen Segmentation
        ↓
SQL + Visual Reporting
        ↓
Operational Decision Framework
```

## What This Demonstrates

**KPI analysis** — volume, response time, resolution time, SLA, CSAT.

**Service analytics** — average, median, and P90 metrics to expose long-tail cases.

**Segmentation** — channel, priority, issue type, team, and month.

**Root-cause analysis** — escalation and reopen concentration.

**Business communication** — `Demand → service → customer outcome → root cause → operational action`.

## Tech Stack

**Python · pandas · NumPy · SQL · Matplotlib · Git/GitHub · GitHub Actions · pytest · Streamlit**

## Reproduce It

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/support_analysis.py
python src/create_visualizations.py
pytest -q
```

## Repository Map

| Folder | Purpose |
|---|---|
| `app.py` | Interactive Streamlit dashboard |
| `reports/` | Executive support interpretation |
| `visualizations/` | Recruiter-visible charts |
| `sql/` | Reusable operational queries |
| `src/` | Data generation and analytics pipeline |
| `tests/` | Automated validation |
| `.github/workflows/` | CI quality checks |

## Data Integrity

The dataset is **synthetic** and exists solely for portfolio demonstration. It contains no private customer records, employer data, or production support information. Results demonstrate analytical methodology rather than real-company performance.

## Portfolio

Part of a three-project analytics portfolio:

- **Macro Market Intelligence** — economic and market context
- **Trading Risk & Performance Analytics** — financial risk and performance
- **Customer Support Analytics** — business and operations analytics
