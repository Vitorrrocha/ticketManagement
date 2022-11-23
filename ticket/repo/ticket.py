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
            - boolean value
        """

        with DBConnectionHandler() as db_connection:
            ticket = db_connection.session.query(Tickets).get(id)
            if not ticket:
                raise Exception("The ticket identifier was not found!".format(id))
            if ticket.redeemed:

                return {'status': 410, 'message': 'GONE'}

            return {'status': 200, 'message': 'OK'}

