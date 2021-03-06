from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    #initialization of the application
    app=Flask(__name__)
    bootstrap.init_app(app)
    #creating app configurations
    app.config.from_object(config_options[config_name])
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .requests import configure_request
    configure_request(app)

    return app
