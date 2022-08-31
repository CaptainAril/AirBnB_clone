#!/usr/bin/python3
"""This module defines class BaseModel and all it's attributes/methods."""
import uuid
from datetime import datetime


class BaseModel:
    """Represents a class BaseModel."""
    def __init__(self):
        """Instantiates a BaseModel class instance,
        with the following public attributes:

        Attr_1:
            id - Unique ID for each BaseModel instance
            created_at - Current datetime the instance is created
            updated_at - Current datetime when instance is created,
                        and to updated every time object is changed
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns the string representation of BaseModel instance.
        """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the instance attribute `updated_at` with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary representation of the BaseModel instance.
        """
        return self.__dict__
