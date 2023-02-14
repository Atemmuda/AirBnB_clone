#!/usr/bin/python3
"""
Modelling the user of the application
"""

from base_model import BaseModel


class User(BaseModel):
    """
    User class for creating a user object
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor for the user object
        """
        super().__init__(*args, **kwargs)
