from fastapi import FastAPI,HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()
names = {"tagline" : "hello tagline!! how are you?"}


@app.get("/items/{item_name}")
async def check_data(item_name: str):
    if item_name not in names:
        raise HTTPException(status_code=404, detail="name not found to the list")
    return {"item_name":item_name}

login_creadential = {"tagline":"login is allowed to the tagline",
                     "hello":"login allowed to the hello"
                     }

@app.get("/users/{user_login_name}")
async def check_user_login(login_name: str):
    if login_name in login_creadential:
        return {"login_name": login_creadential[login_name]}
        
    elif login_name == "hemil":
       raise HTTPException(status_code=400, detail=f"{login_name}  is not supported") 
    else:
        raise HTTPException(status_code=404,
             detail=f"{login_name}  not permission to the login",
              headers={"X-Error": "There goes my error"})       
    

