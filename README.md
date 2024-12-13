# 🚀 FastAPI + Celery Project

This project is an example of an application using FastAPI for the web server and Celery for asynchronous tasks. Redis is used as the message broker for Celery. Poetry is also used for managing dependencies.

## Description

This project demonstrates how to use:

- **FastAPI** to create a high-performance web application.
- **Celery** for processing asynchronous tasks, such as report generation, email sending, and other background processes.
- **Redis** as the message broker for Celery, so tasks can be queued and processed independently from the main program.
- **Poetry** for managing dependencies and virtual environments.

### Key Features:

- Creating asynchronous tasks with Celery.
- Handling long-running operations (e.g., report generation) in the background.
- Connecting Celery and Redis via Docker.
- Using JWT for user authentication.

## 🛠 Technologies

- **FastAPI** — Web framework for building high-speed APIs.
- **Celery** — Library for executing asynchronous tasks.
- **Redis** — Message broker for Celery.
- **Poetry** — Tool for managing dependencies and virtual environments.
- **Docker** — Used for containerizing the application.

## ⚙️ Installing and running

1. **Clone repository:**

   ```bash
   git clone https://github.com/Anakion/CeleryGenerateCsv.git

2. **Open directory**
   ```bash
   cd CeleryGenerateCsv
3. **Launching an application:**

   **To run an application using Docker, execute:**

    ```bash
      docker-compose up -d
    ```
4. **Access to the application:**

    **FastAPI will be available at**
  
      ```bash
        http://localhost:8000.
      ```
    **Flower (for monitoring Celery tasks) will be available at** 
    
      ```bash
        http://localhost:5556
      ```
## 🚀 API Endpoints

**POST /generate_report**

**This endpoint creates a task to generate a report.**

**Example of a request:**

```bash
curl -X 'POST' 'http://localhost:8000/generate_report' -H 'accept: application/json'
```

**Example response:**

```bash
{
  "report_id": "5335b923-3149-4684-a726-0c7eccd8c523",
  "status": "Task submitted"
}
```



