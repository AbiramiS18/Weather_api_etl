from app.extract import extract_weather, save_raw_json

data = extract_weather(13.0827, 80.2707)

save_raw_json(data)

print(data)