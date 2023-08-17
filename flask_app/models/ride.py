from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Ride:
    DB='ohana_rideshare'
    def __init__(self,data):
        self.id = data['id']
        self.destination = data['destination']
        self.origin = data['origin']
        self.date = data['date']
        self.details = data['details']
        self.driver_id = data['driver_id']
        self.rider_id = data['rider_id']
        self.rider = None
        self.driver = None
        self.messages = []

    @classmethod
    def assign_driver(cls,data):
        query = """
                UPDATE rides
                SET driver_id = %(driver_id)s
                WHERE id=%(ride_id)s; 
                """
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def unassign_driver(cls,data):
        query = """
                UPDATE rides
                SET driver_id = null
                WHERE id=%(ride_id)s; 
                """
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def delete(cls,ride_id):
        data = {
            'id' : ride_id
        }
        query = """
                DELETE FROM rides
                WHERE id=%(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO rides (destination,origin,date,details,rider_id)
                VALUES (%(destination)s, %(origin)s, %(date)s, %(details)s, %(rider_id)s);
                """
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = """
                UPDATE rides 
                SET origin = %(origin)s, details = %(details)s
                WHERE id=%(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def get_open_rides(cls):
        query = """
                SELECT * FROM rides
                LEFT JOIN users ON rides.rider_id = users.id
                WHERE rides.driver_id is null;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        ride_list = []
        for row in results:# solutions video shows an alternate way to do this!!! 
            ride_obj = cls(row) #instead of immediately creating the ride_obj, create a copy of the row
            # so that you have a normal dict instead of an immutable object
            # then add your rider object to that dict. 
            # Here's the code:
            # rider_dict = row.copy()
            # rider_dict['id'] = row['rider_id'] # I'm wondering if you need to repeat this line for 'created_at' and 'updated_at' as well???
            # rider = User(rider_dict)
            # ride_dict = row.copy()
            # ride_dict['rider'] = rider
            # ride_dict['driver'] = None
            # ride = cls(ride_dict)
            data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            ride_obj.rider = user.User(data)
            ride_list.append(ride_obj)
        return ride_list

    @classmethod
    def get_filled_rides(cls):
        query = """
				SELECT * FROM rides
                LEFT JOIN users AS riders ON rides.rider_id = riders.id
                LEFT JOIN users AS drivers ON rides.driver_id = drivers.id
                WHERE rides.driver_id is not null;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        ride_list = []
        for row in results:# solutions video shows an alternate way to do this!!! 
            ride_obj = cls(row) #instead of immediately creating the ride_obj, create a copy of the row
            # so that you have a normal dict instead of an immutable object
            # then add your rider and driver objects to that dict 
            # Here's the code:
            # rider_dict = row.copy()
            # rider_dict['id'] = row['rider_id']
            # rider = User(rider_dict)
            # ride_dict = 
            data = {
                'id' : row['riders.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['riders.created_at'],
                'updated_at' : row['riders.updated_at']
            }
            ride_obj.rider = user.User(data)
            data = {
                'id' : row['drivers.id'],
                'first_name' : row['drivers.first_name'],
                'last_name' : row['drivers.last_name'],
                'email' : row['drivers.email'],
                'password' : row['drivers.password'],
                'created_at' : row['drivers.created_at'],
                'updated_at' : row['drivers.updated_at']
            }
            ride_obj.driver = user.User(data)
            ride_list.append(ride_obj)
        return ride_list

    @classmethod
    def get_one_by_id(cls,ride_id):
        data = {
            'id': ride_id
        }
        query = """
				SELECT * FROM rides
                LEFT JOIN users AS riders ON rides.rider_id = riders.id
                LEFT JOIN users AS drivers ON rides.driver_id = drivers.id
                WHERE rides.id = %(id)s;
                """
        ride_dict = (connectToMySQL(cls.DB).query_db(query,data))[0]
        ride_obj = cls(ride_dict)
        data = {
            'id' : ride_dict['riders.id'],
            'first_name' : ride_dict['first_name'],
            'last_name' : ride_dict['last_name'],
            'email' : ride_dict['email'],
            'password' : ride_dict['password'],
            'created_at' : ride_dict['riders.created_at'],
            'updated_at' : ride_dict['riders.updated_at']
        }
        ride_obj.rider = user.User(data)
        data = {
            'id' : ride_dict['drivers.id'],
            'first_name' : ride_dict['drivers.first_name'],
            'last_name' : ride_dict['drivers.last_name'],
            'email' : ride_dict['drivers.email'],
            'password' : ride_dict['drivers.password'],
            'created_at' : ride_dict['drivers.created_at'],
            'updated_at' : ride_dict['drivers.updated_at']
        }
        ride_obj.driver = user.User(data)
        return ride_obj

    @staticmethod
    def ride_is_valid(data):
        is_valid=True
        if len(data['destination'].strip())<3:
            flash("Destination is insufficient.")
            is_valid=False
        if len(data['origin'].strip())<3:
            flash("Pick-up location is insufficient.")
            is_valid=False
        if len(data['details'].strip())<10:
            flash("More details needed.")
            is_valid=False
        if 'date' not in data or data['date']=='':
            flash("Please select a date for this ride.")
            is_valid=False  
        return is_valid