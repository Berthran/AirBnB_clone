#!/usr/bin/python3
'''
Test cases for the Place class
'''

import unittest
import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    '''OOP test for the attributes in the Place class'''

    def test_instance(self):
        '''A Place instance is created'''
        place = Place()
        self.assertIsInstance(place, Place)

    def test_inheritedAttributes(self):
        '''Check if the id, created_at and updated_at attributes are set'''
        place = Place()
        self.assertIn("id", place.__dict__.keys())
        self.assertIn("created_at",  place.__dict__.keys())
        self.assertIn("updated_at",  place.__dict__.keys())
        self.assertIs(type(place.id), str)
        self.assertIs(type(place.created_at), datetime.datetime)
        self.assertIs(type(place.updated_at), datetime.datetime)

    def test_cityId(self):
        '''Checks for city_id attribute set to empty string'''
        place = Place()
        self.assertIn("city_id", dir(place))
        self.assertEqual(place.city_id, "")

    def test_userId(self):
        '''Checks for a user_id attribute set to empty string'''
        place = Place()
        self.assertIn("user_id", dir(place))
        self.assertEqual(place.user_id, "")

    def test_name(self):
        '''Checks for a name attribute set to empty string'''
        place = Place()
        self.assertIn("name", dir(place))
        self.assertEqual(place.name, "")

    def test_description(self):
        '''Checks for a description attribute set to empty string'''
        place = Place()
        self.assertIn("description", dir(place))
        self.assertEqual(place.description, "")

    def test_numberRooms(self):
        '''Checks for a number_rooms attribute set to zero'''
        place = Place()
        self.assertIn("number_rooms", dir(place))
        self.assertEqual(place.number_rooms, 0)

    def test_numberBathrooms(self):
        '''Checks for a number_bathrooms attribute set to zero'''
        place = Place()
        self.assertIn("number_bathrooms", dir(place))
        self.assertEqual(place.number_bathrooms, 0)

    def test_maxGuest(self):
        '''Checks for a max_guest attribute set to zero'''
        place = Place()
        self.assertIn("max_guest", dir(place))
        self.assertEqual(place.max_guest, 0)

    def test_priceByNight(self):
        '''Checks for a price_by_night attribute set to zero'''
        place = Place()
        self.assertIn("price_by_night", dir(place))
        self.assertEqual(place.price_by_night, 0)

    def test_latitude(self):
        '''Checks for a latitude attribute set to 0.0'''
        place = Place()
        self.assertIn("latitude", dir(place))
        self.assertEqual(place.latitude, 0.0)

    def test_longitude(self):
        '''Checks for a longitude attribute set to 0.0'''
        place = Place()
        self.assertIn("longitude", dir(place))
        self.assertEqual(place.longitude, 0.0)
    
    def test_amenityIds(self):
        '''Checks for a amenity_ids attribute set to empty string'''
        place = Place()
        self.assertIn("amenity_ids", dir(place))
        self.assertEqual(place.amenity_ids, [])


