from flask import Blueprint, request, session, redirect, render_template
from flask_mysqldb import MySQLdb
from flask import current_app


import re
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    mysql = current_app.mysql
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:

        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM user WHERE email = % s AND password = % s',
            (email, password,))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userId'] = user['userId']
            session['name'] = user['name']
            session['email'] = user['email']
            message = 'Logged in successfully !'
            return render_template('logged.html',
                                   message=message)
        else:
            message = 'Please enter correct email / password !'
    return render_template('login.html', message=message)

@auth_bp.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userId', None)
    session.pop('email', None)
    session.pop('name', None)
    return redirect('/login')

@auth_bp.route('/logged')
def logged():
    return render_template('logged.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    mysql = current_app.mysql
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('SELECT * FROM user WHERE email = % s', (email,))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address !'
        elif not userName or not password or not email:
            message = 'Please fill out the form !'
        else:
            cursor.execute(
                'INSERT INTO user VALUES (NULL, % s, % s, % s)',
                (userName, email, password,))
            mysql.connection.commit()
            message = 'You have successfully registered !'
    elif request.method == 'POST':
        message = 'Please fill out the form !'
    return render_template('register.html', message=message)