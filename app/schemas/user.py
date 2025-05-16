from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    username: str
    password: str
    name: str

    class Config:
        orm_mode = True
    