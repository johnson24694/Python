from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import user, recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/recipes") #Shows the page with all the recipes linked to that user.
def view_all_recipes():
    if "user_id" not in session:
        return redirect("/")
    
    all_recipes = recipe.Recipe.get_all_recipes_with_users()
    logged_user = user.User.get_one_user_by_id({"id": session["user_id"]})
    return render_template("view_all_recipes_page.html", all_recipes = all_recipes, logged_user = logged_user)
    

@app.route("/recipes/<int:id>/view") #shows the page with one recipe on it.
def view_one_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": id
    }
    logged_user = user.User.get_one_user_by_id({"id": session["user_id"]})
    this_recipe = recipe.Recipe.get_one_with_user(data)
    return render_template("view_one_recipe_page.html", this_recipe = this_recipe, logged_user = logged_user)

@app.route("/recipes/new") #Shows the page to add a recipe, NOT for adding in the DB.
def view_add_recipe_page():
    if "user_id" not in session:
        return redirect("/")
       
    data = {
        "id": id
    }
    logged_user = user.User.get_one_user_by_id({"id": session["user_id"]})
    this_recipe = recipe.Recipe.get_one_recipe(data)
    all_users = user.User.get_all_users()
    return render_template("add_one_recipe_page.html", this_recipe = this_recipe, all_users = all_users, logged_user = logged_user)


@app.route("/recipes/create", methods = ["POST"]) #link to add the recipe to the DB and redirect back to all recipes page.
def add_one_recipe_to_db():
    if "user_id" not in session:
        return redirect("/")
    print(request.form)
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect("/recipes/new")
    
    
    # form_results = {
    #     "name": request.form["name"],
    #     "under_thirty_minutes": request.form["under_thirty_minutes"],
    #     "posted_by": request.form["posted_by"],
    #     "date_cooked": request.form["date_cooked"],
    #     "description": request.form["description"],
    #     "instructions": request.form["instructions"],
    # }
    recipe.Recipe.add_one_recipe(request.form)
    return redirect("/recipes")
    

@app.route("/recipes/<int:id>") #Shows the page to edit, NOT for editing in the DB.
def view_edit_page(id):
    if "user_id" not in session:
        return redirect("/")
    
    
    data = {
        "id": id
    }
    logged_user = user.User.get_one_user_by_id({"id": session["user_id"]})
    this_recipe = recipe.Recipe.get_one_recipe(data)
    # if this_recipe.user.id != session["user_id"]:
    #     return redirect("/recipes")
    all_users = user.User.get_all_users()
    
    return render_template("edit_one_recipe_page.html", this_recipe = this_recipe, all_users = all_users, logged_user = logged_user)

@app.route("/recipes/edit", methods = ["POST"]) #Link to edit the recipe in the DB. (Got rid of path variable <int:id> because used a hidden input in the html instead.)
def edit_one_recipe_in_db():
    if "user_id" not in session:
        return redirect("/")
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/{request.form['id']}")    
    print(request.form)
    
    
    recipe.Recipe.edit_recipe_in_db(request.form)
    
    return redirect(f"/recipes/{request.form['id']}/view")
    


@app.route("/delete/<int:id>/recipe") #Delete recipe link.
def delete_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    # Need data dictionary as we need to know the ID
    data = {
        "id": id
    }
    recipe.Recipe.delete_recipe(data)
    return redirect("/recipes")
