from fastapi import FastAPI
from typing import Optional

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"},
    {"name":"tagline infotech"},
    {"name":"hello "}
    ]
@app.get("/items/") 
async def read_item(skip: int =0, limit: int = len(fake_items_db) ):
    print(skip,":skip")
    return fake_items_db[skip : skip + limit]





@app.get("/items/{item_id}")

async def read_item(item_id: str, q: Optional[str] = None):

    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/items/me")
async def item_id_get():
    return{"item_id":"own id compared to this function"}

