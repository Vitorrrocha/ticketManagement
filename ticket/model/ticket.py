from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.orm import relationship
from config import Base


class Ticket(Base):
    """ Tickets Entity """

    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    redeemed = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"Ticket [name={self.name}]"