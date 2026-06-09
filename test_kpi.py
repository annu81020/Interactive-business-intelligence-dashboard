from src.data_loader import load_data
from src.kpi_calculator import calculate_kpis

df = load_data()

kpis = calculate_kpis(df)

for key, value in kpis.items():
    print(f"{key}: {value}")