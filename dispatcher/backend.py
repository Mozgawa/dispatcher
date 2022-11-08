"""Backend."""

from typing import Any, Dict

import sqlalchemy as sa
from celery.backends.database import DatabaseBackend
from celery.backends.database.models import Task, TaskSet


class RCSTask(Task):
    """Override Task."""

    result_string = sa.Column(sa.String(4000), nullable=True)

    def to_dict(self) -> Dict[str, Any]:
        """To dict."""
        task_dict = super().to_dict()
        task_dict.update(
            {
                "result_string": self.result_string,
            }
        )
        return task_dict


class RCSTaskSet(TaskSet):
    """Override TaskSet."""

    result_string = sa.Column(sa.String(4000), nullable=True)

    def to_dict(self) -> Dict[str, Any]:
        """To dict."""
        taskset_dict = super().to_dict()
        taskset_dict.update(
            {
                "result_string": self.result_string,
            }
        )
        return taskset_dict


class RCSDatabaseBackend(DatabaseBackend):  # pylint: disable=abstract-method
    """Override DatabaseBackend"""

    task_cls = RCSTask
    taskset_cls = RCSTaskSet

    # pylint: disable-next=too-many-arguments
    def _update_result(self, task, result, state, traceback=None, request=None):
        super()._update_result(task, result, state, traceback, request)
        setattr(task, "result_string", str(result))
