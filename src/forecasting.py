from prophet import Prophet
import pandas as pd


def generate_forecast(df):

    monthly_sales = (
        df.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    forecast_df = monthly_sales.rename(
        columns={
            "Order Date": "ds",
            "Sales": "y"
        }
    )

    model = Prophet()

    model.fit(forecast_df)

    future = model.make_future_dataframe(
        periods=90
    )

    forecast = model.predict(future)

    return model, forecast