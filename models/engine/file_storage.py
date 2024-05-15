#!/usr/bin/python3
'''
This module handles the serialization and deserialization of instances
in the models package.

Class:
    FileStorage: serializes instances of instances to JSON file
    and deserializes JSON file to instances
'''

import json
from models.base_model import BaseModel
from models.to_inst_attr import to_instantiable_attributes


class FileStorage():
    '''
    Serializes instances of instances to JSON file and deserializes
    JSON file to instances

    Class attributes:
        file_path: string - path to the JSON file (private class attribute)
        objects: a dictionary used to store all objects with the key
                 <class_name.id> (private class attribute)
    Methods:
        all: returns the <objects> attribute
        new: add new instances to the <objects> attribute
        save: serializes the <objects> attribute to the JSON file in <file_path>
        reload: deserializes the JSON file to <objects> if the JSON file exists.
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the <objects> attributes'''
        return (FileStorage.__objects)

    def new(self, obj):
        '''Add an instance/object to the <objects> attribute with a unique ID'''
        # Create a unique instance id using class name and instance id
        class_name = obj.__class__.__name__
        instance_id = obj.id
        instance_storage_id = class_name + "." + instance_id
        # Add instance to <objects> attribute
        FileStorage.__objects.update({instance_storage_id: obj})

    def save(self):
        '''Serializes the <objects> attributes to JSON file'''
        # Convert <object> to JSON string
        instance_storage = {}
        for instance_id, instance in FileStorage.__objects.items():
            instance_storage[instance_id] = instance.to_dict()
        instance_storage_in_JSON = json.dumps(instance_storage)
        # Write the JSON string of <objects> to file.json
        with open(FileStorage.__file_path, "w") as json_file:
            json_file.write(instance_storage_in_JSON)

    def reload(self):
        '''Deserializes the JSON file, creates instance and adds instance to
        <objects>'''
        try:
            # Opening file only if it exists
            with open(FileStorage.__file_path, "r") as json_file:
                # Extracting JSON string from file
                objectsInStringFormat = json_file.read()
                # Deserializing JSON string to dict type
                objectsInDictForm = json.loads((objectsInStringFormat))
                # Creating an instance for each instance data in the file
                for inst_dict in objectsInDictForm.values():
                    # Get the name of the class each instance data belongs to
                    class_name = inst_dict["__class__"]
                    # Modify the data to remove and convert necessary data
                    # suitable for instantiation
                    instance_attributes = \
                            to_instantiable_attributes(**inst_dict)
                    # Create instance based on class name
                    baseModel = BaseModel(**instance_attributes)
                    # Add instance to <objects> attribute
                    self.new(baseModel)
        except Exception:
            pass







