#!/usr/bin/python3
'''
Test cases for the City class
'''

import unittest
import datetime
from models.city import City


class TestCity(unittest.TestCase):
    '''OOP test for the attributes in the City class'''

    def test_instance(self):
        '''A City instance is created'''
        city = City()
        self.assertIsInstance(city, City)

    def test_inheritedAttributes(self):
        '''Check if the id, created_at and updated_at attributes are set'''
        city = City()
        self.assertIn("id", city.__dict__.keys())
        self.assertIn("created_at",  city.__dict__.keys())
        self.assertIn("updated_at",  city.__dict__.keys())
        self.assertIs(type(city.id), str)
        self.assertIs(type(city.created_at), datetime.datetime)
        self.assertIs(type(city.updated_at), datetime.datetime)

    def test_stateID(self):
        '''Checks for an state_id attribute set to empty string'''
        city = City()
        self.assertIn("state_id", dir(city))
        self.assertEqual(city.state_id, "")

    def test_ame(self):
        '''Checks for a name attribute set to empty string'''
        city = City()
        self.assertIn("name", dir(city))
        self.assertEqual(city.name, "")
