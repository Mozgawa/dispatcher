"""Worker."""

from celery import Celery
import os
import subprocess
import pymysql

pymysql.install_as_MySQLdb()

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")
celery.conf.task_track_started = True


@celery.task
def execute(command_line: str):
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
