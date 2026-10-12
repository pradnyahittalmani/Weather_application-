from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Add your WeatherAPI.com key here, or set the WEATHER_API_KEY environment variable.
API_KEY = os.getenv("WEATHER_API_KEY", "YOUR_API_KEY_HERE")
API_URL = "https://api.weatherapi.com/v1/forecast.json"


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."
        elif API_KEY == "YOUR_API_KEY_HERE":
            error = "Please add your WeatherAPI.com API key in app.py or set WEATHER_API_KEY."
        else:
            try:
                params = {
                    "key": API_KEY,
                    "q": city,
                    "days": 1,
                    "alerts": "yes",
                    "aqi": "no"
                }

                response = requests.get(API_URL, params=params, timeout=10)
                data = response.json()

                if response.status_code != 200:
                    error = data.get("error", {}).get(
                        "message", "Unable to get weather information."
                    )
                else:
                    current = data["current"]
                    location = data["location"]

                    alerts = []
                    for alert in data.get("alerts", {}).get("alert", []):
                        alerts.append({
                            "headline": alert.get("headline", "Weather Alert"),
                            "severity": alert.get("severity", ""),
                            "event": alert.get("event", ""),
                            "description": alert.get("desc", "")
                        })

                    weather = {
                        "city": location["name"],
                        "region": location.get("region", ""),
                        "country": location["country"],
                        "local_time": location.get("localtime", ""),
                        "temperature": current["temp_c"],
                        "feels_like": current["feelslike_c"],
                        "humidity": current["humidity"],
                        "wind_speed": current["wind_kph"],
                        "condition": current["condition"]["text"],
                        "icon": "https:" + current["condition"]["icon"],
                        "alerts": alerts
                    }

            except requests.exceptions.RequestException:
                error = "Could not connect to the weather service. Check your internet connection."
            except (KeyError, ValueError):
                error = "Unexpected weather data received."

    return render_template("index.html", weather=weather, error=error, city=city)


if __name__ == "__main__":
    app.run(debug=True)
