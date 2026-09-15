# Customer Support Analytics

## Support operations → measurable decisions

A recruiter-ready, reproducible business analytics project that evaluates customer-support operations through **Python, SQL, KPI analysis, service-level metrics, segmentation, and visualization**.

> **Portfolio focus:** connecting workload, service performance, customer experience, and operational complexity into actionable questions.

## Executive Dashboard

See the recruiter-facing interpretation layer: **[Executive Support Dashboard](reports/executive_dashboard.md)**.

### Visual Analysis

![Monthly Support Ticket Volume](visualizations/monthly_ticket_volume.svg)

![SLA Attainment by Priority](visualizations/sla_by_priority.svg)

![Average CSAT by Channel](visualizations/csat_by_channel.svg)

![Median Resolution Time by Issue Type](visualizations/resolution_by_issue.svg)

These charts are generated from the project's fixed-seed synthetic support dataset and committed as SVG so they render directly on GitHub.

## Analyst Snapshot

| Capability | Demonstrated here |
|---|---|
| Data preparation | Validation, cleaning, type handling |
| KPI analysis | Volume, SLA, response, resolution, CSAT |
| Service analytics | Average, median, and P90 metrics |
| Segmentation | Channel, priority, issue type, team, month |
| Root-cause analysis | Escalation and reopen concentration |
| SQL | Reusable operational analysis queries |
| Communication | Executive support dashboard and decision framework |
| Reproducibility | Scripted pipeline + tests + GitHub Actions |

## Business Questions

- Where is ticket demand concentrated by month, channel, priority, and issue type?
- Are service-level targets being met?
- Does the long tail of response or resolution time tell a different story than averages?
- Where are escalations and reopenings concentrated?
- Which teams or channels show weaker operational performance?
- How does SLA performance relate to CSAT?
- Which issue categories should receive operational attention first?

## Analytical Workflow

```text
Synthetic Support Data → Validation & Cleaning
        ↓
KPI Calculation → P90 Service Metrics
        ↓
SLA / CSAT Analysis → Escalation Root-Cause Segmentation
        ↓
SQL → Visual Reporting → Operational Decision Framework
```

## Tech Stack

**Python · pandas · NumPy · SQL · Matplotlib · Git/GitHub · GitHub Actions · pytest**

## Reproducibility

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/support_analysis.py
python src/create_visualizations.py
pytest -q
```

The synthetic dataset uses a fixed random seed. The visualization script now generates SVG outputs that are versioned in Git so the portfolio's visual layer is visible on GitHub.

## Data Integrity

The dataset is **synthetic** and exists solely for portfolio demonstration. It contains no private customer records, employer data, or production support information. Results should be interpreted as an analytical demonstration rather than claims about a real support organization.

## Portfolio

Part of a three-project Data Analyst portfolio:

- **Macro Market Intelligence** — economic and market context
- **Trading Risk & Performance Analytics** — financial risk and performance
- **Customer Support Analytics** — business and operations analytics
