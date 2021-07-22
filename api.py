from fastapi import FastAPI
from fastapi.responses import FileResponse
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
    operation: str
    arg1: float
    arg2: float
    is_error: bool = False
    msg: Optional[str]


app = FastAPI()


# Load the Vue web ui from app.html
@app.get("/app")
def read_index():
    return FileResponse("./app.html")


# POST a simple math problem
@app.post("/math")
async def math(payload: MathQuestion) -> MathResult:
    response = {"arg1": payload.arg1,
                "arg2": payload.arg2,
                "operation": payload.operation,
                }
    try:
        if payload.operation in ["add", "plus", "sum"]:
            response["result"] = payload.arg1 + payload.arg2
        elif payload.operation in ["sub", "minus", "subtract", "difference"]:
            response["result"] = payload.arg1 - payload.arg2
        elif payload.operation in ["multiply", "product", "mult"]:
            response['result'] = payload.arg1 * payload.arg2
        elif payload.operation in ["exp", "exponent"]:
            response['result'] = payload.arg1 ** payload.arg2
        elif payload.operation in ["mod", "modulus"]:
            response['result'] = payload.arg1 % payload.arg2
        elif payload.operation in ["divide", "div"]:
            response['result'] = payload.arg1 / payload.arg2
        else:
            response.update({"is_error": True,
                             "msg": f"I don't know how to {payload.operation}!"})
    except (DivisionByZero, InvalidOperation) as e:
        response.update({"is_error": True,
                         "msg": f"{e}"})
    return MathResult(**response)


@app.get('/add/{arg1}/{arg2}')
async def add(arg1: float, arg2: float) -> MathResult:
    return MathResult(result=arg1 + arg2, is_error=False)