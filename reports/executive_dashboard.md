# Executive Support Intelligence — Customer Support Analytics

> **Support operations → evidence → scenario → next decision**

This is the recruiter-facing interpretation layer for the analytical output. The project uses fixed-seed synthetic support data, so findings demonstrate methodology rather than real-company performance.

## Executive View

| Lens | KPI | Decision question |
|---|---|---|
| Demand | Ticket volume / monthly trend | Where is workload concentrated? |
| Responsiveness | Average / median / P90 first response | Are long-tail cases hidden by averages? |
| Resolution | Average / median / P90 resolution | Where does case handling slow down? |
| SLA | Overall / priority attainment | Which service commitments are at risk? |
| Customer | CSAT / low-CSAT rate | Where is customer experience weakest? |
| Complexity | Escalation / reopen rate | Which cases create repeat workload? |
| Backlog | Open/pending age buckets | Which unresolved cases need attention? |
| Scenario | Escalation reduction × assumed cost | What could change under explicit assumptions? |

## Analytical Discipline

The project separates:

**Observation** — a measurable pattern in the data.

**Association** — a relationship worth investigating, not proof of causality.

**Scenario** — a hypothetical calculation driven by explicit assumptions.

**Decision** — the next operational question or experiment, rather than an unsupported recommendation.

For example, if missed-SLA tickets show lower CSAT, the correct conclusion is that the two measures are associated in this dataset. It is not evidence that changing SLA performance alone will cause a particular CSAT improvement.

## Operational Interpretation

1. Start with workload concentration and trend.
2. Compare mean, median, and P90 service metrics.
3. Check SLA attainment, especially for high-priority cases.
4. Drill into issue/channel/team segments with meaningful volume.
5. Compare CSAT with SLA status while controlling for obvious segment differences where possible.
6. Review escalation, reopen, and backlog-aging signals for repeat workload.
7. Use scenario analysis only with clearly stated assumptions.
8. Recommend an investigation or controlled operational change before claiming causal impact.

## Synthetic Data Guardrails

- The dataset is synthetic and fixed-seed.
- Some relationships are intentionally simulated by the generator.
- No private customer, employer, or production support data is used.
- Scenario costs are assumptions, not measured financial results.
- Results demonstrate analytical methodology rather than real-company performance.

## Reproduce

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/support_analysis.py
python src/create_visualizations.py
pytest -q
```

**Interview framing:** `Observation → evidence → association → scenario → next investigation.`
