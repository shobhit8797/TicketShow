from application import app
from flask import request, redirect, url_for, render_template, flash
from flask_login import login_required, current_user, logout_user, login_user
from application.models import *


@app.route('/', methods=['GET'])
# @login_required
def index():
    return render_template('/user/index.html')


@app.route('/login', methods=['GET'])
@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('/auth/login.html', props={'title': "Login", 'login_type': "user"})
    elif request.method == 'POST':
        data = request.form
        user = User.query.filter_by(email=data['email']).first()
        if user and user.password_hash == data['password']:
            login_user(user)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('/auth/login.html', props={'title': "Login", 'login_type': "admin"})
    elif request.method == 'POST':
        data = request.form
        user = User.query.filter_by(email=data['email']).first()
        if user and user.password_hash == data['password']:
            login_user(user)

            # redirect to admin dashboard
            return redirect(url_for('index'))
        else:
            return redirect(url_for('admin_login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('/auth/signup.html')
    elif request.method == 'POST':
        data = request.form
        if User.query.filter_by(email=data['email']).first():
            return redirect(url_for('signup'))
        elif User.query.filter_by(email=data['username']).first():
            return redirect(url_for('signup'))
        else:
            user = User(email=data['email'], username=data['username'], password_hash=data['password'],
                        name=data['name'], role=[Role.query.filter_by(id=2).first()])
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))


@app.route('/logout', methods=['GET'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('login'))
    else:
        return {'statusCode': 401, 'message': 'User not logged in'}, 401
