import streamlit as st
import pandas as pd
from src.data_loader import load_data

st.set_page_config(
    page_title="Interactive Business Intelligence Dashboard",
    layout="wide"
)

df = load_data()

st.title("Interactive Business Intelligence Dashboard")

st.markdown("""
This dashboard provides actionable business insights using the Superstore dataset and supports data-driven decision making.
""")

st.divider()

# ---------------- KPI SECTION ---------------- #

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
profit_margin = (total_profit / total_sales) * 100

customers = df["Customer ID"].nunique()
quantity_sold = df["Quantity"].sum()
top_region = df.groupby("Region")["Sales"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Profit Margin", f"{profit_margin:.2f}%")

st.divider()

col5, col6, col7 = st.columns(3)

col5.metric("Customers", f"{customers:,}")
col6.metric("Quantity Sold", f"{quantity_sold:,}")
col7.metric("Top Region", top_region)

st.divider()

# ---------------- BUSINESS INSIGHTS ---------------- #

st.subheader("Key Business Insights")

st.success("""
• West region generates the highest sales revenue.

• Technology category contributes the highest profit.

• Consumer segment accounts for the largest share of sales.

• California is the strongest-performing state.

• Overall sales show a positive growth trend over time.
""")

st.subheader("Business Recommendations")

st.info("""
1. Increase investment in high-performing West region markets.

2. Expand Technology product offerings.

3. Launch loyalty programs for top customers.

4. Reduce excessive discounts on low-margin products.

5. Use forecasting results for inventory planning and demand management.
""")

st.divider()

# ---------------- DATASET SUMMARY ---------------- #

st.subheader("Dataset Summary")

col8, col9 = st.columns(2)

col8.metric("Rows", f"{len(df):,}")
col9.metric("Columns", f"{len(df.columns)}")

st.write("### Sample Dataset Records")

st.dataframe(
    df.head(10),
    width="stretch"
)