from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Column, Field, Relationship, SQLModel

from app.models import auth_model


class Ticket(SQLModel, table=True):
    __tablename__ = "tickets"

    id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            index=True,
            unique=True,
            default=uuid4,
        )
    )
    title: str
    user_id: Optional[UUID] = Field(default=None, foreign_key="users.id")
    description: Optional[str] = Field(
        sa_column=Column(pg.TEXT, nullable=True, default=None)
    )
    status: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False, server_default="open")
    )
    priority: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False, server_default="medium")
    )
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.now)
    )
    updated_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.now)
    )
    user: Optional["auth_model.User"] = Relationship(back_populates="tickets")
