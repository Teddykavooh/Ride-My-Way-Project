import unittest
import sys  # fix import errors
import os
import json
from tests.base import ConfigTestCase
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Authentication(ConfigTestCase):
    """This class represents authentication test cases"""

    def test_missing_d_tokens(self):
        """Test API for missing token"""

        """missing driver token"""
        ride = {"driver": "Denno Kindu", "route": "Mlosi - Junction", "time": "7:30pm"}
        response = self.client().put('/api/v2/rides/1', data=json.dumps(ride), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Please Register and Login", str(response.data))

    def test_missing_u_tokens(self):
        """missing user token"""
        response = self.client().get('/api/v2/rides/1', content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Please Register and Login", str(response.data))

    def test_missing_a_tokens(self):
        """missing admin token"""
        admin_response = self.client().get('api/v2/all_users')
        self.assertEqual(admin_response.status_code, 401)
        self.assertIn("Please Register and Login", str(admin_response.data))

    def test_wrong_d_token(self):
        """Test API for wrong token"""
        """Wrong Driver Token"""
        ride = {"driver": "Denno Kindu", "route": "Mlosi - Junction", "time": "7:30pm"}
        response = self.client().put('/api/v2/rides/1', data=json.dumps(ride), content_type='application/json',
                                     headers=self.user_header)
        self.assertEqual(response.status_code, 401)
        self.assertIn("You are not authorized to perform this function", str(response.data))

    def test_wrong_a_token(self):
        """Wrong Admin Token"""
        response_a = self.client().get('api/v2/all_users', headers=self.user_header)
        self.assertEqual(response_a.status_code, 401)
        self.assertIn("You are not authorized to perform this function", str(response_a.data))


if __name__ == '__main__':
    unittest.main()
