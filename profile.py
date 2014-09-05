class Profile():    
    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

        self.phone = ""
        self.admin = False
        self.address = {}

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
        return data

    @staticmethod
    def dummy_profile():
        profile = Profile("johndoe@foo.bar", "123", "John","Doe")
        profile.add_phone(0701010101)
        profile.add_address("Yoloroad", 1, 13337,"Smallville")
        return profile

    @staticmethod
    def get_profile(data):
        profile = Profile(data["email"], data["password"],
                          data["first_name"], data["last_name"])
        profile.add_phone(data["phone"])
        if data["address"]:
            profile.address = data["address"]
        else:
            profile.address = {}

        return profile
