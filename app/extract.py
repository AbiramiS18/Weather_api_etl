import requests
import json
import os

from app.logger import logger

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def extract_weather(latitude=13.0827, longitude=80.2707):
    """
    Fetch current weather data from Open-Meteo API.
    """

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    try:
        logger.info("Calling Open-Meteo API...")

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        logger.info("API call successful.")

        return data

    except requests.exceptions.Timeout:
        logger.error("API request timed out.")
        raise

    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise

def save_raw_json(data, filename="data/raw/weather.json"):
    """
    Save raw API response to a JSON file.
    """

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    logger.info(f"Raw JSON saved to {filename}")

    return filename