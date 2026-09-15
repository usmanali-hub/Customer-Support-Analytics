"""Interactive dashboard for Customer Support Analytics."""
from pathlib import Path
import subprocess
import sys

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "clean_tickets.csv"

st.set_page_config(page_title="Customer Support Analytics", layout="wide")
st.title("Customer Support Analytics")
st.caption("Interactive portfolio dashboard using the project's fixed-seed synthetic support data.")


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

filtered = df[df["channel"].isin(channels) & df["priority"].isin(priorities)].copy()

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Tickets", f"{len(filtered):,}")
c2.metric("SLA Attainment", f"{filtered.sla_met.mean()*100:.1f}%")
c3.metric("Avg First Response", f"{filtered.first_response_hours.mean():.1f}h")
c4.metric("P90 Resolution", f"{filtered.resolution_hours.quantile(.9):.1f}h")
c5.metric("Avg CSAT", f"{filtered.customer_satisfaction.mean():.2f}/5")

left, right = st.columns(2)
with left:
    st.subheader("Ticket Volume")
    monthly = filtered.assign(month=filtered.created_at.dt.to_period("M")).groupby("month").size()
    monthly.index = monthly.index.astype(str)
    st.line_chart(monthly)
with right:
    st.subheader("CSAT by Channel")
    csat = filtered.groupby("channel")["customer_satisfaction"].mean().sort_values()
    st.bar_chart(csat)

st.subheader("Operational Performance by Priority")
priority = filtered.groupby("priority").agg(
    tickets=("priority", "size"),
    sla_attainment_pct=("sla_met", lambda x: x.mean()*100),
    median_resolution_hours=("resolution_hours", "median"),
    p90_resolution_hours=("resolution_hours", lambda x: x.quantile(.9)),
    escalation_rate_pct=("escalated", lambda x: x.mean()*100),
).round(2)
st.dataframe(priority, use_container_width=True)

st.subheader("Decision Lens")
st.info("Use P90 service metrics, SLA attainment, CSAT, escalation rate, and reopen rate together. The synthetic dataset demonstrates the analytical method; it is not production-company performance.")
