#!/usr/bin/python3
"""File Storage Class
This module is in charge of the storage of the
classes and their management."""

from json import dump, load, dumps
from os.path import exists
from models import base_model, user, place, state, city, amenity, review

BaseModel = base_model.BaseModel
State = state.State
City = city.City
Amenity = amenity.Amenity
Place = place.Place
Review = review.Review
User = user.User
name_class = ["BaseModel", "City", "State",
              "Place", "Amenity", "Review", "User"]


class FileStorage:
    """ FileStorage class to manage instances
    This is the File Storage module.
    Attributes:
        __file_path (str): This is the path of the JSON file in which
            the contents of the `__objects` variable will be stored.
        __objects (dict): This store all the instances data
        """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """Saves a new object in the `__objects` class attribute
        Args:
            obj (inst): The object to adds in the `__objects` class attribute
        Sets in the `__objects` class attribute the instance data
        with a key as <obj class name>.id.
        """
        class_name  = obj.__class__.__name__ 
        id = obj.id
        class_id = class_name + "." + id
        FileStorage.__objects[class_id] = obj

    def save(self):
        """Serializes the content of `__objects` class attribute
        The content of `__objects` class attribute will be serialized
        to the path of `__file_path` class attribute in JSON format
        with the `created_at` and `updated_at` formatted.
        """
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file in `__file_path` class attribute
        If the file on `__file_path` class attribute exists, each object
        on the file will be deserialized and appended to the `__objects`
        class attribute like an instance with the object data.
        """
        dic_obj = {}
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                dict_obj = load(f)
                for k, v in dic_obj.items():
                    class_nam = key.split(".")[0]
                    if class_nam in name_class:
                        FileStorage.__objects[key] = eval(class_nam)(**value)
                    else:
                        pass
