from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from ..tickets.ticket_schema import TicketDetailSchema


class UserDetailSchema(BaseModel):
    id: UUID
    firstname: str
    lastname: str
    username: str
    role: str
    email: EmailStr
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    tickets: List[TicketDetailSchema]


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
