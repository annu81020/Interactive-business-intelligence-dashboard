import pandas as pd


def calculate_kpis(df):
    """
    Calculate business KPIs for dashboard
    """

    total_sales = round(df["Sales"].sum(), 2)

    total_profit = round(df["Profit"].sum(), 2)

    total_orders = df["Order ID"].nunique()

    total_customers = df["Customer ID"].nunique()

    total_quantity = int(df["Quantity"].sum())

    profit_margin = round(
        (total_profit / total_sales) * 100,
        2
    )

    average_order_value = round(
        total_sales / total_orders,
        2
    )

    top_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "total_quantity": total_quantity,
        "profit_margin": profit_margin,
        "average_order_value": average_order_value,
        "top_region": top_region,
    }