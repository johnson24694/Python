from flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def create_user(cls, data):
        query = """ 
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        return connectToMySQL("users_schema").query_db(query, data)
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)
        list_of_user_objects = [] 
        if len(results) == 0: 
            return [] 
        else: 
            for this_user_dictionary in results:
                
                new_user_object = cls(this_user_dictionary) 
                list_of_user_objects.append(new_user_object) 
            return list_of_user_objects
        
    @classmethod
    def get_one_user(cls, data): 
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users_schema").query_db(query, data)
        if len(results) == 0: 
            return None 
        else: 
            new_user_object = cls(results[0])
            return new_user_object 
        
    @classmethod
    def edit(cls,data):
        query = """UPDATE users 
                SET first_name = %(first_name)s,
                last_name = %(last_name)s, email = %(email)s 
                WHERE id = %(id)s;"""
        return connectToMySQL("users_schema").query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL("users_schema").query_db(query, data)

