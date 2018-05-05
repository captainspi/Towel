from unittest import TestCase
from unittest.mock import patch, MagicMock, call
from src.Numerals.RomanToArabicValueConverter import RomanToArabicValueConverter


class TestRomanToArabicValueConverter(TestCase):
    """"Tests the Roman to Arabic value converter"""

    @patch('src.Numerals.Bag.RomanNumeralsBag.RomanNumeralsBag')
    def testConvertToArabicValue(self, roman_numerals_bag_mock_class: MagicMock):
        """Tests the method that converts Roman Numerals to the Arabic counterpart"""
        data_provider = [
            {"roman_numerals_bag_mock_output": ['I', None], "expected_converted_value": 1},
            {"roman_numerals_bag_mock_output": ['V', None], "expected_converted_value": 5},
            {"roman_numerals_bag_mock_output": ['X', None], "expected_converted_value": 10},
            {"roman_numerals_bag_mock_output": ['L', None], "expected_converted_value": 50},
            {"roman_numerals_bag_mock_output": ['C', None], "expected_converted_value": 100},
            {"roman_numerals_bag_mock_output": ['D', None], "expected_converted_value": 500},
            {"roman_numerals_bag_mock_output": ['M', None], "expected_converted_value": 1000},
            {"roman_numerals_bag_mock_output": ['L', 'X', None], "expected_converted_value": 40},
            {"roman_numerals_bag_mock_output": ['V', 'I', "L", "X", "M", "C", "M", None], "expected_converted_value": 1944},
            {"roman_numerals_bag_mock_output": [None], "expected_converted_value": 0}
        ]
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                # Set up
                roman_numerals_bag_mock = roman_numerals_bag_mock_class()
                roman_numerals_bag_mock.get_last_numeral.side_effect = data_provider[test_number]["roman_numerals_bag_mock_output"]
                expected_get_last_numeral_calls = [call(), call()]

                # Exercise
                to_arabic_value_converter = RomanToArabicValueConverter(roman_numerals_bag_mock)
                converted_value = to_arabic_value_converter.convert()

                # Verify
                roman_numerals_bag_mock.get_last_numeral.assert_has_calls(expected_get_last_numeral_calls)
                self.assertEqual(converted_value, data_provider[test_number]["expected_converted_value"])

