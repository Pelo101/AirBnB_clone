#!/usr/bin/python3
""" This module defines the basemodel for all other class."""


import uuid
from datetime import datetime


class BaseModel:
    """ A class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """ Instantiation of a class and common attributes"""

        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, valuei)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of the class"""
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary of the instances"""
        n_dict = self.__dict__.copy()
        n_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        n_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        n_dict['__class__'] = self.__class__.__name__
        return n_dict
