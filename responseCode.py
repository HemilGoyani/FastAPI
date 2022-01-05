from typing import Optional,List
from fastapi import FastAPI,status,File
from pydantic import BaseModel

app = FastAPI()
@app.post("/items/item_name",status_code=status.HTTP_201_CREATED)
async def get_data(item_name: List[str] = File(...)):
    return {"item_name":item_name for i in item_name}