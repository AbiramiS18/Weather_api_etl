import time

from app.extract import extract_weather, save_raw_json
from app.transform import transform_weather
from app.validate import validate_weather
from app.load import load_weather
from app.logger import logger


def main():
    start_time = time.time()

    try:
        logger.info("=" * 50)
        logger.info("Weather API ETL Started")

        # Chennai Coordinates
        data = extract_weather(13.0827, 80.2707)

        save_raw_json(data)

        df = transform_weather(data)

        validate_weather(df)

        load_weather(df)

        execution_time = time.time() - start_time

        logger.info(f"Execution Time: {execution_time:.2f} seconds")
        logger.info("Weather API ETL Completed Successfully")
        logger.info("=" * 50)

        print(f"\n✅ ETL Completed Successfully")
        print(f"⏱ Execution Time: {execution_time:.2f} seconds")

    except Exception as e:
        logger.exception(e)
        print(e)


if __name__ == "__main__":
    main()