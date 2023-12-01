from flask import render_template, redirect, url_for, Blueprint, request, session ### 0

login_blueprint = Blueprint("login", __name__)
dashboard_blueprint = Blueprint("dashboard", __name__)
logout_blueprint = Blueprint("logout", __name__)


@login_blueprint.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.update({"nick" : request.form['nickname']}) ### 1
    elif request.method == "GET" and "nick" not in session:
        return render_template("login.html")

    return redirect(url_for("dashboard.dashboard"))


@logout_blueprint.route('/logout')
def logout():
    if "nick" in session:
        session.pop("nick") ### 2

    return redirect(url_for("login.login"))


@dashboard_blueprint.route('/dashboard')

def dashboard():
    if "nick" in session: ### 3
        return render_template("dashboard.html", nickname=session["nick"])

    return redirect(url_for("login.login"))
