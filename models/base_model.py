#!/usr/bin/python3

'''File with the BaseModel Class'''

import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    frmat = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, frmat))
                elif key != "__class__":
                    setattr(self, key, value)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        t1 = "[" + self.__class__.__name__ + "]"
        t2 = "(" + self.id + ") " + str(self.__dict__)
        return (t1 + t2)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dic = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dic[key] = str(value.isoformat())
            else:
                dic[key] = value
        dic["__class__"] = self.__class__.__name__
        return (dic)
