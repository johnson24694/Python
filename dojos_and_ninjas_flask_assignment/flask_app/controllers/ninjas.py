from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import dojo, ninja 

@app.route("/ninjas/create", methods=['POST']) #Creates a new ninja and redirects to the dojo show page of the dojo selected after creating a ninja.
def create_ninja():
    # form_results = {
    #     "first_name": request.form['first_name'],
    #     "last_name": request.form['last_name'],
    #     "age": request.form['age'],
    #     "dojo_id": request.form['dojo_id'],
    # }
    new_id = ninja.Ninja.add_one_ninja(request.form)
    return redirect(f"/show_dojo/{new_id}")
    

@app.route("/ninjas")
def show_new_ninja_page():
    all_dojos = dojo.Dojo.get_all_dojos()
    return render_template("new_ninja.html", all_dojos = all_dojos)

# @app.route("/show_dojo")
# def show_dojo_page():
#     new_id = ninja.Ninja.add_one_ninja(request.form)
#     return render_template("show_dojo.html", new_id = new_id)

# @app.route("/show_dojo/<int:id>")
# def show_one_dojo(id):
#     data = {
#         "id": id
#     }
    
#     this_dojo = dojo.Dojo.get_one_dojo_with_ninjas(data)
#     return render_template("show_dojo.html", this_dojo = this_dojo)

# @app.route("/show_dojo_with_ninja")
# def show_dojo_page():
#     data = {
#         "id": id
#     }
#     this_dojo = dojo.Dojo.get_one_dojo(data)
#     new_id = ninja.Ninja.add_one_ninja(request.form)
#     return render_template("show_dojo.html", new_id = new_id, this_dojo= this_dojo)
