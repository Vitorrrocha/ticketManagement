from unittest.mock import patch
from mock import MagicMock
import pytest
from ticket.use_case.get_ticket import GetTicket


def test_get_ticket_with_ticket_not_redeemed_return_200():
    """Should get ticket by id if not redeemed return 200"""

    with patch(
        "ticket.repo.ticket.TicketRepository.get_ticket_by_id"
    ) as get_ticket_by_id, patch(
        "ticket.repo.ticket.TicketRepository.update_ticket_by_id"
    ) as update_ticket_by_id:

        id_ = 1
        get_ticket_by_id.return_value = MagicMock(redeemed=False)

        response = GetTicket.get_ticket(id_)

        get_ticket_by_id.assert_called_once_with(1)
        update_ticket_by_id.assert_called_once_with(1)
        assert response == {"status": 200, "message": "OK"}


def test_get_ticket_with_ticket_redeemed_return_410():
    """Should get ticket by id if redeemed return 410"""

    with patch(
        "ticket.repo.ticket.TicketRepository.get_ticket_by_id"
    ) as get_ticket_by_id, patch(
        "ticket.repo.ticket.TicketRepository.update_ticket_by_id"
    ) as update_ticket_by_id:

        id_ = 2
        get_ticket_by_id.return_value = MagicMock(redeemed=True)

        response = GetTicket.get_ticket(id_)

        get_ticket_by_id.assert_called_once_with(2)
        update_ticket_by_id.assert_not_called()
        assert response == {"status": 410, "message": "GONE"}


def test_get_ticket_with_ticket_not_found_raise_exception():
    """Should get ticket by id if not in the database raise exception"""

    with patch(
        "ticket.repo.ticket.TicketRepository.get_ticket_by_id"
    ) as get_ticket_by_id:

        id_ = 3
        get_ticket_by_id.return_value = None
        with pytest.raises(
            Exception, match="The ticket identifier number: 3 was not found!"
        ):

            GetTicket.get_ticket(id_)
