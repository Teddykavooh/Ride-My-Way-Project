from werkzeug.security import generate_password_hash, check_password_hash

request_ride = {}


class Rides:
    """Ride's Functionality"""

    rides = {
        1: {"driver": "Teddy Kavooh", "route": "Vota - Machakos", "time": "5:30am"}
    }

    def get_all_rides(self):
        return self.rides

    def get_a_ride(self, ride_id):
        return self.rides[ride_id]

    def post_a_ride(self, driver, route, time):
        new_id = len(self.rides) + 1
        self.rides[new_id] = {"driver": driver, "route": route, "time": time}
        return {"txt": "Ride Added"}

    def delete_a_ride(self, ride_id):
        del self.rides[ride_id]
        return {"txt": "Ride Deleted"}

    def edit(self, ride_id, driver, route, time):
        self.rides[ride_id] = {"driver": driver, "route": route, "time": time}
        return {"txt": "Ride Edited"}

    def request_to_join_a_ride(self, ride_id, passenger_name, pick_up_station, time):
        self.rides.get(ride_id)
        request_ride[ride_id] = {"passenger_name": passenger_name, "pick_up_station": pick_up_station,
                                 "time": time}
        return {"txt": "Ride Requested"}


# ride = Rides()
# ride.post_a_ride("Mike", "Syoki - Nai", "6:30am")
# print(ride.get_all_rides())
# print(ride.get_a_ride(2))
# print(ride.delete_a_ride(2))
# print(ride.get_all_rides())
# print(ride.edit(2, "Ian", "", ""))
# print(ride.request_to_join_a_ride(2, "Junior Tedd", request=False))


class Users:
    """Users Functionality"""
    users = {"Mueni Kavoo": {"email": "mueni@gmail.com", "password": generate_password_hash("01234"),
                             "driver": False, "admin": True},
             "Mike Mbulwa": {"email": "mike@gmail.com", "password": generate_password_hash("1234"),
                             "driver": True, "admin": False}}

    def get_all_users(self):
        return self.users

    def register(self, username, email, password, driver=False, admin=False):
        hidden = generate_password_hash(password=password)
        self.users[username] = {"email": email, "password": hidden, "driver": driver, "admin": admin}
        return {"txt": "User Registered"}

    def login(self, username, password):
        if username in self.users:
            if check_password_hash(self.users[username]["password"], password=password):
                return {"txt": "Logged In"}
            else:
                return {"txt": "Invalid Password"}
        else:
            return {"txt": "Invalid Username"}

    def delete_a_user(self, username):
        del self.users[username]
        return {"txt": "User Deleted"}


# users_s = Users()
# print(users_s.register("Anton Kavoo", "anton@yahoo.com", "0123", admin=True))
# print(users_s.get_all_users())
# print(users_s.login("Mike Mbulwa", "1234"))
# print(users_s.delete_a_user("Mike Mbulwa"))
# print(users_s.get_all_users())

