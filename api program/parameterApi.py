from typing import Text
from fastapi import FastAPI

app = FastAPI()



@app.get("/items/{id},{name},{address   }")
async def read_item(id: int, name: Text, address: Text):
    #if type(id) == int and type(name) == str and type(address) == str:
        
        return {"identity":id, "name": name, "address": address}
