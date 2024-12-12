from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserDetailSchema(BaseModel):
    id: UUID
    firstname: str = Field(min_length=3)
    lastname: str = Field(min_length=3)
    username: str = Field(max_length=5)
    email: EmailStr
    is_verified: bool
    created_at: datetime
    updated_at: datetime


class UserCreateSchema(BaseModel):
    firstname: str = Field(min_length=3)
    lastname: str = Field(min_length=3)
    username: str = Field(max_length=5)
    email: EmailStr
    password: str = Field(min_length=8)
