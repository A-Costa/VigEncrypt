from flask import Blueprint, render_template

base = Blueprint('base', __name__)

print(base.root_path)


@base.route('/')
def root():
    return render_template('home.html.jinja')
