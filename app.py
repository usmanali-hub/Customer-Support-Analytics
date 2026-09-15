"""Decision-oriented interactive dashboard for Customer Support Analytics."""
from pathlib import Path
import subprocess
import sys

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "clean_tickets.csv"

st.set_page_config(page_title="Customer Support Intelligence", layout="wide")
st.title("Customer Support Intelligence")
st.caption("Synthetic portfolio dataset • descriptive analysis • scenario estimates are assumptions, not company results")


def prepare_data():
    if not DATA.exists():
        subprocess.run([sys.executable, "src/generate_data.py"], cwd=ROOT, check=True)
        subprocess.run([sys.executable, "src/clean_data.py"], cwd=ROOT, check=True)


try:
    prepare_data()
    df = pd.read_csv(DATA, parse_dates=["created_at", "resolved_at"])
except Exception as exc:
    st.error(f"Could not prepare the dataset: {exc}")
    st.stop()

with st.sidebar:
    st.header("Filters")
    channels = st.multiselect("Channel", sorted(df["channel"].unique()), default=sorted(df["channel"].unique()))
    priorities = st.multiselect("Priority", sorted(df["priority"].unique()), default=sorted(df["priority"].unique()))
    issues = st.multiselect("Issue type", sorted(df["issue_type"].unique()), default=sorted(df["issue_type"].unique()))
    teams = st.multiselect("Agent team", sorted(df["agent_team"].unique()), default=sorted(df["agent_team"].unique()))

filtered = df[
    df["channel"].isin(channels)
    & df["priority"].isin(priorities)
    & df["issue_type"].isin(issues)
    & df["agent_team"].isin(teams)
].copy()

if filtered.empty:
    st.warning("No tickets match the selected filters.")
    st.stop()

# Executive health
sla_pct = filtered["sla_met"].mean() * 100
csat = filtered["customer_satisfaction"].mean()
p90_resolution = filtered["resolution_hours"].quantile(0.90)
escalation_pct = filtered["escalated"].mean() * 100
reopen_pct = filtered["reopened"].mean() * 100

st.subheader("Executive Support Health")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Tickets", f"{len(filtered):,}")
c2.metric("SLA Attainment", f"{sla_pct:.1f}%")
c3.metric("P90 Resolution", f"{p90_resolution:.1f}h")
c4.metric("Escalation Rate", f"{escalation_pct:.1f}%")
c5.metric("CSAT", f"{csat:.2f}/5")

# Evidence, not unsupported causal claims.
segment = filtered.groupby("issue_type").agg(
    tickets=("ticket_id", "size"),
    sla_pct=("sla_met", lambda x: x.mean() * 100),
    escalation_pct=("escalated", lambda x: x.mean() * 100),
    reopen_pct=("reopened", lambda x: x.mean() * 100),
    p90_resolution_h=("resolution_hours", lambda x: x.quantile(0.9)),
    csat=("customer_satisfaction", "mean"),
).round(2)
segment["risk_signal"] = (
    (100 - segment["sla_pct"]).clip(lower=0)
    + segment["escalation_pct"]
    + segment["reopen_pct"]
).round(2)
segment = segment.sort_values(["risk_signal", "tickets"], ascending=[False, False])

st.subheader("Top Operational Signals")
for issue, row in segment.head(3).iterrows():
    st.write(
        f"**{issue}** — {int(row['tickets']):,} tickets, "
        f"{row['sla_pct']:.1f}% SLA, {row['escalation_pct']:.1f}% escalated, "
        f"P90 resolution {row['p90_resolution_h']:.1f}h."
    )
st.caption("Signals are descriptive. They identify segments for investigation; they do not establish causality.")

left, right = st.columns(2)
with left:
    st.subheader("Ticket Demand")
    monthly = filtered.assign(month=filtered.created_at.dt.to_period("M")).groupby("month").size()
    monthly.index = monthly.index.astype(str)
    st.line_chart(monthly)
with right:
    st.subheader("CSAT by Channel")
    csat_by_channel = filtered.groupby("channel")["customer_satisfaction"].mean().sort_values()
    st.bar_chart(csat_by_channel)

st.subheader("Service Performance by Priority")
priority = filtered.groupby("priority").agg(
    tickets=("priority", "size"),
    sla_attainment_pct=("sla_met", lambda x: x.mean() * 100),
    median_resolution_hours=("resolution_hours", "median"),
    p90_resolution_hours=("resolution_hours", lambda x: x.quantile(.9)),
    escalation_rate_pct=("escalated", lambda x: x.mean() * 100),
    reopen_rate_pct=("reopened", lambda x: x.mean() * 100),
).round(2)
st.dataframe(priority, use_container_width=True)

st.subheader("Backlog Aging")
open_cases = filtered[filtered["status"].isin(["Open", "Pending"])].copy()
if open_cases.empty:
    st.info("No open or pending tickets in the selected slice.")
else:
    as_of = filtered["created_at"].max()
    age_hours = (as_of - open_cases["created_at"]).dt.total_seconds() / 3600
    bins = [-1, 4, 12, 24, 72, 168, float("inf")]
    labels = ["0–4h", "4–12h", "12–24h", "1–3d", "3–7d", "7d+"]
    aging = age_hours.groupby(pd.cut(age_hours, bins=bins, labels=labels)).size()
    st.bar_chart(aging)
    st.caption(f"Aging is measured against the latest ticket creation timestamp in this synthetic dataset ({as_of.date()}).")

st.subheader("SLA → Customer Outcome")
sla_csat = filtered.groupby("sla_met").agg(
    tickets=("ticket_id", "size"),
    avg_csat=("customer_satisfaction", "mean"),
    low_csat_pct=("customer_satisfaction", lambda x: (x <= 2).mean() * 100),
).round(2)
sla_csat.index = sla_csat.index.map({True: "SLA met", False: "SLA missed"})
st.dataframe(sla_csat, use_container_width=True)
st.caption("This is an observed association in the synthetic dataset, not evidence that SLA performance causes CSAT changes.")

st.subheader("Scenario: Escalation Workload")
sc1, sc2 = st.columns(2)
with sc1:
    cost_per_ticket = st.number_input("Assumed cost per escalated ticket ($)", min_value=0.0, value=8.0, step=1.0)
with sc2:
    reduction_pct = st.slider("Scenario reduction in escalations", 0, 50, 15, 5)

escalated = int(filtered["escalated"].sum())
avoidable = escalated * reduction_pct / 100
scenario_cost = avoidable * cost_per_ticket
m1, m2, m3 = st.columns(3)
m1.metric("Escalated tickets", f"{escalated:,}")
m2.metric("Scenario tickets avoided", f"{avoidable:,.1f}")
m3.metric("Scenario cost avoided", f"${scenario_cost:,.0f}")
st.caption("Scenario only: the cost and reduction assumptions are user inputs. They are not measured financial savings and should not be presented as actual company impact.")

st.subheader("Decision Framework")
st.info(
    "Observation → segment the evidence → test plausible explanations → quantify a scenario → investigate the operational lever. "
    "Do not jump from a correlation or KPI gap directly to a staffing or process recommendation."
)
