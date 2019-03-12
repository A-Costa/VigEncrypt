from flask import Flask
from .views.home import home

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(home)
