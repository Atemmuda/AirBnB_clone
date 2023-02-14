#!/usr/bin/python3
"""Fles storage engine for the objects"""

from json import load, dump
from os.path import exists


class FileStorage():
    """Class for storing object in a json file format"""
    __file_path = "storage_file.json"
    __objects = {}

    def all(self):
        """returns all the dictionary object"""
        return self.__objects

    def new(self, obj):
        """sets in the object with key the obj with
            the key <obj class name>.id and save to file
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
        self.save()

    def save(self):
        """serializes object to the JSON file"""
        dict_rep = {}
        for key, value in self.__objects.items():
            dict_rep[key] = value.to_dict()
        with open(self.__file_path, "w") as file_to:
            file_to.write(dump(dict_rep))

    def reload(self):
        """deserializes the JSON file to __objects if file exists"""
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as from_file:
                for key, value in load(from_file).items():
                    class_name = value("__class__")
