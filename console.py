#!/usr/bin/python3
'''
A command line interpreter for manipulating objects/instances.
'''

import cmd
import uuid
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from console_tools import classExists, isValidClassNameArgument
from console_tools import createClassInstance, saveClassInstanceToJSONFile
from console_tools import hasInstanceId, instanceExists, createInstanceKey
from console_tools import getInstanceFromRecord, showInstance
from console_tools import removeInstanceFromRecord
from console_tools import saveChangesOnInstanceRecordToJSONFile
from console_tools import displayAllInstances, displaySpecificInstances
from console_tools import processClassNameIdArgumentToGetInstanceKey
from console_tools import updateInstanceWithAttributeAndValue
from console_tools import hasAttributeValue, hasAttributeName


class HBNBCommand(cmd.Cmd):
    '''
    Instance of a cmd session
    '''

    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Terminate the cmd session'''
        quit()

    def do_EOF(self, arg):
        '''Terminates the cmd session'''
        quit()

    def do_help(self, arg):
        '''Provide bried description of available commands'''
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        '''Handle empty line commands'''
        pass

    def do_create(self, classNameArgument):
        '''Creates a new instance of the class name argument
        and saves it to a JSON file'''
        empty = ""
        if classNameArgument == empty:
            print("** class name missing **")
        else:
            check = isValidClassNameArgument(classNameArgument)
            if (check is True):
                newClassInstance = createClassInstance(classNameArgument)
                saveClassInstanceToJSONFile(newClassInstance)
                print(newClassInstance.id)

    def do_show(self, classNameAndIdArgument):
        '''Prints the string representation of an instance based
        on the class name and id arguments'''
        instanceKey = \
            processClassNameIdArgumentToGetInstanceKey(classNameAndIdArgument)
        if (instanceKey is not None):
            instance = getInstanceFromRecord(instanceKey)
            showInstance(instance)

    def do_destroy(self, classNameAndIdArgument):
        '''Removes an instance from the instance records
        and saves the changes'''
        instanceKey = \
            processClassNameIdArgumentToGetInstanceKey(classNameAndIdArgument)
        if (instanceKey is not None):
            removeInstanceFromRecord(instanceKey)
            saveChangesOnInstanceRecordToJSONFile()

    def do_all(self, optionalClassNameArgument):
        '''Displays the string representation of all instances in the
        instance records'''
        empty = ""
        if (optionalClassNameArgument == empty):
            displayAllInstances()
        else:
            check = classExists(optionalClassNameArgument)
            if (check is True):
                displaySpecificInstances(optionalClassNameArgument)

    def do_update(self, classNameIdAttributes):
        '''Updates an instance identified by CLassName and Id
        with the attributes'''
        className, instanceId = classNameIdAttributes.split()[:2]
        classNameAndId = className + " " + instanceId
        instanceKey = \
            processClassNameIdArgumentToGetInstanceKey(classNameAndId)
        if (instanceKey is not None):
            check_attributeName = hasAttributeName(classNameIdAttributes)
            if (check_attributeName is True):
                check_attributeValue = hasAttributeValue(classNameIdAttributes)
                if (check_attributeValue is True):
                    updateInstanceWithAttributeAndValue(classNameIdAttributes)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
