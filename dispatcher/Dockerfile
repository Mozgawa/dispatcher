FROM python:3.10.8-slim-buster

ENV PYTHONUNBUFFERED=true
ENV PYTHONDONTWRITEBYTECODE=true
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

WORKDIR /app

COPY /dispatcher dispatcher
COPY pyproject.toml .
COPY README.md .

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --only main
