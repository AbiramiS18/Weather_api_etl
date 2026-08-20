from app.db_connection import get_engine
from app.logger import logger


def load_weather(df):
    """
    Load validated weather DataFrame into MySQL.
    """

    try:
        logger.info("Loading data into MySQL...")

        engine = get_engine()

        df.to_sql(
            name="weather_data",
            con=engine,
            if_exists="append",
            index=False
        )

        logger.info(f"{len(df)} record(s) loaded successfully.")

    except Exception as e:
        logger.error(f"Loading failed: {e}")
        raise