from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Message:
    DB = 'ohana_rideshare'
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.sender_id = data['sender_id']
        self.ride_id = data['ride_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender = None

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO messages (content, sender_id, ride_id) 
                VALUES (%(content)s, %(sender_id)s, %(ride_id)s);
                """
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def get_by_ride_id(cls,ride_id):
        data = {
            'id' : ride_id
        }
        query = """
                SELECT * FROM messages
                LEFT JOIN users ON messages.sender_id = users.id
                WHERE messages.ride_id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        message_list = []
        for row in results:
            message_obj = cls(row)
            sender_data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            message_obj.sender = user.User(sender_data)
            message_list.append(message_obj)
        return message_list


