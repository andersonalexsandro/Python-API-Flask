from flask import Blueprint, render_template, request, redirect, url_for
from app.models.user import User as User_Model
from app.extentions import db


bp = Blueprint("user", __name__)


@bp.route("/user/form", methods=["GET"])
def form():
    return render_template("user/form.html")


@bp.route("/user/", methods=["POST"])
def save():
    new_user = User_Model(name=request.form["name"], email=request.form["email"])
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("user.index"))


@bp.route("/user/", methods=["GET"])
def index():
    all_users = User_Model.query.all()
    return render_template("user/index.html", users=all_users)


@bp.route("/user/<int:id>", methods=["GET"])
def user_id(id):
    return render_template("user/user-id.html", user_id=id)

@bp.route("/user/<int:id>", methods=["DELETE"])
def delete(id):
    user = User_Model.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("user.index"))

