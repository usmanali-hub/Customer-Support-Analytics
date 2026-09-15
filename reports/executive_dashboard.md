# Executive Support Dashboard — Customer Support Analytics

> **Support operations → measurable decisions**

This is the recruiter-facing entry point for the analytical output. Charts are generated reproducibly from the synthetic support dataset.

## Executive View

| Lens | KPI | Decision question |
|---|---|---|
| Demand | Ticket volume / monthly trend | Where is workload concentrated? |
| Responsiveness | Average / median / P90 first response | Are long-tail cases hidden by averages? |
| Resolution | Average / median / P90 resolution | Where does case handling slow down? |
| SLA | Overall / high-priority attainment | Which service commitments are at risk? |
| Customer | CSAT / low-CSAT rate | Where is customer experience weakest? |
| Complexity | Escalation / reopen rate | Which cases create repeat workload? |
| Root cause | Priority + issue type | Which operational segments deserve attention? |

## Generated Visuals

Running `src/create_visualizations.py` creates:

- `monthly_ticket_volume.png` — workload trend
- `sla_by_priority.png` — SLA attainment by priority
- `csat_by_channel.png` — customer outcome by support channel
- `resolution_by_issue.png` — median resolution time by issue type

## Operational Interpretation

1. Start with workload concentration.
2. Compare average, median, and P90 service metrics.
3. Check SLA attainment, especially for high-priority cases.
4. Compare CSAT with SLA status.
5. Drill into issue types and priorities with elevated escalation or reopen rates.
6. Prioritize high-volume segments with measurable service or customer impact.

## Data Integrity

- The dataset is synthetic.
- No private customer, employer, or production support data is used.
- Results demonstrate analytical methodology rather than real-company performance.

## Reproduce

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/support_analysis.py
python src/create_visualizations.py
```

**Interview framing:** `Demand → service → customer outcome → root cause → operational action.`
