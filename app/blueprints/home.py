from flask import Blueprint

bp = Blueprint("home", __name__)


@bp.route("/")
def hello():
    return "<h1>Hello!<h1>"
