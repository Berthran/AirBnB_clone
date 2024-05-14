#!/usr/bin/python3
'''
Modifies the attributes of an instance stored in a dictionary object,
to one that can be used to create an instance of the object.
'''


from datetime import datetime


def to_instantiable_attributes(**kwargs):
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
