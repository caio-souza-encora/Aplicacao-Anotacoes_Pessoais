from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserLogin(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True