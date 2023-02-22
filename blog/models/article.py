from blog.models import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, Text
import datetime
from article_tag import article_tag_association_table
from sqlalchemy.sql import func


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"))
    author = db.relationship("Author", back_populates="articles")
    articles = db.relationship("Article", back_populates="author")
    title = Column(String(200), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    dt_created = Column(DateTime, default=datetime.utcnow,
                        server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    tags = db.relationship("Tag",
                           secondary=article_tag_association_table,
                           back_populates="articles",
                           )

    def __str__(self):
        return self.title
