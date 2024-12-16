from typing import Optional
from uuid import UUID

from sqlmodel import SQLModel

from app.common.shared_schemas import (
    CustomerTicketPublic,
    TicketPublic,
    UserTicketPublic,
)


class TicketBase(SQLModel):
    title: str
    description: Optional[str] = None
    status: str = "open"
    priority: str = "medium"


class TicketCreate(TicketBase):
    owner_id: UUID
    customer_id: UUID


class TicketUpdate(TicketBase):
    pass


class TicketPublicWithOwnerAndCustomer(TicketPublic):
    creator: UserTicketPublic
    customer: CustomerTicketPublic
    owner: UserTicketPublic
