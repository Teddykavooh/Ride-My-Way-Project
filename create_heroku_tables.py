from app.models import create_tables
import psycopg2
from werkzeug.security import generate_password_hash


+create_tables()

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
