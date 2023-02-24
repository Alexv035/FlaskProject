# from blog.models.user import Users
from blog.models.database import db
from blog import commands

from blog.views.articles import articles_app
from blog.views.users import users_app
from flask import render_template
# from markupsafe import escape

from flask import Flask
import click

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.cli.add_command(commands.init_db)
app.cli.add_command(commands.create_init_user)

# def create_app() -> Flask:
#     app = Flask(__name__)
#     app.config.from_object('blog.config')

#     register_extensions(app)
#     register_blueprints(app)
#     register_commands(app)
#     return app


# def register_extensions(app):
#     db.init_app(app)

#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)

#     @login_manager.user_loader
#     def load_user(user_id):
#         return Users.query.get(int(user_id))


# def register_blueprints(app: Flask):
#     from blog.views.auth import auth_app
#     from blog.views.users import users_app

#     app.register_blueprint(users_app)
#     app.register_blueprint(auth_app)


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
