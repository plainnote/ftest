from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

func2 = Blueprint('func2', __name__)

@func2.route('/f2')
def f2():
    return render_template('vtest.html')
