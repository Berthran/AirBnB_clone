#!/usr/bin/python3
'''
This module handles the storage, serialization and deserialization of instances
in the models package.

Class:
    FileStorage: stores instances to a file, serializes
    instances to a JSON file
    and deserializes a JSON file to instances
'''

import json
from models.reload_tools import createInstanceByClassName
from models.reload_tools import modifyKwargsForInstantiation


class FileStorage():
    '''
    Stores, serializes instances to JSON file and deserializes
    JSON file to instances

    Class attributes:
        file_path: string - path to the JSON file : private class attribute
        objects: a dictionary used to store all instances created
        with the unique key
                 <class_name.id> : private class attribute
    Methods:
        all: returns the <objects> attribute
        new: add new instances to the <objects> attribute
        save: serializes the instances in the <objects> attribute and
        stores them in the JSON file specified in <file_path>
        reload: deserializes the JSON file to dictionary objects, creates
        instances and loads the instances into the <objects>
        attribute (only if the JSON file exists).
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the <objects> attributes'''
        return (FileStorage.__objects)

    def new(self, obj):
        '''Add an instance/object to the <objects> attribute
        with a unique ID'''
        # Create a unique instance id using class name and instance id
        class_name = obj.__class__.__name__
        instance_id = obj.id
        instance_storage_id = class_name + "." + instance_id
        # Add instance to <objects> attribute
        FileStorage.__objects.update({instance_storage_id: obj})

    def save(self):
        '''Serializes the instances in the <objects> attributes
        and stores them to the JSON file'''
        # A container to store the serialized instances
        instance_storage = {}
        for instance_id, instance in FileStorage.__objects.items():
            instance_storage[instance_id] = instance.to_dict()
        # Serializing the instances to JSON string
        instance_storage_in_JSON = json.dumps(instance_storage)
        # Writing the JSON string to file.json
        with open(FileStorage.__file_path, "w") as json_file:
            json_file.write(instance_storage_in_JSON)

    def reload(self):
        '''Deserializes the JSON file, creates instances and loads
        each instance into the <objects> attribute'''
        try:
            # Open file.json only if it exists
            with open(FileStorage.__file_path, "r") as json_file:
                recordOfInstancesInStringFormat = json_file.read()
                recordOfInstancesInDictForm = \
                    json.loads((recordOfInstancesInStringFormat))
                for instanceRecord in recordOfInstancesInDictForm.values():
                    classNameOfInstance = instanceRecord["__class__"]
                    instanceAttributes = \
                        modifyKwargsForInstantiation(**instanceRecord)
                    instance = \
                        createInstanceByClassName(classNameOfInstance,
                                                  **instanceAttributes)
                    # Add instance to <objects> attribute
                    self.new(instance)
        except Exception as e:
            print(e)
