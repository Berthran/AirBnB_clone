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

    def do_EOF(self, arg):
        '''Terminates the cmd session'''
        quit()

    def do_help(self, arg):
        '''Provide bried description of available commands'''
        cmd.Cmd.do_help(self, arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
