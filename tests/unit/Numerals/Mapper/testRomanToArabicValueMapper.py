from unittest import TestCase
from src.Numerals.Mapper.Exception import InvalidNumeralMappingException
from src.Numerals.Mapper.RomanToArabicValueMapper import RomanToArabicValueMapper


class TestRomanToArabicValueMapper(TestCase):
    """"Tests the Roman to Arabic value mapper"""

    def test_map_to_arabic_value(self):
        """Tests the method that maps Roman Numerals to the Arabic counterpart"""
        data_provider = [
            {"roman_value": 'I', "expected_converted_value": '1'},
            {"roman_value": 'V', "expected_converted_value": '5'},
            {"roman_value": 'X', "expected_converted_value": '10'},
            {"roman_value": 'L', "expected_converted_value": '50'},
            {"roman_value": 'C', "expected_converted_value": '100'},
            {"roman_value": 'D', "expected_converted_value": '500'},
            {"roman_value": 'M', "expected_converted_value": '1000'},
        ]
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                # Set up
                mapper = RomanToArabicValueMapper()

                # Exercise
                mapped_value = mapper.get_mapped_numeral(data_provider[test_number]['roman_value'])

                # Verify
                self.assertEqual(mapped_value, data_provider[test_number]["expected_converted_value"])

    def test_invalid_mapping_exception(self):
        """Tests the mapping class for exception upon invalid mapping"""
        with self.assertRaises(InvalidNumeralMappingException) as context:
            mapper = RomanToArabicValueMapper()
            mapper.get_mapped_numeral('Z')
