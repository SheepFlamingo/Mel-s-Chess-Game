import unittest
from src.const import *

class TestConst(unittest.TestCase):
    def test_constants(self):
        # Test screen dimentsions
        self.assertEqual(width, height) # Check if width and height are equal

        # Test board dimensions
        self.assertEqual(squareSize, width // cols) # Check if square size is calculated correctly
        self.assertEqual(cols, rows) # Check is cols and rows are equal
        
if __name__ == '__main__':
    unittest.main()

