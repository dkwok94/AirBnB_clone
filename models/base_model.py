#!/usr/bin/python3
import uuid
from datetime import datetime

"""
Base class for all models will contain id, created_at
and updated at attributes. Save() and to_json() methods
"""


class BaseModel:
    """
    Instantiation of class BaseModel
    """
    def __init__(self):
        """
        initializing var
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Method returns string representation
        """
        return ("[{}] ({}) {}".format(str(type(self).__name__),
                                      self.id, str(self.__dict__)))

    def save(self):
        """
        Method to update attrb updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Method to return a dict containing all key/value of __dict__
        instance
        """
        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return (dic)
