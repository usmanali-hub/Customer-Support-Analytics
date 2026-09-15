# Customer Support Analysis Walkthrough

This notebook-style guide mirrors the reproducible pipeline.

## 1. Generate data
```bash
python src/generate_data.py
```

## 2. Validate and enrich
```bash
python src/clean_data.py
```

## 3. Calculate KPIs
```bash
python src/support_analysis.py
```

## 4. Create visualizations
```bash
python src/create_visualizations.py
```

## 5. Interpret
Use the reports to compare demand, SLA attainment, response time, resolution time, CSAT, escalation, and reopening patterns.

The analytical goal is to move from **metric → pattern → operational question → recommendation**, rather than simply producing charts.
