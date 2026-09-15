"""Calculate service, customer, and operational support KPIs."""
from pathlib import Path
import pandas as pd

INPUT = "data/clean_tickets.csv"
Path("reports").mkdir(exist_ok=True)
df = pd.read_csv(INPUT, parse_dates=["created_at", "resolved_at"])


def kpis(frame):
    return pd.Series({
        "tickets": len(frame),
        "sla_attainment_pct": frame["sla_met"].mean() * 100,
        "high_priority_sla_pct": frame.loc[frame["priority"].eq("High"), "sla_met"].mean() * 100 if frame["priority"].eq("High").any() else 0,
        "avg_first_response_hours": frame["first_response_hours"].mean(),
        "p90_first_response_hours": frame["first_response_hours"].quantile(0.90),
        "median_first_response_hours": frame["first_response_hours"].median(),
        "avg_resolution_hours": frame["resolution_hours"].mean(),
        "p90_resolution_hours": frame["resolution_hours"].quantile(0.90),
        "median_resolution_hours": frame["resolution_hours"].median(),
        "avg_csat": frame["customer_satisfaction"].mean(),
        "low_csat_rate_pct": (frame["customer_satisfaction"] <= 2).mean() * 100,
        "escalation_rate_pct": frame["escalated"].mean() * 100,
        "reopen_rate_pct": frame["reopened"].mean() * 100,
    })


overall = kpis(df).round(2).to_frame("value")
overall.to_csv("reports/overall_kpis.csv")

for dimension in ["channel", "priority", "issue_type", "agent_team", "month"]:
    result = df.groupby(dimension, dropna=False).apply(kpis, include_groups=False).round(2)
    result.to_csv(f"reports/{dimension}_analysis.csv")

sla_csat = (
    df.groupby("sla_met")["customer_satisfaction"]
    .agg(["count", "mean", "median"])
    .round(2)
)
sla_csat.to_csv("reports/csat_by_sla_status.csv")

escalations = (
    df.groupby(["priority", "issue_type"], dropna=False)["escalated"]
    .agg(["count", "mean"])
    .rename(columns={"count": "tickets", "mean": "escalation_rate"})
)
escalations["escalation_rate"] = (escalations["escalation_rate"] * 100).round(2)
escalations.to_csv("reports/escalation_by_priority_issue.csv")

print(overall)
print("Analysis reports written to reports/")
