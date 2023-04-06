from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import user

@app.route("/") #Show the Add a New User home page (GET)
def create_page():
    return render_template("create.html")

@app.route("/users/new", methods=['POST']) #Adds one user to the DB (POST)
def add_user():
    # if "name" not in session:
    #     print("Not logged in - going back to root route")
    #     return redirect("/")
    form_results = {    
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],    
    }
    user.User.create_user(form_results)
    return redirect("/users")

@app.route("/users")  #Shows all users (GET)
def show_all_users():
    all_user_objects = user.User.get_all_users()
    return render_template("read_all.html", list_of_user_objects = all_user_objects)

@app.route("/users/<int:id>") #Shows one user (GET)
def view_one_user(id):
    # if "name" not in session:
    #     print("Not logged in - going back to root route")
    #     return redirect("/")    
    data = {
        "id": id
    }
    
    this_user = user.User.get_one_user(data)
    return render_template("view_user.html", this_user = this_user)

@app.route("/users/<int:id>/show_edit_page") #Shows the edit page of one user (GET)
def show_edit_page(id):
    # if "name" not in session:
    #     print("Not logged in - going back to root route")
    #     return redirect("/")
    data = {
        "id": id
    }
    
    this_user = user.User.get_one_user(data)
    return render_template("edit.html", this_user = this_user)
    

@app.route("/users/<int:id>/update", methods=['POST']) # Will update one user (POST)
def edit(id):
    # if "name" not in session:
    #     print("Not logged in - going back to root route")
    #     return redirect("/")    
    form_results = {    
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": id,    
    }
    user.User.edit(form_results)
    return redirect(f"/users/{id}")

    

    
@app.route("/users/<int:id>/delete") #Deletes one user (GET)
def delete(id):
    # if "name" not in session:
    #     print("Not logged in - going back to root route")
    #     return redirect("/")
    data = {
        'id': id
    }
    user.User.delete(data)
    return redirect('/users')
    



