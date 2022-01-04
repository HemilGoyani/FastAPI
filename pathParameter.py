from typing import Optional


from fastapi import FastAPI, Path, Query


app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(...,title = "this is path parameter values"),
    q: Optional[str] = Query(None, alias="this is alias for method"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items2/{item_id}")
async def read_items1(

    *, item_id: int = Path(..., title="The ID of the item to get", gt = 0,le=100), q: Optional[str] = None

):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

