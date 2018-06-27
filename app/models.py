from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
from instance.config import config
request_ride = {}


def create_tables():
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
                passenger_name VARCHAR(255) NOT NULL,
                pick_up_station VARCHAR(255) NOT NULL,
                time VARCHAR(10) NOT NULL
        )
        """)
    conn = None
    try:
        # read the connection parameters
        parameters = config()
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


class Rides:
    """Ride's Functionality"""

    rides = {
        1: {"driver": "Teddy Kavooh", "route": "Vota - Machakos", "time": "5:30am"}
    }

    def get_all_rides(self):
        return self.rides

    def get_a_ride(self, ride_id):
        return self.rides[ride_id]

    def post_a_ride(self, driver, route, time):
        new_id = len(self.rides) + 1
        self.rides[new_id] = {"driver": driver, "route": route, "time": time}
        return {"txt": "Ride Added"}

    def delete_a_ride(self, ride_id):
        del self.rides[ride_id]
        return {"txt": "Ride Deleted"}

    def edit(self, ride_id, driver, route, time):
        self.rides[ride_id] = {"driver": driver, "route": route, "time": time}
        return {"txt": "Ride Edited"}

    def request_to_join_a_ride(self, ride_id, passenger_name, pick_up_station, time):
        self.rides.get(ride_id)
        request_ride[ride_id] = {"passenger_name": passenger_name, "pick_up_station": pick_up_station,
                                 "time": time}
        return {"txt": "Ride Requested"}


class Users:
    """Users Functionality"""
    users = {"Mueni Kavoo": {"email": "mueni@gmail.com", "password": generate_password_hash("01234"),
                             "driver": False, "admin": True},
             "Mike Mbulwa": {"email": "mike@gmail.com", "password": generate_password_hash("1234"),
                             "driver": True, "admin": False}}

    def get_all_users(self):
        return self.users

    def register(self, username, email, password, driver=False, admin=False):
        """Creates new user"""
        conn = psycopg2.connect("dbname=Ride-My-Way-Project user=postgres password=teddy0725143787")
        cur = conn.cursor()
        hidden = generate_password_hash(password=password)
        query = "INSERT INTO users (username, email, password, driver, admin) VALUES " \
                "('" + username + "', '" + email + "', '" + hidden + "', '" + '0' + "','" + '0' + "' )"
        cur.execute(query)
        conn.commit()
        return {"txt": "User Registered"}

    def login(self, username, password):
        conn = psycopg2.connect("dbname=Ride-My-Way-Project user=postgres password=teddy0725143787")
        cur = conn.cursor()
        cur.execute("SELECT username, password from users")
        table_users = cur.fetchall()
        looping_db = {}
        for data_in_db in table_users:
            # global my_data
            my_data = data_in_db[0]
            looping_db[my_data] = {"password": data_in_db[1]}

        if username in looping_db:
            if check_password_hash(looping_db[username]["password"], password=password):
                return {"txt": "Logged In"}
            else:
                return {"txt": "Invalid Password"}
        else:
            return {"txt": "Invalid Username"}

    # def delete_a_user(self, username):
    #     del self.users[username]
    #     return {"txt": "User Deleted"}
