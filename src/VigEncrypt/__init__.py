from flask import Flask
from .blueprints.base import base

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(base, url_prefix='')
