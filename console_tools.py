#!/usr/bin/python3
'''
This module contains some useful functions for the HBNBCommand Class.

It includes utilities for creating an instance, displaying an instance,
destroying an instance, displaying multiple instances and updating instances.

'''

from models import storage
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
    className = classNameArgument.split()[0]
    if (className in nameSpaceOfModule):
        return (True)
    else:
        print("** class doesn't exist **")
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
    else:
        print("** instance id missing **")
        return (False)


def createInstanceKey(classNameAndIdArgument):
    '''Create a key from className and Id'''
    instanceKey = classNameAndIdArgument.replace(" ", ".")
    return (instanceKey)


def getInstanceFromRecord(instanceKey):
    '''Returns instance from the instance record using its className and Id'''
    instanceRecords = storage.all()
    instance = instanceRecords.get(instanceKey)
    return (instance)


def instanceExists(classNameAndIdArgument):
    '''Checks that both classname and id corresponding to an existing
    class instance'''
    instanceKey = createInstanceKey(classNameAndIdArgument)
    instanceRecords = storage.all()
    if (instanceKey in instanceRecords.keys()):
        return (True)
    else:
        print("** no instance found **")
        return (False)


def showInstance(instance):
    '''Prints the string representation of an instance based
    on the class name and id arguments'''
    print(instance)


def removeInstanceFromRecord(instanceKey):
    '''Removes an instance from the instance records'''
    instanceRecords = storage.all()
    instanceRecords.pop(instanceKey)


def saveChangesOnInstanceRecordToJSONFile():
    '''Updates the instance record with latest changes'''
    storage.save()


def createListOfInstances(classNameArgument=""):
    '''Creates a list of all instances  in the instance records or
    just the instances specified by classNameArguments'''
    empty = ''
    instanceRecords = storage.all()
    listOfInstances = []
    if (classNameArgument == empty):
        for instance in instanceRecords.values():
            listOfInstances.append(str(instance))
    else:
        for instanceId, instance in instanceRecords.items():
            className = instanceId.split(".")[0]
            if (className == classNameArgument):
                listOfInstances.append(str(instance))
    return (listOfInstances)


def displayAllInstances():
    '''Displays a list of the string representation of all instances in
    the instance record'''
    listOfInstances = createListOfInstances()
    print(listOfInstances)


def displaySpecificInstances(classNameArgument):
    '''Displays a list of the string representation of the classNameArgument
    instances'''
    listOfInstances = createListOfInstances(classNameArgument)
    print(listOfInstances)
