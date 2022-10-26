FROM python:3.10.8-slim-buster

ENV PYTHONUNBUFFERED=true
ENV PYTHONDONTWRITEBYTECODE=true
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

WORKDIR /app

COPY /dispatcher /app
COPY pyproject.toml /app

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
