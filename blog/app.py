from blog.models.database import db
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello web!"


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
