#!/usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def emptyline(self):
        """Does nothing when empty line is entered"""
        pass

    def do_quit(self):
        """Exits console"""
        return True

    def do_EOF(self):
        """Exits console"""
        return True

    def do_help(self, arg: str):
        """Help command"""
        return super().do_help(arg)
