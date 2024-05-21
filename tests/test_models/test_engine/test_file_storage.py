#!/usr/bin/python3
'''
Test cases for the FileStorage Class
'''

import json
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFilestorage(unittest.TestCase):
    '''A series of OOP tests for the attributes and methods in the
    FileStorage class'''

    def test_instance(self):
        '''Validates that an instance of FileStorage is created'''
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_filePath(self):
        '''Validates that the __file_path attribute is set'''
        storage = FileStorage()
        self.assertIn("_FileStorage__file_path", dir(FileStorage))
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertIs(type(FileStorage._FileStorage__file_path), str)

    def test_objects(self):
        '''Validates that the __object attribute is set'''
        storage = FileStorage()
        self.assertIn("_FileStorage__objects", dir(FileStorage))
        self.assertIs(type(FileStorage._FileStorage__objects), dict)

    def test_all(self):
        '''Validates the __object attribute is returned'''
        storage = FileStorage()
        self.assertIs(type(storage.all()), dict)

    def test_new(self):
        '''Checks if a new instance is added to storage'''
        baseModel = BaseModel()
        storageModel = FileStorage()
        storage = storageModel.all()
        storageModel.new(baseModel)
        instanceKey = baseModel.__class__.__name__ + "." + baseModel.id
        self.assertIn(instanceKey, storage)

    def test_save(self):
        '''Validates that an instance is saved into a JSON file'''
        baseModel = BaseModel()
        storage = FileStorage()
        baseModel.name = "Gabriel"
        baseModel.number = 52
        baseModelKey = "BaseModel." + baseModel.id
        baseModel.save()

        with open(FileStorage._FileStorage__file_path, "r") as file:
            json_objs = json.load(file)
        self.assertIn(baseModelKey, json_objs.keys())

    def test_reload(self):
        '''Checks that persisted instances are reloaded'''
        baseModel = BaseModel()
        baseModel.save()
        storageModel = FileStorage()
        storageModel.reload()
        storage = storageModel.all()
        instanceKey = baseModel.__class__.__name__ + "." + baseModel.id
        self.assertIn(instanceKey, storage)
