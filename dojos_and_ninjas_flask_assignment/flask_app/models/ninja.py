from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo 

class Ninja:
    db_name = "dojos_and_ninjas_schema" 

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # We're linking ONE Company to this Electronic object
        self.dojo = None # This will eventually hold a Company object

    @classmethod
    def add_one_ninja(cls, data):
        query = """
        INSERT INTO ninjas
        (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """ 
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all_ninjas_with_dojos(cls):
        query = """
        SELECT * FROM ninjas
        JOIN dojos
        ON ninjas.dojo_id = dojos.id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        all_ninja_objects = [] 
        if len(results) == 0: 
            return [] 
        else: 
            for this_ninja_dictionary in results:
                print(this_ninja_dictionary) # 
                new_ninja_object = cls(this_ninja_dictionary) 
                new_dojo_dictionary = {
                    "id": this_ninja_dictionary['dojos.id'], 
                    "name": this_ninja_dictionary['dojos.name'],
                    "created_at": this_ninja_dictionary['dojos.created_at'], 
                    "updated_at": this_ninja_dictionary['dojos.updated_at'], 
                }
                new_dojo_object = dojo.Dojo(new_dojo_dictionary) 

                new_ninja_object.dojo = new_dojo_object
                
                all_ninja_objects.append(new_ninja_object)

            return all_ninja_objects
        

    @classmethod
    def get_one_ninja_with_dojo(cls, data):
        query = """
        SELECT * FROM ninjas
        JOIN dojos
        ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)   
        if len(results) == 0:
            return None
        else:
            ninja_dictionary = results[0]

            new_ninja_object = cls(ninja_dictionary)

            new_dojo_dictionary = {
                    "id": ninja_dictionary['dojos.id'], 
                    "name": ninja_dictionary['dojos.name'],
                    "created_at": ninja_dictionary['dojos.created_at'], 
                    "updated_at": ninja_dictionary['dojos.updated_at'], 
            }
            new_dojo_object = dojo.Dojo(new_dojo_dictionary)

            new_ninja_object.dojo = new_dojo_object

            return new_ninja_object
