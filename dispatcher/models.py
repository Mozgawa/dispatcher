"""Models."""

from pydantic import BaseModel


class DispatchRequest(BaseModel):
    """Dispatch request model."""

    command: str
