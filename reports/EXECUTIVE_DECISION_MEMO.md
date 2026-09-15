# Customer Support Intelligence — Executive Decision Memo

> **Portfolio case study | Synthetic data | Decision-oriented operations analytics**

## Situation

Support performance can look healthy when viewed through averages while a smaller set of slow, high-priority, escalated, or reopened cases creates disproportionate operational complexity.

This analysis evaluates demand, service performance, customer outcomes, backlog risk, and a hypothetical escalation-reduction scenario.

## Key Analytical Findings

Using the fixed-seed synthetic dataset of **1,800 tickets**:

1. **SLA performance is high overall, but the urgent segment is materially different.** Overall first-response SLA attainment is approximately **96.9%**, while urgent tickets are approximately **71.5%**. Urgent tickets also show a substantially higher escalation rate than the overall dataset.

2. **Average resolution time understates the long tail.** Mean resolution time is approximately **22.9 hours**, while P90 resolution is approximately **43.0 hours**. This gap shows why tail metrics matter for operational planning.

3. **Escalation risk is concentrated in specific segments.** Specialist-team tickets have an escalation rate of approximately **39.8%**, compared with roughly **3.5%** for Tier 1 and **1.8%** for Tier 2 in this generated dataset.

4. **SLA and CSAT show an observed association, not a causal relationship.** Tickets that missed SLA have lower average CSAT in this dataset, but the difference should not be interpreted as evidence that SLA performance alone causes the CSAT outcome.

5. **Issue-level resolution performance also varies.** Technical tickets have the highest P90 resolution time in the generated dataset at approximately **49 hours**, while Account tickets are approximately **39.7 hours**. These differences are useful investigation signals, not evidence of root cause.

## Operational Risk

The strongest investigation signals are:

- Urgent-ticket SLA performance
- Specialist-team escalation concentration
- Long-tail resolution time
- Technical-ticket resolution tail
- Open/pending backlog aging

These signals identify where an operations team could investigate workflow, routing, staffing, knowledge-base coverage, or escalation policies.

## Scenario Impact

The dashboard includes an escalation-reduction scenario where the user supplies:

- assumed cost per escalated ticket
- assumed percentage reduction in escalations

The resulting workload and cost figures are **scenario estimates**, not measured company savings.

The appropriate management question is therefore:

> **If the identified escalation drivers can be reduced by an experimentally validated amount, what workload and cost could potentially be avoided?**

## Recommended Investigation Sequence

1. Review urgent-ticket routing and first-response workflow.
2. Examine why Specialist-team tickets are escalated at a higher rate.
3. Segment Technical tickets by channel, priority, and team to identify repeat patterns.
4. Review backlog-aging buckets for unresolved cases approaching service-risk thresholds.
5. Test one operational intervention with a defined baseline and success metric.
6. Re-measure SLA, P90 resolution, escalation, reopen, and CSAT outcomes after the intervention.

## Analytical Guardrails

- The dataset is synthetic and fixed-seed.
- Relationships are intentionally simulated for portfolio demonstration.
- Observed association does not establish causation.
- Scenario costs are assumption-driven rather than measured financial results.
- Findings demonstrate analytical workflow, not real-company performance.

## Recruiter Takeaway

This project demonstrates a complete analytical reasoning loop:

```text
Operational Data
      ↓
KPI Measurement
      ↓
Segmentation
      ↓
Risk Signals
      ↓
Association Analysis
      ↓
Scenario Modeling
      ↓
Operational Investigation
```

The objective is not simply to produce charts. It is to show how an analyst moves from **data → evidence → uncertainty → business question → measurable next step**.
