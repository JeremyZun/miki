from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from win10toast import ToastNotifier

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCGEMY_DATABASE_URI'] = 'salite:///users.sqlite3'
app.config['SQLALCGEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("screen.html")

@app.route("/index-tw")
def home():
    return render_template("index-tw.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/stream")
def stream():
    return render_template("stream.html")

@app.route("/signup")
def sign_up():
    return render_template("signup.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
                
        return render_template("user.html", email = email)
    else:
        flash("Your are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash(f"You Have been logged out!","info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/submit",methods=["GET", "POST"])
#?????????????????????????????? ???????????????json??????
def submit():
    #??????POST???GET??????????????????????????????????????????if?????????????????????
    if request.method == "POST":
        # ??????????????????
        name = request.form.get("name")
        password = request.form.get("password")
    if request.method == "GET":
        name = request.args.get("name")
        password = request.args.get("password")
    #???????????????????????????
    if len(name) == 0 and len(password) == 0:
        # ?????????????????? json
        return {'message':"??????!?????????????????????!!"}
    else:
        return {'message':"??????!!",'Account':name,'Password':password}

if __name__ == "__main__":
    app.run( debug=True)
