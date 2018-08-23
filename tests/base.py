import unittest
import sys  # fix import errors
from app import create_app
import os
from app.models import Rides, Users, create_tables
from werkzeug.security import generate_password_hash
import psycopg2
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ConfigTestCase(unittest.TestCase):
    """This class represents the basic configs for all test case"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        with self.app.app_context():
            create_tables()

            user = Users()
            user.register("Elneny Mohah", "mohah@gmail.com", "01234", "True", False)
            user.register("Honeybunch Kaindu", "kaindu@gmail.com", "1440", "False", False)

            ride = Rides()
            ride.post_a_ride("Elneny Mohah", "Meru - Embu", "6:30pm")
            ride.post_a_ride("Elneny Mohah", "Timba - Head", "5:30pm")

            """Admin Creation"""
            conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                    password=os.getenv('password'))
            cur = conn.cursor()
            hidden = generate_password_hash("teddy0725143787")

            query = "INSERT INTO users (username, email, password, driver, admin) VALUES " \
                    "('Teddy Kavooh', 'teddykavooh@gmail.com', '" + hidden + "', '1', '1')"
            cur.execute(query)
            conn.commit()

            """Driver Creation"""
            conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                    password=os.getenv('password'))
            cur = conn.cursor()
            hidden = generate_password_hash("123")

            query = "INSERT INTO users (username, email, password, driver, admin) VALUES " \
                    "('Hola Delmonte', 'hola@gmail.com', '" + hidden + "', '1', '0')"
            cur.execute(query)
            conn.commit()

            """User Creation"""
            conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                    password=os.getenv('password'))
            cur = conn.cursor()
            hidden = generate_password_hash("456")

            query = "INSERT INTO users (username, email, password, driver, admin) VALUES " \
                    "('User Pele', 'user@gmail.com', '" + hidden + "', '0','0')"
            cur.execute(query)
            conn.commit()

            """Getting Tokens"""
            """User Login"""

            test_admin = {"email": "teddykavooh@gmail.com", "password": "teddy0725143787"}
            test_driver = {"email": "hola@gmail.com", "password": "123"}
            test_user = {"email": "user@gmail.com", "password": "456"}

            admin_response = self.client().post('/api/v2/users/login', data=json.dumps(test_admin),
                                                content_type='application/json')
            driver_response = self.client().post('/api/v2/users/login', data=json.dumps(test_driver),
                                                 content_type='application/json')
            user_response = self.client().post('/api/v2/users/login', data=json.dumps(test_user),
                                               content_type='application/json')

            admin_token_dict = json.loads(admin_response.get_data(as_text=True))
            driver_token_dict = json.loads(driver_response.get_data(as_text=True))
            user_token_dict = json.loads(user_response.get_data(as_text=True))

            admin = admin_token_dict["token"]
            driver = driver_token_dict["token"]
            user = user_token_dict["token"]

            self.admin_header = {"Content-Type": "application/json", "x-access-token": admin}
            self.driver_header = {"Content-Type": "application/json", "x-access-token": driver}
            self.user_header = {"Content-Type": "application/json", "x-access-token": user}

    def tearDown(self):
        """Deletes all test related data"""
        with self.app.app_context():

            conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                    password=os.getenv('password'))
            cur = conn.cursor()
            query = "DROP TABLE requests, rides, users;"
            cur.execute(query)
            conn.commit()


if __name__ == '__main__':
    unittest.main()
