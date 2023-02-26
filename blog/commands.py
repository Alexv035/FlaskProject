import click
from werkzeug.security import generate_password_hash

from blog.models.database import db
# from blog.app import app


@click.command("init-db")
def init_db():
    from wsgi import app

    # import models for creating tables
    from blog.models.user import Users

    db.create_all(app=app)
    print("done!")


@click.command("create-users")
def create_users():

    from blog.models.user import Users
    from wsgi import app

    admin = Users(username="admin", is_staff=True)
    james = Users(username="james", is_staff=True)

    with app.app_context():
        # db.session.add(admin)
        db.session.add(james)
        db.session.commit()
    print("done! created users:", admin, james)
