FROM python:3.13-slim

RUN apt-get update && apt-get install -y gcc curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY . /app

RUN poetry install --no-dev --no-root

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
