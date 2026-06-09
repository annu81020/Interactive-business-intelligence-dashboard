import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

import streamlit as st
import requests

st.title("Live Business Insights")

st.subheader("Live Exchange Rates")

try:

    response = requests.get(
        "https://api.frankfurter.app/latest?from=USD"
    )

    data = response.json()

    usd_to_eur = data["rates"]["EUR"]
    usd_to_gbp = data["rates"]["GBP"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "USD → EUR",
            round(usd_to_eur, 4)
        )

    with col2:
        st.metric(
            "USD → GBP",
            round(usd_to_gbp, 4)
        )

    st.success(
        "Exchange rates updated successfully."
    )

except Exception as e:

    st.error(
        f"Unable to fetch live data: {e}"
    )

st.markdown("""
### Business Interpretation

Exchange rate fluctuations can influence:

- International purchasing power
- Product pricing strategies
- Revenue forecasting
- Global market expansion decisions

Real-time economic indicators help decision-makers
adapt to changing market conditions.
""")