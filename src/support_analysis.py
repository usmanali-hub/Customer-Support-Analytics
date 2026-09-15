from pathlib import Path
import pandas as pd

INPUT = "data/clean_tickets.csv"
Path("reports").mkdir(exist_ok=True)
df = pd.read_csv(INPUT, parse_dates=["created_at", "resolved_at"])

def kpis(frame):
    return pd.Series({
        "tickets": len(frame),
        "sla_attainment_pct": frame["sla_met"].mean() * 100,
        "avg_first_response_hours": frame["first_response_hours"].mean(),
        "median_first_response_hours": frame["first_response_hours"].median(),
        "avg_resolution_hours": frame["resolution_hours"].mean(),
        "median_resolution_hours": frame["resolution_hours"].median(),
        "avg_csat": frame["customer_satisfaction"].mean(),
        "escalation_rate_pct": frame["escalated"].mean() * 100,
        "reopen_rate_pct": frame["reopened"].mean() * 100,
    })

overall = kpis(df).round(2).to_frame("value")
overall.to_csv("reports/overall_kpis.csv")

for dimension in ["channel", "priority", "issue_type", "agent_team", "month"]:
    result = df.groupby(dimension, dropna=False).apply(kpis, include_groups=False).round(2)
    result.to_csv(f"reports/{dimension}_analysis.csv")

print(overall)
print("Analysis reports written to reports/")
