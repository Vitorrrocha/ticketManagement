from sqlalchemy import Column, Integer, Boolean, ForeignKey
from ticket.config import Base


class Tickets(Base):
    """Tickets Entity"""

    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    redeemed = Column(Boolean, nullable=False)
    events_id = Column(Integer, ForeignKey("events.id"), nullable=False)

    def __repr__(self):
        return f"Ticket [event_id={self.events_id}]"
