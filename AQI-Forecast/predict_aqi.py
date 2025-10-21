import pandas as pd
import joblib

# Load model
model = joblib.load("AQI-Forecast/models/aqi_model.pkl")

# Load latest data
df = pd.read_csv("AQI-Forecast/data/latest_data.csv")

# Define features
features = ['temperature', 'humidity', 'pressure', 'windspeed',
            'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']

# Predict AQI
df['predicted_aqi'] = model.predict(df[features])

# Save results
df.to_csv("AQI-Forecast/data/predicted_aqi.csv", index=False)
print("✅ Predicted AQI saved as predicted_aqi.csv")
