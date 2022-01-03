from fastapi import FastAPI
from typing import Optional

app = FastAPI()
@app.get("/operation/sumetion")
async def sum(num1: int,num2: int):
    return {"Sumetion":num1+num2}

@app.get("/operation/subtraction")
async def sub(n1: int,n2: int):
    return {"Sub":n1-n2}

@app.get("/operation/multiplication")
async def mul(n1: int,n2: int):
    return {"Mul":n1*n2}

@app.get("/operation/division")
async def div(n1: int,n2: Optional[int] = 2):
    return {"Div":n1 / n2}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}