#!usr/bin/python3
'''
The fundamental representation of objects/instances used in the
entire project.


Classes:
    BaseModel: the base class of all models used in the project.
'''

from datetime import datetime
import uuid

class BaseModel():
    '''A class that defines all common attributes and methods
    for other classes in the AirBnB project.

    Methods:
        save: updates the `updated_at` with the current datetime
        to_dict: returns a dictionary containing all keys/values of __dict__
        of the instance
    '''

    def __init__(self):
        '''Initialize the model.
        Attributes:
            id: unique identification for each instance created
            created_at: the time the instance is created
            updated_at: the time the instance is updated
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        # (To be updated every time object is changed)

    def __str__(self):
        '''A human readable string representation of the object'''
        class_name = self.__class__.__name__
        instance_id = self.id
        class_dict = self.__dict__
        return (f"[{class_name}] ({instance_id}) {class_dict}")

    def save(self):
        '''Updates the public instance attribute `updated_at`with the
        current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        instanceAttributes = self.__dict__
        # Add a __class__ attribute with the class name as it's value
        instanceAttributes['__class__'] = self.__class__.__name__
        # Change the created_at attribute to string format (isoformat)
        if (type(instanceAttributes.get("created_at")) is datetime):
            instanceAttributes['created_at'] = datetime.isoformat(self.created_at)        # Change the updated_at attribute to string format (isoformat)
        if (type(instanceAttributes.get("updated_at")) is datetime):
            instanceAttributes['updated_at'] = datetime.isoformat(self.updated_at)        return (instanceAttributes)
