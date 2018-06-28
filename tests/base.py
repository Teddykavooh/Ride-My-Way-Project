import unittest
import sys  # fix import errors
from app import create_app
import os
from app.models import Rides, Users
import psycopg2
from instance.config import config2
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ConfigTestCase(unittest.TestCase):
    """This class represents the basic configs for all test case"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        ride = Rides()
        ride.post_a_ride("Lewis Liu", "Meru - Embu", "6:30pm")
        ride.post_a_ride("Tedd", "Timba - Head", "5:30pm")

        user = Users()
        user.register("Elneny Mohah", "mohah@gmail.com", "01234")
        user.register("Honeybunch Kaindu", "kaindu@gmail.com", "1440")

    # def tearDown(self):
    #     """Deletes all test related data"""
    #     with self.app.app_context():
    #         conn = psycopg2.connect("dbname=Ride-My-Way-Project user=postgres password=teddy0725143787")
    #         cur = conn.cursor()
    #         cur.execute("DROP TABLE users, rides, requests;")
    #         conn.commit()


def create_tables(self):
        """ Create tables in the PostgreSQL database"""
        commands = (
            """
            CREATE TABLE rides (
                ride_id SERIAL PRIMARY KEY,
                driver VARCHAR(255)NOT NULL,
                route VARCHAR(250) NOT NULL,
                time VARCHAR(10) NOT NULL
            )
            """,
            """ CREATE TABLE users (
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    password VARCHAR(500) NOT NULL,
                    driver BOOLEAN NULL,
                    admin BOOLEAN NULL
                    )
            """,
            """
            CREATE TABLE requests (
                    request_id INTEGER PRIMARY KEY,
                    ride_id VARCHAR(50) NOT NULL,
                    passenger_name VARCHAR(255) NOT NULL,
                    pick_up_station VARCHAR(255) NOT NULL,
                    time VARCHAR(10) NOT NULL
            )
            """)
        conn = None
        try:
            # read the connection parameters
            parameters = config2()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**parameters)
            cur = conn.cursor()
            # create table one by one
            for command in commands:
                cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


if __name__ == '__main__':
    unittest.main()
