from src.Numerals.Bag.RomanNumeralsBag import RomanNumeralsBag


class RomanToArabicValueMapper:
    """Maps a Roman Numeral to its Arabic Value"""

    def __init__(self):
        """Constructor"""
        self.__map = {'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}

    def map(self, roman_number: str) -> str:
        """Maps a Roman Numeral to its Arabic Value"""
        if roman_number in self.__map:
            return self.__map[roman_number]







