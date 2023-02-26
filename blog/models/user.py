from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db


class Users(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    def __init__(self, username, is_staff):
        self.username = username
        self.is_staff = is_staff

    # def __repr__(self):
    #     return f"<User #{self.id} {self.username!r}>"
