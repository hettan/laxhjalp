import unittest

from mongo_database_handler import MongoDatabaseHandler
from profile import Profile

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.db = MongoDatabaseHandler()
        self.db.clear_profiles()
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
    

if __name__ == "__main__":
    unittest.main()

