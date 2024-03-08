#!/usr/bin/python3
"""
creates a class base which is the heart of the AirBnb clone
"""

import uuid
from datetime import datetime, date, time

class BaseModel:
    """
    Base
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize unique id, created_at, and updated_at attributes
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict representation of the instance for serialization"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """
         Return a string representation of the object
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
