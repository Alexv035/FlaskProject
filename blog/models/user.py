from blog.security import flask_bcrypt
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from blog.models.database import db

from sqlalchemy.orm import relationship
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)
    email = Column(String(255), unique=True, nullable=False,
                   default="", server_default="")
    first_name = Column(String(120), unique=False,
                        nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False,
                       nullable=False, default="", server_default="")

    author = relationship("Author", uselist=False, back_populates="user")

    def __str__(self):
        return f'{self.user.email} ({self.user.id})'
