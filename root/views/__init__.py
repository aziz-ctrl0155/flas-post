from flask import Blueprint, render_template
from flask_wtf.csrf import CSRFError

home = Blueprint('home', __name__)


@home.route("/")
def home_page():
    return render_template('home/index.html')


@home.errorhandler(CSRFError)
def csrf_error(reason):
    return render_template('handler/csrf.html', reason=reason), 400
