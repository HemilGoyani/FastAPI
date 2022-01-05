from typing import Optional, Set
from fastapi import FastAPI, status,HTTPException
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
@app.post("/items/create_data", response_model=Items, status_code=status.HTTP_201_CREATED)
async def Get_name(item: Items):
    return item


class Item1(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []



@app.post("/items1/", response_model=Item1, tags=["Create data"],response_description="post method is call")
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


@app.get("/items2/", tags=["Read Data"])
async def read_items():
    return [{"name": "Foo", "price": 42}]

@app.get("/users/", tags=["User Data read"])
async def read_users():
    return [{"username": "johndoe"}]


class ItemJSON(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str] = None

user_db = {
    "tagline": {"name": "tagline infotech", "description":"software comapny"},
    "Toshal": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "infotech": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}
@app.get("/userData/")
async def read_data(user_name: str):
    if user_name not in user_db:
        raise HTTPException(status_code=404, detail="data not found")
    return user_db[user_name]
    
@app.put("/itemsJSON/")
def update_item(name: str, item: ItemJSON):
    json_compatible_item_data = jsonable_encoder(item)
    if name in user_db:
        user_db[name] = json_compatible_item_data
        return user_db   
    raise HTTPException(status_code=404, detail="name not found")

@app.patch("/items/{item_name}", response_model=ItemJSON)
async def update_item(item_id: str, item: ItemJSON):
    
    user_db[item_id] = jsonable_encoder(item)
    return user_db[item_id]

