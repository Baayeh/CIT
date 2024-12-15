from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import SQLModel

from app.common.shared_schemas import CustomerPublic, TicketPublic, UserPublic


class TicketBase(SQLModel):
    title: str
    description: Optional[str] = None
    status: str = "open"
    priority: str = "medium"


class TicketCreate(TicketBase):
    pass


class TicketUpdate(TicketBase):
    pass


class TicketPublicWithOwnerAndCustomer(TicketPublic):
    creator: UserPublic
    customer: CustomerPublic
