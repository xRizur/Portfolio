from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/devops-project')
def about():
    return render_template('devops-project.html')

@main_bp.route('/grafana')
def grafana():
    return render_template('dashboard.html')
