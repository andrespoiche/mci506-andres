import pandas as pd
import os

df = pd.read_parquet("data/raw/clima.parquet")
df["temp_promedio"] = (df["temperature_2m_max"] + df["temperature_2m_min"]) / 2
result = df[["time", "temp_promedio", "precipitation_sum"]]

os.makedirs("data/processed", exist_ok=True)
result.to_parquet("data/processed/clima_summary.parquet")
print("Transform OK:")
print(result)