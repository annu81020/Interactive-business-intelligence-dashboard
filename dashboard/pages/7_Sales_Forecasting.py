import streamlit as st
import pandas as pd
import plotly.express as px

from src.forecasting import generate_forecast
from src.data_loader import load_data

st.title("Sales Forecasting")

st.write(
    "Forecast future sales using historical transaction data."
)

# Load data
df = load_data()

# Generate forecast
model, forecast = generate_forecast(df)

# ---------------- CHART ---------------- #

st.subheader("Predicted Sales Trend")

fig = px.line(
    forecast,
    x="ds",
    y="yhat",
    title="Sales Forecast"
)

fig.update_layout(
    height=500
)

fig.update_xaxes(
    title="Date"
)

fig.update_yaxes(
    title="Predicted Sales ($)"
)

st.plotly_chart(
    fig,
    width="stretch"
)

# ---------------- TABLE ---------------- #

st.subheader("Forecast Data")

forecast_display = forecast[["ds", "yhat"]].copy()

forecast_display.columns = [
    "Forecast Date",
    "Predicted Sales ($)"
]

forecast_display["Forecast Date"] = (
    pd.to_datetime(
        forecast_display["Forecast Date"]
    ).dt.strftime("%d-%b-%Y")
)

forecast_display["Predicted Sales ($)"] = (
    forecast_display["Predicted Sales ($)"]
    .round(2)
)

st.dataframe(
    forecast_display.tail(30),
    width="stretch"
)