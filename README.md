# Interactive Business Intelligence Dashboard

## Project Overview

The Interactive Business Intelligence Dashboard is a data analytics application developed using Python and Streamlit. The dashboard provides actionable business insights from the Superstore dataset through interactive visualizations, KPI tracking, geographic analysis, customer segmentation, profit analysis, real-time API integration, and machine learning-based sales forecasting.

---

## Features

### Executive Overview

* Total Sales
* Total Profit
* Total Orders
* Profit Margin
* Monthly Sales Trend
* Regional Sales Performance

### Sales Analysis

* Region Filter
* Category Filter
* Sales KPIs
* Top Performing States
* Monthly Sales Trend

### Profit Analysis

* Profit by Category
* Discount vs Profit Analysis
* Profit Margin Tracking

### Customer Insights

* Customer Segment Analysis
* Sales by Segment
* Top Customers
* Customer Value Metrics

### Geographic Analysis

* Interactive US Sales Map
* Regional Performance Comparison

### Live Business Insights

* Real-Time Exchange Rate API Integration
* Business Interpretation of Market Data

### Sales Forecasting

* Prophet Machine Learning Model
* Future Sales Prediction
* Forecast Data Visualization

---

## Technologies Used

* Python
* Streamlit
* Pandas
* Plotly
* Prophet
* Requests
* NumPy

---

## Project Structure

interactive-business-intelligence-dashboard/

├── dashboard/

│ ├── Home.py

│ └── pages/

│ ├── 1_Executive_Overview.py

│ ├── 2_Sales_Analysis.py

│ ├── 3_Profit_Analysis.py

│ ├── 4_Customer_Insights.py

│ ├── 5_Geographic_Analysis.py

│ ├── 6_Live_Business_Insights.py

│ └── 7_Sales_Forecasting.py

├── src/

│ ├── data_loader.py

│ ├── data_cleaning.py

│ ├── forecasting.py

│ └── api_integration.py

├── data/

│ └── raw/

│ └── SampleSuperstore.csv

├── screenshots/

├── report/

└── README.md

---

## Installation

### Clone Repository

git clone <repository_url>

cd interactive-business-intelligence-dashboard

### Create Virtual Environment

Windows:

python -m venv venv

venv\Scripts\activate

Linux:

python3 -m venv venv

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

---

## Running the Application

Navigate to the dashboard directory:

cd dashboard

Run Streamlit:

streamlit run Home.py

The application will start on:

http://localhost:8501

---

## Dataset

Dataset Used:

Sample Superstore Dataset

Columns Include:

* Sales
* Profit
* Category
* Region
* State
* Customer Information
* Order Information

---

## Machine Learning Forecasting

The forecasting module uses Facebook Prophet to:

* Learn historical sales patterns
* Predict future sales
* Visualize forecast trends
* Support inventory planning and business decision-making

---

## Business Insights

Key Findings:

* West region generated the highest sales.
* Technology category generated the highest profit.
* Consumer segment contributed the largest share of sales.
* California was the highest-performing state.
* Sales demonstrated an overall increasing trend.

---

## Future Enhancements

* Cloud Deployment
* Real-Time Sales Database Integration
* Advanced Predictive Analytics
* Customer Churn Prediction
* Inventory Optimization

---


