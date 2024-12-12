from datetime import datetime
from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: EmailStr = Field(unique=True, index=True)
    firstname: str
    lastname: str
    password_hash: str = Field(exclude=True)
    is_verified: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def __repr__(self):
        return f"<User {self.username}>"
