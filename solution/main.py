from flask import (Flask, url_for, request, render_template)


app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


app.run(port=8080, host='127.0.0.1')
