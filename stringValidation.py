from typing import Optional, List
from fastapi import FastAPI,Query
from pydantic import BaseModel


app = FastAPI()

# @app.get("/items/{item_id}")
# async def get_id(q: Optional[str] = None):
#     result = {"items":[{"item_id":"101"},{"item_id":"102"}]}
#     if q:
#         result.update({"q":q})
#     return result   

# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):

#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items

@app.get("/items1/")
async def read_items1(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        deprecated=False
    )
):
    results12 = {"items1": [{"item1_id": "Foo"}, {"item2_id": "Bar"}]}
    if q:
        results12.update({"q": q})
    return results12

@app.get("/items2/")
async def read_items2(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items
@app.get("/item3/")
async def read_item3(q:List = Query([])):
    query_items = {"q":q}
    return query_items