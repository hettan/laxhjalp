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
    
    def test_change_phone(self):
        self.test_add_profile()
        profile_data = self.db.get_profile_data(self.new_prof.email)        
        
        print profile_data
        self.assertTrue(self.db.change_profile(self.new_prof.email,
                                               "phone", 1112233444))
        for p in self.db.get_all_profiles():
            print p
        profile_data = self.db.get_profile_data(self.new_prof.email)
        
        self.assertNotEqual(Profile.get_profile(profile_data).phone,
                            self.new_prof.phone)
    
    def test_rem_profile(self):
        self.assertTrue(self.db.rem_profile(self.new_prof.email))

        profile_data = self.db.get_profile_data(self.new_prof.email)
        self.assertEqual(profile_data, None)

    

if __name__ == "__main__":
    unittest.main()

