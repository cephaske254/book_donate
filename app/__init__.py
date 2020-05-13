from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from config import Config,config_loader
from flask_sqlalchemy import SQLAlchemy

db  = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'


def create_app(config_type):
    app = Flask(__name__)

    # configs
    app.config.from_object(Config)
    app.config.from_object(config_loader[config_type])

    # extensions
    
    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    # all blueprints below
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app





