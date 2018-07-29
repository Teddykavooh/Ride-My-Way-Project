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
        response = self.client().get("/api/v2/all_users", headers=self.admin_header)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        """We are testing user registration"""
        user = {"username": "Mutisya Luke", "email": "mutisya@gmail.com", "password": "5678", "driver": "TRUE",
                "admin": "TRUE"}
        response = self.client().post("/api/v2/users", data=json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_register_without_username(self):
        """We are testing user registration"""
        user = {"username": "", "email": "mutisya@gmail.com", "password": "5678", "driver": "TRUE", "admin": "TRUE"}
        response = self.client().post("/api/v2/users", data=json.dumps(user), content_type='application/json')
        self.assertIn("Username must be filled", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_register_without_email(self):
        """We are testing user registration"""
        user = {"username": "Mutisya Luke", "email": "", "password": "5678", "driver": "TRUE", "admin": "TRUE"}
        response = self.client().post("/api/v2/users", data=json.dumps(user), content_type='application/json')
        self.assertIn("E-Mail must be filled", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_register_without_password(self):
        """We are testing user registration"""
        user = {"username": "Mutisya Luke", "email": "mutisya@gmail.com", "password": "", "driver": "TRUE",
                "admin": "TRUE"}
        response = self.client().post("/api/v2/users", data=json.dumps(user), content_type='application/json')
        self.assertIn("Password must be filled", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_register_without_driver(self):
        """We are testing user registration"""
        user = {"username": "Mutisya Luke", "email": "mutisya@gmail.com", "password": "5678", "driver": "",
                "admin": "TRUE"}
        response = self.client().post("/api/v2/users", data=json.dumps(user), content_type='application/json')
        self.assertIn("Driver must be filled", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_register_with_wrong_driver(self):
        """We are testing user registration"""
        user = {"username": "Mutisya Luke", "email": "mutisya@gmail.com", "password": "5678", "driver": "45",
                "admin": "TRUE"}
        response = self.client().post("/api/v2/users", data=json.dumps(user), content_type='application/json')
        self.assertIn("Driver must either be True or False", str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_already_register(self):
        """We are testing user registration occured"""
        user = {"username": "Elneny Mohah", "email": "mohah@gmail.com", "password": "5678", "driver": "True",
                "admin": True}
        response = self.client().post("/api/v2/users", data=json.dumps(user), content_type='application/json')
        self.assertIn("User cannot be registered due to unique similarities", str(response.data))
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
        response = self.client().delete("/api/v2/users/3", headers=self.admin_header)
        self.assertEqual(response.status_code, 202)

    def test_delete_non_existence_user(self):
        """We are testing response to deleting user not in database"""
        response = self.client().delete("/api/v2/users/99", headers=self.admin_header)
        self.assertIn("User Not Available", str(response.data))
        self.assertEqual(response.status_code, 202)


if __name__ == '__main__':
    unittest.main()
