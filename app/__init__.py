from flask import Flask

from app.extentions import db
from blueprints import home_routes, user_routes

# create the app
app = Flask(__name__)

# Adding Routes##
app.register_blueprint(home_routes.bp)
app.register_blueprint(user_routes.bp)


# Config Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
with app.app_context():
  db.create_all()


# run
app.run(port=5000, host="localhost", debug=True)
