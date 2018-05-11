from unittest import TestCase
from unittest.mock import patch, MagicMock, call

from src.Numerals.Bag.RomanNumeralsBag import RomanNumeralsBag
from src.Numerals.Exception import RomanToArabicValueConverterException
from src.Numerals.Mapper.RomanToArabicValueMapper import RomanToArabicValueMapper
from src.Numerals.RomanToArabicValueConverter import RomanToArabicValueConverter
from src.Numerals.Validator.RomanNumeralsValidator import RomanNumeralsValidator


class TestRomanToArabicValueConverter(TestCase):
    """"Tests the Roman to Arabic value converter"""

    def test_convert_to_arabic_value(self):
        """Tests the method that converts Roman Numerals to the Arabic counterpart"""
        data_provider = [
            {"roman_numerals_bag_mock_output": ['I'], "expected_converted_value": 1},
            {"roman_numerals_bag_mock_output": ['V'], "expected_converted_value": 5},
            {"roman_numerals_bag_mock_output": ['X'], "expected_converted_value": 10},
            {"roman_numerals_bag_mock_output": ['L'], "expected_converted_value": 50},
            {"roman_numerals_bag_mock_output": ['C'], "expected_converted_value": 100},
            {"roman_numerals_bag_mock_output": ['D'], "expected_converted_value": 500},
            {"roman_numerals_bag_mock_output": ['M'], "expected_converted_value": 1000},
            {"roman_numerals_bag_mock_output": ['X', 'L'], "expected_converted_value": 40},
            {"roman_numerals_bag_mock_output": ['M', 'C', 'M', 'X', 'L', 'I', 'V'], "expected_converted_value": 1944},
        ]
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                # Set up
                roman_numerals_bag = RomanNumeralsBag()
                for numeral in data_provider[test_number]["roman_numerals_bag_mock_output"]:
                    roman_numerals_bag.append_numeral(numeral)

                # Exercise
                to_arabic_value_converter = RomanToArabicValueConverter(roman_numerals_bag, RomanToArabicValueMapper(), RomanNumeralsValidator())
                converted_value = to_arabic_value_converter.convert()

                # Verify
                self.assertEqual(converted_value, data_provider[test_number]["expected_converted_value"])


    def test_roman_to_arabic_value_converter_exception(self):
        """Tests the convert method for an exception upon providing invalid numerals in a bag"""
        with self.assertRaises(RomanToArabicValueConverterException) as context:
                # Set up
                roman_numerals_bag = RomanNumeralsBag()
                roman_numerals_bag.append_numeral('I')
                roman_numerals_bag.append_numeral('M')

                # Exercise
                to_arabic_value_converter = RomanToArabicValueConverter(roman_numerals_bag, RomanToArabicValueMapper(), RomanNumeralsValidator())
                to_arabic_value_converter.convert()

