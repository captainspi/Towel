from unittest import TestCase
from unittest.mock import patch, MagicMock, call


class TestRomanToArabicValueConverter(TestCase):
    """"Tests the Roman to Arabic value converter"""

    @patch('src.Numerals.RomanNumeralsBag.RomanNumeralsBag')
    def testConvertToArabicValue(self, roman_numerals_bag_mock_class: MagicMock):
        """Tests the method that converts Roman Numerals to the Arabic counterpart"""
        #Set up
        roman_numerals_bag_mock = roman_numerals_bag_mock_class()
        roman_numerals_bag_mock.__numeralsList = ['X', 'L']
        expected_get_last_numeral_calls = [call(), call()]

        #Exercise
        to_arabic_value_converter = RomanToArabicValueConverter(roman_numerals_bag_mock)
        converted_value = to_arabic_value_converter.convert()

        #Verify
        roman_numerals_bag_mock.get_last_numeral.assert_has_calls(expected_get_last_numeral_calls)
        self.assertEqual(converted_value, 40)
