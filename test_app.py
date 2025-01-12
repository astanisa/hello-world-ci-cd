# test_app.py
import unittest
from app import hello_world
class TestAppunittest.TestCase():
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

If __name__ == '__name__':
    unittest.main()