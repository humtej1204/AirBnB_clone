#!/usr/bin/python3

""" This module supplies the HBNBCommand class"""

import cmd
from models.engine.file_storage import models
from models import storage


class HBNBCommand(cmd.Cmd):
    """Definition of the class"""

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of a class and
        saves to the JSON file and prints the id\n"""

        args = line.split()
        argc = len(args)
        if argc == 0:
            print("** class name missing **")
            return
        try:
            model = models[args[0]]
            obj = model()
            obj.save()
            print(obj.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id

        Args:
            line: input of the console

        Raises:
            KeyError = if the instance is not found\n"""
        args = line.split()
        argc = len(args)
        if argc == 0:
            print("** class name missing **")
            return
        if not args[0] in models:
            print("** class doesn't exist **")
            return
        if argc == 1:
            print("** instance id missing **")
            return

        dict_obj = storage.all()
        key = args[0] + "." + args[1]
        try:
            obj = dict_obj[key]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        and save the change into the JSON file

        Args:
            line = input of the console

        Raises:
            KeyError = if the instance is not found\n"""

        args = line.split()
        argc = len(args)
        if argc == 0:
            print("** class name missing **")
            return
        if not args[0] in models:
            print("** class doesn't exist **")
            return
        if argc == 1:
            print("** instance id missing **")
            return

        dict_obj = storage.all()
        key = args[0] + "." + args[1]
        try:
            del dict_obj[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name

        Args:
            line = input of the console\n"""
        args = line.split()
        argc = len(args)
        dict_obj = storage.all()
        list_str = []
        if argc == 0:
            for v in dict_obj.values():
                list_str.append(str(v))
            print(list_str)
            return
        if not args[0] in models:
            print("** class doesn't exist **")
            return

        for k, v in dict_obj.items():
            if args[0] in k:
                list_str.append(str(v))
        print(list_str)

    def do_count(self, line):
        """Counts the amount the instances of a class

        Args:
            line = input of the console\n"""
        args = line.split()
        argc = len(args)
        dict_obj = storage.all()
        if argc == 0:
            print("** class name missing **")
            return
        if not args[0] in models:
            print("** class doesn't exist **")
            return
        count = 0
        for k, v in dict_obj.items():
            if args[0] in k:
                count += 1
        print(count)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute(save the change into the JSON file

        Args:
            line = input of the console

        Exception:
            KeyError = if the instance is not found\n"""
        args = line.split()
        argc = len(args)
        if argc == 0:
            print("** class name missing **")
            return
        if not args[0] in models:
            print("** class doesn't exist **")
            return
        if argc == 1:
            print("** instance id missing **")
            return
        dict_obj = storage.all()
        key = args[0] + "." + args[1]
        try:
            obj = dict_obj[key]
        except KeyError:
            print("** no instance found **")
            return
        if argc == 2:
            print("** attribute name missing **")
            return
        if argc == 3:
            print("** value missing **")
            return
        setattr(obj, args[2], args[3])
        obj.save()

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        """Pass\n"""
        pass

    def default(self, line):
        """Identify the commands with other syntax and execute
        it respective action

        Args:
            line = input of the console\n"""
        methods = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
                }

        separators = ["(", ")", ".", ",", "\"", "'"]
        input = line
        for s in separators:
            line = line.replace(s, " ")
        list_args = line.split()
        if len(list_args) > 1:
            command = list_args.pop(1)
        else:
            command = list_args[0]
        try:
            methi_cmd = methods[command]
            meth_cmd(" ".join(list_args))
        except KeyError:
            print("*** Unknown syntax: {}".format(input))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
