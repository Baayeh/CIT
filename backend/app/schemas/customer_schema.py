from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CustomerDetailsSchema(BaseModel):
    id: UUID
    name: str
    phone_number: str
    created_at: datetime
    updated_at: datetime


class CustomerCreateSchema(BaseModel):
    name: str
    phone_number: str


class CustomerUpdateSchema(CustomerCreateSchema):
    pass
