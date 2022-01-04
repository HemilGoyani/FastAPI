from typing import Optional
from fastapi import FastAPI,Body
from pydantic import BaseModel,Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


class Data(BaseModel):
    name: str
    address: str
    pin: int
    

@app.put("/data/dataValues")
def update_data(data_id,data: Optional[Data] = Body(...,example={"name":"toshal infotech","address":"surat bhatar","pin":123456})):
    result = {"data_id":data_id,"data":data}
    if data:
        result.update({"data":data})
    return result 



#Multiple example in  body to set
class MultiItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/MultiItem/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: MultiItem = Body(
        ...,

        examples={

            "normal": {

                "value": {

                    "name": "Foo",

                    "description": "A very nice Item",

                    "price": 35.4,

                    "tax": 3.2,

                },

            },

            "converted": {

                "value": {

                    "name": "Bar",

                    "price": "35.4",

                },

            },

            "invalid": {
                "value": {

                    "name": "Baz",

                    "price": "thirty five point four",

                },

            },

        },

    ),
):
    results = {"item_id": item_id, "item": item}
    return results
   