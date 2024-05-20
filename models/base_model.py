#!usr/bin/python3
'''
The fundamental representation of objects/instances used in the
entire project.


Classes:
    BaseModel: the base class of all models used in the AirBnB project.
'''

import uuid
import models
from models import reload_tools
from datetime import datetime


class BaseModel():
    '''A class that defines all common attributes and methods
    for other classes in the AirBnB project.

    Methods:
        save: updates the `updated_at` instance attribute with the current
                datetime
        to_dict: returns a dictionary containing all keys/values of the
                __dict__ attribute of the instance
    '''

    def __init__(self, *args, **kwargs):
        '''Initializes the model.

        Attributes:
            id: unique identification for each instance created
            created_at: the time the instance was created
            updated_at: the time the instance was updated
        '''

        numberOfItemsInKwargs = len(kwargs.items())

        if (numberOfItemsInKwargs == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at  # (To be updated every time an
            # instance is saved)
            # Add the instance to a storage for instances
            models.storage.new(self)
        else:
            kwargsForInstantiation = \
                    reload_tools.modifyKwargsForInstantiation(**kwargs)
            # Initialize instance with the modified attributes in kwargs
            for attribute, value in kwargsForInstantiation.items():
                # Add the attributes and their values to the __dict__
                # attribute of the instance here by instantiating it
                self.__dict__[attribute] = value

    def __str__(self):
        '''
        Displays a human-readable string representation of the
        BaseModel instance
        '''
        className = self.__class__.__name__
        instanceId = self.id
        instanceAttributes = self.__dict__
        return (f"[{className}] ({instanceId}) {instanceAttributes}")

    def save(self):
        ''' Updates the public instance attribute `updated_at` with the
        current date and time and stores the instance to a file'''
        self.updated_at = datetime.now()
        # Call function to store/persist instance to a file
        models.storage.save()

    def to_dict(self):
        ''' Creates a modified dictionary object of the instance attributes
        suitable for storing to a file'''
        # Prevents changes to __dict__ object
        instanceAttributes = self.__dict__.copy()
        # Add a __class__ attribute to the instance attributes,
        # with the class name as it's value
        instanceAttributes['__class__'] = self.__class__.__name__
        # Change the created_at attribute to string format (isoformat)
        if (type(instanceAttributes.get("created_at")) is datetime):
            instanceAttributes['created_at'] = \
                    datetime.isoformat(self.created_at)
        # Change the updated_at attribute to string format (isoformat)
        if (type(instanceAttributes.get("updated_at")) is datetime):
            instanceAttributes['updated_at'] = \
                    datetime.isoformat(self.updated_at)
        return (instanceAttributes)
