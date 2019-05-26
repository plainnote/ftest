from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

func1 = Blueprint('func1', __name__)

@func1.route('/f1')
def f1():
    return render_template('register.html')

