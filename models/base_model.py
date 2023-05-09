#!/usr/bin/python3
'''This module contains a base class that defines all common attributes/methods for other classes.

This class is to be used to create sub-classes for the models package.

Class:
    BaseModel
    
Typical Usage:
    class MyClass(BaseModel):
        pass

Attributes: None
'''
import uuid
from datetime import datetime

class BaseModel():
    '''Defines the base attributes and methods for sub-classes'''
     
    def __init__(self, **kwargs):
         '''Initialise the base class'''
         self.id = str(uuid.uuid4()) # Generates a unique identifier for each base object
         self.created_at = datetime.now() # Assign current value of datetime
         self.updated_at = datetime.now() # Assign current value of datetime
         
    def __str__(self):
        '''Displays a string representation of a base object'''
        return (f"{[self.__class__.__name__]} "
                f"{(self.id)} {(self.__dict__)}")
        
    def save(self):
        '''Updates "updated_at" every time the object is changed'''
        self.updated_at = datetime.now()
    
    def to_json(self):
        '''Creates a dictionary representation of the a base object.
        This method is the first piece of the serialization/deserialization process.
        '''
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__.update({"__class__": self.__class__.__name__})
        return (self.__dict__)
         

