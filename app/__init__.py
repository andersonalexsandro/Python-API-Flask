from flask import Flask
from app.blueprints import home, user


app = Flask(__name__)
app.register_blueprint(home.bp)
app.register_blueprint(user.bp)
app.run()
