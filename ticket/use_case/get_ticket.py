from ticket.repo.ticket import TicketRepository

class GetTicket:

    @classmethod
    def get_ticket(cls, id: int):
        """ get ticket entity
        : param 
            - id: ticket id
        : return 
            - status: 410 or 200
            - message: string message
        """

        ticket = TicketRepository.get_ticket_by_id(id)
        if not ticket:
            raise Exception("The ticket identifier number: {} was not found!".format(id))
        if ticket.redeemed:
            return {'status': 410, 'message': 'GONE'}
            
        TicketRepository.update_ticket_by_id(id)
        return {'status': 200, 'message': 'OK'}