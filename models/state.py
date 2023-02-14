#!/usr/bin/python3
"""model for the states or locations of the houses
"""
from base_model import BaseModel


class State(BaseModel):
    """
    class for the state of the location
    """
    name: str = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor for the state object
        """
        super().__init__(*args, **kwargs)
