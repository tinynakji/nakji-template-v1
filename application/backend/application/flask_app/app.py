import logging
import os
import sys

from flask import Flask, _app_ctx_stack
from flask_cors import CORS
import greenlet
from sqlalchemy.orm import scoped_session

# from flask_cors import CORS
from flask_app.config import ConfigBase, ProdConfig

from flask_app.api.users.endpoints import user_route
from flask_app.db.database import get_db_loaded_session

def create_app(config_class: ConfigBase=ProdConfig):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Set GUnicorn loggers
    gunicorn_logger = logging.getLogger('gunicorn.error')
    if gunicorn_logger:
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

    CORS(
        app,
        resources={r"/api/*": {"origins": "*"}},
    )

    # # DB SESSION
    db_session = get_db_loaded_session(db_uri=config_class.DATABASE_URI)
    app.session = scoped_session(db_session, scopefunc=greenlet.getcurrent)

    # @app.before_request
    # def before_request():
    #     if not app.engine:
    #         app.engine = create_engine("mysql+pymysql://root:password@localhost:3306/mytestdb")
    #         app.session = scoped_session(sessionmaker(bind=app.engine))

    # Add endpoints
    app.register_blueprint(user_route)

    # Add teardown
    @app.teardown_appcontext
    def remove_session(*args, **kwargs):
        app.session.remove()

    return app