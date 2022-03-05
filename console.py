#!/usr/bin/python3
import cmd
from models.engine.file_storage import models
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_create(self, line):
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
        """Quit command to exit the program"""
        return True
    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True
    def help_help(self):
        print("help [command]")

    def emptyline(self):
        pass

    def default(self, line):
        methods = {"all": self.do_all, "count": self.do_count, "show": self.do_show,
                    "destroy": self.do_destroy, "update": self.do_update}
        
        separators = ["(", ")", ".", ",", "\"", "'"]
        input = line
        for s in separators:
            line = line.replace(s, " ")
        list_args = line.split()
        command = list_args.pop(1)
        try:
            meth_cmd = methods[command]
            meth_cmd(" ".join(list_args))
        except KeyError:
            print("*** Unknown syntax: {}".format(input))

if __name__ == '__main__':
    HBNBCommand().cmdloop()