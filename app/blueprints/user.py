from flask import Blueprint, render_template, request

bp = Blueprint("user", __name__)


@bp.route("/user/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        return request.form

    return render_template("user/create.html")


@bp.route("/user/<int:id>", methods=["GET"])
def user_id(id):
        return render_template("user/show.html", user_id=id)

