import unittest
import sys  # fix import errors
import os
from tests.base import ConfigTestCase
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class UserTests(ConfigTestCase):
    """This class contains UserTests """
    def test_get_all_users(self):
        """We are testing if we can get all users"""
        response = self.client().get("/api/v2/all_users")
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        """We are testing user registration"""
        user = {"username": "Mutisya Luke", "email": "mutisya@gmail.com", "password": "5678", "driver": False,
                "admin": False}
        response = self.client().post("/api/v2/users", data=json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        """We are testing user login"""
        user = {"username": "Mutisya Luke", "password": "5678"}
        response = self.client().post("/api/v2/users/login", data=json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_invalid_username(self):
        """We are testing response to invalid username"""
        user = {"username": "Mue Kavoo", "password": "5678"}
        response = self.client().post("/api/v2/users/login", data=json.dumps(user), content_type='application/json')
        self.assertIn("Invalid Username", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_invalid_password(self):
        """We are testing response to invalid username"""
        user = {"username": "Elneny Mohah", "password": "34"}
        response = self.client().post("/api/v2/users/login", data=json.dumps(user), content_type='application/json')
        self.assertIn("Invalid Password", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_delete_a_user(self):
        """Test for deleting a user"""
        response = self.client().delete("/api/v2/users/3")
        self.assertEqual(response.status_code, 202)


if __name__ == '__main__':
    unittest.main()
