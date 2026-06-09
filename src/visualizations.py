import plotly.express as px


def monthly_sales_trend(df):

    monthly_sales = (
        df.groupby("Month-Year")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly_sales,
        x="Month-Year",
        y="Sales",
        title="Monthly Sales Trend",
        markers=True
    )

    return fig


def sales_by_region(df):

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        title="Sales by Region"
    )

    return fig


def sales_by_category(df):

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category_sales,
        names="Category",
        values="Sales",
        title="Sales Distribution by Category"
    )

    return fig


def profit_by_category(df):

    category_profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_profit,
        x="Category",
        y="Profit",
        title="Profit by Category"
    )

    return fig