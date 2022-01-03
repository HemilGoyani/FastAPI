from enum import Enum
from fastapi import FastAPI
app = FastAPI()

class ModelName(Enum):

    alexnet = "alexnet"

    resnet = "resnet"

    lenet = "lenet"
    
    tagline = "tagline"
    
    # def sum(a = 10,b = 10):
    #     return "sum is:",(a + b)

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name.value == "tagline":
        return {"model_name":model_name,"message":"your selection is good"}
    if model_name == ModelName.resnet:
        return {"model_name": model_name, "Mesage":"your selection is resnet"}
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "Mesage":"your selection is alexnet"}
    
    return {"model_name": model_name, "Mesage":"your selection is lenet"}

# @app.get("/Operations/{sum_operation}")
# async def get_operationl(sum_operation: ModelName.sum()):
#         return {"sum_operation":sum_operation}