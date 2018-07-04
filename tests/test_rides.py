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
        response = self.client().get("/api/v2/rides")
        self.assertEqual(response.status_code, 200)

    def test_get_a_ride(self):
        """Test for getting a ride"""
        response = self.client().get("/api/v2/rides/1", headers=self.user_header)
        self.assertEqual(response.status_code, 200)

    def test_post_a_ride(self):
        """Test for adding a ride"""
        ride = {"driver": "Denno Kindu", "route": "Mlosi - Junction", "time": "7:30pm"}
        response = self.client().post("/api/v2/rides", data=json.dumps(ride), content_type='application/json',
                                      headers=self.driver_header)
        self.assertEqual(response.status_code, 201)

    def test_post_a_ride_missing_route(self):
        """Test API response to missing route"""
        ride = {"driver": "Denno Kindu", "time": "7:30pm"}
        response = self.client().post("/api/v2/rides", data=json.dumps(ride), content_type='application/json',
                                      headers=self.driver_header)
        self.assertEqual(response.status_code, 400)

    def test_edit(self):
        """Test API can edit rides"""
        ride = {"driver": "Denno Kindu", "route": "Mlosi - Junction", "time": "7:30pm"}
        response = self.client().put("/api/v2/rides/3", data=json.dumps(ride), content_type='application/json',
                                     headers=self.driver_header)
        self.assertEqual(response.status_code, 202)

    def test_delete_a_ride(self):
        """Test for deleting a ride"""
        response = self.client().delete("/api/v2/rides/2", headers=self.driver_header)
        self.assertEqual(response.status_code, 202)

    def test_request_to_join_a_ride(self):
        """Test for requesting to join a ride"""
        ride = {"passenger_name": "Teddy Antony", "pick_up_station": "Kwa Ndeti", "time": "9:30am"}
        response = self.client().post("/api/v2/rides/2/requests", data=json.dumps(ride),
                                      content_type='application/json', headers=self.user_header)
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
