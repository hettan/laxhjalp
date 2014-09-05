from pymongo import MongoClient

from database_handler import DatabaseHandler

class MongoDatabaseHandler(DatabaseHandler):
    
    def __init__(self):
        client = MongoClient("localhost", 27017)
        self.db = client.laxhjalp
    
    def clear_profiles(self):
        self.db.drop_collection("profiles")
    
    def clear_all(self):
        self.clear_profiles()

    def add_profile(self, profile):
        self.db.profiles.insert(profile.get_data())
        return True

    def rem_profile(self, email):
        self.db.profiles.remove({"email":email})
        return True

    def get_profile_data(self, email):
        return self.db.profiles.find_one({"email":email})

    def password_correct(self, email, password):
        return True

    def change_profile(self, email, field, value):
        print "{'email': %s}, {'$set': {%s: %s}}"%(email, field, value)
        self.db.profiles.update({"email": email}, {"$set": {field: value}})
        return True

    def change_address(self, email, field, value):
        return True

    def get_all_profiles(self):
        return self.db.profiles.find()
