from flask import Blueprint, request, redirect,render_template

user_bp = Blueprint('user', __name__)  # для связи routers c app.py

@user_bp.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')


@user_bp.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')


@user_bp.route('/login', methods=['GET','POST'])
def logout():
    return render_template('login.html')