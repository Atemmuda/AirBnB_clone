#!/usr/bin/python3
"""City Location of the houses
"""
from base_model import BaseModel


class City(BaseModel):
    """Class representation of the city
    """
    state_id: str = ""
    name: str = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor for the city object
        """
        super().__init__(*args, **kwargs)
