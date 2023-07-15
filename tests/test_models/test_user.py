#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_default_attr(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_update_attr(self):
        self.user.email = "sakata@example.com"
        self.user.password = "zuuurrrraaaa"
        self.user.first_name = "Sakata"
        self.user.last_name = "Gintoki"

        self.assertEqual(self.user.email, "sakata@example.com")
        self.assertEqual(self.user.password, "zuuurrrraaaa")
        self.assertEqual(self.user.first_name, "Sakata")
        self.assertEqual(self.user.last_name, "Gintoki")

    def test_inheritance(self):
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)


if __name__ == "__main__":
    unittest.main()