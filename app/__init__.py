from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

cors = CORS()
app = Flask(__name__)

def create_app(debug=False):
    """
    Flask application factory
    Use this function to create new app and use current_app to access
    app related configuration if needed.
    :param debug: boolean
    """

    app.config['SWAGGER'] = {'title': 'Api Documentation', 'uiversion': 2}
    app.config.from_object('config')
    app.debug = debug

    # register blueprints
    from app.router.blur import mod as blur_route

    app.register_blueprint(blur_route)

    # register extensions
    cors.init_app(app)
    swagger = Swagger(app)


    return app

