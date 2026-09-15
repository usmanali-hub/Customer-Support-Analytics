from pathlib import Path
import pandas as pd

INPUT = "data/tickets.csv"
OUTPUT = "data/clean_tickets.csv"
REQUIRED = [
    "ticket_id", "created_at", "resolved_at", "channel", "priority",
    "issue_type", "agent_team", "first_response_hours", "resolution_hours",
    "sla_hours", "customer_satisfaction", "status", "reopened", "escalated"
]

df = pd.read_csv(INPUT, parse_dates=["created_at", "resolved_at"])
missing = [c for c in REQUIRED if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns: {missing}")

df = df.drop_duplicates("ticket_id").copy()
for col in ["first_response_hours", "resolution_hours", "sla_hours", "customer_satisfaction"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["ticket_id", "created_at", "first_response_hours", "resolution_hours"])
df = df[(df["first_response_hours"] >= 0) & (df["resolution_hours"] >= 0)]
df["sla_met"] = df["resolution_hours"] <= df["sla_hours"]
df["month"] = df["created_at"].dt.to_period("M").astype(str)
df = df.sort_values("created_at")

Path("data").mkdir(exist_ok=True)
df.to_csv(OUTPUT, index=False)
print(f"Validated {len(df):,} tickets and wrote {OUTPUT}")
