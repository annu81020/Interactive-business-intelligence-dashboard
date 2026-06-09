import pandas as pd
from pathlib import Path

RAW_DATA_PATH = "data/raw/SampleSuperstore.csv"
PROCESSED_DATA_PATH = "data/processed/cleaned_superstore.csv"


def clean_data():

    df = pd.read_csv(RAW_DATA_PATH, encoding="latin1")

    print("Original Shape:", df.shape)

    # Date conversion
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Date features
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month Name"] = df["Order Date"].dt.strftime("%B")
    df["Quarter"] = df["Order Date"].dt.quarter
    df["Month-Year"] = df["Order Date"].dt.to_period("M").astype(str)

    # Shipping days
    df["Shipping Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    # Profit margin
    df["Profit Margin"] = (
        df["Profit"] / df["Sales"]
    ) * 100

    # Cleanup
    df.replace([float("inf"), float("-inf")], 0, inplace=True)
    df.fillna(0, inplace=True)

    Path("data/processed").mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    print("Cleaned Shape:", df.shape)
    print("Saved:", PROCESSED_DATA_PATH)

    return df


if __name__ == "__main__":
    clean_data()