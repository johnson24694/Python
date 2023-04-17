from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user 
from flask import flash

class Recipe:
    db_name = "recipes_schema" 

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.under_thirty_minutes = data["under_thirty_minutes"]
        self.date_cooked = data["date_cooked"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data['user_id']
        self.user = None


    @classmethod
    def get_all_recipes_with_users(cls):
        query = """
        SELECT * FROM recipes
        JOIN users
        ON recipes.user_id = users.id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        all_recipe_objects = [] 
        if len(results) == 0: 
            return [] 
        else: 
            for this_recipe_dictionary in results: 
                new_recipe_object = cls(this_recipe_dictionary) 
                user_dictionary = {
                    "id": this_recipe_dictionary['users.id'], 
                    "first_name": this_recipe_dictionary['first_name'],
                    "last_name": this_recipe_dictionary['last_name'],
                    "email": this_recipe_dictionary['email'],
                    "password": this_recipe_dictionary['password'],                    
                    "created_at": this_recipe_dictionary['users.created_at'], 
                    "updated_at": this_recipe_dictionary['users.updated_at'], 
                }
                user_object = user.User(user_dictionary) 

                new_recipe_object.user = user_object
                
                all_recipe_objects.append(new_recipe_object)

            return all_recipe_objects
        
    @classmethod
    def get_one_recipe(cls, data): 
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0: # Nothing in DB
            return None # Return an empty list - nothing to get
        else: 
            new_recipe_object = cls(results[0])
            return new_recipe_object
        
    @classmethod
    def add_one_recipe(cls, data):
        query = """
        INSERT INTO recipes
        (name, description, instructions, date_cooked, under_thirty_minutes, user_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_thirty_minutes)s, %(user_id)s);
        """ 
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_one_with_user(cls, data):
        query = """
        SELECT * FROM recipes
        JOIN users
        ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s;
        """ 
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0: 
            return None
        else: 
            new_recipe_object = cls(results[0])
            user_dictionary = {
                "id": results[0]['users.id'], 
                "first_name": results[0]['first_name'],
                "last_name": results[0]['last_name'],
                "email": results[0]['email'],
                "password": results[0]['password'],                    
                "created_at": results[0]['users.created_at'], 
                "updated_at": results[0]['users.updated_at'], 
            }
            user_object = user.User(user_dictionary) 

            new_recipe_object.user = user_object
            return new_recipe_object
            
            
            
            # new_user_object = user.User(new_user_dictionary)
        
            # new_recipe_object.user = new_user_object
            
            # return new_recipe_object    user_id = %(user_id)s
        
    @classmethod
    def edit_recipe_in_db(cls, data):
        query = """
        UPDATE recipes SET
        name = %(name)s,
        description = %(description)s,
        instructions = %(instructions)s,
        date_cooked = %(date_cooked)s,
        under_thirty_minutes = %(under_thirty_minutes)s,
        user_id = %(user_id)s
        
        WHERE
        id = %(id)s;
        """ 
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe["name"]) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(recipe["description"]) < 3:
            is_valid = False
            flash("Description must be at least 3 characters.")
        if len(recipe["instructions"]) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        if recipe['date_cooked'] == '':
            flash("Please input a date.")
            is_valid = False
        if 'under_thirty_minutes' not in recipe:
            flash("Give me a cook time.")
            is_valid = False

        return is_valid
