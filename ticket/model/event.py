from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from ticket.config import Base


class Events(Base):
    """ Events Entity """

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    date = Column(Date, nullable=False)
    id_ticket = relationship("Tickets")

    def __repr__(self):
        return f"Event [name={self.name}]"