import unittest
from src.Converter.RomanNumeralsBag import RomanNumeralsBag

class Test(unittest.TestCase):
    """ Tests the RomanNumeralsBag"""

    def test_equals(self):
        """Tests the output of the actual list entries of the Bag"""
        roman_numerals_bag = RomanNumeralsBag()
        roman_numerals_bag.append_numeral('X')
        self.assertEqual(roman_numerals_bag.numeralsList, ['X'])
        roman_numerals_bag.append_numeral('L')
        self.assertEqual(roman_numerals_bag.numeralsList, ['X', 'L'])
        roman_numerals_bag.append_numeral('II')
        self.assertEqual(roman_numerals_bag.numeralsList, ['X', 'L', 'I', 'I'])

    def test_stringify(self):
        """Tests the output after performing basic insert operation on the Bag"""
        roman_numerals_bag = RomanNumeralsBag()
        roman_numerals_bag.append_numeral('X')
        self.assertEqual(str(roman_numerals_bag), 'X')
        roman_numerals_bag.append_numeral('L')
        self.assertEqual(str(roman_numerals_bag), 'XL')