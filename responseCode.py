from typing import Optional,List
from fastapi import FastAPI,status
from pydantic import BaseModel

app = FastAPI()
@app.get("/items/item_name",status_code=status.HTTP_201_CREATED)
async def get_data(item_name: str):
    return {"item_name":item_name}