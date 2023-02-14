#!/usr/bin/python3
"""model for the amenities for the inside a house
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ amenities class for the things in the room or house
    """
    name: str = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor for the amenity object
        """
        super().__init__(*args, **kwargs)
