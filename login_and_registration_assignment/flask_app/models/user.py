from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)    



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db_name = "login_and_registration_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def add_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    
    @classmethod
    def get_one_user_by_id(cls, data): 
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0: 
            return None 
        else: 
            return cls(results[0])
            

    @classmethod
    def get_one_user_by_email(cls, data): 
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0: 
            return None 
        else: 
            return cls(results[0])
        

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 2:
            flash("First Name must be at least 2 characters.", "registration")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last Name must be at least 2 characters.", "registration")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "registration")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be 8 characters or greater.", "registration")
            is_valid = False
        if (user['password']) != (user['confirm_password']):
            flash("Passwords do not match.", "registration")
            is_valid = False
        #check to see if someone already registered with that email.
        found_user_or_none = User.get_one_user_by_email({"email" : user["email"]})
        if found_user_or_none != None:
            is_valid = False
            flash("User already registered with that email.", "registration")
        return is_valid
    
    @staticmethod
    def validate_login(user):
        is_valid = True 
        found_user_or_none = User.get_one_user_by_email({"email" : user["email"]})
        if found_user_or_none == None:
            is_valid = False
            flash("Invalid login credentials.", "login")
            return False
        if not bcrypt.check_password_hash(found_user_or_none.password, user["password"]):
            is_valid = False
            flash("Invalid login credentials.", "login")
        return is_valid
    
    