#!/usr/bin/python3
'''
Test cases for the User class
'''

import unittest
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    '''OOP test for the attributes in the User class'''

    def test_instance(self):
        '''A User instance is created'''
        user_1 = User()
        self.assertIsInstance(user_1, User)

    def test_inheritedAttributes(self):
        '''Check if the id, created_at and updated_at attributes are set'''
        user_1 = User()
        self.assertIn("id", user_1.__dict__.keys())
        self.assertIn("created_at",  user_1.__dict__.keys())
        self.assertIn("updated_at",  user_1.__dict__.keys())
        self.assertIs(type(user_1.id), str)
        self.assertIs(type(user_1.created_at), datetime.datetime)
        self.assertIs(type(user_1.updated_at), datetime.datetime)

    def test_email(self):
        '''Checks for an email attribute set to empty string'''
        user_1 = User()
        self.assertIn("email", dir(user_1))
        self.assertEqual(user_1.email, "")

    def test_password(self):
        '''Checks for a password attribute set to empty string'''
        user_1 = User()
        self.assertIn("password", dir(user_1))
        self.assertEqual(user_1.password, "")

    def test_firstName(self):
        '''Checks for a first_name attribute set to empty string'''
        user_1 = User()
        self.assertIn("first_name", dir(user_1))
        self.assertEqual(user_1.first_name, "")

    def test_lastName(self):
        '''Checks for a last_name attribute set to empty string'''
        user_1 = User()
        self.assertIn("last_name", dir(user_1))
        self.assertEqual(user_1.last_name, "")
