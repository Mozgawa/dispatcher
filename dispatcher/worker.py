"""Worker."""

import subprocess
from datetime import datetime
from typing import Dict

from celery import Celery

celery = Celery(__name__)
celery.conf.task_track_started = True
celery.conf.result_persistent = False


@celery.task  # type: ignore
def execute(command_line: str) -> Dict[str, str | int]:
    """Execute command task."""
    call_start_date = str(datetime.now())
    result = subprocess.run(args=command_line, shell=True)
    return {
        "call_cmnd_txt": command_line,
        "call_sttus_code": result.returncode,
        "call_start_date": call_start_date,
        "call_end_date": str(datetime.now()),
    }
