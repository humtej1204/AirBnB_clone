#!/usr/bin/python3

'''File with the class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances'''

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


models = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }


class FileStorage:
    '''FileStorage Class'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return (FileStorage.__objects)

    def new(self, obj):
        '''Sets in __objects the obj with key
        <obj class name>.id'''
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file
        (path: __file_path)'''
        dic = {}
        for k, v in FileStorage.__objects.items():
            dic[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(dic, f)

    def reload(self):
        '''Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.)'''
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                dict_dict = json.load(f)
        except FileNotFoundError:
            dict_dict = {}
        for k, v in dict_dict.items():
            models_key = v["__class__"]
            model = models[models_key]
            FileStorage.__objects[k] = model(**v)
