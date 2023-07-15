#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for BaseModel class."""

    def setUp(self):
        self.base_model = BaseModel()

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_attributes_assignment(self):
        attributes = {
            "name": "Test",
            "value": 10,
            "created_at": "2023-07-15T12:00:00.000000",
            "updated_at": "2023-07-15T12:30:00.000000",
        }
        base_model = BaseModel(**attributes)
        self.assertEqual(base_model.name, "Test")
        self.assertEqual(base_model.value, 10)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_to_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn("__class__", base_model_dict)
        self.assertIn("created_at", base_model_dict)
        self.assertIn("updated_at", base_model_dict)

    def test_save(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_str(self):
        base_model_str = str(self.base_model)
        self.assertIsInstance(base_model_str, str)
        self.assertIn("[BaseModel]", base_model_str)
        self.assertIn(self.base_model.id, base_model_str)
        self.assertIn(str(self.base_model.__dict__), base_model_str)


if __name__ == "__main__":
    unittest.main()
