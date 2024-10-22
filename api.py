from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calculator import Calculator

app = FastAPI()
calculator = Calculator()


class OperationData(BaseModel):
    a: float
    b: float


@app.post("/add")
async def add(data: OperationData):
    result = calculator.add(data.a, data.b)
    return {"result": result}


@app.post("/subtract")
async def subtract(data: OperationData):
    result = calculator.subtract(data.a, data.b)
    return {"result": result}
