from blog.models.user import User
from flask_sqlalchemy import SQLAlchemy
from blog.models.tag import Tag

db = SQLAlchemy()
__all__ = [
    "db",
]

__all__ = [
    "User",
    "Tag"

]
