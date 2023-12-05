from flask import Blueprint, render_template, request

bp = Blueprint("user", __name__)


@bp.route("/user/", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        return "<h1>Getting Users</h1>"

    else:
        return "<h1>Creating Users</h1>"


@bp.route("/user/", methods=["DELETE", "PUT"])
def user_id():
    if request.method == "DELETE":
        return "<h1>Deleting User</h1>"

    else:
        return "<h1>Updating User</h1>"
