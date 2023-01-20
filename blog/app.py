from flask_migrate import Migrate
import os
from blog.models.database import db

from blog.views.articles import articles_app
from blog.views.users import users_app
from flask import render_template

from flask import Flask

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

cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")

migrate = Migrate(app, db)
