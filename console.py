#!/usr/bin/python3
'''
A command line interpreter for manipulating objects/instances.
'''

import cmd
import uuid
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    '''
    Instance of a cmd session
    '''

    prompt = "(hbnb) "



if __name__ == "__main__":
    HBNBCommand().cmdloop()
