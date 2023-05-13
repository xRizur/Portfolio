from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')
    @app.route('/devops-project')
    def about():
        return render_template('devops-project.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)