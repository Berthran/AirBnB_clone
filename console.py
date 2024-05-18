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

    def do_quit(self, arg):
        '''Terminate the cmd session'''
        quit()



if __name__ == "__main__":
    HBNBCommand().cmdloop()
