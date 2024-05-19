#!/usr/bin/python3
'''
This module contains some useful functions for the HBNBCommand Class.

It includes utilities for creating an instance, displaying an instance,
destroying an instance, displaying multiple instances and updating instances.

'''


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

def hasOnlyClassNameArgument(classNameArgument):
    '''Checks that <classNameArgument> has only the class
    name as its argument'''
    noOfArgsInClassNameArgument = len(classNameArgument.split())
    if (noOfArgsInClassNameArgument == 1):
        return (True)
    return (False)

def classExists(classNameArgument):
    '''Returns true if the classNameArgument is an existing class object
    in the module's namespace'''
    nameSpaceOfModule = globals()
    if (classNameArgument in nameSpaceOfModule):
        return (True)
    return (False)

def isValidClassNameArgument(classNameArgument):
    '''Confirms the <classNameArgument> is a valid class name'''
    if (hasOnlyClassNameArgument(classNameArgument)):
        if (classExists(classNameArgument)):
            return (True)
        return (False)
    return (False)


def createClassInstance(classNameArgument):
    '''Creates an instance of the class given by the classNameArgument'''
    availableClasses = {"BaseModel": BaseModel(),
                        "FileStorage": FileStorage()}
    for className, classInstance in availableClasses.items():
        if className == classNameArgument:
            return (classInstance)

def saveClassInstanceToJSONFile(classInstance):
    '''Saves the class instance to a JSON file'''
    classInstance.save()

def hasInstanceId(classNameAndIdArgument):
    '''Checks if the argument has an ID argument'''
    if (len(classNameAndIdArgument.split()) == 2):
        return (True)
    print("** instance id missing **")
    return (False)



