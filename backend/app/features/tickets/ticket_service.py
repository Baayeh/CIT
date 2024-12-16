from fastapi import HTTPException, status
from sqlmodel import Session, desc, select

from .ticket_model import Ticket
from .ticket_schema import TicketCreate, TicketUpdate


class TicketService:
    def get_all_tickets(self, session: Session):
        """Retrieve all tickets from database"""
        statement = select(Ticket).order_by(desc(Ticket.created_at))
        result = session.exec(statement)

        return result.all()

    def get_user_tickets(self, user_id: str, session: Session):
        """Retrieve all tickets created by current user"""
        statement = (
            select(Ticket)
            .where(Ticket.owner_id == user_id)
            .order_by(desc(Ticket.created_at))
        )
        result = session.exec(statement)

        return result.all()

    def get_ticket(self, ticket_id: str, session: Session):
        """Retrieve a single ticket from database"""
        statement = select(Ticket).where(Ticket.id == ticket_id)

        result = session.exec(statement)

        ticket = result.first()

        if not ticket:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ticket was not found",
            )

        return ticket

    def create_ticket(self, ticket_data: TicketCreate, user_id: str, session: Session):
        """Create a new ticket record in the database"""
        ticket_data_dict = ticket_data.model_dump()

        new_ticket = Ticket(**ticket_data_dict)
        new_ticket.creator_id = user_id

        session.add(new_ticket)
        session.commit()
        session.refresh(new_ticket)

        return new_ticket

    def update_ticket(
        self, ticket_id: str, update_data: TicketUpdate, session: Session
    ):
        """Update the details of a ticket"""
        ticket_to_update = self.get_ticket(ticket_id, session)

        update_data_dict = update_data.model_dump()

        for field, value in update_data_dict.items():
            setattr(ticket_to_update, field, value)

        session.commit()
        session.refresh(ticket_to_update)

        return ticket_to_update

    def delete_ticket(self, ticket_id: str, session: Session):
        """Delete a single ticket from database"""
        ticket_to_update = self.get_ticket(ticket_id, session)

        session.delete(ticket_to_update)
        session.commit()
