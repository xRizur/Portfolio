from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv('../.env')
    db_password = os.environ.get('MYSQL_PASSWORD')
    app = Flask(__name__)
    app.secret_key = 'xyzsdfg'
    # Set MySQL data
    app.config['MYSQL_HOST'] = 'mysql'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = db_password
    app.config['MYSQL_DB'] = 'user-system'

    mysql = MySQL(app)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
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

    # Make function for logout session
    @app.route('/logout')
    def logout():
        session.pop('loggedin', None)
        session.pop('userId', None)
        session.pop('email', None)
        session.pop('name', None)
        return redirect('/login')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
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

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/devops-project')
    def about():
        return render_template('devops-project.html')
    @app.route('/grafana')
    def grafana():
        return render_template('dashboard.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
