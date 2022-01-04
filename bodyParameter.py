from typing import Optional
from fastapi import FastAPI, Path,Body
from pydantic import BaseModel,Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    pin: int

class user(BaseModel):
    id: int
    name: str
    address: str

@app.put("/items/{item_id}")
async def update_item(
    *,

    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),

    q: Optional[str] = None,

    item: Optional[Item] = None,

):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

@app.put("/items2/{item_id}")
async def update_item(item_id: int, item: Optional[Item] = None, user: Optional[user] = None, iportance: int =  Body(...)):
    results = {"item_id": item_id,"item":item, "user": user,"importance":iportance}
    return results


