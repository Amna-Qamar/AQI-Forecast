import requests
import pandas as pd
from datetime import datetime
import os

# Load API key from environment variable (for GitHub Actions)
API_KEY = os.getenv("fb6ebadc9782dfb7b422292bd7489279")

# Karachi coordinates
LAT, LON = 24.8607, 67.0011

def fetch_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()
    return {
        "city": res["name"],
        "temperature": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "pressure": res["main"]["pressure"],
        "windspeed": res["wind"]["speed"],
        "time": datetime.now()
    }

def fetch_air_pollution_data():
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"
    res = requests.get(url).json()
    comp = res["list"][0]["components"]
    return {
        "co": comp["co"],
        "no": comp["no"],
        "no2": comp["no2"],
        "o3": comp["o3"],
        "so2": comp["so2"],
        "pm2_5": comp["pm2_5"],
        "pm10": comp["pm10"],
        "nh3": comp["nh3"],
        "aqi": res["list"][0]["main"]["aqi"],
        "time": datetime.now()
    }

def get_combined_data():
    weather = fetch_weather_data()
    pollution = fetch_air_pollution_data()
    combined = {**weather, **pollution}
    df = pd.DataFrame([combined])
    df.to_csv("AQI-Forecast/data/latest_data.csv", index=False)
    print("✅ Live data fetched and saved as latest_data.csv")
    return df

if __name__ == "__main__":
    get_combined_data()
