from ticket.use_case.get_ticket import GetTicket


def routes(app):
    """Routes"""

    @app.route("/")
    def index():
        return "Index Page"

    @app.route("/reedem/<int:ticket_identifier>", methods=["GET"])
    def get_ticket(ticket_identifier):
        response = GetTicket.get_ticket(ticket_identifier)
        return f"{response['status']} {response['message']}"

    @app.errorhandler(404)
    def error404(error):
        return " 😣 404 Error \nWhat you were looking for is just not there."
