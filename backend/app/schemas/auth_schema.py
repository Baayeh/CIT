from pydantic import BaseModel, EmailStr, Field


class UserCreateSchema(BaseModel):
    firstname: str = Field(min_length=3)
    lastname: str = Field(min_length=3)
    username: str = Field(max_length=5)
    email: EmailStr
    password: str = Field(min_length=8)
