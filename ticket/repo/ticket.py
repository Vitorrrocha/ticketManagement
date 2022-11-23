# pylint: disable=E1101

from collections import namedtuple
from ticket.config import DBConnectionHandler
from ticket.model.ticket import Tickets


class TicketRepository:
    """ Class to manage ticket Repository """

    @classmethod
    def get_ticket_by_id(cls, id: int):
        """ get ticket entity
        : param 
            - id: ticket id
        : return 
            - the data value from database
        """

        with DBConnectionHandler() as db_connection:
            ticket = db_connection.session.query(Tickets).get(id)
            return ticket
