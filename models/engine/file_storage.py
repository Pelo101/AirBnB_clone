#!/usr/bin/python3
""" A module that serializes and deserializes instances to a JSON file"""

import json
from models.base_model import BaseModel
class FileStorage:
    """A class that serialies  and desrializes instance"""

    def __init__(self):
        """ instantiaton of  a class"""

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"[{obj.__class__.__name__}]({obj.id})"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""

        instance_obj = {}

        for key, value in self.__objects.items():
            instance_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w')as file:
            json.dump(instance_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:

                instance_obj = json.load(file)

                for key, value in instance_obj.items():

                    self.__objects[key] = value

        except FileNotFoundError:
            pass
