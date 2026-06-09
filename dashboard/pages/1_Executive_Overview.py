import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

import streamlit as st

from src.data_loader import load_data
from src.kpi_calculator import calculate_kpis
from src.visualizations import (
    monthly_sales_trend,
    sales_by_region,
    sales_by_category,
    profit_by_category
)

st.set_page_config(
    page_title="Executive Overview",
    layout="wide"
)

df = load_data()

kpis = calculate_kpis(df)

st.title("Executive Overview")

st.markdown(
    "High-level business performance indicators and trends."
)

st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"${kpis['total_sales']:,.0f}"
)

col2.metric(
    "Total Profit",
    f"${kpis['total_profit']:,.0f}"
)

col3.metric(
    "Total Orders",
    f"{kpis['total_orders']:,}"
)

col4.metric(
    "Profit Margin",
    f"{kpis['profit_margin']}%"
)

st.divider()

col5, col6 = st.columns(2)

with col5:
    st.plotly_chart(
        monthly_sales_trend(df),
        use_container_width=True
    )

with col6:
    st.plotly_chart(
        sales_by_region(df),
        use_container_width=True
    )

st.divider()

col7, col8 = st.columns(2)

with col7:
    st.plotly_chart(
        sales_by_category(df),
        use_container_width=True
    )

with col8:
    st.plotly_chart(
        profit_by_category(df),
        use_container_width=True
    )