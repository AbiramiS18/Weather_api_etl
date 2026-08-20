import os
import pandas as pd
from datetime import datetime

from app.logger import logger


def transform_weather(data, output_file="data/processed/weather.csv"):
    """
    Transform raw weather JSON into a DataFrame
    and save it as a CSV.
    """

    logger.info("Transforming weather data...")

    current = data["current"]

    weather = {
        "latitude": data["latitude"],
        "longitude": data["longitude"],
        "timezone": data["timezone"],
        "observation_time": current["time"],
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "etl_timestamp": datetime.now()
    }

    df = pd.DataFrame([weather])

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    df.to_csv(output_file, index=False)

    logger.info(f"Processed CSV saved to {output_file}")

    return output_file