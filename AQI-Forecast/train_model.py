import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Load latest data
df = pd.read_csv("AQI-Forecast/data/latest_data.csv")

# Define features and target
features = ['temperature', 'humidity', 'pressure', 'windspeed',
            'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']
target = 'aqi'

X = df[features]
y = df[target]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
os.makedirs("AQI-Forecast/models", exist_ok=True)
joblib.dump(model, "AQI-Forecast/models/aqi_model.pkl")
print("✅ Model trained and saved at models/aqi_model.pkl")
