from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class UserBase(BaseModel):
    username: str

class UserCreateInput(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(UserBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True