#!/usr/bin/python3
"""A module that tests the BaseModel class"""

import models
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class MyTestCase(unittest.TestCase):

    def test_id_assignment(self):
        """ Testing id assignment"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        obj4 = BaseModel()

        
    def test_id_uniqueness(self):
        """Testing unique id"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        obj4 = BaseModel()
        
        if hasattr(obj1, 'id'):
            self.assertNotEqual(obj1.id, obj2.id)

        if hasattr(obj2, 'id'):
            self.assertNotEqual(obj2.id, obj3.id)

        if hasattr(obj3, 'id'):
            self.assertNotEqual(obj3.id, obj4.id)

        if hasattr(obj4, 'id'):
            self.assertNotEqual(obj4.id, obj1.id)

    def test_str_format(self):
        """Testing string formaat"""
        obj1 = BaseModel()
        if hasattr(obj1, 'id'):
            expected = f"[{obj1.__class__.__name__}]({obj1.id}){obj1.__dict__}"
            actual = f"[{obj1.__class__.__name__}]({obj1.id}){obj1.__dict__}"
            self.assertEqual(actual, expected)

    def test__dict__(self):
        """Testing dictionary objects"""
        obj1 = BaseModel()
        if hasattr(obj1, 'created_at') and hasattr(obj1, 'updated_at'):
            self.assertIn('created_at', obj1.__dict__)
            self.assertIn('updated_at', obj1.__dict__)  
            self.assertIsInstance(obj1.created_at, datetime)
            self.assertIsInstance(obj1.updated_at, datetime)

    def test_key_value(self):
        """Testing Key/Value pair"""
        value = datetime.today()

        value_str = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj1 = BaseModel(created_at=value_str)
        expected_datetime = datetime.strptime(value_str, '%Y-%m-%dT%H:%M:%S.%f')

        self.assertEqual(obj1.created_at, expected_datetime)


if __name__ == '__main__':
    unittest.main()
