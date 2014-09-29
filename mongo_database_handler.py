from pymongo import MongoClient

from database_handler import DatabaseHandler

class MongoDatabaseHandler(DatabaseHandler):
    
    def __init__(self):
        client = MongoClient("localhost", 27017)
        self.db = client.laxhjalp
    
    def clear_profiles(self):
        self.db.drop_collection("profiles")

    def clear_pages(self):
        self.db.drop_collection("pages")
    
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

        if profile:
            return profile["password"]
        else:
            return None

    def change_profile(self, email, field, value):
        self.db.profiles.update({"email": email}, {"$set": {field: value}})
        return True

    def change_address(self, email, field, value):
        self.db.profiles.update({"email": email},
                                {"$set": {"address."+field: value}})
        return True

    def get_all_profiles(self):
        return self.db.profiles.find()

    def add_page(self, name):
        page = {"name": name, "fields": {}}
        self.db.pages.insert(page)
        return True

    def get_page(self, name):
        return self.db.pages.find_one({"name": name})

    def add_field(self, page_name, field_name, field):
        self.db.pages.update({"name": page_name},
                             {"$set": {"fields."+field_name: field}})
        return True
    
    def update_page_field(self, page_name, field_name, field):
        #TODO add check if field exist
        return self.add_field(page_name, field_name, field)
        
    def update_page_fields(self, page_name, fields):
        for field_name, field in fields.items():
            if not self.update_page_field(page_name, field_name, field):
                return False
        return True

