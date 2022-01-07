from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
from sqlalchemy import Column,String, Integer, Boolean
from database import Base,engine


class User(Base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True, index=True)
    email=Column(String,unique=True,index=True)
    is_active=Column(Boolean,default=True)

class UserSchemas(BaseModel):
    id: int
    email: EmailStr  
    is_active:bool
     
Base.metadata.create_all(bind = engine)
app = FastAPI()

@app.post("/users")
async def index(user:UserSchemas):
    
    