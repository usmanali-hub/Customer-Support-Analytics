from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

Path("visualizations").mkdir(exist_ok=True)
df = pd.read_csv("data/clean_tickets.csv", parse_dates=["created_at"])
monthly = df.groupby("month").size()
monthly.plot(kind="line", marker="o", title="Monthly Support Ticket Volume")
plt.ylabel("Tickets")
plt.tight_layout()
plt.savefig("visualizations/monthly_ticket_volume.png", dpi=160)
plt.close()

sla = df.groupby("priority")["sla_met"].mean().mul(100).sort_values()
sla.plot(kind="barh", title="SLA Attainment by Priority")
plt.xlabel("SLA attainment (%)")
plt.tight_layout()
plt.savefig("visualizations/sla_by_priority.png", dpi=160)
plt.close()

csat = df.groupby("channel")["customer_satisfaction"].mean().sort_values()
csat.plot(kind="barh", title="Average CSAT by Channel")
plt.xlabel("CSAT")
plt.tight_layout()
plt.savefig("visualizations/csat_by_channel.png", dpi=160)
plt.close()

resolution = df.groupby("issue_type")["resolution_hours"].median().sort_values()
resolution.plot(kind="barh", title="Median Resolution Time by Issue Type")
plt.xlabel("Hours")
plt.tight_layout()
plt.savefig("visualizations/resolution_by_issue.png", dpi=160)
plt.close()

print("Created four support analytics charts in visualizations/")
