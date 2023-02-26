from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from blog.models.database import db


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('Users', back_populates='author')
    articles = relationship('Article', back_populates='author')

    def __str__(self):
        return self.user.email
