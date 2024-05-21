#!/usr/bin/python3
'''
Test cases for the Review class
'''

import unittest
import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    '''OOP test for the attributes in the Review class'''

    def test_instance(self):
        '''A Review instance is created'''
        review = Review()
        self.assertIsInstance(review, Review)

    def test_inheritedAttributes(self):
        '''Check if the id, created_at and updated_at attributes are set'''
        review = Review()
        self.assertIn("id", review.__dict__.keys())
        self.assertIn("created_at",  review.__dict__.keys())
        self.assertIn("updated_at",  review.__dict__.keys())
        self.assertIs(type(review.id), str)
        self.assertIs(type(review.created_at), datetime.datetime)
        self.assertIs(type(review.updated_at), datetime.datetime)

    def test_placeId(self):
        '''Checks for a place_id attribute set to empty string'''
        review = Review()
        self.assertIn("place_id", dir(review))
        self.assertEqual(review.place_id, "")

    def test_userId(self):
        '''Checks for a user_id attribute set to empty string'''
        review = Review()
        self.assertIn("user_id", dir(review))
        self.assertEqual(review.user_id, "")

    def test_text(self):
        '''Checks for a name attribute set to empty string'''
        review = Review()
        self.assertIn("text", dir(review))
        self.assertEqual(review.text, "")
