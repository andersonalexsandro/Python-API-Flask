from flask import Blueprint, render_template, request, redirect, url_for
from app.models.user import User as User_Model
from app.models.user_deleted import User_deleted
from app.extentions import db
from datetime import datetime

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
    user = User_Model.query.get(id)
    return render_template("user/user-id.html", user=user)


@bp.route("/user/<string:name>", methods=["GET"])
def user_name(name):
    user = db.one_or_404(db.select(User_Model).filter_by(name=name))
    return render_template("user/user-id.html", user=user)


@bp.route("/user/<int:id>", methods=["DELETE"])
def delete(id):
    user = User_Model.query.get(id)
    db.session.delete(user)
    db.session.commit()
    user_deleted = User_deleted(name=user.name, email=user.email, date_time=datetime.now())
    db.session.add(user_deleted)
    db.session.commit()
    return redirect(url_for("user.index"))

