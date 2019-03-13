from flask import Flask
from .blueprints.base import base
from .blueprints.api import api

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(base, url_prefix='')
app.register_blueprint(api, url_prefix='/api')
