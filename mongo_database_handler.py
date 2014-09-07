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

    def email_unique(self, email):
        return self.db.profiles.find({"email":email}).count() == 0

    def add_profile(self, profile):
        if self.email_unique(profile.email):
            self.db.profiles.insert(profile.get_data())
            return True
        else:
            print "Email is already registered"
            return False
        
    def rem_profile(self, email):
        self.db.profiles.remove({"email":email})
        return True

    def get_profile_data(self, email):
        return self.db.profiles.find_one({"email":email})

    def get_password(self, email):
        profile = self.db.profiles.find_one({"email":email})
        return profile["password"]

    def change_profile(self, email, field, value):
        self.db.profiles.update({"email": email}, {"$set": {field: value}})
        return True

    def change_address(self, email, field, value):
        self.db.profiles.update({"email": email},
                                {"$set": {"address."+field: value}})
        return True

    def get_all_profiles(self):
        return self.db.profiles.find()
