from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

Path("visualizations").mkdir(exist_ok=True)
df = pd.read_csv("data/clean_tickets.csv", parse_dates=["created_at"])
monthly = df.groupby("month").size(); monthly.plot(kind="line", marker="o", title="Monthly Support Ticket Volume"); plt.ylabel("Tickets"); plt.tight_layout(); plt.savefig("visualizations/monthly_ticket_volume.svg", format="svg"); plt.close()
sla = df.groupby("priority")["sla_met"].mean().mul(100).sort_values(); sla.plot(kind="barh", title="SLA Attainment by Priority"); plt.xlabel("SLA attainment (%)"); plt.tight_layout(); plt.savefig("visualizations/sla_by_priority.svg", format="svg"); plt.close()
csat = df.groupby("channel")["customer_satisfaction"].mean().sort_values(); csat.plot(kind="barh", title="Average CSAT by Channel"); plt.xlabel("CSAT"); plt.tight_layout(); plt.savefig("visualizations/csat_by_channel.svg", format="svg"); plt.close()
resolution = df.groupby("issue_type")["resolution_hours"].median().sort_values(); resolution.plot(kind="barh", title="Median Resolution Time by Issue Type"); plt.xlabel("Hours"); plt.tight_layout(); plt.savefig("visualizations/resolution_by_issue.svg", format="svg"); plt.close()

print("Created four support analytics SVG charts in visualizations/")
