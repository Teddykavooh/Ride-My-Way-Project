from flask import Flask
from flask_restplus import Api
from instance.config import app_config


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    api = Api(app=app, description="Ride-my App is a carpooling application that "
                                   "provides drivers with the ability to"
                                   " create ride oﬀers  and passengers  "
                                   "to join available ride oﬀers.",
              title="Ride-My-Way",
              version='1.0',

              doc='/api/v1/documentation'
              )

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
