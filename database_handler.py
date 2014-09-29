from passlib.apps import custom_app_context as pwd_context

class DatabaseHandler():
    def __init__(self):
        pass

    def clear_profiles(self):
        pass

    def clear_pages(self):
        pass
    
    def clear_interests(self):
        pass

    def clear_all(self):
        self.clear_profiles()
        self.clear_pages()
        self.clear_interests()
        
    def add_profile(self, email):
        return False

    def rem_profile(self, email):
        return False

    def get_profile_data(self, email):
        return None

    def get_all_profiles(self):
        return None

    def email_unique(self, email):
        return False

    def get_password(self, email):
        return None

    def add_page(self, name):
        return None

    def get_page(self, name):
        return None

    def add_field(self, page_name, field_name, field):
        return None

    def update_page_field(self, page_name, field_name, field):
        return None

    def update_page_fields(self, page_name, fields):
        return None

    def setup_pages(self):
        self.add_page("startsida")
        carousel = []
        carousel.append({"header": {"type": "text", "value": "h1"}, "text": {"type": "text", "value": "texten1"},
                         "button": {"type": "text", "value": "button text1"},
                         "image": {"type": "image", "value": "/static/img/examle1.JPG"}})  
        carousel.append({"header": {"type": "text", "value": "h2"}, "text": {"type": "text", "value": "texten2"},
                         "button": {"type": "text", "value": "button text2"},
                         "image": {"type": "image", "value": "/static/img/examle2.JPG"}})  
        carousel.append({"header": {"type": "text", "value": "h3"}, "text": {"type": "text", "value": "texten3"},
                         "button": {"type": "text", "value": "button text3"},
                         "image": {"type": "image", "value": "/static/img/examle3.JPG"}})  
        
        self.add_field("startsida", "carousel", carousel)
                
    @staticmethod
    def password_hash(password):
        return pwd_context.encrypt(password)
        
    def password_correct(self, email, password):
        password_hash = self.get_password(email)
        if password_hash:
            return pwd_context.verify(password, password_hash)
        return False
            
    def change_profile(self, email, field, value):
        return False

    def change_password(self, email, old_password, new_password):
        if self.password_correct(email, old_password):
            new_password = DatabaseHandler.password_hash(new_password)
            self.change_profile(email, "password", new_password)
            return True
        else:
            return False

    def change_first_name(self, email, first_name):
        return self.change_profile(email, "first_name", first_name)
    
    def change_last_name(self, email, last_name):
        return self.change_profile(email, "last_name", last_name)
    
    def change_phone(self, email, phone):
        return self.change_profile(email, "phone", phone)
        
    #Subclass should override
    def change_address(self, email, field, value):
        return False

    def change_address_road(self, email, road):
        return self.change_address(email, "road", road)
        
    def change_address_number(self, email, number):
        return self.change_address(email, "number", number)
    
    def change_address_postal(self, email, postal):
        return self.change_address(email, "postal", postal)

    def change_address_city(self, email, city):
        return self.change_address(email, "city", city)
    
    def add_interest_data(self, data):
        return False

    def add_interest(self, email, name, address, phone, help_with, start_date):
        interest = {}
        interest["email"] = email
        interest["name"] = name
        interest["address"] = address
        interest["phone"] = phone
        interest["help_with"] = help_with
        interest["start_date"] = start_date
        interest["read"] = False
        return self.add_interest_data(interest)

    def remove_interest(self, _id):
        return False

    def get_interest(self, _id):
        return None

    def get_all_interests(self):
        return None

    def get_all_unread_interests(self):
        return None

    def set_interest_read(self, _id, value):
        if value == "True":
            value = True
        elif value == "False":
            value = False
        else:
            return False

        return self.set_interest_field(_id, "read", value)

    def set_interest_field(self, _id, field, value):
        return None
