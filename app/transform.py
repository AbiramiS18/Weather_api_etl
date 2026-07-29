import pandas as pd
from datetime import datetime

from app.logger import logger


def transform_weather(data):
    """
    Transform raw weather JSON into a DataFrame.
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

    logger.info("Transformation completed.")

    return df