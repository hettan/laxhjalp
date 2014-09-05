class DatabaseHandler():
    def __init__(self):
        pass

    def clear_profiles(self):
        pass

    def clear_all(self):
        pass

    def add_profile(self, user):
        return False

    def rem_profile(self, email):
        return False

    def get_profile_data(self, email):
        return None

    def password_correct(self, user, password):
        return False

    def change_profile(self, user, field, value):
        return False

    def change_password(self, user, old_password, new_password):
        if self.password_correct(user, old_password):
            self.change_profile(user, new_password)
            return True
        else:
            return False

    def change_first_name(self, user, first_name):
        return self.change_profile(user, "first_name", first_name)
    
    def change_last_name(self, user, last_name):
        return self.change_profile(user, "last_name", last_name)
    
    def change_phone(self, user, phone):
        return self.change_profile(user, "phone", phone)
        
    def change_address(self, user, field, value):
        return False

    def change_address_road(self, user, road):
        return self.change_address(user, "road", road)
        
    def change_address_number(self, user, number):
        return self.change_address(user, "number", number)
    
    def change_address_postal(self, user, postal):
        return self.change_address(user, "postal", postal)

    def change_address_city(self, user, city):
        return self.change_address(user, "city", city)
