#!/usr/bin/python3
'''
Modifies the attributes (key/value pair) in a dictionary object,
to one that can be used to create an instance of a specified type.

Functions:
    modifyKwargsForInstantiation: takes the attributes and suit them up for instantiation
'''

from models.user import User
from datetime import datetime
from models.base_model import BaseModel


def modifyKwargsForInstantiation(**kwargs):
    '''Modifies the keyword arguments to be able to create an instance with them
    Returns the modified keyword arguments
    '''
    # STEP 1: Removes the "__class__" attribute
    if "__class__" in kwargs.keys():
        kwargs.pop("__class__")
    # STEP 2: Changes the "created_at" attribute from a string format to a datetime format
    if "created_at" in kwargs.keys():
        # Error handling in case the format is already changed to a datetime format before calling this function
        if (type(kwargs['created_at']) is str):
            str_format_of_created_at = kwargs["created_at"]
            datetime_format_of_created_at = \
                    datetime.fromisoformat(str_format_of_created_at)
            kwargs["created_at"] = datetime_format_of_created_at
    # STEP 3: Change the "updated_at" attribute from string format to a datetime format
    if "updated_at" in kwargs.keys():
        # Error handling in case the format is already changed to a datetime format before calling this function
        if (type(kwargs['updated_at']) is str):
            str_format_of_updated_at = kwargs["updated_at"]
            datetime_format_of_updated_at = \
                    datetime.fromisoformat(str_format_of_updated_at)
            kwargs["updated_at"] = datetime_format_of_updated_at
    return (kwargs)


def createInstanceByClassName(classNameOfInstance, **instanceAttributes):
    '''Creates an instance of a class specified by classNameOfInstance'''
    availableInstances = {"BaseModel": BaseModel(**instanceAttributes),
                          "User": User(**instanceAttributes)}
    for className, instance in availableInstances.items():
        if (className == classNameOfInstance):
            return (instance)
