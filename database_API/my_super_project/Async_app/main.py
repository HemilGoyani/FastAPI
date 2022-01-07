from typing import List, Optional
from fastapi import FastAPI
from fastapi.param_functions import Depends
from pydantic import BaseModel,EmailStr
from sqlalchemy import Column,String, Integer, Boolean
from sqlalchemy.orm.session import Session
from database import Base,engine,SessionLocal

#models
class User(Base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True, index=True)
    email=Column(String,unique=True,index=True)
    is_active=Column(Boolean,default=True)

#schemas
class UserSchemas(BaseModel):
    id: int
    email: EmailStr  
    is_active:bool
    
    class Config:
         orm_mode = True 
         
def get_db():
     db = SessionLocal()
     try:
         yield db
     finally:
         db.close()
        
                 
Base.metadata.create_all(bind = engine)
app = FastAPI()

@app.post("/users",response_model=UserSchemas)
async def index(user:UserSchemas,db:Session=Depends(get_db)):
    u = User(id=user.id,email=user.email,is_active=user.is_active)
    db.add(u)
    db.commit()
    return u

@app.get("/users/",response_model= List[UserSchemas])
async def index(db:Session=Depends(get_db)):
    return db.query(User).all()