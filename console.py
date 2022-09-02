#!/usr/bin/python3
"""This module the defines the entry point
for the console command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBComand(cmd.Cmd):
    intro = "Welcome to the AirBnB Console.\
        Type help to list commands.\n"

    prompt = "(hbnb) "

    class_model = (
        "BaseModel",
        "User",
        "City",
        "State",
        "Place",
        "Amenity",
        "Review"
        )

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    @classmethod
    def HBNBError(cls, line, command=None):
        args = line.split()
        if not args:
            print("** class name missing **")
            return True
        if args[0] not in HBNBComand.class_model:
            print("** class doesn't exist **")
            return True
        if len(args) < 2 and command != 'create':
            print("** instance id missing **")
            return True
        return False

    def do_create(self, line):
        """Creates a new instance of <class>."""
        args = line.split()
        if HBNBComand.HBNBError(line, "create"):
            return
        
        class_ = eval(args[0])
        obj_ = class_()
        print(obj_.__dict__["id"])
        storage.save()


    def do_show(self, line):
        """Prints string representation of instance
        based on class name and id."""
        args = line.split()
        if HBNBComand.HBNBError(line):
            return
        
        obj = storage.all()
        key = args[0] + '.' + args[1]
        print(obj.get(key))

    def destroy(self, line):
        """Deletes an instance based on class name and id."""
        pass

    def emptyline(self):
        pass

    # def default(self, line):
    #     args = line.split()
    #     print(args)

    # def parseline(self, line):
    #     print(line)


if __name__ == "__main__":
    HBNBComand().cmdloop()
    # import sys
    # input = open(sys.argv[1], 'rt')
    # try:
    #     HelloWorld(stdin=input).cmdloop()
    # finally:
    #     input.close()
