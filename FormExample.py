from typing import Text,List
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import HTMLResponse


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




# Multiple file upload  in API
@app.post("/files/")

async def create_files(files: List[bytes] = File(...)):

    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")

async def create_upload_files(files: List[UploadFile] = File(...)):

    return {"filenames": [file.filename for file in files]}


@app.post("/filesFormFiles/")
async def create_file(
    file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
