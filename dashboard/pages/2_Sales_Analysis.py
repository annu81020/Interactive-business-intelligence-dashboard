import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

import streamlit as st
import plotly.express as px

from src.data_loader import load_data

st.set_page_config(
    page_title="Sales Analysis",
    layout="wide"
)

st.title("Sales Analysis")

df = load_data()

# ======================
# Filters
# ======================

st.subheader("Filters")

col1, col2 = st.columns(2)

with col1:
    selected_region = st.selectbox(
        "Select Region",
        ["All"] + sorted(df["Region"].unique().tolist())
    )

with col2:
    selected_category = st.selectbox(
        "Select Category",
        ["All"] + sorted(df["Category"].unique().tolist())
    )

# Apply Filters

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

# ======================
# KPI Cards
# ======================

st.divider()

total_sales = round(
    filtered_df["Sales"].sum(),
    2
)

total_profit = round(
    filtered_df["Profit"].sum(),
    2
)

total_orders = filtered_df["Order ID"].nunique()

avg_order_value = round(
    total_sales / total_orders,
    2
) if total_orders > 0 else 0

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(
        "Total Sales",
        f"${total_sales:,.0f}"
    )

with kpi2:
    st.metric(
        "Total Profit",
        f"${total_profit:,.0f}"
    )

with kpi3:
    st.metric(
        "Orders",
        f"{total_orders:,}"
    )

with kpi4:
    st.metric(
        "Avg Order Value",
        f"${avg_order_value:,.0f}"
    )

# ======================
# Top States Chart
# ======================

st.divider()

sales_by_state = (
    filtered_df.groupby("State")["Sales"]
    .sum()
    .reset_index()
    .sort_values(
        "Sales",
        ascending=False
    )
    .head(10)
)

fig1 = px.bar(
    sales_by_state,
    x="State",
    y="Sales",
    title="Top 10 States by Sales"
)

fig1.update_layout(height=500)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ======================
# Monthly Sales Trend
# ======================

monthly_sales = (
    filtered_df.groupby("Month-Year")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    monthly_sales,
    x="Month-Year",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)

fig2.update_layout(height=500)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ======================
# Sales By Category
# ======================

sales_by_category = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig3 = px.pie(
    sales_by_category,
    names="Category",
    values="Sales",
    title="Sales Distribution by Category"
)

fig3.update_layout(height=500)

st.plotly_chart(
    fig3,
    use_container_width=True
)