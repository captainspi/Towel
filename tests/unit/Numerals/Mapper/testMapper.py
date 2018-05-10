from unittest import TestCase
from src.Numerals.Mapper.Exception import InvalidNumeralMappingException
from src.Numerals.Mapper.RomanToArabicValueMapper import RomanToArabicValueMapper


class TestMapper(TestCase):
    """"Tests the Roman to Arabic value mapper"""

    def test_map(self):
        """Tests the method that maps Roman Numerals to the Arabic counterpart"""
        # Set up
        mapper = RomanToArabicValueMapper()
        mapper.map_numeral('A', 'B')

        # Exercise
        mapped_value = mapper.get_mapped_numeral('A')

        # Verify
        self.assertEqual(mapped_value, 'B')

    def test_invalid_mapping_exception(self):
        """Tests the mapping class for exception upon invalid mapping"""
        with self.assertRaises(InvalidNumeralMappingException) as context:
            mapper = RomanToArabicValueMapper()
            mapper.get_mapped_numeral('Z')
