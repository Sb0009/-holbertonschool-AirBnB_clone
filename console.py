#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
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
