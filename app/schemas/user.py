from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    username: str
    password: str
    name: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserLoginResult(BaseModel):
    Status: bool
    token: str

class UserCreate(UserBase):
    username: str
    password: str
    name: str

class User(UserBase):
    id: int
    username: str
    password: str
    name: str

    model_config = ConfigDict(from_attributes=True)