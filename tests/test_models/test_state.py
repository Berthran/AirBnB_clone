#!/usr/bin/python3
'''
Test cases for the State class
'''

import unittest
import datetime
from models.state import State


class TestState(unittest.TestCase):
    '''OOP test for the attributes in the State class'''

    def test_instance(self):
        '''A State instance is created'''
        state_1 = State()
        self.assertIsInstance(state_1, State)

    def test_inheritedAttributes(self):
        '''Check if the id, created_at and updated_at attributes are set'''
        state_1 = State()
        self.assertIn("id", state_1.__dict__.keys())
        self.assertIn("created_at",  state_1.__dict__.keys())
        self.assertIn("updated_at",  state_1.__dict__.keys())
        self.assertIs(type(state_1.id), str)
        self.assertIs(type(state_1.created_at), datetime.datetime)
        self.assertIs(type(state_1.updated_at), datetime.datetime)

    def test_name(self):
        '''Checks for a name attribute set to empty string'''
        state_1 = State()
        self.assertIn("name", dir(state_1))
        self.assertEqual(state_1.name, "")
