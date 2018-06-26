import unittest
import sys  # fix import errors
from app import create_app
import os
from app.models import Rides, Users
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ConfigTestCase(unittest.TestCase):
    """This class represents the basic configs for all test case"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        ride = Rides()
        ride.post_a_ride("Lewis Liu", "Murang'a - Embu", "6:30pm")
        ride.post_a_ride("Tedd", "Timba - Head", "5:30pm")

        user = Users()
        user.register("Elneny Mohah", "mohah@gmail.com", "01234", driver=True)
        user.register("Honeybunch Kaindu", "kaindu@gmail.com", "1440", driver=False)


if __name__ == '__main__':
    unittest.main()
