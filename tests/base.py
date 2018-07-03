import unittest
import sys  # fix import errors
from app import create_app
import os
from app.models import Rides, Users, create_tables
# from werkzeug.security import generate_password_hash
import psycopg2
# import json
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
            user.register("Elneny Mohah", "mohah@gmail.com", "01234", True, False)
            user.register("Honeybunch Kaindu", "kaindu@gmail.com", "1440", False, False)
            #
            # """Admin Creation"""
            # conn = psycopg2.connect(os.getenv('Db'))
            # cur = conn.cursor()
            # hidden = generate_password_hash("teddy0725143787")
            #
            # query = "INSERT INTO users (username, email, password, driver, admin) VALUES " \
            #         "('teddykavooh@gmail.com', 'admin', '" + hidden + "', '" + '1' + "','" + '1' + "' )"
            # cur.execute(query)
            # conn.commit()
            #
            # """Driver Creation"""
            # conn = psycopg2.connect(os.getenv('Db'))
            # cur = conn.cursor()
            # hidden = generate_password_hash("123")
            #
            # query = "INSERT INTO users (username, email, password, driver, admin) VALUES " \
            #         "('teddykavooh@gmail.com', 'admin', '" + hidden + "', '" + '1' + "','" + '0' + "' )"
            # cur.execute(query)
            # conn.commit()
            #
            # """User Creation"""
            # conn = psycopg2.connect(os.getenv('Db'))
            # cur = conn.cursor()
            # hidden = generate_password_hash("456")
            #
            # query = "INSERT INTO users (username, email, password, driver, admin) VALUES " \
            #         "('teddykavooh@gmail.com', 'admin', '" + hidden + "', '" + '0' + "','" + '0' + "' )"
            # cur.execute(query)
            # conn.commit()
            #
            # """Getting Tokens"""
            # """User Login"""
            # test_user = {"username": "Inamoto Kagawa", "password": "123"}
            # test_driver = {"username": "Kesuke Honda", "password": "456"}
            # test_admin = {"username": "Teddykavooh", "password": "teddy0725143787"}
            #
            # user_response = self.client().post('/api/v2/login', data=json.dumps(test_user),
            #                                    content_type='application/json')
            # driver_response = self.client().post('/api/v2/login', data=json.dumps(test_driver),
            #                                      content_type='application/json')
            # admin_response = self.client().post('/api/v2/login', data=json.dumps(test_admin),
            #                                     content_type='application/json')
            #
            # user_token_dict = json.loads(user_response.get_data(as_text=True))
            # driver_token_dict = json.loads(driver_response.get_data(as_text=True))
            # admin_token_dict = json.loads(admin_response.get_data(as_text=True))
            #
            # user_token = user_token_dict["token"]
            # driver_token = driver_token_dict["token"]
            # admin_token = admin_token_dict["token"]
            #
            # self.user_header = {"Content-Type": "application/json", "x-access-token": user_token}
            # self.driver_header = {"Content-Type": "application/json", "x-access-token": driver_token}
            # self.admin_header = {"Content-Type": "application/json", "x-access-token": admin_token}

    def tearDown(self):
        """Deletes all test related data"""
        with self.app.app_context():
            conn = psycopg2.connect(os.getenv('Db'))
            cur = conn.cursor()
            cur.execute("DROP TABLE users, rides, requests;")
            conn.commit()


if __name__ == '__main__':
    unittest.main()
