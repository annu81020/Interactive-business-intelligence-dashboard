import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

import streamlit as st
import plotly.express as px

from src.data_loader import load_data

st.set_page_config(
    page_title="Profit Analysis",
    layout="wide"
)

st.title("Profit Analysis")

df = load_data()

# ======================
# Filters
# ======================

selected_category = st.selectbox(
    "Select Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

# ======================
# KPIs
# ======================

total_profit = round(
    filtered_df["Profit"].sum(),
    2
)

total_sales = round(
    filtered_df["Sales"].sum(),
    2
)

profit_margin = round(
    (total_profit / total_sales) * 100,
    2
) if total_sales > 0 else 0

avg_profit = round(
    filtered_df["Profit"].mean(),
    2
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Profit",
        f"${total_profit:,.0f}"
    )

with col2:
    st.metric(
        "Profit Margin",
        f"{profit_margin}%"
    )

with col3:
    st.metric(
        "Average Profit",
        f"${avg_profit:,.2f}"
    )

st.divider()

# ======================
# Profit by Category
# ======================

profit_category = (
    filtered_df.groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    profit_category,
    x="Category",
    y="Profit",
    title="Profit by Category"
)

fig1.update_layout(height=500)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ======================
# Discount vs Profit
# ======================

fig2 = px.scatter(
    filtered_df,
    x="Discount",
    y="Profit",
    color="Category",
    title="Discount vs Profit"
)

fig2.update_layout(height=500)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ======================
# Top Profitable States
# ======================

state_profit = (
    filtered_df.groupby("State")["Profit"]
    .sum()
    .reset_index()
    .sort_values(
        "Profit",
        ascending=False
    )
    .head(10)
)

fig3 = px.bar(
    state_profit,
    x="State",
    y="Profit",
    title="Top 10 Profitable States"
)

fig3.update_layout(height=500)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ======================
# Loss Making States
# ======================

st.subheader("Loss Making States")

loss_states = (
    filtered_df.groupby("State")["Profit"]
    .sum()
    .reset_index()
)

loss_states = loss_states[
    loss_states["Profit"] < 0
].sort_values(
    "Profit"
)

st.dataframe(
    loss_states,
    use_container_width=True
)