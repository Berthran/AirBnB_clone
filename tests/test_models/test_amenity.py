#!/usr/bin/python3
'''
Test cases for the Amenity class
'''

import unittest
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''OOP test for the attributes in the Amenity class'''

    def test_instance(self):
        '''An Amenity instance is created'''
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_inheritedAttributes(self):
        '''Check if the id, created_at and updated_at attributes are set'''
        amenity = Amenity()
        self.assertIn("id", amenity.__dict__.keys())
        self.assertIn("created_at",  amenity.__dict__.keys())
        self.assertIn("updated_at",  amenity.__dict__.keys())
        self.assertIs(type(amenity.id), str)
        self.assertIs(type(amenity.created_at), datetime.datetime)
        self.assertIs(type(amenity.updated_at), datetime.datetime)

    def test_name(self):
        '''Checks for a name attribute set to empty string'''
        amenity = Amenity()
        self.assertIn("name", dir(amenity))
        self.assertEqual(amenity.name, "")
