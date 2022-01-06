from pydantic import BaseModel

class user(BaseModel):
    id: int
    name: str
    address: str
    password: str
