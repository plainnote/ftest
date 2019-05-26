from flask import render_template, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/help')
def help():
    return render_template('help.html')
