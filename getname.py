from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root(name,address):
    return(f'''hello {name}!! how are you? your address is {address}''')


