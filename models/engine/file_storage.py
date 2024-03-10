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
        dict_instances = {}

        for key, value in self.__objects.items():
            if hasattr(value, 'to_dict') and callable
            (getattr(value, 'to_dict')):
                dict_instances[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(dict_instances, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:

                self.__objects = json.load(file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.__objects = {}
