from flask_restplus import Resource, Namespace, reqparse, fields
from app.models import Users

user = Users()
user_api = Namespace("Users", description="All User Endpoints")
user_register = user_api.model("Register A User", {"username": fields.String,
                                                   "email": fields.String,
                                                   "password": fields.String,
                                                   "driver is either True Or False": fields.String})
user_login = user_api.model("Login User", {"username": fields.String,
                                           "password": fields.String})


class Users(Resource):
    """Contains POST"""
    @user_api.expect(user_register)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="Username must be provided",
                            required=True, location=["json"])
        parser.add_argument("email", type=str, help="E-Mail must be provided", location=["json"],
                            required=True, )
        parser.add_argument("password", type=str, help="Password must be provided",
                            location=["json"], required=True, )
        parser.add_argument("driver", type=str, help="Fill if you are a driver", location=["json"],
                            required=False)
        parser.add_argument("admin", type=str, help="Fill if you are a driver", location=["json"],
                            required=False)
        args = parser.parse_args()
        response = user.register(username=args["username"], email=args["email"],
                                 password=args["password"], driver=args["driver"], admin=args["admin"])
        return response, 201


class Login(Resource):
    """Contains POST"""
    @user_api.expect(user_login)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="Username must be provided", required=True,
                            location=["json"])
        parser.add_argument("password", type=str, help="Password must be provided", location=["json"],
                            required=True)
        args = parser.parse_args()
        response = user.login(username=args["username"], password=args["password"])
        return response


user_api.add_resource(Users, "/users")
user_api.add_resource(Login, "/users/login")
