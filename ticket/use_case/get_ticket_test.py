from ticket.use_case.get_ticket import GetTicket
from ticket.repo.ticket import TicketRepository
from mock import MagicMock
from unittest.mock import patch

def test_get_ticket_with_ticket_not_redeemed_return_200():
    with patch('ticket.repo.ticket.TicketRepository.get_ticket_by_id') as get_ticket_by_id,\
        patch('ticket.repo.ticket.TicketRepository.update_ticket_by_id') as update_ticket_by_id:

        id = 5
        get_ticket_by_id.return_value = MagicMock(redeemed = False)

        response = GetTicket.get_ticket(id)

        get_ticket_by_id.assert_called_once()
        update_ticket_by_id.assert_called_once()
        assert response == {'status': 200, 'message': 'OK'}