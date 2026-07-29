from app.logger import logger


def validate_weather(df):
    """
    Validate transformed weather data.
    """

    logger.info("Validating weather data...")

    # Check for missing values
    if df.isnull().values.any():
        raise ValueError("Validation Failed: Missing values found.")

    # Check for duplicate records
    if df.duplicated().any():
        raise ValueError("Validation Failed: Duplicate records found.")

    # Validate latitude
    if not df["latitude"].between(-90, 90).all():
        raise ValueError("Validation Failed: Invalid latitude.")

    # Validate longitude
    if not df["longitude"].between(-180, 180).all():
        raise ValueError("Validation Failed: Invalid longitude.")

    # Validate temperature
    if not df["temperature"].between(-100, 60).all():
        raise ValueError("Validation Failed: Invalid temperature.")

    logger.info("Validation passed.")

    return True