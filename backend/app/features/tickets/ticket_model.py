from datetime import datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Column, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from ..auth.auth_model import User
    from ..customers.customer_model import Customer


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

    owner_id: UUID = Field(foreign_key="users.id", ondelete="RESTRICT")
    customer_id: UUID = Field(foreign_key="customers.id", ondelete="RESTRICT")

    creator: "User" = Relationship(back_populates="created_tickets")
    # assignee: "User" = Relationship(back_populates="assigned_tickets")

    customer: "Customer" = Relationship(back_populates="tickets")


# event listener to assign ticket to current user if not set
# @event.listens_for(Ticket, "before_insert")
# def set_default_assign_to(mapper, connection, target):
#     if target.assign_to is None:
#         target.assign_to = target.owner_id
