from flask import Flask

APP = Flask(__name__)


@APP.route('/')
def index():
    return "Hello World!"


if __name__ == "__main__":
    APP.debug = True
    APP.run()
