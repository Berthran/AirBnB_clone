#!usr/bin/python3
'''
The fundamental representation of objects/instances used in the
entire project.


Classes:
    BaseModel: the base class of all models used in the AirBnB project.
'''

import uuid
import models
from datetime import datetime


class BaseModel():
    '''A class that defines all common attributes and methods
    for other classes in the AirBnB project.

    Methods:
        save: updates the `updated_at` with the current datetime
        to_dict: returns a dictionary containing all keys/values of __dict__
        of the instance
    '''

    def __init__(self, *args, **kwargs):
        '''Initialize the model.
        Attributes:
            id: unique identification for each instance created
            created_at: the time the instance is created
            updated_at: the time the instance is updated
        '''

        numberOfItemsInKwargs = len(kwargs.items())
        
        if (numberOfItemsInKwargs == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at # (To be updated every time an
            # instance is saved)
            models.storage.new(self)
        else:
            kwargs = self.to_instantiable_attributes(**kwargs)
            # Initialize instance with the modified attributes in kwargs
            for attribute, value in kwargs.items():
                self.__dict__[attribute] = value


    def __str__(self):
        '''Displays a human readable string representation of the object'''
        className = self.__class__.__name__
        instanceId = self.id
        instanceAttributes = self.__dict__
        return (f"[{className}] ({instanceId}) {instanceAttributes}")

    def save(self):
        '''Updates the public instance attribute `updated_at`with the
        current datetime'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Creates a modified dictionary object of the instance attributes'''
        instanceAttributes = self.__dict__.copy() # Prevents changes to __dict__ object
        # Add a __class__ attribute with the class name as it's value
        instanceAttributes['__class__'] = self.__class__.__name__
        # Change the created_at attribute to string format (isoformat)
        if (type(instanceAttributes.get("created_at")) is datetime):
            instanceAttributes['created_at'] = datetime.isoformat(self.created_at)
        # Change the updated_at attribute to string format (isoformat)
        if (type(instanceAttributes.get("updated_at")) is datetime):
            instanceAttributes['updated_at'] = datetime.isoformat(self.updated_at)
        return (instanceAttributes)

    def to_instantiable_attributes(self, **kwargs):
        '''Modifies the kwargs to be able create an instance'''
        # Remove the "__class__" attribute
        if "__class__" in kwargs.keys():
            kwargs.pop("__class__")
        # Change "created_at" attribute from string format to datetime
        if "created_at" in kwargs.keys():
            str_format_of_created_at = kwargs["created_at"]
            datetime_format_of_created_at = \
                    datetime.fromisoformat(str_format_of_created_at)
            kwargs["created_at"] = datetime_format_of_created_at
        # Change "updated_at" attribute from string format to datetime
        if "updated_at" in kwargs.keys():
            str_format_of_updated_at = kwargs["updated_at"]
            datetime_format_of_updated_at = \
                    datetime.fromisoformat(str_format_of_updated_at)
            kwargs["updated_at"] = datetime_format_of_updated_at
        return (kwargs)
