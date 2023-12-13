from flask import Flask
from hashlib import md5


def create_app():
    app = Flask(__name__)
    encryptor = md5()
    app.debug = True
    app.secret_key = encryptor.digest()

    from main import login_blueprint, dashboard_blueprint, logout_blueprint
    app.register_blueprint(login_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(logout_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8000)
