#!/usr/bin/python3
"""Test model for the for the base class
"""

import unittest
from models.base_model import BaseModel
"""import time
from datetime import datetime, timedelta"""


class TestBaseModel(unittest.TestCase):
    """Class for the base model testing"""

    def test_class_docs(self):
        """test for class documentation"""
        self.assertGreater(len(BaseModel.__doc__), 0)

    def test_init_docs(self):
        """test for documentation of the constructor"""
        self.assertGreater(len(BaseModel.__init__.__doc__), 0)

    def test_str_docs(self):
        """test for the documentation of the __str__ function"""
        self.assertGreater(len(BaseModel.__str__.__doc__), 0)

    def test_str(self):
        """test for correct printing of the __str__ function"""
        baseM1 = BaseModel()
        baseM1.name = "first base model"
        baseM1.number = 89
        self.assertEqual(baseM1.__str__(),
                         "[{}] ({}) {}"
                         .format(BaseModel.__name__,
                                 baseM1.id,
                                 baseM1.__dict__))

    def test_save_docs(self):
        """test for the documentation of the save function"""
        self.assertGreater(len(BaseModel.save.__doc__), 0)

    def test_saved(self):
        """test for the updated_at changes when the saved function is called"""
        baseModel = BaseModel()
        updated = baseModel.updated_at
        self.assertNotEqual((baseModel.save()), updated)

    def test_to_dict_docs(self):
        """test for the documentation of the to_dict function"""
        self.assertGreater(len(BaseModel.to_dict.__doc__), 0)
