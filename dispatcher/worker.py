"""Worker."""

import os
import subprocess
from typing import Dict

import pymysql
from celery import Celery

pymysql.install_as_MySQLdb()

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")
celery.conf.task_track_started = True


@celery.task  # type: ignore
def execute(command_line: str) -> Dict[str, str | int]:
    """Execute command task."""
    result = subprocess.run(
        args=command_line,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return {
        "cmnd": command_line,
        "stderr": result.stderr.decode("utf-8"),
        "stdout": result.stdout.decode("utf-8"),
        "code": result.returncode,
    }
