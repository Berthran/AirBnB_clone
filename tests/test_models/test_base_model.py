#!/usr/bin/python3
'''
Test file for the base_model module.
'''


import unittest
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''
    An OOP test for the attributes and methods in the BaseModel class
    '''
    

    def test_instance_created(self):
        '''Validate that an instance of BaseModel is created'''
        model_1 = BaseModel()
        self.assertIsInstance(model_1, BaseModel)

    def test_id(self):
        '''Validate that the id is a str'''
        model_1 = BaseModel()
        self.assertIs(type(model_1.id), str)

    def test_created_at(self):
        '''Validate that the attribute created_at is a datetime object'''
        model_1 = BaseModel()
        self.assertIs(type(model_1.created_at), datetime.datetime)

    def test_updated_at(self):
        '''Validate that the attribute updated_at is a datetime object
        and that it is the same as created_at'''
        model_1 = BaseModel()
        self.assertIs(type(model_1.updated_at), datetime.datetime)
        self.assertEqual(model_1.created_at, model_1.updated_at)

    def test_str(self):
        '''Validate that when printed the object is printed in the right
        format'''
        model_1 = BaseModel()
        obj_str = f"[BaseModel] ({model_1.id}) {model_1.__dict__}"
        self.assertEqual(str(model_1), obj_str)

    def test_save(self):
        '''Validate that the attribute updated_at is updated to current
        time when save() method is called'''
        model_1 = BaseModel()
        time_1 = model_1.updated_at
        model_1.save()
        time_2 = model_1.updated_at
        self.assertNotEqual(time_1, time_2)

    def test_to_dict(self):
        '''Validates the dictionary contains all the required keys and value
        in thier correct data type.'''
        model_1 = BaseModel()
        model_dict = model_1.to_dict()
        # Check that a '__class__' key is present
        self.assertIn('__class__', model_dict.keys())
        # Check that the datetime objects are converted to strings
        self.assertIs(type(model_dict['created_at']), str)
        self.assertIs(type(model_dict['updated_at']), str)




