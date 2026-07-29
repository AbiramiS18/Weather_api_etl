from app.extract import extract_weather
from app.transform import transform_weather
from app.validate import validate_weather

data = extract_weather(13.0827, 80.2707)

df = transform_weather(data)

validate_weather(df)

print("✅ Validation Successful")
