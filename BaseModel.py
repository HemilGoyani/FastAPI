from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class Item(BaseModel):
#     Name: str
#     Address: str
#     Pin: int
#     Mobile: int
#     Father_Name: Optional[str] = None

# @app.post("/items/")
# async def post_data(item:Item):
#     return item

class Item1(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item1: Item1):
    item_dict = item1.dict()
    if item1.tax:
        price_with_tax = item1.price + item1.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict