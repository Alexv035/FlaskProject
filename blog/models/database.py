# from blog.models import User
from flask_sqlalchemy import SQLAlchemy
from blog.models.tag import Tag

from blog.models.author import Author
from blog.models.article import Article

db = SQLAlchemy()


__all__ = [
    "db",
]

__all__ = [
    "User",
    "Tag"
    "Author",
    "Article",
]
