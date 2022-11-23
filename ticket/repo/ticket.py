# pylint: disable=E1101

from ticket.config import DBConnectionHandler
from ticket.model.ticket import Tickets
from sqlalchemy import text


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
            db_connection.session.close()
            return ticket

    @classmethod   
    def update_ticket_by_id(cls, ticket_id: int):
        """ update data in ticket entity
        : param - ticket_id: ticket id
        : return - None
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = text(
                    '''UPDATE Tickets
                    SET redeemed = True
                    WHERE Tickets.id = %s;''' % ticket_id
                    )
                db_connection.session.execute(query)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
               db_connection.session.close()
