# Weather API ETL Pipeline

A Data Engineering ETL pipeline that extracts live weather data from the Open-Meteo API, transforms and validates the data, and loads it into MySQL using Apache Airflow for workflow orchestration.

---

## Features

- Extract live weather data from Open-Meteo API
- Transform JSON into structured format
- Validate data quality
- Load data into MySQL
- Airflow DAG orchestration
- Raw JSON and processed CSV storage
- Logging and exception handling
- Dockerized Airflow and MySQL
- Environment variable configuration

---

## Tech Stack

- Python
- Apache Airflow 2.10.0
- Requests
- Pandas
- SQLAlchemy
- PyMySQL
- MySQL
- Docker & Docker Compose

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
DB_HOST=weather_mysql
DB_PORT=3306
DB_NAME=weather_api
DB_USER=root
DB_PASSWORD=
```

---

## Run with Docker

```
cd airflow
docker compose up -d
```

---

## Airflow

```
Open the Airflow UI:
http://localhost:8081

Login:

Username: admin
Password: admin
```

---

## Verify MySQL Data

```
docker exec -it weather_mysql \
mysql -uroot -proot \
-e "USE weather_api; SELECT * FROM weather_data;
```

---

## Stop Services

```
docker compose down
```
