from passlib.apps import custom_app_context as pwd_context

from database_handler import DatabaseHandler

class Profile():    
    
    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password_not_hashed = password
        self.password = DatabaseHandler.password_hash(password)
        self.first_name = first_name
        self.last_name = last_name

        self.phone = ""
        self.admin = False
        self.address = {}
        
    def set_admin(self):
        self.admin = True

    def add_phone(self, phone):
        self.phone = phone

    def add_address(self, road, number, postal, city):
        self.address["road"] = road
        self.address["number"] = number
        self.address["postal"] = postal
        self.address["city"] = city

    def get_data(self):
        data = {}
        data["email"] = self.email
        data["password"] = self.password
        data["first_name"] = self.first_name
        data["last_name"] = self.last_name
        data["phone"] = self.phone
        data["address"] = self.address
        data["admin"] = self.admin
        return data

    @staticmethod
    def dummy_profile():
        profile = Profile("johndoe@foo.bar", "123", "John","Doe")
        profile.add_phone(0701010101)
        profile.add_address("Yoloroad", 1, 13337,"Smallville")
        return profile

    @staticmethod
    def dummy_profiles():
        profile1 = Profile("johndoe1@foo.bar", "123", "John","Doe")
        profile1.add_phone(0701010101)
        profile1.add_address("Yoloroad", 1, 13337,"Smallville")
        profile2 = Profile("johndoe2@foo.bar", "123", "John","Doe")
        profile2.add_phone(0701010101)
        profile2.add_address("Yoloroad", 1, 13337,"Smallville")
        profile3 = Profile("johndoe3@foo.bar", "123", "John","Doe")
        profile3.add_phone(0701010101)
        profile3.add_address("Yoloroad", 1, 13337,"Smallville")
        
        profiles = []
        profiles.append(profile1)
        profiles.append(profile2)
        profiles.append(profile3)
        return profiles

    @staticmethod
    def get_profile(data):
        #password = ""
        #if "password" in data.keys():
        password = data["password"]
        
        profile = Profile(data["email"], password,
                          data["first_name"], data["last_name"])
        profile.add_phone(data["phone"])
        if data["address"]:
            profile.address = data["address"]
        else:
            profile.address = {}

        return profile
