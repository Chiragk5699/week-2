import unittest
from apputil import ways


class TestWays(unittest.TestCase):
    """Test cases for the ways function"""
    
    def test_zero_cents(self):
        """Test with 0 cents"""
        self.assertEqual(ways(0), 1)
    
    def test_one_to_four_cents(self):
        """Test with 1-4 cents (only pennies possible)"""
        self.assertEqual(ways(1), 1)
        self.assertEqual(ways(2), 1)
        self.assertEqual(ways(3), 1)
        self.assertEqual(ways(4), 1)
    
    def test_five_cents(self):
        """Test with 5 cents (2 ways: 1 nickel or 5 pennies)"""
        self.assertEqual(ways(5), 2)
    
    def test_ten_cents(self):
        """Test with 10 cents (3 ways)"""
        self.assertEqual(ways(10), 3)
    
    def test_fifteen_cents(self):
        """Test with 15 cents (4 ways)"""
        self.assertEqual(ways(15), 4)
    
    def test_twenty_cents(self):
        """Test with 20 cents (5 ways)"""
        self.assertEqual(ways(20), 5)
    
    def test_twenty_five_cents(self):
        """Test with 25 cents (6 ways)"""
        self.assertEqual(ways(25), 6)
    
    def test_large_amount(self):
        """Test with a larger amount (51 cents = 11 ways)"""
        self.assertEqual(ways(50), 11)


if __name__ == '__main__':
    unittest.main()
