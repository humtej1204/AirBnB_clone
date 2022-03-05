#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

models = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
            "Amenity": Amenity, "Place": Place, "Review": Review}

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        dic = {}
        for k, v in FileStorage.__objects.items():
            dic[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(dic, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                dict_dict = json.load(f)
        except FileNotFoundError:
            dict_dict = {}
        for k, v in dict_dict.items():
            models_key = v["__class__"]
            model = models[models_key]
            FileStorage.__objects[k] = model(**v)
