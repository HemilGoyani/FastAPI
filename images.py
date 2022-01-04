from typing import List,Optional, Dict
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/")

async def create_multiple_images(images: List[Image]):
    return images

@app.post("/index-weights/")
async def create_index_weights(weights: Dict[str, float]):
    return weights