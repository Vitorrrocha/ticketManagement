from sqlalchemy import Column, String, Integer, Date
from config import Base


class Event(Base):
    """ Events Entity """

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    date = Date(String, nullable=False)

    def __repr__(self):
        return f"Event [name={self.name}]"