from app.models import create_tables
import psycopg2
from werkzeug.security import generate_password_hash
import os


# if __name__ == '__main__':
create_tables()

"""Creates new user"""
conn = psycopg2.connect(database=os.getenv('Db'), host=os.getenv('host'), user=os.getenv('user'),
                        password=os.getenv('password'))
cur = conn.cursor()
hidden = generate_password_hash("teddy0725143787")
query = "INSERT INTO users (username, email, password, driver, admin) values ('{}', '{}', '{}', '{}', '{}')"\
    .format("Antony Kavooh", "teddykavooh@gmail.com", hidden, True, True)
cur.execute(query)
conn.commit()
print("Admin Created")
