from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db_name = "dojos_and_ninjas_schema" 
    def __init__(self, data): 
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def create_dojo(cls, data):
        query = """
        INSERT INTO dojos (name) 
        VALUES (%(name)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0: 
            return None 
        else: 
            new_dojo_object = cls(results[0]) # cls() means create an Object inside this class - in this case, Company()
            # Return this one object
            return new_dojo_object
    
    @classmethod
    def get_all_dojos(cls): 
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db_name).query_db(query)
        list_of_dojo_objects = [] 
        if len(results) == 0: 
            return []
        else: 
            for this_dojo_dictionary in results:
            
                new_dojo_object = cls(this_dojo_dictionary) 

                list_of_dojo_objects.append(new_dojo_object) 
            return list_of_dojo_objects
        
    @classmethod
    def get_one_dojo_with_ninjas(cls, data):
        query= """
        SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)

        if len(results) == 0: 
            return None 
        else: 
            new_dojo_object = cls(results[0]) # cls() means create an Object inside this class - in this case, Company()

            for each_ninja_dictionary in results:
                new_ninja_dictionary = {
                    "id": each_ninja_dictionary["ninjas.id"],
                    "first_name": each_ninja_dictionary["first_name"],
                    "last_name": each_ninja_dictionary["last_name"],
                    "age": each_ninja_dictionary["age"],
                    "created_at": each_ninja_dictionary["ninjas.created_at"],
                    "updated_at": each_ninja_dictionary["ninjas.updated_at"],
                }
                new_ninja_object = ninja.Ninja(new_ninja_dictionary)
                new_dojo_object.ninjas.append(new_ninja_dictionary)
            return new_dojo_object