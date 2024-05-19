#!/usr/bin/python3
'''
A command line interpreter for manipulating objects/instances.
'''

import cmd
import uuid
from datetime import datetime
from models.base_model import BaseModel
from console_tools import classExists, isValidClassNameArgument
from console_tools import createClassInstance, saveClassInstanceToJSONFile
from console_tools import hasInstanceId, instanceExists, createInstanceKey
from console_tools import getInstanceFromRecord, showInstance


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
        empty = ""
        if classNameAndIdArgument == empty:
            print("** class name missing **")
        else:
            check = classExists(classNameAndIdArgument)
            if (check is True):
                check = hasInstanceId(classNameAndIdArgument)
                if (check is True):
                    check = instanceExists(classNameAndIdArgument)
                    if (check is True):
                        instanceKey = createInstanceKey(classNameAndIdArgument)
                        instance = getInstanceFromRecord(instanceKey)
                        showInstance(instance)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
