from app.models import create_tables
import psycopg2
from werkzeug.security import generate_password_hash


if __name__ == '__main__':
    create_tables()

"""Creates new user"""
conn = psycopg2.connect("dbname=Ride-My-Way-Project user=postgres password=teddy0725143787")
cur = conn.cursor()
hidden = generate_password_hash("teddy0725143787")
query = "INSERT INTO users (username, email, password, driver, admin) VALUES " "('" + 'Antony Kavooh' "'," \
        " '" + 'teddykavooh@gmail.com' + "', '" + hidden + "', '" + '1' + "', '" + '1' + "')"

cur.execute(query)
conn.commit()
print("Admin Created")
