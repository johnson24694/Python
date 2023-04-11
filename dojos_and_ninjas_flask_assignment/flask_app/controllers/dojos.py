from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import dojo

@app.route("/")
def index():
    return redirect("/all_dojos")

@app.route("/dojos", methods=['POST']) #Creates a new dojo and redirects to same page, but new dojo will now show up in the list of all dojos.
def create_dojo():
    form_results = {
        "name": request.form['name'],
    }
    dojo.Dojo.create_dojo(form_results)
    return redirect("/all_dojos")


@app.route("/all_dojos")  #Shows all dojos (Home Page)(GET)
def show_all_dojos():
    all_dojo_objects = dojo.Dojo.get_all_dojos()
    return render_template("new_dojo_home.html", list_of_dojo_objects = all_dojo_objects)


# @app.route("/show_dojo/<int:id>")
# def show_one_dojo(id):
#     data = {
#         "id": id
#     }
#     this_dojo = dojo.Dojo.get_one_dojo_with_ninjas(data)
#     return render_template("show_dojo.html", this_dojo = this_dojo)

@app.route("/show_dojo/<int:id>")
def show_one_dojo(id):
    data = {
        "id": id
    }
    
    this_dojo = dojo.Dojo.get_one_dojo_with_ninjas(data)
    return render_template("show_dojo.html", this_dojo = this_dojo)



    
