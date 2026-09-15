from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 1800
start = pd.Timestamp("2025-01-02")
created = start + pd.to_timedelta(rng.integers(0, 365 * 24, N), unit="h")

channels = rng.choice(["Email", "Chat", "Phone", "Web"], N, p=[0.28, 0.38, 0.22, 0.12])
priorities = rng.choice(["Low", "Medium", "High", "Urgent"], N, p=[0.28, 0.45, 0.20, 0.07])
issues = rng.choice(["Account", "Billing", "Technical", "Delivery", "Product", "Access"], N)
teams = rng.choice(["Tier 1", "Tier 2", "Specialist"], N, p=[0.55, 0.30, 0.15])

priority_factor = pd.Series(priorities).map({"Low": 1.35, "Medium": 1.0, "High": 0.75, "Urgent": 0.50}).to_numpy()
channel_factor = pd.Series(channels).map({"Email": 1.10, "Chat": 0.70, "Phone": 0.85, "Web": 1.00}).to_numpy()
first_response = np.clip(rng.gamma(2.0, 1.8, N) * priority_factor * channel_factor, 0.1, 30)
resolution = np.clip(first_response + rng.gamma(2.4, 8.0, N) * priority_factor, 0.5, 120)

sla_hours = pd.Series(priorities).map({"Low": 24, "Medium": 12, "High": 6, "Urgent": 2}).to_numpy()
status = rng.choice(["Resolved", "Open", "Pending"], N, p=[0.83, 0.10, 0.07])
escalated = ((teams == "Specialist") | (priorities == "Urgent")) & (rng.random(N) < 0.45)
reopened = (rng.random(N) < 0.09)
csat = np.clip(np.round(4.8 - first_response * 0.07 - resolution * 0.008 + rng.normal(0, 0.55, N), 1, 5), 1, 5)

resolved_at = created + pd.to_timedelta(resolution, unit="h")
df = pd.DataFrame({
    "ticket_id": [f"T{100001+i}" for i in range(N)],
    "created_at": created,
    "resolved_at": resolved_at,
    "channel": channels,
    "priority": priorities,
    "issue_type": issues,
    "agent_team": teams,
    "first_response_hours": np.round(first_response, 2),
    "resolution_hours": np.round(resolution, 2),
    "sla_hours": sla_hours,
    "customer_satisfaction": csat,
    "status": status,
    "reopened": reopened,
    "escalated": escalated,
})

Path("data").mkdir(exist_ok=True)
df.to_csv("data/tickets.csv", index=False)
print(f"Generated {len(df):,} synthetic tickets in data/tickets.csv")
