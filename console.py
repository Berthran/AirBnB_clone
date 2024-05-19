#!/usr/bin/python3
'''
A command line interpreter for manipulating objects/instances.
'''

import cmd
import uuid
from datetime import datetime
from models.base_model import BaseModel
from console_tools import createClassInstance
from console_tools import isValidClassNameArgument
from console_tools import saveClassInstanceToJSONFile


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
            if (isValidClassNameArgument(classNameArgument)):
                    newClassInstance = createClassInstance(classNameArgument)
                    saveClassInstanceToJSONFile(newClassInstance)
                    print(newClassInstance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, classNameAndIdArgument):
        '''Prints the string representation of an instance based
        on the class name and id'''
        empty = ""
        if classNameAndIdArgument == empty:
            print("** class name missing **")
        else:
            if (hasInstanceId(classNameAndIdArgument):
                    if (isValidClass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
