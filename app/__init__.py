from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from app.blueprints import home, user

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

## create the app
app = Flask(__name__)

## initializing database
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

## Adding Routes##
app.register_blueprint(home.bp)
app.register_blueprint(user.bp)

##run
app.run(port=5000, host="localhost", debug=True)


class User(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String, nullable=False)
  email: Mapped[str] = mapped_column(String, unique=True, nullable=False)


with app.app_context():
  db.create_all()
