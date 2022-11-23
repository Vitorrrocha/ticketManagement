
def routes(app):
        @app.route('/')
        def index():
            return 'Index Page'

        @app.route('/reedem/<ticketIdentifier>')
        def hello():
            return 'Hello, World'

        @app.errorhandler(404)
        def error404(error):
            return ' 😣 404 Error \nWhat you were looking for is just not there.'