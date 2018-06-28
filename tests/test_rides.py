import unittest
import sys  # fix import errors
import os
from tests.base import ConfigTestCase
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class RideTests(ConfigTestCase):
    """This class contains RideTests """
    def test_get_rides(self):
        """We are testing if we can get all rides"""
        response = self.client().get("/api/v1/rides")
        self.assertEqual(response.status_code, 200)

    def test_get_a_ride(self):
        """Test for getting a ride"""
        response = self.client().get("/api/v1/rides/1")
        self.assertEqual(response.status_code, 200)

    def test_post_a_ride(self):
        """Test for adding a ride"""
        ride = {"driver": "Denno Kindu", "route": "Mlosi - Junction", "time": "7:30pm"}
        response = self.client().post("/api/v1/rides", data=json.dumps(ride), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_a_ride_missing_route(self):
        """Test API response to missing route"""
        ride = {"driver": "Denno Kindu", "time": "7:30pm"}
        response = self.client().post("/api/v1/rides", data=json.dumps(ride), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_edit(self):
        """Test API can edit rides"""
        ride = {"driver": "Denno Kindu", "route": "Mlosi - Junction", "time": "7:30pm"}
        response = self.client().put("/api/v1/rides/2", data=json.dumps(ride), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_a_ride(self):
        """Test for deleting a ride"""
        response = self.client().delete("/api/v1/rides/2")
        self.assertEqual(response.status_code, 200)

    def test_request_to_join_a_ride(self):
        """Test for requesting to join a ride"""
        ride = {"passenger_name": "Teddy Antony", "pick_up_station": "Kwa Ndeti", "time": "9:30am"}
        response = self.client().post("/api/v1/rides/1/requests", data=json.dumps(ride),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
