import unittest
from app import add, greet
from app import add, greet, multiply
class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_greet(self):
        self.assertEqual(greet("DevOps"), "Hello, DevOps!")

if __name__ == "__main__":
    unittest.main()