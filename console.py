#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
<<<<<<< HEAD
    """ console class """
prompt = "(hbnb)"
# storage = models.storage


def do_quit(self, arg):
    """quit the program"""
    return True


def do_EOF(self, arg):
    """Quit the program"""

    print('')
    return True
=======

    prompt = '(hbnb)'

    def emptyline(self):
        """Does nothing when empty line is entered"""
        pass

    def do_quit(self, arg):
            """quit the program"""
            return True

    def do_EOF(self,arg):
        """Quit the program"""
        return True
>>>>>>> 8811a5db9fcf38a0ccb9ae62597430194ee3c950
