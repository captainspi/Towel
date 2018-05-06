import re
from src.Numerals.Validator.Error import Error
from src.Numerals.Validator.Exception import RomanNumeralsValidatorException


class RomanNumeralsValidator:
    """Validates Roman Numerals"""

    def __init__(self):
        """ constructor """
        self.__errors = []

    def validate(self, numeral_sequence: str) -> bool:
        """" Validates roman numerals """
        self.__is_valid_set(numeral_sequence)
        if self.__errors:
            raise RomanNumeralsValidatorException(self.__errors)

        return True

    def __is_valid_set(self, numeral_sequence: str):
        """Verifies if the numeral belongs to a list of valid roman numeral types"""
        allowed_roman_numerals_pattern = '[^IVXLCDM]'
        x = re.search(allowed_roman_numerals_pattern, numeral_sequence)
        if x:
            self.__errors.append(Error(Error.NUMERAL_SET, numeral_sequence))