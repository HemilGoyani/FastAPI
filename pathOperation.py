from typing import Optional, Set
from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime


class Items(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []


app = FastAPI()


@app.post("/items/", response_model=Items, status_code=status.HTTP_201_CREATED)
async def Get_name(item: Items):
    return item


class Item1(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []



@app.post("/items1/", response_model=Item1, tags=["items1"],response_description="post method is call")

async def create_item(item: Item1):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item



@app.get("/items2/", tags=["items2"])
async def read_items():
    return [{"name": "Foo", "price": 42}]



@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


# JSON Encoer example in api

class ItemJSON(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str] = None

fake_db = {}
app = FastAPI()
@app.put("/itemsJSON/",tags = ["Put API in data"])
def update_item(id: str, item: ItemJSON):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    return fake_db
    print(fake_db)

