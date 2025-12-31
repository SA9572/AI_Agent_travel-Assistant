"""
Weather Lookup Tool (FINAL – Stable & Standalone)

Uses Open-Meteo API (No API key required)

Run:
python -m tools.weather_tool
"""

from pathlib import Path
import requests


# 🔹 City → Coordinates mapping (based on your project cities)
CITY_COORDINATES = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "goa": (15.2993, 74.1240),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "hyderabad": (17.3850, 78.4867),
    "kolkata": (22.5726, 88.3639),
    "jaipur": (26.9124, 75.7873),
}


OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(city: str, days: int = 3) -> dict:
    """
    Get daily maximum temperature forecast for a city.

    Args:
        city (str): City name
        days (int): Number of days (max 7)

    Returns:
        dict: Weather forecast
    """

    city_key = city.lower()

    if city_key not in CITY_COORDINATES:
        return {
            "status": "error",
            "message": f"Coordinates not available for city: {city}"
        }

    latitude, longitude = CITY_COORDINATES[city_key]

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max",
        "timezone": "auto"
    }

    try:
        response = requests.get(OPEN_METEO_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        dates = data["daily"]["time"][:days]
        temps = data["daily"]["temperature_2m_max"][:days]

        forecast = [
            {
                "date": date,
                "max_temp_c": temp
            }
            for date, temp in zip(dates, temps)
        ]

        return {
            "status": "success",
            "city": city,
            "forecast_days": len(forecast),
            "forecast": forecast
        }

    except requests.RequestException as exc:
        return {
            "status": "error",
            "message": "Failed to fetch weather data",
            "details": str(exc)
        }


# ✅ Terminal output guaranteed
if __name__ == "__main__":
    print(get_weather("Goa", days=3))
