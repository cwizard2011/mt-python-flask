from flask import Flask
import os

from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_json import FlaskJSON
from flask_jwt_extended import JWTManager
from flask_jsontools import DynamicJSONEncoder

from flask_mail import Mail
from schema import schema
from config import config
from helpers.database import db_session

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.json_encoder = DynamicJSONEncoder
    CORS(app)
    FlaskJSON(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
    JWTManager(app)
    mail.init_app(app)

    app.add_url_rule(
        '/mt',
        view_func=GraphQLView.as_view(
            'mt',
            schema=schema,
            graphiql=True
        )
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
