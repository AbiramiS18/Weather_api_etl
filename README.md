# Weather API ETL Pipeline

A production-style Data Engineering ETL pipeline that extracts live weather data from the Open-Meteo API, transforms and validates the data, and loads it into a MySQL database.

---

## Features

- Extract live weather data from Open-Meteo API
- Transform JSON into structured format
- Validate data quality
- Load data into MySQL
- Logging
- Exception Handling
- Environment variable configuration
- Docker support

---

## Tech Stack

- Python
- Requests
- Pandas
- SQLAlchemy
- PyMySQL
- MySQL
- Docker

---

## Architecture

```

Open-Meteo API
↓
Extract
↓
Transform
↓
Validate
↓
MySQL
↓
Logging

```

---

## Installation

```bash
git clone <repo_url>

cd weather_api_etl

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

## Environment Variables

```
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

---

## Run

```
python -m app.main
```

---

## Sample Output

```
ETL Completed Successfully

Execution Time: 0.81 seconds
```
