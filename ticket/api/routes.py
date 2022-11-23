from ticket.use_case.get_ticket import GetTicket


def routes(app):
    @app.route("/")
    def index():
        return "Index Page"

    @app.route("/reedem/<int:ticketIdentifier>", methods=["GET"])
    def get_ticket(ticketIdentifier):
        response = GetTicket.get_ticket(ticketIdentifier)
        return "{} {}".format(response["status"], response["message"])

    @app.errorhandler(404)
    def error404(error):
        return " 😣 404 Error \nWhat you were looking for is just not there."
