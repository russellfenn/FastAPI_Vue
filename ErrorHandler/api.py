from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse, PlainTextResponse
from pydantic import BaseModel
from typing import Dict, Optional, Union
import json
import logging
import os

DEFAULT_LOGGING_LEVEL = logging.WARN  # 30
LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", DEFAULT_LOGGING_LEVEL)


class SampleData(BaseModel):
    type_int: int
    type_float: float
    type_bool: bool
    type_str: str


class SampleResponse(BaseModel):
    is_error: bool = False
    msg: str
    input: SampleData


app = FastAPI()

# Logging
logger: logging.Logger = logging.getLogger(__name__)
try:
    logger.setLevel(LOGGING_LEVEL)
except ValueError:
    logger.warn(f"Invalid log level '{LOGGING_LEVEL}'. Setting to default {DEFAULT_LOGGING_LEVEL}.")
    LOGGING_LEVEL = DEFAULT_LOGGING_LEVEL
    logger.setLevel(LOGGING_LEVEL)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc):
    ct = request.headers.get('Content-Type', "No Content-Type sent")
    logger.info(f"Request Content-Type => {ct}")
    logger.warn(str(exc))
    return JSONResponse(str(exc), status_code=422)


@app.post("/test1")
async def post_sample_data_1(data: SampleData):
    return SampleResponse(
        is_error=False,
        msg="We got a good request",
        input=data
    )


@app.post('/dict')
async def post_any_dict(data: Dict[str, str], request: Request):
    response = {"data": data}
    headers: Dict[str, str] = dict()
    for h in request.headers:
        headers[h] = request.headers[h]
    response['request_headers'] = headers
    return response


@app.get("/")
async def read_root():
    return {"msg": "Ok"}
