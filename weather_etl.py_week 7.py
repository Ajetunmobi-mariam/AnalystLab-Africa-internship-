# ==========
# TASK 1 Extract Data
# ==========
# ========== import libraries
import requests
import pandas as pd

API_KEY = "b7d06bc153967f27a3a08f40c4bc53ea"

cities = ["Lagos", "Abuja", "Port Harcourt"]

weather_data = []

for city in cities:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_condition = data["weather"][0]["main"]
    wind_speed = data["wind"]["speed"]
    date_time = data["dt"]

    weather_data.append({
        "City": city_name,
        "Temperature": temperature,
        "Humidity": humidity,
        "Weather Condition": weather_condition,
        "Wind Speed": wind_speed,
        "Date_Time": date_time
    })

    print("\nRAW WEATHER DATA")
print(weather_data)

# ==========
# TASK 2: TRANSFORM DATA
# =========
df = pd.DataFrame(weather_data)

df["Date_Time"] = pd.to_datetime(df["Date_Time"], unit="s")

print(df)

# =========
# TASK 3: LOAD DATA
# =========
df.to_csv("weather_data.csv", index=False)

print("Weather data saved successfully!")

# =========
# TASK 4: BASIC ANALYSIS
# =========
print("\nBASIC ANALYSIS")

print("Average Temperature:", df["Temperature"].mean())

highest_humidity = df.loc[df["Humidity"].idxmax()]

print("\nCity with Highest Humidity:")
print(highest_humidity["City"], "-", highest_humidity["Humidity"])

print("\nWeather Conditions:")
print(df["Weather Condition"].value_counts())
