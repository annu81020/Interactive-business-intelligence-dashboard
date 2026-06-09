import pandas as pd


def load_data():
    df = pd.read_csv(
        "data/processed/cleaned_superstore.csv"
    )

    return df