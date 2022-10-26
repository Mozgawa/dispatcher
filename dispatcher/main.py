"""Server."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from worker import execute
from models import DispatchRequest

app = FastAPI()


@app.post("/api/v1/call/sync")
def sync_call(r: DispatchRequest):
    async_result = execute.delay(command_line=r.command)
    result = async_result.wait()
    return JSONResponse(
        status_code=200, headers={"x-task-id": async_result.id}, content=result
    )


@app.post("/api/v1/call/async")
def async_call(r: DispatchRequest):
    result = execute.delay(command_line=r.command)
    return JSONResponse(status_code=200, content={"callId": result.id})
