#!/usr/bin/python3
'''
This module contains some useful functions for the HBNBCommand Class.

It includes utilities for creating an instance, displaying an instance,
destroying an instance, displaying multiple instances and updating instances.

'''


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

def isValidClassNameArgument(classNameArgument):
    '''Checks the argument(s) in classNameArgument'''
    noOfArgsInClassNameArgument = len(classNameArgument.split())
    nameSpaceOfModule = globals()
    if (noOfArgsInClassNameArgument != 1):
        return (0)
    if (classNameArgument not in nameSpaceOfModule):
        return (0)
    return (1)

def getAndCreateClassInstance(classNameArgument):
    '''Retrieves the class object from the class name and
    creates an instance of the class'''
    availableClasses = {"BaseModel": BaseModel(),
                        "FileStorage": FileStorage()}
    for className, classInstance in availableClasses.items():
        if className == classNameArgument:
            return (classInstance)

def saveClassInstanceToJSONFile(classInstance):
    '''Saves the class instance to a JSON file and prints its id'''
    classInstance.save()
    print(classInstance.id)
