import click
from werkzeug.security import generate_password_hash

from blog.models.database import db
from .app import app


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models.user import Users
    admin = Users(username="admin", is_staff=True)
    james = Users(username="james")
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)

# @click.command('init-db')
# def init_db():
#     from wsgi import app

#     # import models for creating tables
#     from blog.models import User

#     db.create_all(app=app)


# @click.command('create-init-user')
# def create_init_user():
#     from blog.models.user import Users
#     from wsgi import app

#     with app.app_context():
#         db.session.add(
#             Users(email='name@example.com',
#                  password=generate_password_hash('test123'))
#         )
#         db.session.commit()
