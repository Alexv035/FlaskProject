from blog.security import flask_bcrypt
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from blog.models import db
# from blog.models.user import User
from sqlalchemy.orm import relationship
from blog.app import app
from flask_login import UserMixin


db.init_app(app)

<<<<<<< HEAD
=======
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
>>>>>>> c1efac286ac479b4e9cdcc78b28f3c85ab541efc

class Users(db.Model):
    __tablename__ = 'users'

<<<<<<< HEAD
=======
class User(db.Model, UserMixin):
>>>>>>> c1efac286ac479b4e9cdcc78b28f3c85ab541efc
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

<<<<<<< HEAD
    def __init__(self, username, is_staff):
        self.username = username
        self.is_staff = is_staff

    # def __repr__(self):
    #     return f"<User #{self.id} {self.username!r}>"
=======
    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"

    _password = Column(LargeBinary, nullable=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)


@app.cli.command("create-admin")
def create_admin():
    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"
    db.session.add(admin)
    db.session.commit()
    print("created admin:", admin)
>>>>>>> c1efac286ac479b4e9cdcc78b28f3c85ab541efc
