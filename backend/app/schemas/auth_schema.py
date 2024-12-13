from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserDetailSchema(BaseModel):
    id: UUID
    firstname: str
    lastname: str
    username: str
    email: EmailStr
    is_verified: bool
    created_at: datetime
    updated_at: datetime


class UserCreateSchema(BaseModel):
    firstname: str = Field(min_length=3, max_length=25)
    lastname: str = Field(min_length=3, max_length=25)
    username: str = Field(min_length=5, max_length=25)
    email: EmailStr
    password: str = Field(min_length=8)

    model_config = {"extra": "forbid"} 


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

    model_config = {"extra": "forbid"}
