import re


class RomanNumeralsValidator:
    """Validates Roman Numerals"""

    def __init__(self):
        """ constructor """
        self.__errors = []

    def validate(self, roman_numerals: str) -> bool:
        """" Validates roman numerals """
        self.__is_valid_numeral(roman_numerals)
        if self.__errors:
            return False
        else:
            return True

    def __is_valid_numeral(self, numeral: str):
        """Verifies if the numeral belongs to a list of valid roman numeral types"""
        allowed_roman_numerals_pattern = '[^IVXLCDM]'
        x = re.search(allowed_roman_numerals_pattern, numeral)
        if x:
            self.__errors.append('Error')