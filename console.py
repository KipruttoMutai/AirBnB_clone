#!/usr/bin/python3
"""

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """

    """
    prompt = "(hbnb)"

    def do_quit(self, line):
        """implements builtin quit function"""
        return True

    def do_EOF(self, line):
        """ïmplements the end of file function"""
        return True
    def emptyline(self):
        """Ëmpty line with enter doesnt execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
