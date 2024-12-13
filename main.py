import os
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from celery.result import AsyncResult
from app.celery_worker import generate_report_task
import logging


os.makedirs("logs", exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="logs/app.log",
    filemode="a"
)

logger = logging.getLogger(__name__)


app = FastAPI()

@app.post("/generate_report")
async def generate_report():
    report_id = str(uuid4())
    data = [
        ["Alice", 30, "New York"],
        ["Bob", 25, "London"],
        ["Charlie", 40, "Paris"],
        ["David", 35, "Tokyo"],
    ]

    logger.info(f"Submitting task to Celery with report_id={report_id} and data={data}")

    task = generate_report_task.delay(data, report_id)

    logger.info(f"Task submitted: id={task.id}")

    return {"report_id": report_id, "task_id": task.id, "status": "Task submitted"}



@app.get("/report-status/{report_id}")
async def report_status(report_id: str):
    logger.info(f"Checking status for task with report_id={report_id}")

    task = AsyncResult(report_id)

    if task:
        logger.info(f"Task found: id={task.id}, status={task.status}, result={task.result}")
    else:
        logger.warning(f"Task with id={report_id} not found")
        raise HTTPException(status_code=404, detail="Report not found")

    if task.ready():
        logger.info(f"Task with id={report_id} is completed")
        return {"status": "completed", "file": f"/download/{report_id}"}

    logger.info(f"Task with id={report_id} is in progress")
    return {"status": "in progress"}



@app.get("/download/{report_id}")
async def download_report(report_id: str):
    filename = f"report/{report_id}.csv"
    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(filename)


