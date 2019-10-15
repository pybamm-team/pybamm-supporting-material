import unittest
from squared import squared


class TestSquared(unittest.TestCase):
    def test_squared(self):
        self.assertEqual(squared(2), 4)
        self.assertEqual(squared(0), 0)

    def test_cubed(self):
        self.assertEqual(squared(2, action="cube"), 8)
        self.assertEqual(squared(0, action="cube"), 0)


if __name__ == "__main__":
    unittest.main()
