from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal, DivisionByZero, InvalidOperation

# Data Model


class MathQuestion(BaseModel):
    arg1: Decimal = Field(Decimal, example=3.5)
    arg2: Decimal = Field(Decimal, example=1.2)
    operation: str = Field(str, example="add")


# Can you see where this is going?
class MathResult(BaseModel):
    result: Optional[float]
    is_error: bool = False
    msg: Optional[str]
    question: MathQuestion


app = FastAPI()


# Load the Vue web ui from app.html
@app.get("/app")
def read_index():
    return FileResponse("./app.html")


# POST a simple math problem
@app.post("/math")
async def math(payload: MathQuestion) -> MathResult:
    response: MathResult = MathResult(question=payload)
    try:
        if payload.operation in ["add", "plus", "sum", "+"]:
            response.result = payload.arg1 + payload.arg2
        elif payload.operation in ["sub", "minus", "subtract", "difference", "-"]:
            response.result = payload.arg1 - payload.arg2
        elif payload.operation in ["multiply", "product", "mul", "*"]:
            response.result = payload.arg1 * payload.arg2
        elif payload.operation in ["exp", "exponent", "^", "**"]:
            response.result = payload.arg1 ** payload.arg2
        elif payload.operation in ["mod", "modulus", "%"]:
            response.result = payload.arg1 % payload.arg2
        elif payload.operation in ["divide", "div", "/"]:
            response.result = payload.arg1 / payload.arg2
        else:
            response.is_error = True
            response.msg = f"I don't know how to {payload.operation}!"
    except DivisionByZero:
        response.is_error = True
        response.msg = "Division by Zero"
    except InvalidOperation:
        response.is_error = True
        response.msg = "Invalid Operation"
    except Exception as e:
        response.is_error = True
        response.msg = str(e)
    return response


@app.get('/add/{arg1}/{arg2}')
async def add(arg1: float, arg2: float) -> MathResult:
    question: MathQuestion = MathQuestion(operation="add",
                                          arg1=arg1,
                                          arg2=arg2)
    return await math(question)


@app.get('/', response_class=RedirectResponse)
async def get_root(request: Request):
    for h in request.headers:
        print(f"{h} => {request.headers[h]}")
    if "Accept" in request.headers:
        if "text/html" in request.headers['Accept']:
            return "app"
