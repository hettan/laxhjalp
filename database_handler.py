from passlib.apps import custom_app_context as pwd_context

class DatabaseHandler():
    def __init__(self):
        pass

    def clear_profiles(self):
        pass

    def clear_pages(self):
        pass

    def clear_all(self):
        self.clear_profiles()
        self.clear_pages()

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

    def add_field(self, page_name, field_name, value):
        return None

    def update_page(self, page_name, fields):
        return None

    def setup_pages(self):
        self.add_page("startsida")
        carousel = []
        corousel.append({"header": "h1", "text": "texten1", "button":"button text1"})  
        corousel.append({"header": "h2", "text": "texten2", "button":"button text2"})  
        corousel.append({"header": "h2", "text": "texten3", "button":"button text3"})  
        self.add_field("startsida", "carousel", carousel)
        marketing = []
        marketing.append({"header": "h1", "text": "marketing1", "button":"button text1"})
        marketing.append({"header": "h2", "text": "marketing2", "button":"button text2"})
        marketing.append({"header": "h3", "text": "marketing3", "button":"button text3"})
        self.add_field("startsida", "marketing", marketing)
        
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
