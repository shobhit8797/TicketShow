from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import LoginManager


app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
apia = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)


app.app_context().push()


#routes for the application
from application import controllers

# from application.api import *

# apia.add_resource(LoginApi, '/user/login')
# apia.add_resource(SignupApi, '/user/signup')
# apia.add_resource(LogoutApi, '/user/logout')