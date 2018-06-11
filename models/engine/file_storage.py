#!/usr/bin/python3
"""
This module contains code related to file storage
for the airbnb clone project. A json data format
for serialization and deserialization of data.
"""
import json
import models


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public instance method to return
        the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Public instance method that
        sets in __objects with key id
        """
        if obj:
            self.__objects["{}.{}".format(str(type(obj).__name__),
                                          obj.id)] = obj

    def save(self):
        """
        Public instance that serializes __objects
        to the JSON file
        """
        dic = {}
        for id, object in self.__objects.items():
            dic[id] = object.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as myfile:
            json.dump(dic, myfile)

    def reload(self):
        """
        Public instance method to deserialize the JSON file
        to __objects only if file exists
        """
        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as myfile:
                object = json.load(myfile)
            for key, value in object.items():
                name = value["__class__"]
                del value["__class__"]
                self.__objects[key] = eval(name)(**value)
        except FileNotFoundError:
            pass
