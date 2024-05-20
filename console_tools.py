#!/usr/bin/python3
'''
This module contains some useful functions for the HBNBCommand Class.

It includes utilities for creating an instance, displaying an instance,
destroying an instance, displaying multiple instances and updating instances.

'''

import re
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def processClassNameIdArgumentToGetInstanceKey(classNameAndIdArgument):
    '''Process the classNameAndIdArgument'''
    empty = ""
    if classNameAndIdArgument == empty:
        print("** class name missing **")
        return (None)
    else:
        check = classExists(classNameAndIdArgument)
        if (check is True):
            check = hasInstanceId(classNameAndIdArgument)
            if (check is True):
                check = instanceExists(classNameAndIdArgument)
                if (check is True):
                    instanceKey = createInstanceKey(classNameAndIdArgument)
                    return (instanceKey)
                return (None)
            return (None)
        return (None)


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


def hasInstanceId(classNameAndIdArgument):
    '''Checks if the argument has an ID argument'''
    if (len(classNameAndIdArgument.split()) == 2):
        return (True)
    else:
        print("** instance id missing **")
        return (False)


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


def createInstanceKey(classNameAndIdArgument):
    '''Create a key from className and Id'''
    instanceKey = classNameAndIdArgument.replace(" ", ".")
    return (instanceKey)


# do_create() function tools
# ==========================

def createClassInstance(classNameArgument):
    '''Creates an instance of the class given by the classNameArgument'''
    availableClasses = {"BaseModel": BaseModel(),
                        "FileStorage": FileStorage(),
                        "User": User()}
    for className, classInstance in availableClasses.items():
        if className == classNameArgument:
            return (classInstance)


def saveClassInstanceToJSONFile(classInstance):
    '''Saves the class instance to a JSON file'''
    classInstance.save()


# do_show() function tools
# ========================

def getInstanceFromRecord(instanceKey):
    '''Returns instance from the instance record using its className and Id'''
    instanceRecords = storage.all()
    instance = instanceRecords.get(instanceKey)
    return (instance)


def showInstance(instance):
    '''Prints the string representation of an instance based
    on the class name and id arguments'''
    print(instance)


# do_destroy() function tools
# ===========================

def removeInstanceFromRecord(instanceKey):
    '''Removes an instance from the instance records'''
    instanceRecords = storage.all()
    instanceRecords.pop(instanceKey)


def saveChangesOnInstanceRecordToJSONFile():
    '''Updates the instance record with latest changes'''
    storage.save()


# do_show() function tools
# ========================

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


# do_all() function tools
# =======================

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


# do_update() function tools
# ==========================

def hasAttributeName(classNameIdAttributesArgument):
    '''Checks if the given argument has an attribute name'''
    numberOfArguments = len(classNameIdAttributesArgument.split())
    if (numberOfArguments < 3):
        print("** attribute name missing **")
        return (False)
    return (True)


def hasAttributeValue(classNameIdAttributesArgument):
    '''Checks if the given argument has an attribute value'''
    numberOfArguments = len(classNameIdAttributesArgument.split())
    if (numberOfArguments < 4):
        print("** value missing **")
        return (False)
    return (True)


def convertAttributeValueToRightType(attributeValue):
    '''Checks the pattern of the attribute value and convert
    to the right type'''
    int_pattern = re.compile(r'^\d+$')
    float_pattern = re.compile(r'^\d+\.\d+$')
    str_pattern = re.compile(r'^".*"$')
    if (int_pattern.match(attributeValue)):
        attributeValue = int(attributeValue)
    elif (float_pattern.match(attributeValue)):
        attributeValue = float(attributeValue)
    elif (str_pattern.match(attributeValue)):
        attributeValue = attributeValue.strip("\"")
    return (attributeValue)


def updateInstanceWithAttributeAndValue(classNameIdAttributesArgument):
    '''Updates or assign a new attribute to the instance'''
    className, instanceId, attributeName, attributeValue = \
        classNameIdAttributesArgument.split()[:4]
    instanceKey = className + "." + instanceId
    instance = getInstanceFromRecord(instanceKey)
    attributeValue = convertAttributeValueToRightType(attributeValue)
    instance.__dict__.update({attributeName: attributeValue})

    saveClassInstanceToJSONFile(instance)
