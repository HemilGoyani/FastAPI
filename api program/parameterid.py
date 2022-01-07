from fastapi import FastAPI
import fastapi

app = FastAPI()
@app.get("/items/me")
async def item_id_get():
    return{"item_id":"own id compared to this function"}

@app.get("/items/{item_id}")
async def item_id_get(item_id):
    return{"item_id":item_id}

# @app.get("/items/{item_id}")
# async def item_id_get(item_id):
#     if type(item_id) == int:
#         return{"item_id":item_id}
#     else:
#         return {"not string is accepted"}