from flask_restful import Resource
from application.models import *
from flask import request
from flask_login import login_user, logout_user, current_user

# Authentication apis
# path '/auth/'
class LoginApi(Resource):
    def post(self):
        data = request.form
        user = User.query.filter_by(email=data['email']).first()
        if user and user.password_hash == data['password']:
            print(user.username, 'logging in')
            login_user(user)
            print('User logged in successfully')
            return {'statusCode': 200, 'message': 'User logged in successfully'}, 200
        else:
            return {'statusCode': 401, 'message': 'User does not exist'}, 409
class SignupApi(Resource):
    def post(self):
        data = request.form
        if User.query.filter_by(email=data['email']).first():
            return {'statusCode': 409, 'message': 'Email already exists'}, 409
        elif User.query.filter_by(email=data['username']).first():
            return {'statusCode': 409, 'message': 'Username already exists'}, 409
        else:
            user = User(email=data['email'], username=data['username'], password_hash=data['password'], name=data['name'], role=[Role.query.filter_by(id=2).first()])
            db.session.add(user)
            db.session.commit()
            return {'statusCode': 200, 'message': 'User created successfully'}, 200
class LogoutApi(Resource):
    def post(self):
        if current_user.is_authenticated:
            logout_user()
            return {'statusCode': 200, 'message': 'User logged out successfully'}, 200
        else:
            return {'statusCode': 401, 'message': 'User not logged in'}, 401