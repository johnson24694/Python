from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")  #Shows the login and registration page.
def reg_and_login_page():
    return render_template("reg_and_login_page.html")

@app.route("/register", methods = ["POST"]) #Validated Route that adds a new user to the DB.
def register_user():
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
        return redirect("/recipes")
    

@app.route("/login", methods = ["POST"]) #Validated Route that logs in an existing user.
def login_user():
    print(request.form)
    if not user.User.validate_login(request.form):
        return redirect("/")
    else:
        data = {
            "email": request.form["email"]
        }
        found_user = user.User.get_one_user_by_email(data)
        session["user_id"] = found_user.id #save id in session.
    return redirect("/recipes")

@app.route("/logout") #Link that logs out the user.
def logout_user():
    session.clear()
    return redirect("/")



