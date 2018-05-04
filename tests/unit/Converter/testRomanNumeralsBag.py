import unittest
from src.Converter.RomanNumeralsBag import RomanNumeralsBag

class Test(unittest.TestCase):
    """ Tests the RomanNumeralsBag"""

    def test_equals(self):
        """Tests the basic insert operation of the Bag"""
        #Set Up
        roman_numerals_bag = RomanNumeralsBag()
        roman_numerals_bag.append('X')
        self.assertEqual(str(roman_numerals_bag), 'X')
        roman_numerals_bag.append('L')
        self.assertEqual(str(roman_numerals_bag), 'XL')