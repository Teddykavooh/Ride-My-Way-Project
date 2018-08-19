import os
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import jwt
import datetime
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
            time VARCHAR(10) NOT NULL,
            FOREIGN KEY (driver) REFERENCES users (username) ON DELETE CASCADE 
        )
        """,
        """ CREATE TABLE users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(500) NOT NULL,
                driver BOOLEAN NULL,
                admin BOOLEAN NULL
                )
        """,
        """
        CREATE TABLE requests (
                request_id SERIAL PRIMARY KEY,
                ride_id VARCHAR(50) NOT NULL,
                passenger_name VARCHAR(255) NOT NULL,
                pick_up_station VARCHAR(255) NOT NULL,
                time VARCHAR(10) NOT NULL,
                response VARCHAR(10),
                FOREIGN KEY (passenger_name) REFERENCES users (username) ON DELETE CASCADE,
                FOREIGN KEY (ride_id) REFERENCES rides (ride_id) ON DELETE CASCADE 
        )
        """)
    conn = None
    try:
        parameters = config()
        conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                password=os.getenv('password'))
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


class Rides:
    """Ride's Functionality"""
    def get_all_rides(self):
        conn = conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                       password=os.getenv('password'))
        cur = conn.cursor()
        cur.execute("SELECT ride_id, driver, route, time FROM rides ORDER BY ride_id")
        rides = cur.fetchall()
        all_rides = {}
        for ride in rides:
            my_data = ride[0]
            all_rides[my_data] = {"driver": ride[1], "route": ride[2], "time": ride[3]}
        if all_rides == {}:
            return {"txt": "No rides are available"}
        else:
            conn.commit()
            cur.close()
            return all_rides

    def get_a_ride(self, ride_id):
        conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                password=os.getenv('password'))
        cur = conn.cursor()
        cur.execute("SELECT * FROM rides")
        rides = cur.fetchall()
        all_rides = {}
        for ride in rides:
            my_data = ride[0]
            all_rides[my_data] = {"driver": ride[1], "route": ride[2], "time": ride[3]}
        if ride_id in all_rides:
            conn.commit()
            cur.close()
            return all_rides
        else:
            return {"txt": "Ride not available"}

    def post_a_ride(self, driver, route, time):
        conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                password=os.getenv('password'))
        cur = conn.cursor()
        query = "INSERT INTO rides (driver, route, time) VALUES " \
                "('" + driver + "', '" + route + "', '" + time + "')"
        cur.execute(query)
        conn.commit()
        cur.close()
        return {"txt": "Ride Added"}

    def delete_a_ride(self, ride_id):
        conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                password=os.getenv('password'))
        cur = conn.cursor()
        cur.execute("SELECT * FROM rides")
        rides = cur.fetchall()
        all_rides = {}
        for ride in rides:
            my_data = ride[0]
            all_rides[my_data] = {"driver": ride[1], "route": ride[2], "time": ride[3]}
        if ride_id in all_rides:
            cur.execute("DELETE FROM rides WHERE ride_id = %s", (ride_id,))
            conn.commit()
            cur.close()
            return {"txt": "Ride Deleted"}
        else:
            return {"txt": "Ride not available"}

    def edit(self, ride_id, driver, route, time):
        conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                password=os.getenv('password'))
        cur = conn.cursor()
        cur.execute("SELECT * FROM rides")
        rides = cur.fetchall()
        all_rides = {}
        for ride in rides:
            my_data = ride[0]
            all_rides[my_data] = {"driver": ride[1], "route": ride[2], "time": ride[3]}
        if ride_id in all_rides:
            sql = """ UPDATE rides SET driver = %s, route = %s, time = %s WHERE ride_id = %s"""
            cur.execute(sql, (driver, route, time, ride_id))
            conn.commit()
            cur.close()
            return {"txt": "Ride Edited"}
        else:
            return {"txt": "Ride not available"}

    def request_to_join_a_ride(self, ride_id, passenger_name, pick_up_station, time):
        conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                password=os.getenv('password'))
        cur = conn.cursor()
        cur.execute("SELECT * FROM rides")
        rides = cur.fetchall()
        all_rides = {}
        for ride in rides:
            my_data = ride[0]
            all_rides[my_data] = {"driver": ride[1], "route": ride[2], "time": ride[3]}
            # if my_data in all_rides:
            #     return {"txt": "You can't request more rides"}
            # else:
            if ride_id in all_rides:
                sql = """ INSERT INTO requests(ride_id, passenger_name, pick_up_station, time)
                 VALUES(%s, %s, %s, %s) RETURNING ride_id, passenger_name, pick_up_station, time;"""
                cur.execute(sql, (ride_id, passenger_name, pick_up_station, time))
                conn.commit()
                cur.close()
                return {"txt": "Ride Requested"}
            else:
                return {"txt": "Ride does not exist"}

    def accept_or_reject_a_ride_request(self, ride_id, request_id, response):
        responses = ["Accepted", "Rejected"]
        if response in responses:
            conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                    password=os.getenv('password'))
            cur = conn.cursor()
            cur.execute("SELECT * FROM requests")
            requests = cur.fetchall()
            all_requests = {}
            for request in requests:
                my_data = request[0]
                all_requests[my_data] = {"ride_id": request[1], "passenger_name": request[2],
                                         "pick_up_station": request[3],
                                         "time": request[4]}
            if ride_id in all_requests:
                if request_id in all_requests:
                    sql = """ UPDATE requests SET response = %s, ride_id = %s WHERE request_id= %s"""
                    cur.execute(sql, (response, ride_id, request_id))
                    conn.commit()
                    cur.close()
                    return {"txt": "Response to request given"}
                else:
                    return {"txt": "Invalid Ride Request"}
            else:
                return {"txt": "Ride does not exist"}
        else:
            return {"txt": "Response should be either Accepted or Rejected"}

    def get_all_requests(self, ride_id):
        conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                password=os.getenv('password'))
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests ")
        requests = cur.fetchall()
        all_rides = {}
        for request in requests:
            my_data = request[0]
            my_ride = request[1]
            all_rides[my_data] = {"ride_id": request[1], "passenger_name": request[2], "pick_up_station": request[3],
                                  "time": request[4], "response": request[5]}
            if ride_id == my_ride:
                conn.commit()
                cur.close()
                return all_rides
            if all_rides == {}:
                return {"txt": "No requests are available"}
            else:
                return {"txt": "Error Occurred"}


