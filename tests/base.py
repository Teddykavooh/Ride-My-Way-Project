import unittest
import sys  # fix import errors
from app import create_app, connect
import os
from app.models import Rides, Users, create_tables
import psycopg2
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ConfigTestCase(unittest.TestCase):
    """This class represents the basic configs for all test case"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        with self.app.app_context():
            create_tables()

            ride = Rides()
            ride.post_a_ride("Lewis Liu", "Meru - Embu", "6:30pm")
            ride.post_a_ride("Tedd", "Timba - Head", "5:30pm")

            user = Users()
            user.register("Elneny Mohah", "mohah@gmail.com", "01234", True, True)
            user.register("Honeybunch Kaindu", "kaindu@gmail.com", "1440", False, False)

    def tearDown(self):
        """Deletes all test related data"""
        with self.app.app_context():
            conn = psycopg2.connect("dbname=Ride-My-Way-Project user=postgres password=teddy0725143787")
            cur = conn.cursor()
            cur.execute("DROP TABLE users, rides, requests;")
            conn.commit()


if __name__ == '__main__':
    unittest.main()
