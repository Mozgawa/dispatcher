FROM python:3.10.8-slim-buster

ENV PYTHONUNBUFFERED=true
ENV PYTHONDONTWRITEBYTECODE=true
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN apt-get update \
    && apt-get -y install unzip \
    && apt-get -y install libaio1 \
    && apt-get -y install wget \
    && mkdir -p /opt/oracle \
    && apt-get -y install git

WORKDIR /opt/oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/218000/instantclient-basiclite-linux.x64-21.8.0.0.0dbru.zip
RUN unzip instantclient-basiclite-linux.x64-21.8.0.0.0dbru.zip
RUN pip install --no-cache-dir git+https://github.com/Mozgawa/celery.git
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_8:$LD_LIBRARY_PATH

WORKDIR /app

COPY /dispatcher dispatcher
COPY pyproject.toml .
COPY README.md .

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --only main
