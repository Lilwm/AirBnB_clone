#!/usr/bin/python3
"""a base model class
"""
from pathlib import Path
import models
from uuid import uuid4
from datetime import datetime
import json


class BaseModel:
    """a class from which future classes will be derived """

    def __init__(self, *args, **kwargs):
        """initialization for base model class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.__setattr__(key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dic = {}
        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dic[key] = value

        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic

    def __str__(self):
        """String representation of the BaseModel class"""
        return"[{}]({}){}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
