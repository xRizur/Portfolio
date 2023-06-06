from flask import Flask
from dotenv import load_dotenv
import os
from flask_mysqldb import MySQL

from .auth import auth_bp
from .tasks import tasks_bp
from .main import main_bp

def create_app():
    load_dotenv('../.env')
    db_password = os.environ.get('MYSQL_PASSWORD')
    app = Flask(__name__)
    app.secret_key = 'xyzsdfg'
    # Set MySQL data
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = db_password
    app.config['MYSQL_DB'] = 'user-system'

    # Store MySQL object in app.
    app.mysql = MySQL(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(main_bp)

    return app
