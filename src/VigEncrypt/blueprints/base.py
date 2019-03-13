from flask import Blueprint, render_template

base = Blueprint('base', __name__)


@base.route('/')
def root():
    return render_template('home.html.jinja')
