import unittest
import sys  # fix import errors
import os
from tests.base import ConfigTestCase
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class RequestsTests(ConfigTestCase):
    """This class contains Requests Tests """
    def test_request_to_join_a_ride(self):
        """Test for requesting to join a ride"""
        ride = {"passenger_name": "Teddy Antony", "pick_up_station": "Kwa Ndeti", "time": "9:30am"}
        response = self.client().post("/api/v2/rides/1/requests", data=json.dumps(ride),
                                      content_type='application/json', headers=self.user_header)
        self.assertIn("Ride Requested", str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_request_to_join_a_ride_not_in_db(self):
        """Test for requesting to join a ride"""
        ride = {"passenger_name": "Teddy Antony", "pick_up_station": "Kwa Ndeti", "time": "9:30am"}
        response = self.client().post("/api/v2/rides/99/requests", data=json.dumps(ride),
                                      content_type='application/json', headers=self.user_header)
        self.assertIn("Ride does not exist", str(response.data))
        self.assertEqual(response.status_code, 201)

    # def test_response_to_request(self):
    #     """Test for responding to requested ride"""
    #     response_choice = {"response": "Accepted"}
    #     response = self.client().put("/api/v2/rides/3/requests/1", data=json.dumps(response_choice),
    #                                  content_type='application/json', headers=self.driver_header)
    #     self.assertIn("Response to request given", str(response.data))
    #     self.assertEqual(response.status_code, 202)

    def test_wrong_response_to_request(self):
        """Test for requesting to join a ride"""
        response_choice = {"response": "TRUE"}
        response = self.client().put("/api/v2/rides/1/requests/1", data=json.dumps(response_choice),
                                     content_type='application/json', headers=self.driver_header)
        self.assertIn("Response should be either Accepted or Rejected", str(response.data))
        self.assertEqual(response.status_code, 202)


if __name__ == '__main__':
    unittest.main()
