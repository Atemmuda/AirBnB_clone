#!/usr/bin/python3
"""
Model for testing amenity class
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    class for testing Amenity objects
    """

    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(Amenity.__doc__), 0)

    def test_init_docs(self):
        """test for documentation of the constructor"""
        self.assertGreater(len(Amenity.__init__.__doc__), 0)
