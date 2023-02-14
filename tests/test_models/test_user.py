#!/usr/bin/python3

"""
Model for testing the user model
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class for testing user object"""

    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(User.__doc__), 0)

    def test_init_docs(self):
        """test for documentation of the constructor"""
        self.assertGreater(len(User.__init__.__doc__), 0)
