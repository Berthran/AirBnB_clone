#!/usr/bin/python3
'''
This module handles the serialization and deserialization of instances
in the models package.

Class:
    FileStorage: serializes instances of instances to JSON file
    and deserializes JSON file to instances
'''


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

    __file_path
