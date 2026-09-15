# Customer Support Analytics

## Turning support operations data into decisions

A reproducible business analytics project that evaluates customer-support operations through **Python, SQL, KPI analysis, segmentation, and visualization**.

The goal is not simply to report how many tickets arrived. The analysis is designed to answer the operational questions a support leader actually needs to make decisions: **where demand is concentrated, where service levels break down, what drives escalations and reopenings, and how operational performance connects to customer satisfaction.**

## Business Questions

- How does ticket demand change over time and across support channels?
- Which priorities and issue types create the greatest operational load?
- Are first-response and resolution SLAs being met?
- Where are escalations and reopened cases concentrated?
- Which teams or channels show slower response or resolution performance?
- How does service performance relate to CSAT?
- Where should support operations focus improvement efforts first?

## Analytical Workflow

```text
Synthetic Support Data
        ↓
Data Validation & Cleaning
        ↓
KPI Calculation
        ↓
Segmentation & Trend Analysis
        ↓
SQL Business Queries
        ↓
Visual Reporting
        ↓
Operational Findings & Recommendations
```

## Key KPIs

| Area | Metrics |
|---|---|
| Demand | Ticket volume, backlog, monthly trend |
| Service | First-response time, resolution time, SLA attainment |
| Customer | CSAT, reopen rate |
| Operations | Escalation rate, workload by team/channel |
| Segmentation | Priority, issue type, channel, team |

## Tech Stack

- **Python** — analysis and automation
- **pandas / NumPy** — data preparation and KPI calculations
- **SQL** — operational and segmentation queries
- **Matplotlib** — analytical visualization
- **Git / GitHub** — version control and reproducibility

## Repository Structure

```text
├── data/                 # Dataset documentation; generated CSVs are ignored
├── docs/                 # Methodology and analytical findings
├── notebooks/            # Notebook-style analytical walkthrough
├── reports/              # Executive interpretation and recommendations
├── sql/                  # Business analysis queries
├── src/                  # Data generation, cleaning, analysis and visualization
├── visualizations/       # Documentation for generated charts
├── .gitignore
├── requirements.txt
└── README.md
```

## Reproducibility

Run the complete pipeline with:

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/support_analysis.py
python src/create_visualizations.py
```

Generated CSV and PNG outputs are intentionally excluded from Git. The repository contains the code, methodology, SQL, and reporting layer required to reproduce the analysis.

## Data Integrity Note

The dataset is **synthetic** and exists solely for portfolio demonstration. It does not contain private customer records, employer data, or production support information. Results should therefore be interpreted as an analytical demonstration rather than as claims about a real support organization.

## What This Project Demonstrates

This project demonstrates the ability to move from **raw operational data → validated metrics → segmented analysis → business interpretation** rather than stopping at descriptive charts.

It is designed to showcase practical Data Analyst skills in **customer operations, KPI reporting, SLA analysis, root-cause-oriented segmentation, SQL, Python, and decision-focused communication**.
