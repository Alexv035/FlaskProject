from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


__all__ = [
    "db",
    "User",
    "Tag"
    "Author",
    "Article",
]
