#!/usr/bin/python3
""" MOdel the place of the rooms or houses
"""
from base_model import BaseModel


class Place(BaseModel):
    """
    Class represention of the places of location
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []

    def __init__(self, *args, **kwargs):
        """constructor for the lace object"""
        super().__init__(*args, **kwargs)
