import pandas as pd

from src.decision_metrics import backlog_aging, scenario_impact, segment_signal


def test_support_kpi_logic():
    df = pd.DataFrame({
        "priority": ["High", "Low", "High", "Low"],
        "sla_met": [True, True, False, False],
        "first_response_hours": [1.0, 2.0, 6.0, 4.0],
        "resolution_hours": [4.0, 8.0, 24.0, 12.0],
        "customer_satisfaction": [5, 4, 2, 1],
        "escalated": [False, False, True, True],
        "reopened": [False, False, True, False],
    })
    assert df["sla_met"].mean() * 100 == 50.0
    assert df["first_response_hours"].quantile(0.90) > df["first_response_hours"].median()
    assert (df["customer_satisfaction"] <= 2).mean() * 100 == 50.0


def test_high_priority_sla_is_separately_measurable():
    df = pd.DataFrame({
        "priority": ["High", "High", "Low"],
        "sla_met": [True, False, True],
    })
    high = df.loc[df["priority"].eq("High"), "sla_met"]
    assert high.mean() * 100 == 50.0


def test_backlog_aging_buckets_open_cases():
    df = pd.DataFrame({
        "ticket_id": ["1", "2", "3"],
        "created_at": pd.to_datetime(["2025-01-01 00:00", "2025-01-01 20:00", "2025-01-02 00:00"]),
        "status": ["Open", "Pending", "Resolved"],
    })
    aging = backlog_aging(df)
    assert aging["tickets"].sum() == 2


def test_scenario_impact_is_explicit_and_bounded():
    df = pd.DataFrame({"escalated": [True, True, False, False]})
    result = scenario_impact(df, cost_per_ticket=10, reduction_pct=25)
    assert result["escalated_tickets"] == 2
    assert result["scenario_tickets_avoided"] == 0.5
    assert result["scenario_cost_avoided"] == 5


def test_segment_signal_requires_minimum_volume():
    df = pd.DataFrame({
        "ticket_id": ["1", "2", "3", "4"],
        "issue_type": ["Billing", "Billing", "Billing", "Technical"],
        "sla_met": [True, False, False, False],
        "escalated": [False, True, True, True],
        "reopened": [False, False, True, True],
        "customer_satisfaction": [5, 3, 2, 1],
        "resolution_hours": [2, 10, 12, 20],
    })
    result = segment_signal(df, "issue_type", min_tickets=3)
    assert list(result.index) == ["Billing"]
