from flask import Flask, render_template

APP = Flask(__name__)


@APP.route('/hello')
def index():
    return render_template('page.html')


@APP.route('/word')
def word():
    return "wow"


@APP.route('/cat')
def cat():
    return "cat"


if __name__ == "__main__":
    APP.debug = True
    APP.run(host='0.0.0.0', port=8000)
