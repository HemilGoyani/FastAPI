from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class items(BaseModel):
    id : int
    name: str
    address: str
    price: int
    tax: float
@app.put("/items/item_id")    
async def put_data(item_id: int, item:items,q: Optional[str] = None):
    result = {"item_id":item_id, **item.dict()}
    if q:
        result.update({"q":q})
    return result