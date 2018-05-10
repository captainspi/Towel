from src.Numerals.Mapper.Mapper import Mapper


class RomanToArabicValueMapper(Mapper):
    """Maps a Roman Numeral to its Arabic Value"""
    """This should be protected technically. But Python problems :("""
    map = {'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}

