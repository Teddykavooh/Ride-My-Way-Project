from flask_restplus import Resource, Namespace, reqparse, fields
from app.models import Rides

rides = Rides()

ride_api = Namespace("Rides", description="All Rides Endpoints")
ride_offer = ride_api.model("Offer A Ride", {"driver": fields.String,
                                             "route": fields.String,
                                             "time": fields.String})

ride_request = ride_api.model("Request To Join A Ride", {"passenger_name": fields.String,
                                                         "pick_up_station": fields.String,
                                                         "time": fields.String})


class Rides(Resource):
    """Contains GET and POST"""
    def get(self):
        response = rides.get_all_rides()
        return response

    @ride_api.expect(ride_offer)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("driver", type=str, help="Driver must be provided", required=True,
                            location=["json"])
        parser.add_argument("route", type=str, help="Route must be provided", location=["json"],
                            required=True,)
        parser.add_argument("time", type=str, help="Time must be provided", location=["json"],
                            required=True,)
        args = parser.parse_args()
        response = rides.post_a_ride(driver=args["driver"], route=args["route"], time=args["time"])
        return response, 201


class Ride(Resource):
    def get(self, ride_id):
        response = rides.get_a_ride(ride_id=ride_id)
        return response

    @ride_api.expect(ride_offer)
    def put(self, ride_id):
        parser = reqparse.RequestParser()
        parser.add_argument("driver", type=str, help="Driver must be provided", location=["json"],
                            required=True)
        parser.add_argument("route", type=str, help="Route must be provided", location=["json"],
                            required=True)
        parser.add_argument("time", type=str, help="Time must be provided", location=["json"],
                            required=True)
        args = parser.parse_args()
        response = rides.edit(ride_id=ride_id, driver=args["driver"], route=args["route"],
                              time=args["time"])
        return response

    def delete(self, ride_id):
        response = rides.delete_a_ride(ride_id=ride_id)
        return response


class Request(Resource):
    """Contains POST for user ride requests"""

    @ride_api.expect(ride_request)
    def post(self, ride_id):
        parser = reqparse.RequestParser()
        parser.add_argument("passenger_name", type=str, help="Your name must be provided.",
                            location=["json"], required=True)
        parser.add_argument("pick_up_station", type=str, help="Your pick up station must be provided.",
                            location=["json"], required=True)
        parser.add_argument("time", type=str, help="Your time must be provided.",
                            location=["json"], required=True)
        args = parser.parse_args()
        response = rides.request_to_join_a_ride(ride_id=ride_id, passenger_name=args["passenger_name"],
                                                pick_up_station=args["pick_up_station"],
                                                time=args["time"])
        return response


ride_api.add_resource(Rides, "/rides")
ride_api.add_resource(Ride, "/rides/<int:ride_id>")
ride_api.add_resource(Request, "/rides/<int:ride_id>/requests")
