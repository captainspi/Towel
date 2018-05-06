from unittest import TestCase
from src.Numerals.Validator.RomanNumeralsValidator import RomanNumeralsValidator


class TestRomanNumeralsValidator(TestCase):
    """"Tests the Validator for RomanNumerals"""

    def testValidRomanNumeralsSet(self):
        """Tests the basic set of roman numerals for validity"""
        data_provider = ['V', 'V', 'X', 'L', 'C', 'D', 'M', 'XL']
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                roman_numerals_validator = RomanNumeralsValidator()
                self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)
