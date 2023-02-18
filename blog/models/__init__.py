from blog.models.user import User
from flask_sqlalchemy import SQLAlchemy
from blog.models.author import Author
from blog.models.article import Article

db = SQLAlchemy()
__all__ = [
    "db",
]

__all__ = [
    "User",
    "Author",
    "Article",
]
