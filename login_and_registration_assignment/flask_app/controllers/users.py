from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def view_login_and_registration_page():
    return render_template("login.html")


@app.route("/dashboard")
def view_dashboard_page():
    if "user_id" not in session:
        return redirect("/")

    data = {
        "id": session["user_id"]
    }
    this_user = user.User.get_one_user_by_id(data)
    return render_template("dashboard.html", this_user = this_user)

@app.route("/register", methods=["POST"])
def add_user_to_db():
    if not user.User.validate_user(request.form):
        return redirect("/")
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": pw_hash,
        }
        session["user_id"] = user.User.add_user(data)
        return redirect("/dashboard")
    

@app.route("/login", methods=["POST"])
def user_login():
    print(request.form)
    if not user.User.validate_login(request.form):
        return redirect("/")
    else:
        data = {
            "email": request.form["email"]
        }
        found_user = user.User.get_one_user_by_email(data)
        session["user_id"] = found_user.id #save id in session.
        return redirect("/dashboard")


@app.route("/logout", methods=["POST"])
def user_logout():
    session.clear()
    return redirect("/")