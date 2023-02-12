from application import app
from flask import request, redirect, url_for, render_template, flash
from flask_login import login_required, current_user

@app.route('/', methods=['GET'])
@login_required
def index():
    return render_template('base.html')

@app.route('/login', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('/auth/login.html')

@app.route('/signup', methods=['GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('/auth/signup.html')