from typing import Text
from fastapi import FastAPI, Form, UploadFile, File


app = FastAPI()
@app.post("/login/",status_code=201)
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

# file upload control used in python
@app.post("/files/")
async def create_file(file: bytes = File(...)):

    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename":file.filename}
