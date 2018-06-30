from flask_restplus import Resource, Namespace
from app.models import Users
# from resources.authentication import admin_required

user = Users()
user_api = Namespace("Admin", description="All Admin Endpoints")


class Users1 (Resource):
    """Contains GET"""
    @user_api.doc(security='apikey')
    # @admin_required
    def get(self):
        response = user.get_all_users()
        return response, 200


class Users2(Resource):
    """Contains DELETE"""
    @user_api.doc(security='apikey')
    # @admin_required
    def delete(self, user_id):
        response = user.delete_a_user(user_id=user_id)
        return response


user_api.add_resource(Users1, "/all_users")
user_api.add_resource(Users2, "/users/<int:user_id>")
