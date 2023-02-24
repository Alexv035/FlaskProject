
from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.models.user import Users
from flask_login import login_required


users_app = Blueprint("users_app", __name__)


# user = Blueprint('user', __name__, url_prefix='/users',
#                  static_folder='../static')

users_table = {
    1: "James",
    2: "Brian",
    3: "Peter",
}


@users_app.route("/", endpoint="list")
def users_list():
    users = Users.query.all()
    return render_template("users/list.html", users=users)


@users_app.route("/<int:user_id>/", endpoint="details")
def user_details(user_id: int):
    user = Users.query.filter_by(id=user_id).one_or_none()
    # if user is None:
    #     raise NotFound(f"User #{user_id} doesn't exist!")
    #     return render_template("users/details.html", user=user)

    try:
        user_name = users_table[user_id]
    except KeyError:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template('users/details.html', user_id=user_id,
                           user_name=user_name)


# @user.route('/<int:pk>')
# @login_required
# def profile(pk: int):
#     selected_user = User.query.filter_by(id=pk).one_or_none()
#     if not selected_user:
#         raise NotFound(f"User #{pk} doesn't exist!")

#     return render_template(
#         'users/profile.html',
#         user=selected_user,
#     )
