from flask import Blueprint, render_template, request

bp = Blueprint("user", __name__)

@bp.route("/user/create", methods=["GET"])
def create():
    return render_template("user/create.html")


@bp.route("/user/", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        return render_template("user/index.html")

    else:
        return "<h1>User Created</h1>!"


@bp.route("/user/<int:id>", methods=["DELETE", "PUT", "GET"])
def user_id(id):
    if request.method == "DELETE":
        return "<h1>Deleting User</h1>"

    elif request.method == "PUT":
        return "<h1>Updating User</h1>"

    else:
        return render_template("user/show.html", id=id)

