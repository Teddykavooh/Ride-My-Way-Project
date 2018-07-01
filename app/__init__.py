from flask import Flask
from flask_restplus import Api
from instance.config import app_config
from instance.config import config
import psycopg2


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    authorizations = {'apikey': {'type': 'apiKey', 'in': 'header', 'name': 'x-access-token'}}

    api = Api(app=app,
              description="Ride-my App is a carpooling application that "
                          "provides drivers with the ability to" 
                          " create ride oﬀers  and passengers  "
                          "to join available ride oﬀers.",
              title="Ride-My-Way",
              version='1.0',
              authorizations=authorizations,
              doc='/api/v1/documentation'
              )
    app.config['SWAGGER_UI_JSONEDITOR'] = True
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.url_map.strict_slashes = False

    from resources.rides import ride_api
    api.add_namespace(ride_api, path="/api/v1")
    from resources.users import user_api
    api.add_namespace(user_api, path="/api/v1")
    from resources.admin import user_api
    api.add_namespace(user_api, path="/api/v1")
    return app


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        parameters = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**parameters)
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
