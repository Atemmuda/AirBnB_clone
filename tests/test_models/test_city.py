#!/usr/bin/python3

"""
Model for testing the city model
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Class for testing features/funtionality of the city class/object
    """
    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(City.__doc__), 0)

    def test_init_docs(self):
        """test for documentation of the constructor"""
        self.assertGreater(len(City.__init__.__doc__), 0)
