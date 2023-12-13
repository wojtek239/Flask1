from flask import render_template, redirect, url_for, Blueprint, request, session, \
    flash, SQLALchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://nazwa_bazy.sqlite3'
db = SQLAlchemy(app)


class Users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, email):
        self.name, self.email = name, email


login_blueprint = Blueprint("login", __name__)
dashboard_blueprint = Blueprint("dashboard", __name__)
logout_blueprint = Blueprint("logout", __name__)


@login_blueprint.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.update({"nick" : request.form['nickname']})
        flash("You've been successfully logged in.")
    elif request.method == "GET" and "nick" not in session:
        return render_template("login.html")
    elif request.method == "GET" and "nick" in session:
        flash("Already logged in!")
    return redirect(url_for("dashboard.dashboard"))


@logout_blueprint.route('/logout')
def logout():
    if "nick" in session:
        session.pop("nick")
        flash("You have been logged out!")
    else:
        flash("You are not logged in!")

        return redirect(url_for("login.login"))


@dashboard_blueprint.route('/dashboard')
def dashboard():
    if "nick" in session:
        return render_template("dashboard.html", nickname=session["nick"])
    else:
        flash("You are not logged in!")
    return redirect(url_for("login.login"))
