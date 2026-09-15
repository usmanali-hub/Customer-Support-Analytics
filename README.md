# Customer Support Analytics

A reproducible business analytics project for turning customer-support ticket data into operational insights using Python, pandas, SQL, KPI analysis, and visualization.

## Business questions
- How does ticket demand change over time and across channels?
- Are first-response and resolution SLAs being met?
- Which priorities and issue types consume the most support capacity?
- Where are escalations and reopenings concentrated?
- How do response/resolution performance relate to customer satisfaction?

## Workflow
**Synthetic ticket data → validation → KPI calculation → segmentation → SQL analysis → visualization → recommendations**

## KPIs
Ticket volume, SLA attainment, first-response time, resolution time, CSAT, escalation rate, reopen rate, backlog, and performance by channel, priority, issue type, and team.

## Tech stack
Python, pandas, NumPy, Matplotlib, SQL, data cleaning, KPI analysis, exploratory analysis, business reporting.

## Data note
The dataset is synthetic and created for portfolio demonstration. It does not contain private customer, employer, or production support data.

## Run
```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/support_analysis.py
python src/create_visualizations.py
```

The generated CSV and PNG outputs are excluded from Git so the project remains reproducible without committing generated artifacts.
