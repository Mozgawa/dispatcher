"""Server."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from dispatcher.models import DispatchRequest
from dispatcher.worker import execute

app = FastAPI()


@app.post("/api/v1/call/sync")
def sync_call(request: DispatchRequest) -> JSONResponse:
    """Executes the command synchronously."""
    async_result = execute.delay(command_line=request.command)
    result = async_result.wait()
    return JSONResponse(status_code=200, headers={"x-task-id": async_result.id}, content=result)


@app.post("/api/v1/call/async")
def async_call(request: DispatchRequest) -> JSONResponse:
    """Executes the command asynchronously."""
    result = execute.delay(command_line=request.command)
    return JSONResponse(status_code=200, content={"callId": result.id})
