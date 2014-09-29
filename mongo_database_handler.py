from pymongo import MongoClient
from bson.objectid import ObjectId
import time

from database_handler import DatabaseHandler

class MongoDatabaseHandler(DatabaseHandler):
    
    def __init__(self):
        client = MongoClient("localhost", 27017)
        self.db = client.laxhjalp
    
    def clear_profiles(self):
        self.db.drop_collection("profiles")

    def clear_pages(self):
        self.db.drop_collection("pages")

    def clear_interests(self):
        self.db.drop_collection("interests")

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

    def get_all_profiles(self):
        return self.db.profiles.find()

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

    def update_page(self, page):
        self.db.pages.update({"name": page["name"]}, {"$set": {"fields": page["fields"]}})
        return True

    def add_field(self, page_name, field_name, field):
        self.db.pages.update({"name": page_name},
                             {"$set": {"fields."+field_name: field}})
        return True

    def replace_field(self, fields, field, value):
        print "replace_field(%s, %s, %s)" % ( str(fields), str(field), str(value))
        if len(field) == 0:
            return None
        
        next_field_name = field[0]
        for f_name, f_value in fields.items():
            if f_name == next_field_name:
                print "Found %s"%f_name
            
                if len(field) == 1:
                    print "Final field, setting value"
                    fields[f_name]["value"] = value
                    print "fields = %s"%str(fields)
                    return fields
                else:
                    print "Nested value %s left."%str(field[1:])
                    found = self.replace_field(f_value, field[1:], value)
                    if found:
                        fields[f_name] = found
                        return fields

        return None      
    

    def update_page_field(self, page_name, field, value):
        field = field.split(".")
        page = self.get_page(page_name)
        updated_fields = self.replace_field(page["fields"], field, value)
        print "updated_fields = %s"%updated_fields
        if updated_fields:
            page["fields"] = updated_fields
            return self.update_page(page)
        else:
            return False
        #TODO add check if field exist
        
        #return self.add_field(page_name, field_name, field)
        
    #Doesn't work anymore, have to redo to work with update_page_field()
    def update_page_fields(self, page_name, fields):
        for field_name, field in fields.items():
            if not self.update_page_field(page_name, field_name, field):
                return False
        return True

    def add_interest_data(self, interest):
        current_time = time.localtime()
        interest["added"] = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
        self.db.interests.insert(interest)
        return True

    def remove_interest(self, _id):
        return self.db.interests.remove({"_id" :  ObjectId(_id)}) 

    def get_interest(self, _id):
        return self.db.interests.find_one({"_id" : ObjectId(_id)}) 

    def get_all_interests(self):
        return self.db.interests.find()
        
    def get_all_unread_interests(self):
        return self.db.interests.find({"read": False})

    def set_interest_field(self, _id, field, read):
        self.db.interests.update({"_id" : ObjectId(_id)},
                                 {"$set": {field: read}})
        return True
