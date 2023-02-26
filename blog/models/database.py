# from .user import Users
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# from blog import app

login_manager = LoginManager()
db = SQLAlchemy()


__all__ = [
    "db",
]
