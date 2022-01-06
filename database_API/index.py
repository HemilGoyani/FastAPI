from fastapi import FastAPI
from routs.index import user

app = FastAPI()
app.include_router(user)
