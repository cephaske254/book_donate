from . import main
from flask import redirect,render_template

@main.route('/')
def index():
    title='Home'
    return render_template('index.html',title=title)