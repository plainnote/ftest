import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

##################################### 
# config
##################################### 
app.config['SECRET_KEY']='samplesecret'

#####################################
#  db setup
#####################################
basedir =  os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#####################################
#  login condfig
#####################################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

#####################################
#  blueprint configs
#####################################
from src.core.views import core
from src.users.views import users
from src.func1.views import func1
from src.func2.views import func2
from src.error_pages.handlers import error_pages

#####################################
# Register the apps
#####################################
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(func1)
app.register_blueprint(func2)
app.register_blueprint(error_pages)
