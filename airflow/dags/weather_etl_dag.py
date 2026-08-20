from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import json
import os

from app.extract import extract_weather, save_raw_json
from app.transform import transform_weather
from app.validate import validate_weather
from app.load import load_weather


def extract_task():
    data = extract_weather(13.0827, 80.2707)

    raw_file = "/opt/project/data/raw/weather.json"

    save_raw_json(data, raw_file)

    return raw_file


def transform_task(ti):
    raw_file = ti.xcom_pull(task_ids="extract")

    with open(raw_file, "r") as file:
        data = json.load(file)

    processed_file = "/opt/project/data/processed/weather.csv"

    transform_weather(data, processed_file)

    return processed_file


def validate_task(ti):
    processed_file = ti.xcom_pull(task_ids="transform")

    print("Processed file:", processed_file)
    print("Type:", type(processed_file))

    df = pd.read_csv(str(processed_file))

    validate_weather(df)

    return processed_file


def load_task(ti):
    processed_file = ti.xcom_pull(task_ids="validate")

    print("Processed file:", processed_file)
    print("Type:", type(processed_file))

    df = pd.read_csv(str(processed_file))

    load_weather(df)


with DAG(
    dag_id="weather_etl",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["weather", "etl"],
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_task,
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_task,
    )

    validate = PythonOperator(
        task_id="validate",
        python_callable=validate_task,
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_task,
    )

    extract >> transform >> validate >> load