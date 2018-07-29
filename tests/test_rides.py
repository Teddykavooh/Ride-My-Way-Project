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

    def test_get_a_ride_not_in_db(self):
        """Test for getting a ride"""
        response = self.client().get("/api/v2/rides/99", headers=self.user_header)
        self.assertIn("Ride not available", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_post_a_ride(self):
        """Test for adding a ride"""
        ride = {"driver": "Denno Kindu", "route": "Mlosi - Junction", "time": "7:30pm"}
        response = self.client().post("/api/v2/rides", data=json.dumps(ride), content_type='application/json',
                                      headers=self.driver_header)
        self.assertIn("Ride Added", str(response.data))
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
        response = self.client().put("/api/v2/rides/1", data=json.dumps(ride), content_type='application/json',
                                     headers=self.driver_header)
        self.assertIn("Ride Edited", str(response.data))
        self.assertEqual(response.status_code, 202)

    def test_edit_ride_not_in_db(self):
        """Test API can edit rides"""
        ride = {"driver": "Denno Kindu", "route": "Mlosi - Junction", "time": "7:30pm"}
        response = self.client().put("/api/v2/rides/99", data=json.dumps(ride), content_type='application/json',
                                     headers=self.driver_header)
        self.assertIn("Ride not available", str(response.data))
        self.assertEqual(response.status_code, 202)

    def test_delete_a_ride(self):
        """Test for deleting a ride"""
        response = self.client().delete("/api/v2/rides/2", headers=self.driver_header)
        self.assertIn("Ride Deleted", str(response.data))
        self.assertEqual(response.status_code, 202)

    def test_delete_a_ride_not_in_db(self):
        """Test for deleting a ride"""
        response = self.client().delete("/api/v2/rides/99", headers=self.driver_header)
        self.assertIn("Ride not available", str(response.data))
        self.assertEqual(response.status_code, 202)


if __name__ == '__main__':
    unittest.main()
