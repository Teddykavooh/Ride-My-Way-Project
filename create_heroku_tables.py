import os
from app.models import create_tables
import psycopg2
from werkzeug.security import generate_password_hash


create_tables()


"""Creates new user"""
conn = psycopg2.connect(os.getenv('Db'))
cur = conn.cursor()
hidden = generate_password_hash("teddy0725143787")
query = "INSERT INTO users (username, email, password, driver, admin) VALUES " "('" + 'Antony Kavooh' "'," \
        " '" + 'teddykavooh@gmail.com' + "', '" + hidden + "', '" + '1' + "', '" + '1' + "')"

cur.execute(query)
conn.commit()
print("Admin Created")
