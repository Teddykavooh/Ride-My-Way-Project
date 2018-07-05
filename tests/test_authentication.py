import unittest
import sys  # fix import errors
import os
import json
from tests.base import ConfigTestCase
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Authentication(ConfigTestCase):
    """This class represents authentication test cases"""

    def test_missing_tokens(self):
        """Test API for missing token"""

        """missing driver token"""
        ride = {"driver": "Denno Kindu", "route": "Mlosi - Junction", "time": "7:30pm"}
        response = self.client().put('/api/v2/rides/1', data=json.dumps(ride), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Please Register and Login", str(response.data))

        """missing user token"""
        response = self.client().get('/api/v2/rides/1', content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Please Register and Login", str(response.data))

        """missing admin token"""
        admin_response = self.client().get('api/v2/all_users')
        self.assertEqual(admin_response.status_code, 401)
        self.assertIn("Please Register and Login", str(admin_response.data))

    # def test_invalid_token(self):
    #     """Test API for invalid token"""
    #
    #     ride = {"driver": "Liz Naibor", "route": "Mlosi - Junction", "time": "7:30pm"}
    #     token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
    # eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.\
    #         SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    #     driver_header = {"Content-Type": "application/json", "x-access-token": token}
    #     response_d = self.client().put('/api/v2/rides/1', data=json.dumps(ride), content_type='application/json',
    #                                    headers=driver_header)
    #     self.assertEqual(response_d.status_code, 500)
    #     self.assertIn("Please, provide a valid token in the header", str(response_d.data))
    #
    #     """invalid user token token"""
    #     user_header = {"Content-Type": "application/json", "x-access-token": "qwertyuioasdfghj"}
    #     response_u = self.client().get('/api/v2/rides/1', content_type='application/json', headers=user_header)
    #     self.assertEqual(response_u.status_code, 401)
    #     self.assertIn("Please, provide a valid token in the header", str(response_u.data))
    #
    #     """invalid admin token"""
    #     admin_header = {"Content-Type": "application/json", "x-access-token": "qwertyuioasdfghj"}
    #     response_a = self.client().get('api/v2/all_users', headers=admin_header)
    #     self.assertEqual(response_a.status_code, 401)
    #     self.assertIn("Please, provide a valid token in the header", str(response_a.data))

    def test_wrong_token(self):
        """Test API for wrong token"""
        """Wrong Driver Token"""
        ride = {"driver": "Denno Kindu", "route": "Mlosi - Junction", "time": "7:30pm"}
        response = self.client().put('/api/v2/rides/1', data=json.dumps(ride), content_type='application/json',
                                     headers=self.user_header)
        self.assertEqual(response.status_code, 401)
        self.assertIn("You are not authorized to perform this function", str(response.data))

        """Wrong Admin Token"""
        response_a = self.client().get('api/v2/all_users', headers=self.user_header)
        self.assertEqual(response_a.status_code, 401)
        self.assertIn("You are not authorized to perform this function", str(response_a.data))


if __name__ == '__main__':
    unittest.main()
