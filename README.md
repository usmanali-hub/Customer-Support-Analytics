# Customer Support Analytics

## Support operations → measurable decisions

A reproducible business analytics project that evaluates customer-support operations through **Python, SQL, KPI analysis, service-level metrics, segmentation, and visualization**.

### Why this project matters

The analysis goes beyond ticket counts. It connects **demand → response → resolution → escalation → customer satisfaction** to identify where an operations team should investigate or improve.

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

## Advanced Analytics

| Area | Metrics |
|---|---|
| Demand | Ticket volume, monthly trend, segmentation |
| Service | Average/median/P90 first response and resolution |
| SLA | Overall and high-priority SLA attainment |
| Customer | Average CSAT, low-CSAT rate |
| Operations | Escalation rate, reopen rate |
| Root cause | Escalation by priority and issue type |
| Relationship | CSAT grouped by SLA status |

P90 metrics are included deliberately because averages can hide long-running customer cases.

## Tech Stack

**Python · pandas · NumPy · SQL · Matplotlib · Git/GitHub · GitHub Actions**

## Repository Structure

```text
├── data/                 # Synthetic dataset documentation
├── docs/                 # Methodology, dictionary, decision framework
├── notebooks/            # Analytical walkthrough
├── reports/              # KPI and executive outputs
├── sql/                  # Operational analysis queries
├── src/                  # Generation, cleaning, analysis, visualization
├── visualizations/       # Chart documentation
├── .github/workflows/    # Automated quality checks
├── README.md
└── requirements.txt
```

## Reproducibility

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/support_analysis.py
python src/create_visualizations.py
```

Generated CSV and PNG outputs are intentionally excluded from Git. GitHub Actions runs Python compilation checks on pushes and pull requests.

## Operational Decision Framework

**Demand:** Find where workload is concentrated.

**Service:** Compare SLA attainment with P90 response and resolution times.

**Customer:** Compare CSAT and low-CSAT rates alongside service outcomes.

**Complexity:** Identify issue types and priorities with elevated escalation or reopen rates.

**Action:** Prioritize high-volume segments with measurable service or customer-impact problems.

## Data Integrity

The dataset is **synthetic** and exists solely for portfolio demonstration. It contains no private customer records, employer data, or production support information. Results should be interpreted as an analytical demonstration rather than claims about a real support organization.
