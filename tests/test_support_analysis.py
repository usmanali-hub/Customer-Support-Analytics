import pandas as pd


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