class Users:
    """Users Functionality"""
    def get_all_users(self):
        conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                password=os.getenv('password'))
        cur = conn.cursor()
        cur.execute("SELECT * FROM users ORDER BY user_id")
        users = cur.fetchall()
        all_users = {}
        for user in users:
            my_data = user[0]
            all_users[my_data] = {"username": user[1], "email": user[2], "password": user[3]}
        if all_users == {}:
            return {"txt": "No users are available"}
        else:
            conn.commit()
            cur.close()
            return all_users

    def register(self, username, email, password, driver, admin):
        """Creates new user"""
        driver_mode = ["True", "False"]
        if driver in driver_mode:
            conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                    password=os.getenv('password'))
            cur = conn.cursor()
            cur.execute("SELECT email from users")
            conn.commit()
            table_users = cur.fetchall()
            looping_db = {}
            for data_in_db in table_users:
                my_data = data_in_db[0]
                looping_db[my_data] = {}
            if email in looping_db:
                return {"txt": "User cannot be registered due to unique similarities"}
            else:
                hidden = generate_password_hash(password=password)
                query = "INSERT INTO users (username, email, password, driver, admin) VALUES "\
                        "('" + username + "', '" + email + "', '" + hidden + "', '" + driver + "', '" + '0' + "')"
                print(query)
                cur.execute(query)
                conn.commit()
                cur.close()
                return {"txt": "User Registered"}
        else:
            return {"txt": "Driver must either be True or False"}, 400

    def login(self, email, password):
        conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                password=os.getenv('password'))
        cur = conn.cursor()
        cur.execute("SELECT username, email, password, driver, admin from users where email='{}'".format(email))
        conn.commit()
        row = cur.fetchone()
        # print(row)
        if email in row:
            if check_password_hash(row[2], password=password):
                token = jwt.encode({"username": row[0], "driver": row[3],
                                    "admin": row[4],
                                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)},
                                   os.getenv('SECRET_KEY'))
                return {"txt": "Successfully logged In",
                        "token": token.decode('UTF-8')}
            else:
                return {"txt": "Invalid Password"}
        else:
            return {"txt": "Invalid Email"}

    def delete_a_user(self, user_id):
        conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                                password=os.getenv('password'))
        cur = conn.cursor()
        cur.execute("SELECT * from users where user_id='{}'".format(user_id))
        conn.commit()
        row = cur.fetchone()
        if user_id == 1:
            return {"txt": "SuperAdmin can't be deleted."}
        if row is None:
            return {"txt": "User Not Available"}
        else:
            cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            conn.commit()
            cur.close()
            return {"txt": "User Deleted"}
