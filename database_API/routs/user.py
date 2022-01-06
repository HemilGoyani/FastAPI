from fastapi import APIRouter
from sqlalchemy.sql.functions import user
from config.db import conn
from schemas.index import User
from models.index import users
app = APIRouter()

@app.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@app.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where (users.c.id == id)).fetchall()

@app.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name = user.name,
        address = user.address,
        password = user.password
    ))
    return conn.execute(users.select()).fetchall()

@app.put("/{id}")
async def update_data(id:int,user:User):
    conn.execute(users.update(
        name = user.name,
        address = user.address,
        password = user.password
    )).where (users.c.id == id)
    return conn.execute(users.select().where (users.c.id == id)).fetchall()

@app.delete("/{id}")
async def delet_data(id: int):
    conn.execute(users.delete().where (users.c.id == id))
    return conn.execute(users.select().where (users.c.id == id)).fetchall()
