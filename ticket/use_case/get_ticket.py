from ticket.repo.ticket import TicketRepository


class GetTicket:
    """ " Use case class GetTicket"""

    @classmethod
    def get_ticket(cls, id_: int):
        """get ticket entity
        : param
            - id_: ticket id
        : return
            - status: 410 or 200
            - message: string message
        """

        ticket = TicketRepository.get_ticket_by_id(id_)
        if not ticket:
            raise Exception(f"The ticket identifier number: {id_} was not found!")
        if ticket.redeemed:
            return {"status": 410, "message": "GONE"}

        TicketRepository.update_ticket_by_id(id_)
        return {"status": 200, "message": "OK"}
