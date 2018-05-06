from src.Numerals.Bag.RomanNumeralsBag import RomanNumeralsBag


class RomanNumeralsValidator:
    """Validates Roman Numerals"""

    def __init__(self):
        """ constructor """
        self.__errors = []

    def validate(self, roman_numerals: str) -> bool:
        """" Validates roman numerals """
        self.__is_valid_numeral(roman_numerals)
        if not self.__errors:
            return True

    def __is_valid_numeral(self, numeral: str) -> bool:
        """Verifies if the numeral belongs to a list of valid roman numeral types"""
        allowed_roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        return numeral in allowed_roman_numerals





