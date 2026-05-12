import pandas as pd
import requests
import os

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -17.78,
    "longitude": -63.18,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/La_Paz",
    "forecast_days": 7
}

response = requests.get(url, params=params)
data = response.json()["daily"]

df = pd.DataFrame(data)
os.makedirs("data/raw", exist_ok=True)
df.to_parquet("data/raw/clima.parquet")
print("Extract OK:", df.shape)