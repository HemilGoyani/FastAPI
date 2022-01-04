from typing import Optional,List,Set
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl

# # body fields example
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = Field(
#         None, title="The description of the item", max_length=300
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: Optional[float] = None
    
# app = FastAPI()

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id,"item":item}
#     return results



app = FastAPI()
class Item12(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None


@app.put("/items1/{item_id}")
async def update_item(item_id: int, item: Item12 = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


# nested model in body parameter

class Image(BaseModel):
    url: HttpUrl
    name: str


class ItemNested(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    image: Optional[List[Image]] = None
    tags: Set[str] = set() #List[str] = []



@app.put("/ItemNested/{item_id}")
async def update_item(item_id: int, item: ItemNested):
    results = {"item_id": item_id, "item": item}
    return results

# deply nested models

class Image1(BaseModel):
    url: HttpUrl
    name: str


class Item11(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image1]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item11]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.post("/images/")
class img():
    url: HttpUrl
    name: str
    
async def create_images(image: img):
    return image