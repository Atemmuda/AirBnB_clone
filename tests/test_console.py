#!/usr/bin/python3

"""Testing the console model"""

import unittest
from cmd import Cmd
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """For testing the console class"""

    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(HBNBCommand.__doc__), 0)
