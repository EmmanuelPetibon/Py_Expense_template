import unittest
from user import add_user

class TestUser(unittest.TestCase):

    def test_add_user(self):
        self.assertEqual(add_user('dzefzef'), True)