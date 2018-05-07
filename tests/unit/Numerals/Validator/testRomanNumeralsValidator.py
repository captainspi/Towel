from unittest import TestCase
from src.Numerals.Validator.RomanNumeralsValidator import RomanNumeralsValidator
from src.Numerals.Validator.Exception import RomanNumeralsValidatorException


class TestRomanNumeralsValidator(TestCase):
    """"Tests the Validator for RomanNumerals"""

    def test_valid_roman_numerals_set(self):
        """Tests the basic set of roman numerals for validity"""
        data_provider = ['V', 'V', 'X', 'L', 'C', 'D', 'M', 'XL']
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                roman_numerals_validator = RomanNumeralsValidator()
                self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)

    def test_valid_repetitions(self):
        """Tests the correct set of repetitive roman numerals for validity"""
        data_provider = ['III', 'XXX', 'CCC', 'MMM', 'XXXIX', 'CCCXC', 'MMMCM']
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                roman_numerals_validator = RomanNumeralsValidator()
                self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)

    def test_valid_subtractions(self):
        """Tests the correct set of roman numerals for subtractive validity"""
        data_provider = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                roman_numerals_validator = RomanNumeralsValidator()
                self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)

    def test_valid_addition(self):
        """Tests the correct set of roman numerals for additive validity"""
        data_provider = ['II', 'VI', 'XI', 'XV', 'XX', 'LI', 'LV', 'LX', 'CI', 'CV', 'CX', 'CL', 'CC', 'DI', 'DV', 'DX', 'DL', 'DC', 'MI', 'MV', 'MX', 'ML', 'MC', 'MD', 'MM']
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                roman_numerals_validator = RomanNumeralsValidator()
                self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)

    def test_exception_invalid_numeral_set(self):
        """Tests the basic set of roman numerals for validity"""
        data_provider = ['A', 'VA', 'AV', 'LZX', 'IC']
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                with self.assertRaises(RomanNumeralsValidatorException) as context:
                    roman_numerals_validator = RomanNumeralsValidator()
                    self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)

    def test_exception_invalid_repetitions_of_D_L_V(self):
        """Tests the roman sequence for invalid repetitions"""
        data_provider = ['DD', 'LL', 'VV']
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                with self.assertRaises(RomanNumeralsValidatorException) as context:
                    roman_numerals_validator = RomanNumeralsValidator()
                    self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)

    def test_exception_invalid_repetition_in_fours_or_more_I_X_C_M(self):
        """Tests the roman sequence for invalid repetitions"""
        data_provider = ['IIII', 'XXXX', 'CCCC', 'MMMM']
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                with self.assertRaises(RomanNumeralsValidatorException) as context:
                    roman_numerals_validator = RomanNumeralsValidator()
                    self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)

    def test_invalid_repetition_inconsecutive_fours_X_C_M(self):
        """Tests the roman sequence for invalid repetitions"""
        data_provider = [
            'XXXVX', 'CCCIC', 'CCCLC', 'CCCVC', 'MMMIM', 'MMMVM', 'MMMXM', 'MMMLM', 'MMMDM'
            'XXXIXX', 'CCCXCC', 'MMMCMM'
        ]
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                with self.assertRaises(RomanNumeralsValidatorException) as context:
                    roman_numerals_validator = RomanNumeralsValidator()
                    self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)

    def test_exception_invalid_subtraction_of_V_L_D(self):
        """Tests the basic set of roman numerals for validity"""
        data_provider = ['VX', 'LC', 'DM', 'ILC', 'MVX']
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                with self.assertRaises(RomanNumeralsValidatorException) as context:
                    roman_numerals_validator = RomanNumeralsValidator()
                    self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)

    def test_exception_invalid_subtraction(self):
        """Tests the basic set of roman numerals for validity"""
        data_provider = ['XD', 'IXM', 'XLXD', 'IL', 'IIC', 'ID', 'MID']
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                with self.assertRaises(RomanNumeralsValidatorException) as context:
                    roman_numerals_validator = RomanNumeralsValidator()
                    self.assertTrue(roman_numerals_validator.validate(data_provider.pop()), True)
