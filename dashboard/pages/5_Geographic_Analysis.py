import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

import streamlit as st
import plotly.express as px

from src.data_loader import load_data

st.title("Geographic Analysis")

df = load_data()

state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .reset_index()
)

fig = px.choropleth(
    state_sales,
    locations="State",
    locationmode="USA-states",
    color="Sales",
    scope="usa",
    title="Sales by State"
)

st.plotly_chart(fig, use_container_width=True)

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Regional Sales Performance"
)

st.plotly_chart(fig2, use_container_width=True)