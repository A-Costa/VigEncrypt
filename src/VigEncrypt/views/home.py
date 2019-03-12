from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.route('/')
def root():
    return render_template('home.html')