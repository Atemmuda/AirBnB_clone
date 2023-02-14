#!/usr/bin/python3

"""
Base model object representation, object serialisation/deserialisation
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for the airbnb clone project
    This class can be used by other classes as a generic representation
    of object.
    """
    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        """
        Constructor function for the base class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value,
                                              "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                elif key != "__class__.__name__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        The string representation of the base object for printing
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the the the time of updated_at"""
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """
            of __dict__ of the instance
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            if not value:
                continue
            if key in ['created_at', 'updated_at']:
                dictionary[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dictionary[key] = value

        dictionary["__class__"] = self.__class__.__name__

        return dictionary
