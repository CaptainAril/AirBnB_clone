#!/usr/bin/python3
"""This module the defines the entry point
for the console command interpreter.
"""
import cmd
from ntpath import join
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
        if len(args) < 2 and command not in ('create', 'all'):
            print("** instance id missing **")
            return True

        if command in ("show", "delete", "update"):
            obj = storage.all()
            key = f"{args[0]}.{args[1]}"
            _str = obj.get(key)
            if _str is None:
                print("** no instance found **")
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
        if HBNBComand.HBNBError(line, "show"):
            return

        obj_dict = storage.all()
        key = f"{args[0]}.{args[1]}"
        _str = obj_dict.get(key)
        print(_str)

    def do_destroy(self, line):
        """Deletes an instance based on class name and id."""
        args = line.split()
        if HBNBComand.HBNBError(line,  "delete"):
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all()
        del (obj[key])
        storage.save()

    def do_all(self, line):
        """Prints all sting representation based or not on the class name."""
        args = line.split()
        _str = []
        obj = storage.all()

        if args:
            if HBNBComand.HBNBError(line, 'all'):
                return
            key = args[0]
            for item in obj:
                if key in item:
                    _str.append(str(obj.get(item)))

        else:
            for item in obj:
                _str.append(str(obj.get(item)))
        ", ".join(_str)
        print(_str)

    def do_update(self, line):
        """Updates an instance based on the class name and id\
            by adding or updating attribute"""
        args = line.split()
        if HBNBComand.HBNBError(line, "update"):
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        print(f"key/value -> {args[2]}: {args[3]}")

        obj_dict = storage.all()
        key = f"{args[0]}.{args[1]}"
        print(key)
        item = obj_dict.get(key)
        print(item)
        # print(type(item))
        # eval(item)[args[2]] = args[3]
        # storage.save()
        #  obj = eval(key)
        setattr(item, args[2], args[3])
        item.save()
        # obj[args[2]] = args[3]
        storage.save()

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
