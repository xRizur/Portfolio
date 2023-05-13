from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#teraz stworz nastepna podstrone ktora zwroci template o nazwie about.html
@app.route('/devops-project')
def about():
    return render_template('devops-project.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)