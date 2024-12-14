from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TicketDetailSchema(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    created_at: datetime
    updated_at: datetime


class TicketCreateSchema(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "open"
    priority: str = "medium"


class TicketUpdateSchema(TicketCreateSchema):
    pass
