#!/usr/bin/python3
'''
Test file for the base_model module.
'''


import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    '''
    An OOP test for the attributes and methods in the BaseModel class
    '''

    def test_instance_created(self):
        '''Validate that an instance of BaseModel is created'''
        model_1 = BaseModel()
        self.assertIsInstance(model_1, BaseModel)

    def test_instance_created_with_kwargs(self):
        '''Validate that an instance of BaseModel is created
        from a key value pair'''
        model_1 = BaseModel()
        model_1_attributes = model_1.to_dict()
        model_2 = BaseModel(**model_1_attributes)
        self.assertIn("id", model_2.__dict__.keys())
        self.assertIn("created_at", model_2.__dict__.keys())
        self.assertIn("updated_at", model_2.__dict__.keys())

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
        model_2 = FileStorage()
        time_1 = model_1.updated_at
        model_1.save()
        time_2 = model_1.updated_at
        self.assertNotEqual(time_1, time_2)
        instanceKey = model_1.__class__.__name__ + "." + model_1.id
        self.assertIn(instanceKey, model_2.all().keys())

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

    def test_all(self):
        '''Validates the __object attribute is returned'''
        model_2 = FileStorage()
        self.assertIs(type(model_2.all()), dict)

    def test_new(self):
        '''Checks if a new instance is added to storage'''
        baseModel = BaseModel()
        storageModel = FileStorage()
        storage = storageModel.all()
        storageModel.new(baseModel)
        instanceKey = baseModel.__class__.__name__ + "." + baseModel.id
        self.assertIn(instanceKey, storage)

    def test_reload(self):
        '''Checks that persisted instances are reloaded'''
        baseModel = BaseModel()
        baseModel.save()
        storageModel = FileStorage()
        storageModel.reload()
        storage = storageModel.all()
        instanceKey = baseModel.__class__.__name__ + "." + baseModel.id
        self.assertIn(instanceKey, storage)
