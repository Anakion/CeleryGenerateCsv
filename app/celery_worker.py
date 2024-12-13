import csv
import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task(name="create_task")
def generate_report_task(data, report_id):
    filename = f"report/{report_id}.csv"
    os.makedirs("report", exist_ok=True)

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])  # Заголовки CSV
        writer.writerows(data)  # Данные

    return filename