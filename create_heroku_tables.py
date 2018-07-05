import os
from werkzeug.security import generate_password_hash
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
                username VARCHAR(255) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(500) NOT NULL UNIQUE,
                driver BOOLEAN NULL,
                admin BOOLEAN NULL
                )
        """,
        """
        CREATE TABLE requests (
                request_id SERIAL PRIMARY KEY,
                ride_id VARCHAR(50) NOT NULL,
                passenger_name VARCHAR(255) NOT NULL UNIQUE,
                pick_up_station VARCHAR(255) NOT NULL,
                time VARCHAR(10) NOT NULL
        )
        """)
    conn = None
    try:
        parameters = config()
        conn = psycopg2.connect(os.getenv('Db'))
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


"""Creates new user"""
conn = psycopg2.connect("dbname=deijb3ntfbebui user=lqwuoejnuwiuwj"
                        " password=5e13ac0dda86f10cd5b079742b51f52e0ac970d1adba23e67e221d018ac14c68"
                        " host=ec2-54-83-12-150.compute-1.amazonaws.com")
cur = conn.cursor()
hidden = generate_password_hash("teddy0725143787")
query = "INSERT INTO users (username, email, password, driver, admin) VALUES " "('" + 'Antony Kavooh' "'," \
        " '" + 'teddykavooh@gmail.com' + "', '" + hidden + "', '" + '1' + "', '" + '1' + "')"

cur.execute(query)
conn.commit()
print("Admin Created")
