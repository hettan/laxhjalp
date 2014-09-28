import unittest

from mongo_database_handler import MongoDatabaseHandler
from profile import Profile

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.db = MongoDatabaseHandler()
        self.db.clear_all()
        self.new_prof = Profile.dummy_profile()
        
    def test_add_profile(self):
        self.assertTrue(self.db.add_profile(self.new_prof))
        profile_data = self.db.get_profile_data(self.new_prof.email)        
        
        self.assertNotEqual(profile_data, None)
        self.assertEqual(Profile.get_profile(profile_data).email,
                         self.new_prof.email)

        #Try add another with same email, should fail 
        self.assertFalse(self.db.add_profile(self.new_prof))

    def test_change_phone(self):
        self.test_add_profile()
                
        self.assertTrue(self.db.change_phone(self.new_prof.email,
                                             1112233444))
        
        profile_data = self.db.get_profile_data(self.new_prof.email)
        self.assertNotEqual(Profile.get_profile(profile_data).phone,
                            self.new_prof.phone)

    def test_change_address(self):
        self.test_add_profile()
        self.assertTrue(self.db.change_address_road(self.new_prof.email,
                                                      "new road"))
        profile_data = self.db.get_profile_data(self.new_prof.email)
        
        self.assertNotEqual(Profile.get_profile(profile_data).address,
                            self.new_prof.address["road"])
        
    def test_rem_profile(self):
        self.test_add_profile()

        self.assertTrue(self.db.rem_profile(self.new_prof.email))
        profile_data = self.db.get_profile_data(self.new_prof.email)
        self.assertEqual(profile_data, None)
        
    def test_profile_password(self):
        self.test_add_profile()

        self.assertTrue(self.db.password_correct(self.new_prof.email,
                                                 self.new_prof.password_not_hashed))
        self.assertFalse(self.db.password_correct(self.new_prof.email,
                                                  "incorrect_password"))
        self.assertTrue(self.db.change_password(self.new_prof.email,
                                                self.new_prof.password_not_hashed,
                                                "new_password"))
        self.assertTrue(self.db.password_correct(self.new_prof.email,
                                                 "new_password"))
    

    def test_get_all_profiles(self):
        profiles = Profile.dummy_profiles()
        for profile in profiles:
            self.assertTrue(self.db.add_profile(profile))

        self.assertEqual(self.db.get_all_profiles().count(), len(profiles))    

    def test_add_page(self):
        page_name = "test"
        self.assertTrue(self.db.add_page(page_name))
    
        field_name = "test_field"
        field = {"header": "test", "text": "test", "button": "test"}
        self.assertTrue(self.db.add_field(page_name, field_name, field))
        
        page = self.db.get_page(page_name)
        self.assertEqual(page["name"], page_name)
        self.assertEqual(page["fields"][0]["field"], field_name)
        self.assertEqual(page["fields"][0]["data"]["header"],
                         field["header"])
    
    def test_interest(self):
        dummy_interest = {}
        dummy_interest["email"] = "interest@yo.yo"
        dummy_interest["name"] = "Johnnny Doeyy"
        dummy_interest["address"] = "address 1"
        dummy_interest["phone"] = "0700311999"
        dummy_interest["help_with"] = "help_with text"
        dummy_interest["date"] = "2014-09-28"
        
        self.assertTrue(self.db.add_interest_data(dummy_interest))
        interests = self.db.get_all_interests()
        interests_unread = self.db.get_all_unread_interests()
        self.assertEqual(interests.count(), 1)
        self.assertEqual(interests.count(), 1)
        interest = self.db.get_interest(interests[0]["_id"])
        self.assertEqual(interest["email"], dummy_interest["email"])
        
if __name__ == "__main__":
    unittest.main()

