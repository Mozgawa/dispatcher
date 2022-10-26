"""Models."""

from pydantic import BaseModel


class DispatchRequest(BaseModel):
    command: str
