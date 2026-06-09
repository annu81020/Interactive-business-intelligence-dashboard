import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

import streamlit as st
import plotly.express as px

from src.data_loader import load_data

st.set_page_config(
    page_title="Customer Insights",
    layout="wide"
)

st.title("👥 Customer Insights")

df = load_data()

# =====================
# Filters
# =====================

segment = st.selectbox(
    "Select Customer Segment",
    ["All"] + sorted(df["Segment"].unique())
)

filtered_df = df.copy()

if segment != "All":
    filtered_df = filtered_df[
        filtered_df["Segment"] == segment
    ]

# =====================
# KPI Cards
# =====================

total_customers = (
    filtered_df["Customer ID"]
    .nunique()
)

total_sales = round(
    filtered_df["Sales"].sum(),
    2
)

avg_customer_value = round(
    total_sales / total_customers,
    2
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Customers",
        total_customers
    )

with col2:
    st.metric(
        "Total Sales",
        f"${total_sales:,.0f}"
    )

with col3:
    st.metric(
        "Avg Customer Value",
        f"${avg_customer_value:,.0f}"
    )

st.divider()

# =====================
# Segment Distribution
# =====================

segment_sales = (
    filtered_df.groupby("Segment")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.pie(
    segment_sales,
    names="Segment",
    values="Sales",
    title="Sales by Segment"
)

fig1.update_layout(height=500)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =====================
# Top Customers
# =====================

top_customers = (
    filtered_df.groupby(
        "Customer Name"
    )["Sales"]
    .sum()
    .reset_index()
    .sort_values(
        "Sales",
        ascending=False
    )
    .head(10)
)

fig2 = px.bar(
    top_customers,
    x="Customer Name",
    y="Sales",
    title="Top 10 Customers"
)

fig2.update_layout(height=500)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================
# Customer Table
# =====================

st.subheader(
    "Top Customer Details"
)

st.dataframe(
    top_customers,
    use_container_width=True
)