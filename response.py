from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []



@app.post("/items/", response_model = Item)
async def create_item(item: Item):
    return item


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr # only to the email restricted
    full_name: Optional[str] = None
    
class UserOut(BaseModel):
    username: str
    email: EmailStr # only to the email restricted
    full_name: Optional[str] = None    


# Don't do this in production!
@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user



class Item5(BaseModel):
    name: str

    description: Optional[str] = None

    price: float

    tax: float = 10.5

    tags: List[str] = []



items = {
    "tagline": {"name": "Foo", "price": 50.2},
    "infotech": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "hello": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items5/{item_id}", response_model=Item5, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
