"""Decision-oriented metrics for support operations analysis."""
from __future__ import annotations

import pandas as pd


def backlog_aging(frame: pd.DataFrame) -> pd.DataFrame:
    """Bucket open/pending tickets using the dataset's latest creation time as the as-of date."""
    open_cases = frame.loc[frame["status"].isin(["Open", "Pending"])].copy()
    if open_cases.empty:
        return pd.DataFrame(columns=["age_bucket", "tickets"])
    as_of = frame["created_at"].max()
    age_hours = (as_of - open_cases["created_at"]).dt.total_seconds() / 3600
    bins = [-1, 4, 12, 24, 72, 168, float("inf")]
    labels = ["0–4h", "4–12h", "12–24h", "1–3d", "3–7d", "7d+"]
    buckets = pd.cut(age_hours, bins=bins, labels=labels)
    return buckets.value_counts(sort=False).rename_axis("age_bucket").reset_index(name="tickets")


def scenario_impact(frame: pd.DataFrame, cost_per_ticket: float, reduction_pct: float) -> dict[str, float]:
    """Estimate avoidable workload/cost under an explicitly labeled scenario."""
    escalated = int(frame["escalated"].sum())
    avoidable = escalated * max(0.0, min(reduction_pct, 100.0)) / 100.0
    return {
        "escalated_tickets": escalated,
        "scenario_tickets_avoided": avoidable,
        "scenario_cost_avoided": avoidable * max(cost_per_ticket, 0.0),
    }


def segment_signal(frame: pd.DataFrame, dimension: str, min_tickets: int = 30) -> pd.DataFrame:
    """Rank segments by a transparent combination of SLA risk, escalation and reopen rates."""
    grouped = frame.groupby(dimension, dropna=False).agg(
        tickets=("ticket_id", "size"),
        sla_attainment_pct=("sla_met", lambda x: x.mean() * 100),
        escalation_rate_pct=("escalated", lambda x: x.mean() * 100),
        reopen_rate_pct=("reopened", lambda x: x.mean() * 100),
        avg_csat=("customer_satisfaction", "mean"),
        p90_resolution_hours=("resolution_hours", lambda x: x.quantile(0.9)),
    )
    grouped = grouped[grouped["tickets"] >= min_tickets].copy()
    if grouped.empty:
        return grouped
    grouped["risk_signal"] = (
        (100 - grouped["sla_attainment_pct"]).clip(lower=0)
        + grouped["escalation_rate_pct"]
        + grouped["reopen_rate_pct"]
    ).round(2)
    return grouped.sort_values(["risk_signal", "tickets"], ascending=[False, False]).round(2)
