#!/usr/bin/python3

"""command line commands for creating, quitting,
help, destroying, showing, updating,
all, update
"""

from cmd import Cmd


class HBNBCommand(Cmd):
    """Class for console commands
    """
    prompt = "(hbnb )"

    def emptyline(self):
        """if an empty line is encountered nothing is done"""
        pass

    def do_exit(self):
        return True

    do_EOF = do_exit(self="")
    def do_add(self,s):
        """add command"""
        l = s.split()
        print(l)
        if len(l) != 2:
            print ("*** invalid number of arguments")
            return
        try:
            l = [int(i) for i in l]
        except ValueError:
            print ("*** arguments should be numbers")

        print (l[0]+l[1])
    
    def help_add(self):
        print ('add two integral numbers')
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
